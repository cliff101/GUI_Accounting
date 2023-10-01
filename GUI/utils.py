import datetime
import pickle
import sys


def pickle_saver(data, save_file, Encrypter):
    '''
function use to encrypt and save data. use it everytime data is edited.
    '''
    last_save_time = str(datetime.datetime.now().replace(microsecond=0))
    data['last_save_time'] = last_save_time
    data['hidden_message'] = "IF YOU SEE THIS, YOU MAY ME THE HACKER OR DOING THE ILLEGAL ACCESS TO THIS DIARY. NOTE THAT IT'S REALLY IMPOLITE TO SEE OTHERS DIARY IN THIS WAY. PLEASE LEAVE, THANKS."
    pickle_data = pickle.dumps(data)
    f = open(save_file, 'wb')
    f.write(Encrypter.encrypt(pickle_data))
    f.close()
    del data['hidden_message']
    return data


def is_full_shape(str_):
    '''
is_full_shape check if string is full shape,
if return list of bool
    '''
    ret = []
    for i in str_:
        if sys.getsizeof(i) > 55:
            ret.append(True)
        else:
            ret.append(False)
    return ret


def get_key_path(in_file):
    '''
function use to get path of key file from input file
    '''
    key_path = ''  # Define key path
    # Handle key path
    key_path = in_file.split('\\')
    key_path[-1] = key_path[-1].split('.')
    key_path[-1][-1] = 'key'
    key_path[-1] = '.'.join(key_path[-1])
    return '\\'.join(key_path)  # Return handled key path


def encrypt_keys(key, passwd, tips, old=False):
    '''
function use to encrypt keys with password user input
    '''
    import random
    import hashlib
    hash_object = hashlib.md5(passwd)  # Get hash object
    random.seed(hash_object.hexdigest())  # Set passwd hash to seed
    key = list(key)
    for i in range(len(key)):  # Start encryption
        key[i] += passwd[i % len(passwd)]+random.randint(100, 1000)
        key[i] %= 257 if old else 256
    key = bytes(key)
    key += b'\n'+tips
    return key


def decrypt_keys(key_encrypted, passwd, old=False):
    '''
function that decrypt keys with password
    '''
    import random
    import hashlib
    hash_object = hashlib.md5(passwd)  # Get hash object
    random.seed(hash_object.hexdigest())  # Set passwd hash to seed
    key_encrypted = list(key_encrypted)
    for i in range(len(key_encrypted)):  # Start decrypt
        key_encrypted[i] -= passwd[i % len(passwd)]+random.randint(100, 1000)
        key_encrypted[i] %= 257 if old else 256
    key_encrypted = bytes(key_encrypted)
    return key_encrypted


def get_version_log():
    log = '''
1.0.0: 本版本歷經許多個月之測試，為相當穩定的版本。
        由封測後唯一更新的功能是寫日記時如果誤觸ctrl+c並不會閃退了。

1.0.1: 由於沒測試過絕對路徑，讀取檔案的key時會出錯，打臉初始版本的長期測試。
        已修正。

1.1.0: 新增自動備份功能，於正常離開程式時會自動備份。
        強制命名副檔名為.bk，並更進一步修正路徑所帶來的錯誤

2.0.0: 重大更新：感變key的方式，使一切更加安全。使用者可以自訂密碼了。
        一個新的工具：passwd_changer.py，為一個獨立工具

2.1.0: 現在可手動備份data了
        新增日記檢視器，可更方便的檢視每日的日記

2.1.1: 小功能更新，可檢視日記的最後儲存時間
        將返回、退出統一改為鍵入"e"
        日記檢視可選擇跳至哪一天
        bugs fix

2.1.2: critical bugs fix

2.1.3(2020-12-03): small display change
                    running in exe detection
                    critical bug fix

3.0.0(2022-04-12): 時隔1年半....總算是有更新了
                    修正了一些小Bug(日記前幾天會發生的)
                    以及--支援指令了開始。現在支援的指令：
                    (str1:hidden-str2)，執行類cool word效果
                    且部分輸入採取讀鍵盤的方式
                    未來可能更新：可選開啟或關閉讀取指令
                    PS. 這個版本資訊加上去後還更新三天XD 原本是2022-04-10

3.0.1(2022-04-12): cool word修正
                    新功能：支援單日背景撥放Youtube audio

3.0.2(2022-04-24): 修正背景撥放只播一次

4.0.0(2023-10-01): 重構程式碼，並上QT
                    盡可能的保留原本的所有功能
                    目前Diary Printer的功能已使用QT Text Browser實現，應該會順暢很多
                    融合了更改密碼的功能，現在可以在主程式中更改密碼了
'''
    return log
