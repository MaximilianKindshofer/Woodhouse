from PySide import QtGui, QtCore
import woodhousegui
import sys, os
import configparser


def saverules(folder, rulename, time, timescale, subfolders):
    #config.filename = 'rules.conf'
    config = configparser.ConfigParser()
    section = str(folder + '::' + rulename)
    config[section] = {}
    config[section]['Time'] = time
    config[section]['Timescale'] = timescale
    config[section]['Subfolder'] = str(subfolders)

    with open('rules.conf','w') as config_file:
        config.write(config_file)
    # saves the rule to a file and sends an ok
    return 'OK'



def deleterules(folder, rulename):
    if not os.path.exists('rules.conf'):
        return 'No config found!'
    config = configparser.ConfigParser()
    config.read('rules.conf')
    section = str(folder + '::' + rulename)
    config.remove_section(section)

    with open('rules.conf', 'w') as config_file:
        config.write(config_file)
    return 'OK'

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
