import os
b = input("ui file name: ")
savePath = "../views"
saveName = "Ui_"+".".join(b.split('.')[:-1])+'.py'
c = os.path.join(savePath, saveName)
print("pyside6-uic {} -o {}".format(b,c))
os.system("pyside6-uic {} -o {}".format(b,c))
