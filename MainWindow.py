from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import requests
import validators
from settings import settings
from urllib.parse import quote
from xml.etree import ElementTree as ET 







class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #settings
        self.settings = settings

        self.loading_label = QLabel()
        self.loading_movie = QtGui.QMovie('icons/loading.gif')
        

        
        
        
        



        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.browser = QWebEngineView()
        self.browser.setUrl(self.settings.value('Homepage'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        
        
        
        
        
           
        

        '''
        menu_bar = QMenuBar()
        bar_menu = QMenu("Main",self)
        bar_menu.setStyleSheet("QMenu {background: rgb(255,255,255)}")
        bar_menu.setIcon(QtGui.QIcon("icons/menu.png"))
        menu_bar.addMenu(bar_menu)
        self.setMenuBar(menu_bar)
        '''

        self.navbar = QToolBar()
        self.navbar_top = QToolBar()
        self.navbar.setStyleSheet("QToolBar {background: rgb(255, 255, 254)}")
        self.navbar_top.setStyleSheet("QToolBar {background: rgb(0, 2, 1)}")

        self.navbar.setMovable(False)
        self.navbar_top.setMovable(False)

        self.navbar_top.setMinimumHeight(30)
        
        
        self.addToolBar(Qt.BottomToolBarArea,self.navbar_top)
        self.addToolBar(self.navbar)
           

        


        back_btn = QAction('Back', self)
        back_btn.setIcon(QtGui.QIcon('icons/back.png'))

        back_btn.triggered.connect(self.browser.back)
        self.navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.setShortcut("Ctrl+N")
        
        forward_btn.setIcon(QtGui.QIcon('icons/next.png'))

        forward_btn.triggered.connect(self.browser.forward)
        self.navbar.addAction(forward_btn)


        
        self.label = QLabel()
        self.navbar_top.addWidget(self.loading_label) 
        self.navbar_top.setStyleSheet("QWidget {padding-right: 10px;}")
        self.navbar_top.setMaximumHeight(30)
        
        self.navbar_top.addWidget(self.label)
        self.browser.titleChanged.connect(self.label.setText)


        


        

        home_btn= QAction('home', self)
        home_btn.setShortcut("Ctrl+H")
        home_btn.setIcon(QtGui.QIcon('icons/home.png'))

        home_btn.triggered.connect(self.navigate_home)
        self.navbar.addAction(home_btn)
        
        self.url_bar = QLineEdit()
        
        self.url_bar.textEdited.connect(self.suggest)
        self.url_bar.setStyleSheet("QLineEdit {color: rgb(255,0,0);border-radius: 20px ;}")




       
        self.search_btn = QPushButton()
        
        self.search_btn.setIcon(QtGui.QIcon("icons/search.png"))

        self.search_btn.clicked.connect(self.search)
        
        self.url_bar.setPlaceholderText("Enter a URL here to go!")
        self.url_bar.returnPressed.connect(self.search)
        
        self.navbar.addWidget(self.url_bar)
        self.navbar.addWidget(self.search_btn)
        ref_btn = QAction('refesh', self)
        ref_btn.setShortcut('Ctrl+R')
        ref_btn.setIcon(QtGui.QIcon('icons/refresh.png'))
        
        ref_btn.triggered.connect(self.browser.reload)
        self.navbar.addAction(ref_btn)

        self.browser.urlChanged.connect(self.update_url)


        ######################################################




    
        
        self.browser.loadStarted.connect(self.start)
        self.browser.loadFinished.connect(self.stop)


    def start(self):
        self.loading_label.setMovie(self.loading_movie)

        self.loading_movie.start()
    
    def stop(self):
        self.loading_movie.stop()
        self.loading_label.clear()
        

    def navigate_home(self):

        
        
        self.browser.setUrl(QUrl('http://google.lk'))

        

 
        

    def search(self):
        Default_Search_Engine = self.settings.value("Default_Search_Engine")
        
        text = self.url_bar.text()
        if validators.url(text):
            self.browser.setUrl(QUrl(text))
            

        else:
            text = quote(text)
            url = self.settings.value(Default_Search_Engine)+text
            
            self.browser.setUrl(QUrl(url))
            print(text)
            print(type(url))
            

    def suggest(self):

        suggestlist =[]

        term = self.url_bar.text()
        if not validators.url(term) :
            url = f"http://toolbarqueries.google.com/complete/search?q={term}&output=toolbar&hl=en"

            suggestions = requests.get(url)
            suggestions = ET.fromstring(suggestions.content)
            for data in suggestions.iter('suggestion'):
                suggestlist.append(data.attrib['data'])
        
        print(suggestlist)
        suggester = QCompleter(suggestlist)
        self.url_bar.setCompleter(suggester)
            




    def update_url(self, changed_url):
        self.url_bar.setText(changed_url.toString())

