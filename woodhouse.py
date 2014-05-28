from PySide import QtGui, QtCore
import woodhousegui
import sys, os, time
import configparser


def saverules(folder, rulename, time, timescale, subfolders):
    #config.filename = 'rules.conf'
    config = configparser.ConfigParser()
    section = str(folder + '::' + rulename)
    config[section] = {}
    config[section]['Time'] = time
    config[section]['Timescale'] = timescale
    config[section]['Subfolder'] = str(subfolders)
    config[section]['activated'] = 'False'

    with open('rules.conf','a') as config_file:
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
    
def toggleactivateRule(folder, rulename):
    config = configparser.ConfigParser()
    config.read('rules.conf')
    section = section = str(folder + '::' + rulename)
    if config[section]['activated'] == 'False':
        config[section]['activated'] = 'True'
    else:
        config[section]['activated'] = 'False'
    with open('rules.conf', 'w') as config_file:
        config.write(config_file)
    return 'OK'
    
def getRules(folder):
    #returns a list of rulenames corresponding to the folder
    listofrules = []
    if not os.path.exists('rules.conf'):
        return None
    config = configparser.ConfigParser()
    config.read('rules.conf')
    sections = config.sections()
    for sec in sections:
        if folder in sec:
            name = sec.split('::')
            listofrules.append(name[1])
    return listofrules

def getFolders():
    #return a list of foldernames
    listoffolders = []
    if not os.path.exists('rules.conf'):
        return listoffolders
    config = configparser.ConfigParser()
    config.read('rules.conf')
    sections = config.sections()
    for sec in sections:
        folder = sec.split('::')
        #remove duplicates
        for item in folder:
            if folder.index(item) %2 == 0:
                listoffolders.append(item)
    listoffolders = list(set(listoffolders))
    return listoffolders


def showruletime(folder, name):
    config = configparser.ConfigParser()
    config.read('rules.conf')
    section = str(folder + '::' + name)
    return config[section]['Time']

def showruletimescale(folder, name):
    config = configparser.ConfigParser()
    config.read('rules.conf')
    section = str(folder + '::' + name)
    return config[section]['Timescale']

def showrulesubfolder(folder, name):
    config = configparser.ConfigParser()
    config.read('rules.conf')
    section = str(folder + '::' + name)
    return config[section]['Subfolder']

def showruleactive(folder, name):
    config = configparser.ConfigParser()
    config.read('rules.conf')
    section = str(folder + '::' + name)
    return config[section]['activated'] 

def testrules():
    pass

def clean():
    if not os.path.exists('rules.conf'):
        return 'There are no rules!'
    else:
        print('I was activated')
        config = configparser.ConfigParser()
        config.read('rules.conf')


def main():
    app = QtGui.QApplication(sys.argv)
    woodhouse = woodhousegui.MainWindow()
    app.exec_()
    sys.exit()



if __name__ == '__main__':
    main()
