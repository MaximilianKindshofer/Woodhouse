from PySide import QtGui, QtCore
import woodhousegui
import sys
from configobj import ConfigObj


def saverules(folder, rulename, time, timescale, subfolders):
    config = ConfigObj()
    config.filename = 'rules.conf'
    config['Folder'] = folder
    config['Name'] = rulename
    config['Time'] = time
    config['Timescale'] = timescale
    config['Subfolders'] = subfolders
    config.write()
    # saves the rule to a file and sends an ok
    return 'OK'

def deleterules():
    pass

def showrules():
    pass

def testrules():
    pass

def main():
    app = QtGui.QApplication(sys.argv)
    woodhouse = woodhousegui.MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
