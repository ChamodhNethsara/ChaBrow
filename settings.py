from PyQt5.QtCore import QSettings,QUrl


settings = QSettings('The Insight Cafe Inc','Browser of Chamodh')
settings.setValue('Homepage', QUrl("https://www.google.com"))
settings.setValue('Google', 'https://www.google.com/search?q=')
settings.setValue('Yahoo', 'https://search.yahoo.com/search?p=')
settings.setValue('Youtube', 'https://www.youtube.com/results?search_query=')
settings.setValue("Default_Search_Engine","Google")