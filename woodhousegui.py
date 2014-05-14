from PySide import QtGui
import sys

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle('Woodhouse')
        self.setGeometry(300, 300, 250, 150)

        #the left side of the window with the folders
        folderbar = QtGui.QLabel('Folders')
        folderlist = QtGui.QListWidget(self)
        folderlist.SingleSelection
        folderaddbutton = QtGui.QPushButton('Add',self)
        folderaddbutton.clicked.connect(self.addFolder)
        folderdeletebutton = QtGui.QPushButton('Delete', self)
        folderdeletebutton.clicked.connect(self.deleteFolder)

        rulebar = QtGui.QLabel('Rules')
        rulelist = QtGui.QListWidget(self)

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(folderbar, 0, 0)
        self.grid.addWidget(folderlist,1, 0)
        self.grid.addWidget(folderaddbutton, 2, 0)
        self.grid.addWidget(folderdeletebutton, 2, 1)
        self.grid.addWidget(rulebar, 0, 1)
        self.grid.addWidget(rulelist, 1, 1)
        self.setLayout(self.grid)
        self.show()

    def addFolder(self):
        pass

    def deleteFolder(self):
        pass

def main():

    app = QtGui.QApplication(sys.argv)
    woodhouse = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
