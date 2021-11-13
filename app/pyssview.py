from PyQt5.QtWidgets import (QLineEdit ,QLabel, QMainWindow, QDialog, QApplication,
                             QListWidget, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
                             QAbstractItemView, QFormLayout, QGridLayout, QSpinBox, QProgressBar,
                             QMessageBox, QFileDialog,QToolButton, QStyle,QSpacerItem,QSizePolicy)
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from pyssview_ui import Ui_PyssviewMainWindow
import pickle
import sys
import os

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))

class Pyssview(QMainWindow, QDialog):
    def __init__(self):
        super(Pyssview, self).__init__()
        
        self.pview = Ui_PyssviewMainWindow()
        self.pview.setupUi(self)
        self.setWindowIcon(QIcon('{}/icons/logo3.svg'.format(ABSOLUT_PATH)))
        #Pyssview.loadChkboxState(self)
        
        self.data = {} #store data
        
        Pyssview.initUI(self)
        Pyssview.loadChkboxState(self)
        
    def initUI(self):
        """
        This function initialize objects like buttons etc
        """
        #buttons
        self.pview.btn_newpass.clicked.connect(self.addPasswords)
        self.pview.btn_removepass.clicked.connect(self.removePasswords)
        
        #Grids
        self.widget2scroll = QWidget()
        self.vbox2scroll = QVBoxLayout()
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vbox2scroll.addSpacerItem(spacerItem)
        
        #MenuBar
        self.pview.quitMenu.triggered.connect(self.close)
        self.pview.showhide_allMenu.triggered.connect(self.showHide_pass)
        self.pview.removeAll_Menu.triggered.connect(self.deleteAllPasswords)
        self.pview.saveMenu.triggered.connect(self.saveProfile)
        self.pview.loadMenu.triggered.connect(self.loadProfile)

    
    def closeEvent(self, event):
        """
        This function close application, but before execute
        the function "saveChkboxState"
        """
        Pyssview.saveChkboxState(self)
        #save file
        with open('{}/saves/sav.pkl'.format(ABSOLUT_PATH), 'wb') as filesave:
            pickle.dump(self.data, filesave, protocol=pickle.HIGHEST_PROTOCOL)
        self.close()

    def loadChkboxState(self):
        """
        This function load the file of status of the checkbox
        """
        with open('{}/states/state.dat'.format(ABSOLUT_PATH), 'r') as file:
            get = file.read()
            
        if get == '2':
            self.pview.chk_remember.setChecked(True)            
            
            with open('{}/saves/sav.pkl'.format(ABSOLUT_PATH), 'rb') as fp:
                data = pickle.load(fp)            
            self.data = data
            
            for id, login_pass_desc in self.data.items():        
                Pyssview.__displayPassword(self,
                                        login_pass_desc[0], login_pass_desc[1], login_pass_desc[2],
                                        objName=id, userid=id) #build fields
        else:
            self.pview.chk_remember.setChecked(False)    
                
    def saveChkboxState(self):
        """
        This function run a "checkState" function to get status of
        a checkbox, then save into a .dat file the state of checkbox.
        """
        get = self.pview.chk_remember.checkState()
        #checkOn
        if int(get) == 2:
            with open('{}/states/state.dat'.format(ABSOLUT_PATH), 'w') as fstate:
                fstate.write('2')
        #CheckOff
        else:
            with open('{}/states/state.dat'.format(ABSOLUT_PATH), 'w') as fstate:
                fstate.write('0')
    
    def saveProfile(self):
        """
        This function builds a dialog to get directory, then
        save profile.
        """
        get_dir, _ = QFileDialog.getSaveFileName(self, 'Save Profile', '')
        
        if get_dir.endswith('.pkl'):
            with open(get_dir, 'wb') as filesave:
                pickle.dump(self.data, filesave, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            with open(get_dir+'.pkl', 'wb') as filesave:
                pickle.dump(self.data, filesave, protocol=pickle.HIGHEST_PROTOCOL)
    
    def loadProfile(self):
        """
        This function builds a dialog to get directory, then
        load profile and create a field with password etc.
        """
        Pyssview.saveChkboxState(self)        
        try:
            get_dir, _ = QFileDialog.getOpenFileName(self, 'Open Profile', '', '(*.pkl) ;; all*') #open dir/namefile as a string
            with open(get_dir, 'rb') as fp:
                data = pickle.load(fp)            
            self.data = data
            
            for id, login_pass_desc in self.data.items():        
                Pyssview.__displayPassword(self,
                                        login_pass_desc[0], login_pass_desc[1], login_pass_desc[2],
                                        objName=id, userid=id) #build fields   
        except:
            pass   
            
    def showHide_pass(self):        
        if not self.pview.showhide_allMenu.isChecked():
            for ids in self.data.keys():
                print(ids)
                self.findChild(QLineEdit, ids).setEchoMode(QLineEdit.Normal)
        else:
            for ids in self.data.keys():
                print(ids)
                self.findChild(QLineEdit, ids).setEchoMode(QLineEdit.Password)
               
    def msgBox(self, msg='Warning'):
        """
        This function build a mini dialog with some mensage
        """
        Box = QMessageBox()
        Box.setIcon(QMessageBox.Warning)
        Box.setText(msg)
        Box.setWindowTitle("Warning!")
        Box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        Box.exec_()
        #msgBox.buttonClicked.connect(self.aff)  
    
    def removePasswords(self):
        get = Removepassdialog()
        get.setWindowTitle('Remove Account')
        get.setStyleSheet("background-color: rgba(84, 84, 84, 0.5);") 
        state = get.exec_() # show dialog
        
        userid = get.lineide.text()
        
        if state != 0:
            Pyssview.__deletePassword(self, id=userid)
            
    def deleteAllPasswords(self):
        ids = list(self.data.keys()).copy()
        for id in ids:
            print(id)
            self.findChild(QLineEdit, id).deleteLater()# REMOVE QLINE
            self.findChild(QLabel, id).deleteLater() # REMOVE QLABEL
            self.findChild(QLabel, id).deleteLater()
        
        self.data = {}
    
    def addAllPasswords(self):
        pass
                   
    def addPasswords(self):
        """
        This functions open a dialog by pressing "new password" button.
        collect datas like :login password etc.
        Then create a label/line with login, password etc.
        Store datas into a dictionary.
        """
        get = Addpassdialog()
        get.setWindowTitle('Add Account')
        get.setStyleSheet("background-color: rgba(84, 84, 84, 0.5);")          
                
        state = get.exec_() # show dialog
        
        #get values from the lines of add passwords dialog
        login = get.linelogin.text()
        password = get.linepassword.text()
        description = get.linedescription.text()
        userid = get.lineid.text()               
        
        if userid == '' or userid in self.data.keys():
            #Check if ID field is empty
            Pyssview.msgBox(self, msg='User ID already exists or incorrect.')
        else:
            #Check if dialog closed with button press or exit
            if state != 0:
                self.data[userid] = [login, password, description] #Store data into a dictionary  
                Pyssview.__displayPassword(self, login, password, description, objName=userid, userid=userid) #build fields
      
    def __displayPassword(self, login, password, desc, objName, userid):
        """
        This function builds a Label and QLine to show login and passwords 
        """        
        
        #Constructing Line and Labels
        idlab = QLabel('ID: {}'.format(userid))
        idlab.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color:rgb(238,238,236); font-size:16px")
        idlab.setObjectName(objName)
        
        if desc == '':
            log = QLabel('Login: {}'.format(login))            
        else:
            log = QLabel('Login: {} ({})'.format(login,desc))
        log.setObjectName(objName)
        log.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color:rgb(238,238,236); font-size:16px")
        
        #Create a Qbutton/Line modify
        passw = ButtonLineEdit('{}/icons/copy_clip.png'.format(ABSOLUT_PATH), objName=objName,tooltip_textLine=desc, tooltip_textBtn='Copy to Clipboard')
        passw.setStyleSheet("background-color: rgba(84, 84, 84, 0.4); color:rgb(238, 238, 236)")
        passw.setText(password)
        passw.buttonClicked.connect(lambda x:self.__copy2clipboard(password))
        passw.setObjectName(objName)
        passw.setEchoMode(QLineEdit.Password)
        
        #Put objects in grid
        self.vbox2scroll.insertWidget(0, idlab)
        self.vbox2scroll.insertWidget(1,log)
        self.vbox2scroll.insertWidget(2,passw)
        
        #put grid in scroll object
        self.widget2scroll.setLayout(self.vbox2scroll)        
        self.pview.scrollArea.setWidget(self.widget2scroll)
    
    def __deletePassword(self, id):
        """
        This function remove the objects bases on ID.
        """
        try:
            self.findChild(QLineEdit, id).deleteLater()# REMOVE QLINE
            self.findChild(QLabel, id).deleteLater() # REMOVE QLABEL
            self.findChild(QLabel, id).deleteLater()
            self.data.pop(id) #remove from dictionary        
        except AttributeError:
            Pyssview.msgBox(self, msg='The ID does not exist!')
       
    def __copy2clipboard(self, passw):
        """
        This function copy a text to clipboard
        """
        cpapp = QApplication.clipboard()
        cpapp.clear(mode=cpapp.Clipboard)
        cpapp.setText(passw, mode=cpapp.Clipboard)           
            
class Addpassdialog(QDialog):
    """
    This classe builds a Dialog window to colect data.
    """
    def __init__(self):
        super().__init__()
        
        self.resize(350, 150)
        self.labellogin = QLabel('Login:')
        self.labellogin.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color: rgb(238, 238, 236)")
        self.linelogin = QLineEdit()
        self.linelogin.setPlaceholderText('Account login.')
        self.linelogin.setStyleSheet("background-color: rgba(84, 84, 84, 0.4); color:rgb(238, 238, 236)")
        
        #self.linelogin.selectAll()       

        self.labelpassword = QLabel('Password:')
        self.labelpassword.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color:rgb(238,238,236)")
        self.linepassword = ButtonLineEdit('{}/icons/eye.png'.format(ABSOLUT_PATH), tooltip_textBtn='Hide/Show password')
        self.linepassword.setPlaceholderText('Account Password.')
        self.linepassword.setStyleSheet("background-color: rgba(84, 84, 84, 0.4); color:rgb(238, 238, 236)")
        self.linepassword.buttonClicked.connect(self.passwordform)
        self.linepassword.setEchoMode(QLineEdit.Password)
        #self.linepassword.selectAll()
        
        self.labeldescription = QLabel('Description:')
        self.labeldescription.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color:rgb(238,238,236)")
        self.linedescription = QLineEdit()
        self.linedescription.setPlaceholderText('Account Description.')
        self.linedescription.setStyleSheet("background-color: rgba(84, 84, 84, 0.4); color:rgb(238, 238, 236)")
        #self.linedescription.selectAll()
        
        self.labelid = QLabel('Identification:')
        self.labelid.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color:rgb(238,238,236)")
        self.lineid = QLineEdit()
        self.lineid.setPlaceholderText('Account ID.')
        self.lineid.setStyleSheet("background-color: rgba(84, 84, 84, 0.4); color:rgb(238, 238, 236)")
        
        self.button = QPushButton('OK')
        self.button.setStyleSheet("""QPushButton{
                                        background-color: rgb(52, 101, 190);
                                        color: rgb(238, 238, 236);
                                        border-radius: 7px;
                                        }
                                        QPushButton:hover {
                                        background-color: rgb(52, 101, 164);
                                        }
                                        QPushButton::pressed{
                                        background-color: rgb(52, 101, 120);
                                        }
                                """)
        self.button.setMinimumSize(0, 40)
        self.button.setMaximumSize(140, 500)
        self.button.clicked.connect(self.accept)
        
        #layout = QVBoxLayout()
        layout = QFormLayout()
        layout.addRow(self.labellogin, self.linelogin)
        #layout.addWidget(self.timelabel)
        layout.addRow(self.labelpassword,self.linepassword)
        layout.addRow(self.labeldescription, self.linedescription)
        layout.addRow(self.labelid, self.lineid)
        layout.addWidget(self.button)
        self.setLayout(layout)        
        
        
        self.cnt = 1
    def passwordform(self):
        #This function change password form to hidden/show
        if self.cnt % 2 == 0:
            get = self.linepassword.setEchoMode(QLineEdit.Password)
        else:
            get = self.linepassword.setEchoMode(QLineEdit.Normal)
        self.cnt += 1

class Removepassdialog(QDialog):
    """
    This classe builds a Dialog window to remove data.
    """
    def __init__(self):
        super().__init__()        
        self.resize(350, 110)
        self.labelide = QLabel('Identification:')
        self.labelide.setStyleSheet("background-color: rgba(84, 84, 84, 0.0); color: rgb(238, 238, 236)")
        self.lineide = QLineEdit()
        self.lineide.setPlaceholderText('Type the identification to remove.')
        self.lineide.setStyleSheet("background-color: rgba(84, 84, 84, 0.4); color:rgb(238, 238, 236)")
        
        #self.linelogin.selectAll()        
        
        self.button = QPushButton('OK')
        self.button.setStyleSheet("""QPushButton{
                                        background-color: rgb(52, 101, 190);
                                        color: rgb(238, 238, 236);
                                        border-radius: 7px;
                                        }
                                        QPushButton:hover {
                                        background-color: rgb(52, 101, 164);
                                        }
                                        QPushButton::pressed{
                                        background-color: rgb(52, 101, 120);
                                        }
                                """)
        self.button.setMinimumSize(0, 40)
        self.button.setMaximumSize(140, 500)
        self.button.clicked.connect(self.accept)
        
        #layout = QVBoxLayout()
        layout = QFormLayout()
        layout.addRow(self.labelide, self.lineide)        
        layout.addWidget(self.button)
        self.setLayout(layout)


class ButtonLineEdit(QLineEdit):
    """
    This classe is a implementation to build a QLine personalized.
    That is a QLine with img in right side
    """
    buttonClicked = pyqtSignal(bool)

    def __init__(self, icon_file, objName='', tooltip_textBtn='', tooltip_textLine='', parent=None):
        super(ButtonLineEdit, self).__init__(parent)

        self.button = QToolButton(self)
        self.button.setIcon(QIcon(icon_file))
        #self.button.setStyleSheet('border: 0px; padding: 0px; ')
        self.button.setStyleSheet(BTN_Qline)
        self.button.setCursor(QtCore.Qt.ArrowCursor)
        self.button.clicked.connect(self.buttonClicked.emit)
        self.button.setToolTip(tooltip_textBtn) #here we acess the QButton objects
        self.setToolTip(tooltip_textLine) #Here we acess the Qline objects
        self.setObjectName(objName)

        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        buttonSize = self.button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))

    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right() - frameWidth - buttonSize.width(),
                         (self.rect().bottom() - buttonSize.height() + 1)/2)
        super(ButtonLineEdit, self).resizeEvent(event)
        
BTN_Qline = """
QPushButton
{
border: 0px; padding: 0px;
background-color: rgb(52, 101, 190);
color: rgb(238, 238, 236);
border-radius: 7px;
}
QPushButton:hover {
background-color: rgb(52, 101, 164);
}
QPushButton::pressed{
background-color: rgb(52, 101, 120);
}
    """


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = Pyssview()
    gui.show()
    sys.exit(app.exec())
    