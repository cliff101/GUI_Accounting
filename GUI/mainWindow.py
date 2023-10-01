from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMenu, QFileDialog, QMessageBox, QDialog, QLineEdit, QInputDialog, QScrollArea, QLabel, QGridLayout, QSizePolicy
from PySide6.QtGui import QAction, QStandardItemModel, QStandardItem, QColor
from PySide6.QtCore import Qt, Signal, QItemSelectionModel
from PySide6 import QtCore
try:
    from .views.Ui_mainWindow import Ui_mainWindow
    from .utils import pickle_saver, is_full_shape, get_key_path, decrypt_keys, encrypt_keys, get_version_log
    from .aDayItemEdit import aDayItemEdit
    from .passwordInput import passwordInput
    from .passwordCreate import passwordCreate
except:
    from views.Ui_mainWindow import Ui_mainWindow
    from utils import pickle_saver, is_full_shape, get_key_path, decrypt_keys, encrypt_keys, get_version_log
    from aDayItemEdit import aDayItemEdit
    from passwordInput import passwordInput
    from passwordCreate import passwordCreate
from qt_material import apply_stylesheet
from cryptography.fernet import Fernet
import sys
import pafy
import time
import threading
import re
import random
import datetime
import shutil
import os
import requests

HAVE_VLC = True
try:
    import vlc
except:
    HAVE_VLC = False

try:
    BASE_PATH = sys._MEIPASS
except Exception:
    BASE_PATH = os.path.abspath(".")

# cmds starts with "(", ends with ")" ex:  (hello python:hidden-bye world)
CMDS = [":hidden-"]
CMDS_DESCRIPTION = ["(str1:hidden-str2)"]


# Define a new class that inherit from QStandardItem, for customizing the item
class myStandartItem(QStandardItem):
    def __init__(self, name, showText, _data=None):
        super(myStandartItem, self).__init__()

        self.name = name
        self.setText(showText)
        self.setEditable(False)
        self._data = _data


# Define a new class that inherit from QMessageBox, use to display long text
class ScrollMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)
        chldn = self.children()
        scrll = QScrollArea(self)
        scrll.setWidgetResizable(True)
        grd = self.findChild(QGridLayout)
        lbl = QLabel(chldn[1].text(), self)
        lbl.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        lbl.setWordWrap(True)
        scrll.setWidget(lbl)
        scrll.setMinimumSize(800, 200)
        grd.addWidget(scrll, 0, 1)
        chldn[1].setText('')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.exec()


class MediaHandler:  # Class for handling background audio
    def __init__(self):
        self.media_player = None
        self.isPlaying = False
        self.serviceIsRunning = False
        self.requestTime = time.time()

    def play_media(self, url):
        threading.Thread(target=self.play_media_core, args=(url,)).start()

    def stop_media(self):
        self.isPlaying = False

    def play_media_core(self, url):
        '''
play_media is the function play the youtube url audio background
        '''
        this_request_time = time.time()
        self.requestTime = this_request_time
        if not self.media_player is None:
            self.isPlaying = False
            while self.serviceIsRunning and this_request_time >= self.requestTime:
                time.sleep(0.1)

        if this_request_time < self.requestTime:  # if the request is too old, ignore it
            return

        self.isPlaying = True
        self.serviceIsRunning = True
        while self.isPlaying:
            try:
                video = pafy.new(url)
                audio = video.audiostreams[-1]
                try:
                    requests.get(audio.url, stream=True)
                except:
                    raise Exception()
                self.media_player = vlc.MediaPlayer(audio.url)
                self.media_player.play()
                while not self.media_player.is_playing() and self.isPlaying:
                    time.sleep(0.1)
                while True:
                    time.sleep(0.1)
                    if not self.isPlaying:
                        self.media_player.stop()
                        break
                    if not self.media_player.is_playing():
                        self.media_player.set_media(
                            self.media_player.get_media())
                        self.media_player.play()
                        while not self.media_player.is_playing():
                            time.sleep(0.1)
                if not self.isPlaying:
                    break
            except:
                pass
        self.serviceIsRunning = False


