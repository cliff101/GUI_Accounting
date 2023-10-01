import sys
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QAction
from GUI.views.Ui_menu import Ui_menu
from qt_material import apply_stylesheet
from cryptography.fernet import Fernet

from GUI.mainWindow import mainWindow
from GUI.passwordInput import passwordInput
from GUI.passwordCreate import passwordCreate
from GUI.utils import pickle_saver, get_key_path, decrypt_keys, encrypt_keys
import ctypes
import os

# 強制將執行序優先級設定為最高 可能會有問題 也不確定是否有效
handle = ctypes.windll.kernel32.GetCurrentProcess()  # 获取当前进程的句柄
ctypes.windll.kernel32.SetPriorityClass(handle, 0x00008000)  # 设置进程的优先级类别为实时优先级


if __name__ == '__main__':  # prevent multiprocessing from import unused package
    class menu(QMainWindow, Ui_menu):
        def __init__(self):
            super(menu, self).__init__()

            self.setupUi(self)
            # 按鈕功能
            self.fileSelectBtn.clicked.connect(self.selected_file)
            self.newFile.clicked.connect(self.creat_file)
            # 副檔名
            self.extensionFilter = ['bk']
            self.fileNames = []

        def selected_file(self):
            filter = []
            for extension in self.extensionFilter:
                # filter.append(f'{extension} Files (*.{extension})')
                filter.append(f'*.{extension}')
            fileName, fileType = QFileDialog.getOpenFileName(
                self, "Open file", "./", "wallet file ("+";".join(filter) + ")")
            # List empty
            if not fileName:
                return

            # Load keys for decryption. Make sure key is in the same path of book file.
            Encrypter = self.load_keys(fileName)
            if Encrypter is None:
                return
            file = open(fileName, 'rb')  # Read in file
            pickle_data = file.read()
            # Decrypt in file content and load with pickle
            data = pickle.loads(Encrypter.decrypt(pickle_data))
            file.close()  # Close in file
            self.open_mainUI(data, fileName, Encrypter)

        def load_keys(self, in_file):
            '''
        function use to load key
            '''
            key_path = get_key_path(
                in_file)  # Get the key path from input file
            if not os.path.exists(key_path):  # Check if key exist
                QMessageBox.critical(
                    self, "錯誤", "金鑰不存在！\n請確認.key的金鑰與.bk檔案放在同一個資料夾資下！", QMessageBox.Ok)
                return None
            key_file = open(key_path, 'rb')  # Open the key file
            key_encrypted = key_file.read()
            key_file.close()  # Close file
            key_tips = key_encrypted.split(b'\n')[-1]  # Get key password tips
            key_encrypted = b'\n'.join(
                key_encrypted.split(b'\n')[:-1])  # Get real key
            pwInput = passwordInput(key_tips.decode('utf-8'))
            pwInput.exec()
            pwd = pwInput.password

            # because old key en/decrypt method have bug, do the translate code here
            # key = decrypt_keys(key_encrypted, pwd.encode('utf-8'), old = True)
            # key_encrypted_new = encrypt_keys(key, pwd.encode('utf-8'), key_tips)
            # key_file = open(key_path, 'wb')# Open the key file
            # key_file.write(key_encrypted_new)# Save key
            # key_file.close()# Close file

            try:
                # Decrypt key and Load key
                Encrypter = Fernet(decrypt_keys(
                    key_encrypted, pwd.encode('utf-8')))
            except:
                QMessageBox.critical(self, "錯誤", "密碼錯誤，請重新輸入！", QMessageBox.Ok)
                return None
            return Encrypter

        def creat_file(self):
            filter = []
            for extension in self.extensionFilter:
                # filter.append(f'{extension} Files (*.{extension})')
                filter.append(f'*.{extension}')
            fileName, fileType = QFileDialog.getSaveFileName(
                self, "Create file", "./", "wallet file ("+";".join(filter) + ")")
            # List empty
            if not fileName:
                return

            # Save key and get key at the same time
            Encrypter = self.save_keys(fileName)
            if Encrypter is None:
                QMessageBox.information(
                    self, "訊息", "金鑰建立失敗，請重新建立！", QMessageBox.Ok)
                return
            data = {}  # Define empty data
            data = pickle_saver(data, fileName, Encrypter)
            QMessageBox.information(
                self, "訊息", "金鑰已經建立！ 請妥善保存金鑰並請勿忘記密碼！！！", QMessageBox.Ok)
            self.open_mainUI(data, fileName, Encrypter)

        def save_keys(self, in_file):
            '''
        function use to save keys and generate key
            '''
            pwCreate = passwordCreate()
            pwCreate.exec()
            pwd = pwCreate.password.encode('utf-8')
            tips = pwCreate.passwordTips.encode('utf-8')

            # Get the key path from input file
            key_path = get_key_path(in_file)
            key = Fernet.generate_key()  # Gnerate key

            key = encrypt_keys(key, pwd, tips)  # Encrypt key

            key_file = open(key_path, 'wb')  # Open the key file
            key_file.write(key)  # Save key
            key_file.close()  # Close file
            Encrypter = self.load_keys(in_file)  # Load key
            return Encrypter

        def open_mainUI(self, data, save_file_path, Encrypter):
            if 'hidden_message' in data:
                del data['hidden_message']
            self.nextUi = mainWindow(data, save_file_path, Encrypter)
            self.nextUi.show()
            self.close()

extra = dict()

extra = {
    'font_size': '12px',
    'font_family': '假粉圓',
}

if __name__ == '__main__':
    # from pycallgraph2 import PyCallGraph
    # from pycallgraph2.output import GraphvizOutput
    # graphviz = GraphvizOutput()
    # graphviz.output_type = 'dot'
    # graphviz.output_file = 'pycallgraph.dot'
    # with PyCallGraph(output=graphviz):
    app = QApplication(sys.argv)
    window = menu()
    apply_stylesheet(app, theme='dark_teal.xml', extra=extra)
    window.show()
    app.exec()
