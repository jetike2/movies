from PyQt5 import QtCore, QtGui, QtWidgets
import json
import random
import webbrowser

genres = ["None","comedy", "sci-fi", "horror", "romance", "action", "thriller", "drama", "mystery", "crime","animation", "adventure", "fantasy"]



class Ui_MainWindow(object):
    def filt(self):
        self.listView.clear()
        with open("movies.json", "r") as f:
            data = json.load(f)
        for i in data["movies"]:
            if str(self.genre.currentText()) != "None":

                if self.name_searcher.text() in i["tilte"] and float(i["rating"]) >= self.rating_box.value() and i["genre"] == str(self.genre.currentText()) and int(i["year"]) >= int(self.year_min.text()) and int(i["year"]) <= int(self.year_max.text()):
                    item = i["tilte"]
                    self.listView.addItem(item)
            
            if str(self.genre.currentText()) == "None":

                if  self.name_searcher.text() in i["tilte"] and float(i["rating"]) >= self.rating_box.value() and int(i["year"]) >= int(self.year_min.text()) and int(i["year"]) <= int(self.year_max.text()):
                    item = i["tilte"] 
                    self.listView.addItem(item)

    def random_filt(self):
        l = []
        with open("movies.json", "r") as f:
            data = json.load(f)
        for i in data["movies"]:
            if str(self.genre.currentText()) != "None":

                if  self.name_searcher.text() in i["tilte"] and float(i["rating"]) >= self.rating_box.value() and i["genre"] == str(self.genre.currentText()) and int(i["year"]) >= int(self.year_min.text()) and int(i["year"]) <= int(self.year_max.text()):
                    l.append(i["link"]) 
            if str(self.genre.currentText()) == "None":

                if  self.name_searcher.text() in i["tilte"] and float(i["rating"]) >= self.rating_box.value() and int(i["year"]) >= int(self.year_min.text()) and int(i["year"]) <= int(self.year_max.text()):
                    l.append(i["link"]) 
        webbrowser.open(random.choice(l))
    
    def random_select(self):
        l = []
        with open("movies.json", "r") as f:
            data = json.load(f)
        for i in data["movies"]:
            l.append(i["link"])
        webbrowser.open(random.choice(l))

    def clicked(self):
        with open("movies.json", "r") as f:
            data = json.load(f)
        for i in data["movies"]:
            if i["tilte"] == self.listView.currentItem().text():
                current = i["link"]
        webbrowser.open(current)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(380, 0, 415, 350))
        self.listView.setObjectName("listView")
        self.listView.itemDoubleClicked.connect(self.clicked)
        self.rating_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rating_box.setGeometry(QtCore.QRect(280, 140, 69, 26))
        self.rating_box.setObjectName("rating_box")
        self.genre = QtWidgets.QComboBox(self.centralwidget)
        self.genre.setGeometry(QtCore.QRect(30, 20, 321, 25))
        self.genre.setObjectName("genre")
        for i in genres:
            self.genre.addItem(i)
        self.name_searcher = QtWidgets.QLineEdit(self.centralwidget)
        self.name_searcher.setGeometry(QtCore.QRect(30, 80, 321, 25))
        self.name_searcher.setObjectName("name_searcher")
        self.Filter = QtWidgets.QPushButton(self.centralwidget)
        self.Filter.setGeometry(QtCore.QRect(30, 220, 89, 25))
        self.Filter.setObjectName("Filter")
        self.Filter.clicked.connect(self.filt) 
        self.random = QtWidgets.QPushButton(self.centralwidget)
        self.random.setGeometry(QtCore.QRect(140, 220, 89, 25))
        self.random.setObjectName("random")
        self.random.clicked.connect(self.random_select)
        self.random_filter = QtWidgets.QPushButton(self.centralwidget)
        self.random_filter.setGeometry(QtCore.QRect(30, 260, 201, 25))
        self.random_filter.setObjectName("random_filter")
        self.random_filter.clicked.connect(self.random_filt)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 120, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 120, 67, 17))
        self.label_5.setObjectName("label_5")
        self.year_min = QtWidgets.QLineEdit(self.centralwidget)
        self.year_min.setGeometry(QtCore.QRect(30, 144, 81, 21))
        self.year_min.setObjectName("year_min")
        self.year_min.setText("0")
        self.year_max = QtWidgets.QLineEdit(self.centralwidget)
        self.year_max.setGeometry(QtCore.QRect(160, 141, 81, 21))
        self.year_max.setObjectName("year_max")
        self.year_max.setText("2020")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movies"))
        self.Filter.setText(_translate("MainWindow", "Filter"))
        self.random.setText(_translate("MainWindow", "Random"))
        self.random_filter.setText(_translate("MainWindow", "Random with benefits"))
        self.label.setText(_translate("MainWindow", "Genre"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Year from-"))
        self.label_4.setText(_translate("MainWindow", "Year to"))
        self.label_5.setText(_translate("MainWindow", "Rating"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

