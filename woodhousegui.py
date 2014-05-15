from PySide import QtGui
import sys

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle('Woodhouse')
        self.setGeometry(300, 300, 250, 350)

        #the left side of the window with the folders
        folderbar = QtGui.QLabel('Folders')
        self.folderlist = QtGui.QListWidget(self)
        self.folderlist.SingleSelection
        folderaddbutton = QtGui.QPushButton('Add',self)
        folderaddbutton.clicked.connect(self.addFolder)
        folderdeletebutton = QtGui.QPushButton('Delete', self)
        folderdeletebutton.clicked.connect(self.deleteFolder)

        #the right side of the window with the rules
        rulebar = QtGui.QLabel('Rules')
        self.rulelist = QtGui.QListWidget(self)
        self.rulelist.SingleSelection
        ruleaddbutton = QtGui.QPushButton('Add', self)
        ruleaddbutton.clicked.connect(self.addRule)
        ruledeletebutton = QtGui.QPushButton('Delete', self)
        ruledeletebutton.clicked.connect(self.deleteRule)
        ruletestbutton = QtGui.QPushButton('Test Rule', self)
        ruletestbutton.clicked.connect(self.ruleTest)

        #GridLayout

        #left side
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(folderbar, 0, 0)
        self.grid.addWidget(self.folderlist,1, 0, 1, 2)
        self.grid.addWidget(folderaddbutton, 2, 0)
        self.grid.addWidget(folderdeletebutton, 2, 1)
        #space between the lists
        self.grid.addWidget(QtGui.QLabel(''),0, 2, 1, 5)
        #right side
        self.grid.addWidget(rulebar, 0, 3)
        self.grid.addWidget(self.rulelist, 1, 3, 1, 3)
        self.grid.addWidget(ruleaddbutton, 2, 3)
        self.grid.addWidget(ruledeletebutton, 2, 4)
        self.grid.addWidget(ruletestbutton,2 , 5)
        self.setLayout(self.grid)
        self.show()

    def addFolder(self):
        #select Folder and display it
        folderselect = QtGui.QFileDialog()
        folderselect.setFileMode(QtGui.QFileDialog.Directory)
        folderselect.setOption(QtGui.QFileDialog.ShowDirsOnly)
        folder = ''
        if folderselect.exec_():
            folder = folderselect.selectedFiles()
            #to Display the Path in the List, we first copy
            #the data in a new variable, it has the form of
            #['u/path/to/blerg'] we slice the first 3 and the 
            #last 2
            showfolder = folder
            showfolder = str(showfolder)[3:-2]
            QtGui.QListWidgetItem(showfolder, self.folderlist)
            

    def deleteFolder(self):
        #wow since adding was so easy i thoght removing is as well
        #but apprently not. the right methode is to takeitem()
        #https://stackoverflow.com/questions/7484699/pyqt4-remove-item-widget-from-qlistwidget
        for selectedfolder in self.folderlist.selectedItems():
            self.folderlist.takeItem(self.folderlist.row(selectedfolder))


    def addRule(self):
        pass

    def deleteRule(self):
        pass

    def ruleTest(self):
        pass
def main():

    app = QtGui.QApplication(sys.argv)
    woodhouse = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
