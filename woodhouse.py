from PySide import QtGui, QtCore
import woodhousegui
import sys, os
import ConfigParser


def saverules(folder, rulename, time, timescale, subfolders):
    #config.filename = 'rules.conf'
    config = ConfigParser.ConfigParser()
    section = str(folder + '::' + rulename)
    config.add_section(section)
    config.set(section, 'Time', time)
    config.set(section, 'Timescale', timescale)
    config.set(section, 'Subfolder', subfolders)

    with open('rules.conf',"wb") as config_file:
        config.write(config_file)
    # saves the rule to a file and sends an ok
    return 'OK'



def deleterules():
    if not os.path.exists('rules'):
        print('No config found!')
    config = ConfigParser.ConfigParser()
    config.read('rules.conf')

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
