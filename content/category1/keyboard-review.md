Title: My super title
Date: 1010-12-03 10:20
Modified: 2010-12-05 19:30
Tags: pelican, publishing
Slug: 123456
Authors: abc
Summary: Short version for index and feeds

Following is a review of my favorite mechanical keyboard.Following is a review of my favorite mechanical keyboard.Following is a review of my favorite mechanical keyboard.Following is a review of my favorite mechanical keyboard.Following is a review of my favorite mechanical keyboard.Following is a review of my favorite mechanical keyboard.Following is a review of my favorite mechanical keyboard.

```
# -*- coding: utf-8 -*-
__author__      = "yicho80@gmail.com"
__copyright__   = "Copyright 2019"

import os
import sys

from logger import MyLogger
from helper import *

logger = MyLogger.__call__().get_logger()

sys.path.append(os.path.relpath('./modules'))
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('main.ui')[0]
class MainWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

	def closeEvent(self, event):
		close = QtWidgets.QMessageBox.question(self, "QUIT")
		if close == QtWidgets.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore

class SandboxApp(QApplication):
    def __init__(self, *args, **kwargs):
        super(SandboxApp, self).__init__(*args)
        self.mainwindow = MainWindow()
        self.mainwindow.show()

if __name__ == '__main__':
    app = SandboxApp(sys.argv)
    sys.exit(app.exec_())
```

[Alt Text]({static}/assets/images/Jellyfish.jpg)