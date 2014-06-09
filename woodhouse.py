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

def clean(test=False, folder=None):
    if not os.path.exists('rules.conf'):
        pass
    else:
        #seconds since the last epoch
        systemtime = time.time()
        config = configparser.ConfigParser()
        config.read('rules.conf')
        sections = config.sections()
        todelete = []
        if test == False:
            for s in sections:
                if config[s]['activated'] == "True":
                    nameandfolder = s.split('::')
                    name = nameandfolder[1]
                    folder = nameandfolder[0]
                    bestbeforetime = float(config[s]['time'])
                    bestbeforescale = config[s]['timescale']

                    #converting the time scale to seconds and multiply them time
                    if bestbeforescale == 'days':
                        #a day has 86400 seconds
                        bestbeforedelta = bestbeforetime * 86400
                    elif bestbeforescale == 'months':
                        #a month has 2628000 seconds
                        bestbeforedelta = bestbeforetime * 2628000
                    elif bestbeforescale == 'years':
                        #a year has 31536000 seconds
                        bestbeforedelta = bestbeforetime * 31536000

                    if config[s]['Subfolder'] == "False":
                        sublevel = 0
                    else:
                        sublevel = 255
                    #https://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below
                    for (path, dirs, files) in walklevel(folder, sublevel):
                        if sublevel !=0:
                            for items in files:
                                fullpath = os.path.join(path,items)
                                #lastmodified in seconds since the last epoch
                                lastmodified = os.path.getmtime(fullpath)
                                bestbefore = lastmodified + bestbeforedelta
                                if bestbefore <= systemtime:
                                    print(fullpath)
                                    os.remove(fullpath)

                                #delete folders
                            for items in dirs:
                                    fullpath = os.path.join(path,items)
                                    lastmodified = os.path.getmtime(fullpath)
                                    bestbefore = lastmodified + bestbeforedelta
                                    if bestbefore <= systemtime:
                                        os.rmdir(fullpath)
                                    else:
                                        pass
                        else:
                            for items in files:
                                fullpath = os.path.join(path,items)
                                #lastmodified in seconds since the last epoch
                                lastmodified = os.path.getmtime(fullpath)
                                bestbefore = lastmodified + bestbeforedelta
                                if bestbefore <= systemtime:
                                    print(fullpath)
                                    os.remove(fullpath)

        if test == True:
            for s in sections:
                if folder in s:
                    nameandfolder = s.split('::')
                    name = nameandfolder[1]
                    folder = nameandfolder[0]
                    bestbeforetime = float(config[s]['time'])
                    bestbeforescale = config[s]['timescale']

                    #converting the time scale to seconds and multiply them time
                    if bestbeforescale == 'days':
                        #a day has 86400 seconds
                        bestbeforedelta = bestbeforetime * 86400
                    elif bestbeforescale == 'months':
                        #a month has 2628000 seconds
                        bestbeforedelta = bestbeforetime * 2628000
                    elif bestbeforescale == 'years':
                        #a year has 31536000 seconds
                        bestbeforedelta = bestbeforetime * 31536000

                    if config[s]['Subfolder'] == "False":
                        sublevel = 0
                    else:
                        sublevel = 255
                    #https://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below
                    for (path, dirs, files) in walklevel(folder, sublevel):
                    #subfolders included
                        for items in files:
                            fullpath = os.path.join(path,items)
                            #lastmodified in seconds since the last epoch
                            lastmodified = os.path.getmtime(fullpath)
                            bestbefore = lastmodified + bestbeforedelta
                            if bestbefore <= systemtime:
                                 todelete.append(fullpath)
                            else:
                                pass
            return todelete

def walklevel(some_dir, level=0):
    #https://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir, topdown=False):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def main():
    app = QtGui.QApplication(sys.argv)
    woodhouse = woodhousegui.MainWindow()
    app.exec_()
    sys.exit()



if __name__ == '__main__':
    main()