class DiaryPrinter:  # Class for printing diary
    def __init__(self, textBrower, updateTextSignal):
        self.textBrower = textBrower
        self.updateTextSignal = updateTextSignal
        self.isRunning = False
        self.serviceIsRunning = False
        self.requestTime = time.time()

    def start_printer(self, text):
        threading.Thread(target=self.diary_printer_core, args=(text,)).start()

    def stop_printer(self):
        self.isRunning = False

    def diary_printer_core(self, text):

        this_request_time = time.time()
        self.requestTime = this_request_time

        self.isRunning = False
        while self.serviceIsRunning and this_request_time >= self.requestTime:
            time.sleep(0.1)

        if this_request_time < self.requestTime:  # if the request is too old, ignore it
            return

        self.isRunning = True
        self.serviceIsRunning = True

        diary_content = text.split("\n")

        c = ['"', "'", '<', '>', '!', '@', '#', '$', '%', '^', '&', '*',
             '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', '/', '*', '`', '~']  # ,'<>','{}','[]'
        cmd_str_list = []  # [[have_cmd_line_index, cmd_index, with_cmd_string, str0, str1, [replace_str1,replace_str2,...]],...]
        for i in range(len(diary_content)):
            for j in range(len(CMDS)):
                this_cmd = re.findall(
                    "(?s)[(](?:(?![(]).)+(?s)"+CMDS[j]+"(?:(?!"+CMDS[j]+").)*?[)]", diary_content[i])
                if j == 0:
                    for k in range(len(this_cmd)):
                        cmd_str_list.append([i, j, this_cmd[k], this_cmd[k].split(
                            ':hidden-')[0][1:], this_cmd[k].split(':hidden-')[1][:-1], [this_cmd[k].split(':hidden-')[0][1:]]*15])
        for l in range(2):
            for i in range(len(cmd_str_list)):
                if l == 0:
                    curstr0 = cmd_str_list[i][3]
                    curstr1 = cmd_str_list[i][4]
                else:
                    curstr0 = cmd_str_list[i][4]
                    curstr1 = cmd_str_list[i][3]
                real_j = 1.
                real_k = 0
                j_bias = 0
                j_bias_cpy = j_bias
                shape_bias_bias = 0
                j_limit = len(curstr1)+sum(is_full_shape(curstr1)
                                           )-sum(is_full_shape(curstr0))
                if j_limit < 0:
                    j_limit = 0
                while True:
                    thisstr = ""
                    coolstr = ""
                    for j in range((len(curstr1)+len(curstr0))*2+1):
                        coolstr += random.choice(c)
                    j = int(real_j)
                    k = int(real_k)
                    if k > len(curstr1):
                        k = len(curstr1)
                    if j <= k:
                        j = k+1
                    if j > j_limit:
                        j = j_limit

                    if j == j_limit:
                        if len(curstr0)+sum(is_full_shape(curstr0)) > len(curstr1)+sum(is_full_shape(curstr1)):
                            j_bias_cpy = j_bias
                            j_bias += 1
                            curstr0 = curstr0[:-2 if k == len(curstr1) else -1]
                            while j+j_bias_cpy > len(curstr0):
                                j_bias_cpy -= 1
                        elif len(curstr0)+sum(is_full_shape(curstr0)) == len(curstr1)+sum(is_full_shape(curstr1)):
                            j_bias_cpy = j_bias
                            j_bias += 1
                            while j+j_bias_cpy > len(curstr0):
                                j_bias_cpy -= 1
                    shape_bias = sum(is_full_shape(
                        curstr0[:j+j_bias_cpy]))-(sum(is_full_shape(curstr1[:k])))
                    if k == len(curstr1) and shape_bias+shape_bias_bias > 0:
                        if shape_bias > 1:
                            shape_bias_bias -= 2
                        elif shape_bias > 0:
                            shape_bias_bias -= 1
                    thisstr = curstr1[:k]+coolstr[k:(j+shape_bias+shape_bias_bias+j_bias_cpy)
                                                  if j+shape_bias+shape_bias_bias+j_bias_cpy >= 0 else 0]+curstr0[j+j_bias_cpy:]

                    # print(curstr1[:k]+coolstr[k:(j+shape_bias+shape_bias_bias+j_bias_cpy) if j+shape_bias+shape_bias_bias+j_bias_cpy>=0 else 0]+curstr0[j+j_bias_cpy:])

                    cmd_str_list[i][5].append(thisstr)
                    if k == len(curstr1) and len(coolstr[k:(j+shape_bias+shape_bias_bias+j_bias_cpy) if j+shape_bias+shape_bias_bias+j_bias_cpy >= 0 else 0]+curstr0[j+j_bias_cpy:]) == 0 and shape_bias+shape_bias_bias <= 0:
                        cmd_str_list[i][5].append(thisstr)
                        cmd_str_list[i][5].append(thisstr)
                        break
                    real_j += random.random()*2.7
                    real_k += random.random()*(1.3 if real_j < len(curstr1) else 2)
        if len(cmd_str_list) == 0:
            # print('\n'.join(diary_content))
            self.updateTextSignal.emit('\n'.join(diary_content))
            self.isRunning = False
            self.serviceIsRunning = False
            return
        j = 0
        diary_content_cpy = diary_content.copy()
        for i in range(len(cmd_str_list)):
            if cmd_str_list[i][1] == 0:
                diary_content_cpy[cmd_str_list[i][0]] = diary_content[cmd_str_list[i][0]].replace(
                    cmd_str_list[i][2], cmd_str_list[i][5][j % len(cmd_str_list[i][5])])
        self.updateTextSignal.emit('\n'.join(diary_content_cpy))
        j += 1
        while self.isRunning:
            cur_line = cmd_str_list[0][0]
            diary_content_cpy = diary_content.copy()
            for i in range(len(cmd_str_list)):
                if cmd_str_list[i][1] == 0:
                    diary_content_cpy[cmd_str_list[i][0]] = diary_content_cpy[cmd_str_list[i][0]].replace(
                        cmd_str_list[i][2], cmd_str_list[i][5][j % len(cmd_str_list[i][5])])
                if i+1 == len(cmd_str_list) or cmd_str_list[i+1][0] != cur_line:
                    if i+1 < len(cmd_str_list):
                        cur_line = cmd_str_list[i+1][0]
                    # replace_lineup(len(diary_content)-cmd_str_list[i][0],diary_content_cpy[cmd_str_list[i][0]])
            self.updateTextSignal.emit('\n'.join(diary_content_cpy))
            j += 1
            time.sleep(0.2)
        self.serviceIsRunning = False


