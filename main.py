import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import socket
import os
import platform
import datetime
import shutil
from distutils.dir_util import copy_tree
import time
import pytsk3

class MyApp(QWidget):
        
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initParser()

    def initUI(self):
        #layout settings : Grid Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        # tab1 = QWidget()
        # tabs = QTabWidget()
        # tabs.addTab(tab1, 'Tab1')
        
        self.main_tab = QWidget()
        self.collect_tab = QWidget()
        self.analysis_tab = QWidget()
        self.report_tab = QWidget()
        
        self.tabs = QTabWidget()
        self.tabs.addTab(self.main_tab, 'MAIN')
        self.tabs.addTab(self.collect_tab, 'COLLECT')
        self.tabs.addTab(self.analysis_tab, 'ANALYSIS')
        self.tabs.addTab(self.report_tab, 'REPORT')
        
        
        
        
        # btn1 = QPushButton('&Button1', self)
        # btn1.clicked.connect(self.func1)
        # button example
        
        # main_btn = QPushButton('MAIN', self)
        # collect_btn = QPushButton('COLLECT', self)
        # analysis_btn = QPushButton('ANALYSIS', self)
        # report_btn = QPushButton('REPORT', self)
        
        self.SelectFile_btn = QPushButton('Select file', self)
        self.SelectFile_btn.clicked.connect(self.fileopen)
        
        
        # label1 = QLabel('Label1', self)
        # label1.move(20, 20)
        # label example
        
        self.HostInfo_label = QLabel('Host Name', self)
        self.Account_label = QLabel('Account list', self)
        self.OSInfo_label = QLabel('OS(Build Version)', self)
        self.OSBootTime_label = QLabel('OS boot time(hour)', self)
        self.ParserExecTime_label = QLabel('Parser execution time', self)
        self.Filepath_label = QLabel('', self)
        
        
        
        self.HostInfo_textbox = QLineEdit()
        self.HostInfo_textbox.setReadOnly(True)
        self.Account_textbox = QLineEdit()
        self.Account_textbox.setReadOnly(True)
        self.OSInfo_textbox = QLineEdit()
        self.OSInfo_textbox.setReadOnly(True)
        self.OSBootTime_textbox = QLineEdit()
        self.OSBootTime_textbox.setReadOnly(True)
        self.ParserExecTime_textbox = QLineEdit()
        self.ParserExecTime_textbox.setReadOnly(True)
        self.ParserExecTime_textbox = QLineEdit()
        self.ParserExecTime_textbox.setReadOnly(True)
        
        self.FilePath_textbox = QLineEdit()
        self.FilePath_textbox.setReadOnly(True)
        
        
        
        self.log_textbox = QTextEdit()
        self.log_textbox.setAcceptRichText(False)
        self.log_textbox.setReadOnly(True)
        
        # grid.addWidget(QLabel('Title:'), 0, 0)
        # grid layout example
        
        # grid.addWidget(main_btn, 0, 0)
        # grid.addWidget(collect_btn, 0, 1)
        # grid.addWidget(analysis_btn, 0, 2)
        # grid.addWidget(report_btn, 0, 3)
        # layout example
        
        self.grid.addWidget(self.tabs, 0, 0)
        
        self.MainTab_layout = QGridLayout()
        self.main_tab.setLayout(self.MainTab_layout)
        
        self.MainTab_layout.addWidget(self.HostInfo_label, 1, 0)
        self.MainTab_layout.addWidget(self.HostInfo_textbox, 1, 1)
        self.MainTab_layout.addWidget(self.Account_label, 2, 0)
        self.MainTab_layout.addWidget(self.Account_textbox, 2, 1)
        self.MainTab_layout.addWidget(self.OSInfo_label, 3, 0)
        self.MainTab_layout.addWidget(self.OSInfo_textbox, 3, 1)
        self.MainTab_layout.addWidget(self.OSBootTime_label, 4, 0)
        self.MainTab_layout.addWidget(self.OSBootTime_textbox, 4, 1)
        self.MainTab_layout.addWidget(self.ParserExecTime_label, 5, 0)
        self.MainTab_layout.addWidget(self.ParserExecTime_textbox, 5, 1)
        self.MainTab_layout.addWidget(self.FilePath_textbox, 6, 0)
        self.MainTab_layout.addWidget(self.SelectFile_btn, 6, 1)
        self.MainTab_layout.addWidget(self.log_textbox, 7, 0, 1, 2)
        
        
        
        self.setWindowTitle('parser')
        self.setGeometry(300, 300, 500, 500)
        self.show()
        
        
        
    def fileopen(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.FilePath_textbox.setText(folder)
        self.Parsing(folder)
    
    
    def initParser(self):
        self.HostInfo_textbox.setText(str(socket.gethostname()))
        self.Account_textbox.setText(str(os.getlogin()))
        if(str(os.getlogin()) != 'administrator'):
            QMessageBox.question(self, 'Message', 'Administrator privileges are recommended',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        self.OSInfo_textbox.setText(str(platform.system()+platform.version()))
        self.OSBootTime_textbox.setText(str(int(time.monotonic()/3600)))
        self.ParserExecTime_textbox.setText(str(datetime.datetime.now()))
        
    def Parsing(self, folder):
        users = os.listdir(r'C:\Users')

        for user in users:
            try:
                if os.path.isdir('C:\\Users\\'+user):
                    self.log_textbox.append('Collect ' + user + ' artifact')
                    self.Browser(user,folder)
                    self.FileSystem('C:', folder)
                    
                    self.log_textbox.append('')
            except Exception as ex:
                self.log_textbox.append(str(ex))
        
        
    def Browser(self, user, folder):
        self.log_textbox.append('[*] Collect browser artifact')
        self.Chrome(user, folder)
        
        
    def Chrome(self, user, folder):
        path = 'C:/Users/'+user
        self.log_textbox.append("[*] Chrome Browser artifact Collecting...")
        check = os.path.isdir(path+"/AppData/Local/Google")
    
        if check == False:
            self.log_textbox.append("[!] Not Found Chrome Path... Default Path is invalid")
            self.log_textbox.append("[!] Default path is " + path + "/AppData/Local/Google")
            
        else:
            self.log_textbox.append("[!] Chrome Directory Path: "+path+"/AppData/Local/Google")
            self.log_textbox.append("[+] Chrome History, Cache, Cookies, Download List Copying...")

            history = path+"/AppData/Local/Google/Chrome/User Data/Default/History"
            cookies = path+"/AppData/Local/Google/Chrome/User Data/Default/Cookies"
            cache = path+"/AppData/Local/Google/Chrome/User Data/Default/Cache/"
            
            CopyFile(history, folder + '/' +user + "/History")
            CopyFile(cookies, folder + '/' +user + "/Cookies")
            CopyDirectory(cache, folder + '/' +user + "/Cache")


    def FileSystem(self, drive, folder):
        self.log_textbox.append('[*] Collect filesystem artifact of '+ drive + ' drive')
        
        volume='\\\\.\\' + drive #드라이브
        img=pytsk3.Img_Info(volume) #드라이브 파일 핸들 생성
        fs=pytsk3.FS_Info(img) #파일 핸들 이용해서 드라이브 내부 정보
        
        
        self.MFT(folder, fs)
        self.LogFile(folder, fs)
        self.Extract_UsnJrnl(folder, fs)
    
    def MFT(self, folder, fs):
        self.log_textbox.append('[*] Collect $MFT')
        self.Extract('/$MFT', folder, fs)
        
    def LogFile(self, folder, fs):
        self.log_textbox.append('[*] Collect $LogFile')
        self.Extract('/$LogFile', folder, fs)
        
    def Extract_UsnJrnl(self, folder, fs):
        self.log_textbox.append('[*] Collect $UsnJrnl')
        try:
            f=fs.open('/$Extend/$UsnJrnl')
            found=False
            
            for attr in f:
                if attr.info.name == b'$J':
                    found=True
                    break
            if not found:
                self.log_textbox.append('[!] $UsnJrnl not found')
            else:
                self.log_textbox.append('[*] $UsnJrnl exists, start copying')
                with open(folder + '/$UsnJrnl','wb') as o:
                    offset=0
                    size=attr.info.size
                    while offset < size:
                        available_to_read = min(1024*1024,size-offset)
                        buf = f.read_random(offset, available_to_read, attr.info.type, attr.info.id) #attr.info.type,attr.info.id
                        if not buf:
                            break
                        o.write(buf)
                        offset += len(buf)
        except Exception as ex:
            self.log_textbox.append('[!] Error occured while collecting $UsnJrnl')
        
        
        
    def Extract(self, filename, folder, fs):
        try:
            f=fs.open(filename)
            with open(folder + filename,'wb') as o:
                self.log_textbox.append('[*] ' + filename + ' exists, start copying')
                offset = 0
                size = f.info.meta.size
                while offset<size:
                    available_to_read = min(1024*1024,size-offset)
                    buf = f.read_random(0,available_to_read)
                    if not buf: break
                    o.write(buf)
                    offset += len(buf)
        except Exception as ex:
            self.log_textbox.append('[!] Error occured while collecting '+ filename)
            self.log_textbox.append(str(ex))
        
        
    def CopyFile(self, src, dst):
        if not os.path.isfile(src):
            self.log_textbox.append('[!] ' + src + ' doen not exist')
        else:
            self.Create(dst)
            self.log_textbox.append('[*] Start copying file from ' + src + ' to ' + dst)
            shutil.copy2(src, dst)
            
    
    def CopyDirectory(self, src, dst):
        self.Create(dst)
        self.log_textbox.append('[*] Start copying directory from ' + src + ' to ' + dst)
        copy_tree(src, dst)
        
        
    def Create(self, folder):
        if not os.path.isdir(folder):
            self.log_textbox.append('[!] ' + folder + ' does not exist, create folder')
            os.mkdir(folder)
        
        
        
        
        
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
