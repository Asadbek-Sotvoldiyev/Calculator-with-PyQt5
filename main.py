from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QCheckBox, QRadioButton, QButtonGroup, \
    QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit

app = QApplication([])

btn_style = """
    QPushButton{
        background-color: #4CAF50;
        color: white;
        font-size: 24px;
        border-radius: 5px;
        height: 40px;
    }

"""

amal_style = """
    QPushButton{
    background-color: #eb8b0e;
    color: white;
    font-size: 24px;
    border-radius: 5px;
    height: 40px;
    }
"""

equal_style = """
    QPushButton{
    background-color: red;
    color: white;
    font-size: 24px;
    border-radius: 5px;
    height: 40px;
    }
"""

line_edit = """
    padding: 15px;
    font-size: 24px;
    border: 2px solid #4CAF50;
    border-radius: 10px;
    background-color: #ffffff;
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300, 400, 400)
        self.setFixedSize(400, 400)
        vertical = QVBoxLayout()

        self.edit = QLineEdit()
        self.edit.setStyleSheet(line_edit)
        vertical.addWidget(self.edit)

        self.misol = ""
        start = 1
        for _ in range(3):
            horizontal = QHBoxLayout()
            end = start + 3
            for j in range(start, end):
                btn = QPushButton(str(j))
                btn.setStyleSheet(btn_style)
                btn.clicked.connect(self.bosildi)
                horizontal.addWidget(btn)
            vertical.addLayout(horizontal)
            start = end

        devide = QPushButton("/")
        multiple = QPushButton("*")
        clear = QPushButton("C")

        devide.setStyleSheet(amal_style)
        multiple.setStyleSheet(amal_style)
        clear.setStyleSheet(equal_style)

        horizont1 = QHBoxLayout()
        horizont1.addWidget(devide)
        horizont1.addWidget(multiple)
        horizont1.addWidget(clear)

        devide.clicked.connect(self.bosildi)
        multiple.clicked.connect(self.bosildi)
        clear.clicked.connect(self.clear)

        vertical.addLayout(horizont1)

        plus_btn = QPushButton("+")
        minus_btn = QPushButton("-")
        equal_btn = QPushButton("=")

        plus_btn.setStyleSheet(amal_style)
        minus_btn.setStyleSheet(amal_style)
        equal_btn.setStyleSheet(equal_style)

        horizont = QHBoxLayout()
        horizont.addWidget(plus_btn)
        horizont.addWidget(minus_btn)
        horizont.addWidget(equal_btn)

        vertical.addLayout(horizont)

        plus_btn.clicked.connect(self.bosildi)
        minus_btn.clicked.connect(self.bosildi)
        equal_btn.clicked.connect(self.equal)



        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)

    def bosildi(self):
        btn = self.sender()
        self.misol += btn.text()
        self.edit.setText(self.misol)


    def equal(self):
        result = eval(self.edit.text())
        self.edit.setText(str(result))

    def clear(self):
        self.misol = ""
        self.edit.setText("")



window = MainWindow()
window.show()
app.exec_()