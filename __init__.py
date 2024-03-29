from anki.hooks import wrap
from aqt.browser import Browser, DataModel
from PyQt5 import QtGui, QtWidgets, QtCore


def initField(self, card=None, search=None):

    form = self.form

    try:
        searchButton = form.searchButton
    except:
        searchButton = form.searchEdit

    try:
        previewButton = form.previewButton
    except:
        previewButton = None

    self.countField = QtWidgets.QLabel("0")

    label = QtWidgets.QLabel("Count: ")

    label.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

    self.countField.setSizePolicy(
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
    )

    grid = form.gridLayout

    grid.addWidget(label, 0, 2)
    grid.addWidget(self.countField, 0, 3)
    grid.addWidget(searchButton, 0, 4)
    if previewButton:
        grid.addWidget(previewButton, 0, 5)


def updateField(self, txt):
    try:
        self.browser.countField.setText(str(len(self.cards)))
    except AttributeError as e:
        pass


Browser.setupSearch = wrap(Browser.setupSearch, initField)
DataModel.search = wrap(DataModel.search, updateField)
