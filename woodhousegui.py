from PySide import QtGui, QtCore
import sys, woodhouse

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initui()
        self.folder = ''
        #TODO: Load Rules on Startup if config file exists

    def initui(self):
        self.setWindowTitle('Woodhouse')
        self.setGeometry(300, 300, 250, 350)

        # the left side of the window with the folders
        folderbar = QtGui.QLabel('Folders')
        self.folderlist = QtGui.QListWidget(self)
        self.folderlist.SingleSelection
        # TODO: When a folder is selected, the Rulesection should show
        # Only the Rules for this folder
        folderaddbutton = QtGui.QPushButton('Add',self)
        folderaddbutton.clicked.connect(self.addFolder)
        folderdeletebutton = QtGui.QPushButton('Delete', self)
        folderdeletebutton.clicked.connect(self.deleteFolder)

        # the right side of the window with the rules
        rulebar = QtGui.QLabel('Rules')
        self.rulelist = QtGui.QListWidget(self)
        self.rulelist.SingleSelection
        ruleaddbutton = QtGui.QPushButton('Add', self)
        ruleaddbutton.clicked.connect(self.configRule)
        ruleviewbutton = QtGui.QPushButton('View', self)
        ruleviewbutton.clicked.connect(self.viewRule)
        ruledeletebutton = QtGui.QPushButton('Delete', self)
        ruledeletebutton.clicked.connect(self.deleteRule)
        ruletestbutton = QtGui.QPushButton('Test Rule', self)
        ruletestbutton.clicked.connect(self.ruleTest)

        # GridLayout

        # left side
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(folderbar, 0, 0)
        self.grid.addWidget(self.folderlist,1, 0, 1, 2)
        self.grid.addWidget(folderaddbutton, 2, 0)
        self.grid.addWidget(folderdeletebutton, 2, 1)
        # space between the lists
        self.grid.addWidget(QtGui.QLabel(''),0, 2, 1, 5)
        # right side
        self.grid.addWidget(rulebar, 0, 3)
        self.grid.addWidget(self.rulelist, 1, 3, 1, 4)
        self.grid.addWidget(ruleaddbutton, 2, 3)
        self.grid.addWidget(ruleviewbutton, 2, 4)
        self.grid.addWidget(ruledeletebutton, 2, 5)
        self.grid.addWidget(ruletestbutton,2 , 6)
        self.setLayout(self.grid)
        self.show()

    def addFolder(self):
        # select Folder and display it
        folderselect = QtGui.QFileDialog()
        folderselect.setFileMode(QtGui.QFileDialog.Directory)
        folderselect.setOption(QtGui.QFileDialog.ShowDirsOnly)
        if folderselect.exec_():
            self.folder = folderselect.selectedFiles()
            # to Display the Path in the List, we first copy
            # the data in a new variable cause we want to
            # give the folder variable to an other function later
            # it has the form of
            # ['u/path/to/blerg'] we slice the first 3 and the
            # last 2
            showfolder = self.folder
            showfolder = str(showfolder)[3:-2]
            duplicates = self.folderlist.findItems(showfolder, QtCore.Qt.MatchExactly)
            if len(duplicates) == 0:
                QtGui.QListWidgetItem(showfolder, self.folderlist)


    def deleteFolder(self):
        # wow since adding was so easy i thoght removing is as well
        # but apprently not. the right methode is to takeitem()
        # https://stackoverflow.com/questions/7484699/pyqt4-remove-item-widget-from-qlistwidget
        # TODO: Delete all Rules for this Folder
        for selectedfolder in self.folderlist.selectedItems():
            self.folderlist.takeItem(self.folderlist.row(selectedfolder))


    def configRule(self):
        # Configurate Rules and calls the addRuleHelper function
        #
        # selectedItems() currentItem would also work but it raises
        # an error after the if statement... not implemented yet error.
        # well I have no clue why, it has something to to with
        # None
        foldername = self.folderlist.selectedItems()
        if foldername == []:
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle('No selected Folder')
            msgBox.setText("Choose a Folder to apply rules to.")
            msgBox.exec_()
        else:
            self.ruleset = QtGui.QDialog(self)
            # how to get the folders humanreadabel text (label)
            # http://stackoverflow.com/questions/12087715/pyqt4-get-list-of-all-labels-in-qlistwidget
            # again this could be more elegant but since I got the list from
            # selectedItems it would be wasteful just to use it for the
            # first check. Room for improvement.
            title = [t.text() for t in foldername]
            self.ruleset.setWindowTitle(title[0] + " rule set")
            namelabel = QtGui.QLabel('Name of the rule: ')
            self.nameline = QtGui.QLineEdit()
            timelabel = QtGui.QLabel('Delete files older than')
            self.time = QtGui.QLineEdit()
            self.time.setInputMask("999")
            self.timescale = QtGui.QComboBox()
            self.timescale.insertItems(0,['days','months','years'])
            self.foldercheck = QtGui.QCheckBox('Include containing folders',self)
            savebutton = QtGui.QPushButton('Save',self)
            self.rulefolder = title[0]
            savebutton.clicked.connect(self.addRuleHelper)
            closebutton = QtGui.QPushButton('Close',self)
            closebutton.clicked.connect(self.ruleset.accept)
            #Grid for the rule window
            rulegrid = QtGui.QGridLayout()
            rulegrid.addWidget(namelabel, 0, 0)
            rulegrid.addWidget(self.nameline, 0, 1)
            rulegrid.addWidget(timelabel, 1, 0)
            rulegrid.addWidget(self.time, 1, 1)
            rulegrid.addWidget(self.timescale,1, 2)
            rulegrid.addWidget(self.foldercheck, 2, 0)
            rulegrid.addWidget(savebutton, 3, 1)
            rulegrid.addWidget(closebutton, 3, 2)
            self.ruleset.setLayout(rulegrid)
            self.ruleset.exec_()

    def addRuleHelper(self):
        #get the text from configRule's QLineEdit
        if self.nameline.text() == '':
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle('Name rule')
            msgBox.setText('Please name your rule')
            msgBox.exec_()
        #check for duplicated rulenames
        elif len(self.rulelist.findItems(self.nameline.text(),
                                         QtCore.Qt.MatchExactly)) != 0:
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle('Duplicate rule')
            msgBox.setText('Please use an other name')
            msgBox.exec_()
        else:
            self.ruleset.accept()
            #TODO: Write real code in the Main File
            pathobject = self.folderlist.selectedItems()
            path = [p.text() for p in pathobject]
            saved = woodhouse.saverules(path[0], self.nameline.text(),
                                        self.time.text(),
                                        self.timescale.currentText(),
                                        self.foldercheck.isChecked())
            if saved == 'OK':
                self.addRule(self.nameline.text())

    def addRule(self, name):
            label = name
            QtGui.QListWidgetItem(label, self.rulelist)

    def viewRule(self):
        pass

    def deleteRule(self):
        #like delete folder
        # TODO: Delete Rule from Save
        for selectedRule in self.rulelist.selectedItems():
            self.rulelist.takeItem(self.rulelist.row(selectedRule))

    def ruleTest(self):
        pass
def main():

    app = QtGui.QApplication(sys.argv)
    woodhouse = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