# TODO: can hide no data date, but click edit today data will disable it
class mainWindow(QMainWindow, Ui_mainWindow):
    setTodayDiaryTextBrowserSignal = Signal(str)

    def __init__(self, data, save_file_path, Encrypter):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()  # 將視窗最大化

        # fix old
        for x in data.keys():
            if x == "last_save_time":
                continue
            if "cost_val" in data[x]:
                del data[x]["cost_val"]
            if "earn_val" in data[x]:
                del data[x]["earn_val"]

        # set Qss stylesheet
        file = QtCore.QFile(os.path.join(BASE_PATH, "style.qss"))
        file.open(QtCore.QFileDevice.ReadOnly)
        self.setStyleSheet(file.readAll().toStdString())

        # allDay
        self.allDayStdModel = QStandardItemModel()
        self.allDayListview.setModel(self.allDayStdModel)
        self.allDayListview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.allDayListview.customContextMenuRequested.connect(
            self.onContextAllDay)
        self.allDayListview.selectionModel().selectionChanged.connect(
            self.oneDaySelectionChanged)
        self.editTodayDataBtn.clicked.connect(self.editTodayDataBtnClicked)
        self.showVersionLogBtn.clicked.connect(lambda: ScrollMessageBox(
            QMessageBox.Information, "版本資訊", get_version_log(), QMessageBox.Ok))
        self.showMonthlyDataBtn.clicked.connect(self.printMonthlyData)
        self.setPasswordBtn.clicked.connect(self.setPasswordBtnClicked)

        # today cost
        self.todayCostStdModel = QStandardItemModel()
        self.todayCostListview.setModel(self.todayCostStdModel)
        self.todayCostListview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.todayCostListview.customContextMenuRequested.connect(
            self.onContextTodayCost)
        self.addCostBtn.clicked.connect(self.addCostBtnClicked)

        # today income
        self.todayIncomeStdModel = QStandardItemModel()
        self.todayIncomeListview.setModel(self.todayIncomeStdModel)
        self.todayIncomeListview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.todayIncomeListview.customContextMenuRequested.connect(
            self.onContextTodayIncome)
        self.addIncomeBtn.clicked.connect(self.addIncomeBtnClicked)

        # today song
        self.editTodaySong.clicked.connect(self.editTodaySongClicked)

        # today money
        self.editTodayMoney.clicked.connect(self.editTodayMoneyClicked)

        # today diary
        self.editTodayDiaryStatus = 0  # 0 = Edit  1 = Edit finish
        self.editTodayDiaryBtn.clicked.connect(self.editTodayDiaryClicked)
        self.setTodayDiaryTextBrowserSignal.connect(
            self.todayDiaryTextBrowserUpdateText)

        self.data = data
        self.save_file_path = save_file_path
        self.Encrypter = Encrypter
        self.mediaHandler = MediaHandler()
        self.diaryPrinter = DiaryPrinter(
            self.todayDiaryTextBrowser, self.setTodayDiaryTextBrowserSignal)

        self.cmdTipsBtn.clicked.connect(self.cmdTipsBtnClicked)

        self.selectedKey = None
        self.prevselectedKey = None

        self.refreshUI()
        # self.disableADayUI()

    # Update text in today diary text browser
    def todayDiaryTextBrowserUpdateText(self, text):
        vScrollBarValue = self.todayDiaryTextBrowser.verticalScrollBar().value()
        self.todayDiaryTextBrowser.setText(text)
        self.todayDiaryTextBrowser.verticalScrollBar().setValue(vScrollBarValue)

    # Funcions for all day
    # When selection changed in all day listview
    def oneDaySelectionChanged(self, selection):
        index = self.allDayListview.currentIndex()
        item = self.allDayStdModel.itemFromIndex(index)
        print("oneDaySelectionChanged", item.name)

        # self.disableADayUI(inverse=True)
        self.selectedKey = item.name  # Set selected key
        self.editDayLabel.setText("編輯日期： " + item.name)
        self.refreshADayData()

    def onContextAllDay(self, point):  # When right click in all day listview
        index = self.allDayListview.indexAt(point)
        print("onContextAllDay", index)

        if not index.isValid():  # If not valid, return
            return

        # create menu
        menu = QMenu(self.allDayListview)
        menu.addAction("刪除", self.deleteOneDayItem)
        menu.exec_(self.allDayListview.mapToGlobal(point))

    def deleteOneDayItem(self):  # Delete one day item
        index = self.allDayListview.currentIndex()
        item = self.allDayStdModel.itemFromIndex(index)
        print("deleteOneDayItem", item.name)

        reply = QMessageBox.warning(
            self, "警告", f"真的要刪除{self.selectedKey}的資料嗎？\n刪除後將無法復原！", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            del self.data[item.name]
            self.saveData()
            self.refreshAllDayListview()

    def editTodayDataBtnClicked(self):  # When edit today data button clicked
        print("editTodayDataBtnClicked")

        fix = 1  # Define when is the last day of the data, so as to fix the missing data content
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        date_day = datetime.datetime.strptime(
            date, "%Y-%m-%d")  # Get datetime from date string
        real_money_last = 0
        if len(self.data) > 1:  # If there is nothing in data, no need to fix missing data
            # Get the last data content of data
            last_item = [x for x in list(
                self.data.keys()) if x != "last_save_time"][-1]
            last_day = datetime.datetime.strptime(
                last_item, "%Y-%m-%d")  # Change it to datetime
            # Get the real money of last data content
            real_money_last = self.data[last_item]['real_money']
            # Loop to fill the data that is missing
            while date_day > last_day+datetime.timedelta(days=fix):
                # For missing days, fill them with default item, real money will fill the value in last value of data content
                self.data[(last_day+datetime.timedelta(days=fix)).strftime("%Y-%m-%d")] = {
                    'cost': {}, 'earn': {}, 'real_money': real_money_last}
                fix += 1  # Next day that is missing
            
        self.data[date] = {'cost': {}, 'earn': {}, 'real_money': real_money_last}

        self.saveData()
        self.refreshAllDayListview(selected=date)

    def printMonthlyData(self):  # Print monthly data
        '''
function that will print all day in the data, contain some informaiton of data in every single day
        '''
        st_total = ''  # Define the final output string
        st = ''  # Define the string of every month, each month will reset this string, can be recognized as a local string
        cur = ''  # Define the month of the date
        month_cost = 0  # Define monthly cost
        month_earn = 0  # Define monthly earn
        have_diary = False  # Define bool if that day have diary
        have_diary_str = ''  # Define string to display if that day have diary
        for date in self.data:  # Iterate date from data
            if date == "last_save_time":
                continue
            # Check if thay day have diary
            have_diary = 'diary' in self.data[date]
            # String to display if that day have diary
            have_diary_str = 'with diary: '+str(have_diary)
            if cur == '':  # For the first time of the loop, get the month
                cur = date[:7]  # '2020-09-27'[:7] is the month '2020-09'
            elif cur != date[:7]:  # If the month have changed, print the monthly data
                st_total += cur+'===Month earn: {:=<11,}Month cost: {:=<11,}'.format(
                    month_earn, month_cost)+'='*20+'\n'+st+'\n'  # Add monthly data to final output string
                st = ''  # Reset string local string
                month_cost = 0  # Reset mothly cost
                month_earn = 0  # Reset monthly earn
                cur = date[:7]  # Set the month to the next month

            cost_val = sum(x for x in self.data[date]['cost'].values())
            earn_val = sum(x for x in self.data[date]['earn'].values())
            month_cost += cost_val  # Add monthly cost
            month_earn += earn_val  # Add monthly earn
            st += date+'   Earn: {:<11,}Cost: {:<11,}Money real owned: {:<11,}'.format(
                earn_val, cost_val, self.data[date]['real_money'])+have_diary_str+'\n'  # Add a day in current month

        # For the last loop, last month will not be show, so use this to fix it
        st_total += cur+'===Month earn: {:=<11,}Month cost: {:=<11,}'.format(
            month_earn, month_cost)+'='*20+'\n'+st+'\n'
        st = ''
        month_cost = 0
        month_earn = 0
        ScrollMessageBox(QMessageBox.Information, "所有資料", st_total)

    def setPasswordBtnClicked(self):  # When set password button clicked
        print("setPasswordBtnClicked")
        if self.save_file_path is None:
            return

        # Get the key path from input file
        key_path = get_key_path(self.save_file_path)
        key_file = open(key_path, 'rb')  # Open the key file
        key_encrypted = key_file.read()
        key_file.close()  # Close file
        key_tips = key_encrypted.split(b'\n')[-1]  # Get key password tips
        key_encrypted = b'\n'.join(
            key_encrypted.split(b'\n')[:-1])  # Get real key
        pwInput = passwordInput(key_tips.decode('utf-8'))
        pwInput.exec()
        pwd = pwInput.password

        try:
            # Decrypt key and Load key
            Fernet(decrypt_keys(key_encrypted, pwd.encode('utf-8')))
        except:
            QMessageBox.critical(self, "錯誤", "密碼錯誤，請重新輸入！", QMessageBox.Ok)
            return

        pwCreate = passwordCreate()
        pwCreate.tipsLineedit.setText(key_tips.decode('utf-8'))
        pwCreate.passwdLineedit.setText(pwd)
        pwCreate.exec()
        pwd = pwCreate.password.encode('utf-8')
        tips = pwCreate.passwordTips.encode('utf-8')

        # Get the key path from input file
        key_path = get_key_path(self.save_file_path)
        key = Fernet.generate_key()  # Gnerate key

        key = encrypt_keys(key, pwd, tips)  # Encrypt key

        key_file = open(key_path, 'wb')  # Open the key file
        key_file.write(key)  # Save key
        key_file.close()  # Close file
        # Decrypt key and Load key
        self.Encrypter = Fernet(decrypt_keys(key, pwd))
        self.saveData()
        QMessageBox.information(self, "成功", "密碼重設成功！", QMessageBox.Ok)

    # Functions for today cost
    def onContextTodayCost(self, point):  # When right click in today cost listview
        index = self.todayCostListview.indexAt(point)
        print("onContextTodayCost", index)

        if not index.isValid():
            return

        # create menu
        menu = QMenu(self.todayCostListview)
        menu.addAction("刪除", self.deleteTodayCostItem)
        menu.addAction("編輯", self.editTodayCostItem)
        menu.exec_(self.todayCostListview.mapToGlobal(point))

    def deleteTodayCostItem(self):  # Delete today cost item
        index = self.todayCostListview.currentIndex()
        item = self.todayCostStdModel.itemFromIndex(index)
        print("deleteTodayCostItem", item.name)

        del self.data[self.selectedKey]['cost'][item.name]

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    def editTodayCostItem(self):  # Edit today cost item
        index = self.todayCostListview.currentIndex()
        item = self.todayCostStdModel.itemFromIndex(index)
        print("editTodayCostItem", item.name)

        # Create a dialog to ask information of today cost
        todayItemEditCost = aDayItemEdit(True, item.name, item._data)
        todayItemEditCost.exec()
        ok = todayItemEditCost.OK
        itemName = todayItemEditCost.itemName
        value = todayItemEditCost.value
        if not ok or itemName == "" or value == "":
            return
        value = int(value)

        # Resolve the same name problem
        ori_name = item.name
        name = itemName
        i = 2
        while itemName in self.data[self.selectedKey]['cost'].keys() and itemName != ori_name:
            itemName = f"{name} ({i})"
            i += 1

        # Update the data
        this_cost_keys = list(self.data[self.selectedKey]['cost'])
        this_cost_value = list(self.data[self.selectedKey]['cost'].values())
        this_cost_keys[index.row()] = itemName
        this_cost_value[index.row()] = value
        self.data[self.selectedKey]['cost'] = dict(
            zip(this_cost_keys, this_cost_value))

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    def addCostBtnClicked(self):  # Add cost button clicked
        print("addCostBtnClicked")

        # Create a dialog to add today cost item
        todayItemEditCost = aDayItemEdit(True)
        todayItemEditCost.exec()
        ok = todayItemEditCost.OK
        itemName = todayItemEditCost.itemName
        value = todayItemEditCost.value
        if not ok or itemName == "" or value == "":
            return
        value = int(value)

        # Resolve the same name problem
        name = itemName
        i = 2
        while itemName in self.data[self.selectedKey]['cost'].keys():
            itemName = f"{name} ({i})"
            i += 1

        # Update the data
        item = myStandartItem(itemName, f"{itemName}   花費 = {value}", value)
        self.todayCostStdModel.appendRow(item)
        self.data[self.selectedKey]['cost'][itemName] = value

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    # Functions for today income
    # When right click in today income listview
    def onContextTodayIncome(self, point):
        index = self.todayIncomeListview.indexAt(point)
        print("onContextTodayIncome", index)

        if not index.isValid():
            return

        # create menu
        menu = QMenu(self.todayIncomeListview)
        menu.addAction("刪除", self.deleteTodayIncomeItem)
        menu.addAction("編輯", self.editTodayIncomeItem)
        menu.exec_(self.todayIncomeListview.mapToGlobal(point))

    def deleteTodayIncomeItem(self):  # Delete today income item
        index = self.todayIncomeListview.currentIndex()
        item = self.todayIncomeStdModel.itemFromIndex(index)
        print("deleteTodayIncomeItem", item.name)

        del self.data[self.selectedKey]['earn'][item.name]

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    def editTodayIncomeItem(self):  # Edit today income item
        index = self.todayIncomeListview.currentIndex()
        item = self.todayIncomeStdModel.itemFromIndex(index)
        print("editTodayIncomeItem", item.name)

        # Create a dialog to edit today income item
        todayItemEditIncome = aDayItemEdit(False, item.name, item._data)
        todayItemEditIncome.exec()
        ok = todayItemEditIncome.OK
        itemName = todayItemEditIncome.itemName
        value = todayItemEditIncome.value
        if not ok or itemName == "" or value == "":
            return
        value = int(value)

        # Resolve the same name problem
        ori_name = item.name
        name = itemName
        i = 2
        while itemName in self.data[self.selectedKey]['earn'].keys() and itemName != ori_name:
            itemName = f"{name} ({i})"
            i += 1

        # Update the data
        this_earn_keys = list(self.data[self.selectedKey]['earn'])
        this_earn_value = list(self.data[self.selectedKey]['earn'].values())
        this_earn_keys[index.row()] = itemName
        this_earn_value[index.row()] = value
        self.data[self.selectedKey]['earn'] = dict(
            zip(this_earn_keys, this_earn_value))

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    def addIncomeBtnClicked(self):  # Add income button clicked
        print("addIncomeBtnClicked")

        # Create a dialog to ask information of today income
        todayItemEditIncome = aDayItemEdit(False)
        todayItemEditIncome.exec()
        ok = todayItemEditIncome.OK
        itemName = todayItemEditIncome.itemName
        value = todayItemEditIncome.value
        if not ok or itemName == "" or value == "":
            return
        value = int(value)

        # Resolve the same name problem
        name = itemName
        i = 2
        while itemName in self.data[self.selectedKey]['earn'].keys():
            itemName = f"{name} ({i})"
            i += 1

        # Update the data
        item = myStandartItem(name, f"{itemName}   收入 = {value}", value)
        self.todayIncomeStdModel.appendRow(item)
        self.data[self.selectedKey]['earn'][itemName] = value

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    # Functions for today song
    def editTodaySongClicked(self):  # Edit today song button clicked
        print("editTodaySongClicked")

        # Create a dialog to ask URL of today song
        todaySongDialog = QInputDialog(self)
        todaySongDialog.setInputMode(QInputDialog.TextInput)
        todaySongDialog.setWindowTitle("編輯今日主題歌")
        todaySongDialog.setLabelText("今日主題歌：")
        if "yt_audio_theme" in self.data[self.selectedKey].keys():
            todaySongDialog.setTextValue(
                self.data[self.selectedKey]['yt_audio_theme']['url'])
        todaySongDialog.resize(500, todaySongDialog.height())
        ok = todaySongDialog.exec()

        # Update the data
        url = todaySongDialog.textValue()
        if not ok or not url:  # If not ok or url is empty, return
            return
        self.disableAllUI()
        try:  # Try to get the title of the video
            video = pafy.new(url)
        except:  # If fail, show error and return
            self.disableAllUI(inverse=True)
            QMessageBox.critical(self, "錯誤", "網址錯誤，請重新輸入！", QMessageBox.Ok)
            return
        self.disableAllUI(inverse=True)
        self.data[self.selectedKey]['yt_audio_theme'] = {
            'url': url, 'title': video.title}

        self.saveData()
        self.refreshADayData(forcePlaySong=True)
        self.refreshAllDayListview(selected=self.prevselectedKey)

    # Functions for today money
    def editTodayMoneyClicked(self):  # Edit today money button clicked
        print("editTodayMoneyClicked")

        # Create a dialog to ask URL of today song
        todayMoneyDialog = QInputDialog(self)
        todayMoneyDialog.setIntMaximum(999999999)
        todayMoneyDialog.setInputMode(QInputDialog.IntInput)
        todayMoneyDialog.setWindowTitle("編輯本日餘款")
        todayMoneyDialog.setLabelText("本日餘款：")
        todayMoneyDialog.setIntValue(
            self.data[self.selectedKey]['real_money'])
        todayMoneyDialog.resize(500, todayMoneyDialog.height())
        ok = todayMoneyDialog.exec()

        # Update the data
        value = todayMoneyDialog.intValue()
        if not ok:  # If not ok or url is empty, return
            return
        self.data[self.selectedKey]['real_money'] = value

        self.saveData()
        self.refreshADayData()
        self.refreshAllDayListview(selected=self.prevselectedKey)

    # Functions for today diary
    def editTodayDiaryClicked(self):  # Edit today diary button clicked
        print("editTodayDiaryClicked")

        if self.editTodayDiaryStatus == 0:  # If status is 0, start editing

            # 等待日記Printer停止，先Disable所有UI
            self.disableAllUI()
            self.diaryPrinter.stop_printer()
            while self.diaryPrinter.serviceIsRunning:
                time.sleep(0.1)
            self.disableAllUI(inverse=True)
            self.disableCostIncomeUI()
            self.disableAllDayUI()

            # 開始編輯日記
            if 'diary' in self.data[self.selectedKey].keys():
                self.todayDiaryTextBrowser.setText(
                    self.data[self.selectedKey]['diary'])
            else:
                self.todayDiaryTextBrowser.setText("")
            self.editTodayDiaryBtn.setText("完成編輯")
            self.editTodayDiaryStatus = 1
            self.todayDiaryTextBrowser.setReadOnly(False)
            self.todayDiaryTextBrowser.setStyleSheet("background-color: black")
        else:  # If status is 1, finish editing

            # 完成編輯日記
            self.editTodayDiaryBtn.setText("編輯日記")
            self.editTodayDiaryStatus = 0
            self.todayDiaryTextBrowser.setReadOnly(True)
            self.data[self.selectedKey]['diary'] = self.todayDiaryTextBrowser.toPlainText()
            self.todayDiaryTextBrowser.setStyleSheet("dark_teal.xml")

            self.disableCostIncomeUI(inverse=True)
            self.disableAllDayUI(inverse=True)

            self.saveData()
            self.refreshADayData(forceRunDiaryPrinter=True)
            self.refreshAllDayListview(selected=self.prevselectedKey)

    def cmdTipsBtnClicked(self):  # Cmd tips button clicked
        print("cmdTipsBtnClicked")
        cmd_tips_string = "指令開始於 \"(\"， 結束於 \")\"。 範例：  (hello python:hidden-bye world)\n\n"
        for i in range(len(CMDS)):
            cmd_tips_string += f"{i+1}.  指令：{CMDS[i]}   說明：{CMDS_DESCRIPTION[i]}\n"
        ScrollMessageBox(QMessageBox.Information, "指令說明", cmd_tips_string)
    

    # Functions for global
    def saveData(self):  # Save data
        if not self.Encrypter is None:  # If Encrypter None, now is in test mode, no need to encrypt/save
            self.data = pickle_saver(
                self.data, self.save_file_path, self.Encrypter)

    def backup_data(self):  # Backup data
        '''
function that backup data
        '''
        key_path = get_key_path(self.save_file_path)
        data_path = self.save_file_path
        data_path = data_path.replace("/", "\\")
        data_path_split = data_path.split("\\")
        data_name = '.'.join(data_path_split[-1].split('.')[:-1])
        backup_dir = 'backup_'+data_name
        try:
            os.mkdir('\\'.join(data_path_split[:-1])+'\\'+backup_dir)
        except:
            pass
        shutil.copy(data_path, '\\'.join(data_path_split[:-1])+'\\'+backup_dir+'\\'+data_name+'  '+str(
            datetime.datetime.now().replace(microsecond=0)).replace(':', '-')+'.bk')
        shutil.copy(key_path, '\\'.join(
            data_path_split[:-1])+'\\'+backup_dir+'\\'+data_name+'.key')

    # Functions of refresh UI
    def refreshUI(self):  # Refresh UI
        # 更新每日資料的ListView
        self.refreshAllDayListview()
        self.refreshADayData()

    def refreshAllDayListview(self, selected=None):  # Refresh all day listview
        # disconnect the signal, clear the model, and reconnect the signal
        self.allDayListview.selectionModel().selectionChanged.disconnect()
        self.allDayStdModel.clear()
        self.allDayListview.selectionModel().selectionChanged.connect(
            self.oneDaySelectionChanged)

        # refresh all day listview
        entries = self.data.keys()
        selected_index = None
        for x in entries:
            if x == "last_save_time":
                continue
            this_cost = sum(self.data[x]['cost'].values())
            this_earn = sum(self.data[x]['earn'].values())
            this_remain = self.data[x]['real_money']
            have_diary = 'diary' in self.data[x].keys()
            if this_cost or this_earn or have_diary:
                item = myStandartItem(
                    x, "{}   =+=+=+=+=+=+=+=+=+=   cost={}   earn={}   remain={}   have diary={}   =+=+=+=+=+=+=+=+=+=".format(x, this_cost, this_earn, this_remain, have_diary))
            else:
                item = myStandartItem(x, "{}   cost={}   earn={}   remain={}   have diary={}".format(
                    x, this_cost, this_earn, this_remain, have_diary))
            self.allDayStdModel.appendRow(item)
            # If selected is not None and found the item want to select, select the selected item
            if not selected is None and x == selected:
                selected_index = item.index()
                # self.allDayListview.setCurrentIndex(selected_index)
                self.allDayListview.selectionModel().setCurrentIndex(
                    selected_index, QItemSelectionModel.Select)

        # select the last item if no item is selected or selected item not found
        if selected_index is None and len(entries) > 1:
            selected_index = item.index()  # Using the last item
            # self.allDayListview.setCurrentIndex(selected_index)
            self.allDayListview.selectionModel().setCurrentIndex(
                selected_index, QItemSelectionModel.Select)

    # Refresh a day data
    def refreshADayData(self, forcePlaySong=False, forceRunDiaryPrinter=False):
        if self.selectedKey is None:  # If nothing is selected, return
            return
        self.todayCostStdModel.clear()
        self.todayIncomeStdModel.clear()

        # refresh today cost
        totalcost = 0
        entries = self.data[self.selectedKey]['cost'].keys()
        for x in entries:
            this_cost = self.data[self.selectedKey]['cost'][x]
            totalcost += this_cost
            item = myStandartItem(x, f"{x}   支出 = {this_cost}", this_cost)
            self.todayCostStdModel.appendRow(item)
        self.todayCostListview.scrollToBottom()
        self.todayCostLabel.setText(f"本日花費： {totalcost}")

        # refresh today income
        totalearn = 0
        entries = self.data[self.selectedKey]['earn'].keys()
        for x in entries:
            this_earn = self.data[self.selectedKey]['earn'][x]
            totalearn += this_earn
            item = myStandartItem(x, f"{x}   收入 = {this_earn}", this_earn)
            self.todayIncomeStdModel.appendRow(item)
        self.todayIncomeListview.scrollToBottom()
        self.todayIncomeLabel.setText(f"本日花費： {totalearn}")

        # refresh today song
        if "yt_audio_theme" in self.data[self.selectedKey].keys():
            self.todaySongLabel.setText(
                f"今日主題歌： {self.data[self.selectedKey]['yt_audio_theme']['title']}")
            if self.prevselectedKey != self.selectedKey or forcePlaySong:
                self.mediaHandler.play_media(
                    self.data[self.selectedKey]['yt_audio_theme']['url'])
        else:
            self.todaySongLabel.setText("今日主題歌： 未設定")
            self.mediaHandler.stop_media()

        # refresh today money
        self.todayMoneyLabel.setText(
            f"本日餘款： {self.data[self.selectedKey]['real_money']}")

        # refresh yest money
        data_keys_list = list(self.data.keys())
        data_keys_list.remove("last_save_time")
        yest_index = data_keys_list.index(self.selectedKey)-1
        yest_money = 0
        if yest_index < 0:
            self.yestMoneyLabel.setText("昨日餘款： 0")
        else:
            yest_date = data_keys_list[yest_index]
            yest_money = self.data[yest_date]['real_money']
            self.yestMoneyLabel.setText(
                f"昨日餘款： {yest_money}")

        # refresh today should money
        cost_val = sum(self.data[self.selectedKey]['cost'].values())
        earn_val = sum(self.data[self.selectedKey]['earn'].values())
        today_should_money = yest_money - cost_val + earn_val
        self.todayShouldMoneyLabel.setText(
            f"本日應餘： {today_should_money}")

        # refresh today diary
        todayDiary = ""
        if "diary" in self.data[self.selectedKey].keys():
            todayDiary = self.data[self.selectedKey]['diary']
        if self.prevselectedKey != self.selectedKey or forceRunDiaryPrinter:
            self.diaryPrinter.start_printer(todayDiary)

        self.todayDiaryTextBrowser.setReadOnly(True)
        self.editTodayDiaryStatus = 0
        self.editTodayDiaryBtn.setText("編輯日記")

        self.prevselectedKey = self.selectedKey

    def disableADayUI(self, inverse=False):  # Disable a day UI
        self.disableCostIncomeUI(inverse)
        self.disableDiaryUI(inverse)
        QApplication.processEvents()

    def disableCostIncomeUI(self, inverse=False):  # Disable cost income UI
        self.todayCostListview.setEnabled(inverse)
        self.addCostBtn.setEnabled(inverse)
        self.todayIncomeListview.setEnabled(inverse)
        self.addIncomeBtn.setEnabled(inverse)
        self.editTodaySong.setEnabled(inverse)
        self.editTodayMoney.setEnabled(inverse)
        QApplication.processEvents()

    def disableDiaryUI(self, inverse=False):  # Disable diary UI
        self.todayDiaryTextBrowser.setEnabled(inverse)
        self.editTodayDiaryBtn.setEnabled(inverse)
        self.cmdTipsBtn.setEnabled(inverse)
        QApplication.processEvents()

    def disableAllDayUI(self, inverse=False):  # Disable all day UI
        self.allDayListview.setEnabled(inverse)
        self.editTodayDataBtn.setEnabled(inverse)
        self.showMonthlyDataBtn.setEnabled(inverse)
        self.showVersionLogBtn.setEnabled(inverse)
        self.setPasswordBtn.setEnabled(inverse)
        QApplication.processEvents()

    def disableAllUI(self, inverse=False):  # Disable all UI
        self.disableADayUI(inverse)
        self.disableAllDayUI(inverse)
        self.disableDiaryUI(inverse)
        QApplication.processEvents()

    def closeEvent(self, event):  # When close the window
        print('mainWindow closeEvent')

        self.mediaHandler.stop_media()  # Stop media
        if not self.save_file_path is None:  # If save file path is not None, save data
            self.saveData()
            self.backup_data()  # Backup data before close
        event.accept()  # let the window close


extra = dict()

extra = {
    'font_size': '12px',
    'font_family': '假粉圓',
}

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml', extra=extra)
    ###data_ = {'2020-08-24': {"diary": "finally...", "yt_audio_theme": {'url': 'https://www.youtube.com/watch?v=49ohUZeHjP8', 'title': 'K-391 - Lighthouse (Official Video)'}, 'cost': {"test": 123}, 'earn': {'初值': 46736}, 'cost_val': 0, 'earn_val': 46736, 'real_money': 46736}, '2020-08-25': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-08-26': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-08-27': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-08-28': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-08-29': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-08-30': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-08-31': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-09-01': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-09-02': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 46736}, '2020-09-03': {'cost': {}, 'earn': {'生活費': 15000}, 'cost_val': 0, 'earn_val': 15000, 'real_money': 61736}, '2020-09-04': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-05': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-06': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-07': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-08': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-09': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-10': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-11': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-12': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-13': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-14': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-15': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-16': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-17': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-18': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-19': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-20': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-21': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-22': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-23': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-24': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-25': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-26': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-27': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-28': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-29': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-09-30': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-01': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-02': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-03': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-04': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-05': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-06': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 61736}, '2020-10-07': {'cost': {'領生活費': 2000}, 'earn': {'轉帳': 500}, 'cost_val': 2000, 'earn_val': 500, 'real_money': 60236}, '2020-10-08': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-09': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-10': {'cost': {}, 'earn': {},
                #   'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-11': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-12': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-13': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-14': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-15': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-16': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-17': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-18': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-19': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-20': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-21': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-22': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-23': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-24': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-25': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-26': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-27': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-28': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-29': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-30': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-10-31': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-01': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-02': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-03': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-04': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-05': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-06': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 60236}, '2020-11-07': {'cost': {'統計 過去幾天之領生活費': 5000}, 'earn': {}, 'cost_val': 5000, 'earn_val': 0, 'real_money': 55236}, '2020-11-08': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-09': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-10': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-11': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-12': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-13': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-14': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-15': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-16': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-17': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-18': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-19': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-20': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-21': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-22': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-23': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-24': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-25': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, '2020-11-26': {'cost': {}, 'earn': {}, 'cost_val': 0, 'earn_val': 0, 'real_money': 55236}, 'last_save_time': '2020-11-26 22:26:23'}
    data_ = {"last_save_time":None}
    window = mainWindow(data_, None, None)
    window.show()
    sys.exit(app.exec_())
