import sys
from urllib.request import urlopen

from lxml import etree
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout

class Course(QObject):
	CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
	def get(self):
		with urlopen(self.CBR_URL) as r:
			tree = etree.parse(r)
			value = tree.xpath('*[@ID="R01235"]/Value')[0].text
			return float(value.replace(',','.'))

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._initUI()
		self._initSignals()
		self._initLayouts()

	def _initUI(self):
		self.setWindowTitle('Конвертер валют')

		self.srcLabel = QLabel('Сумма в рублях', self)
		self.resultLabel = QLabel('Сумма в долларах', self)

		self.srcAmountEdit = QDoubleSpinBox(self)
		self.srcAmountEdit.setMaximum(999999999)
		self.resultAmountEdit = QDoubleSpinBox(self)
		self.resultAmountEdit.setMaximum(999999999)

		self.convertBtn = QPushButton('Перевести', self)

		self.clearBtn = QPushButton('Очистить', self)

		self.convertBtn.setEnabled(False)



	def _initSignals(self):
		self.convertBtn.clicked.connect(self.onClickConvertBtn)

		self.srcAmountEdit.valueChanged.connect(self.enabled)
		self.resultAmountEdit.valueChanged.connect(self.enabled)	
			
		self.clearBtn.clicked.connect(self.onClickClearBtn)


	def _initLayouts(self):
		w = QWidget(self)

		self.mainLayout = QVBoxLayout(w)

		self.mainLayout.addWidget(self.srcLabel)
		self.mainLayout.addWidget(self.srcAmountEdit)
		self.mainLayout.addWidget(self.resultLabel)
		self.mainLayout.addWidget(self.resultAmountEdit)
		self.mainLayout.addWidget(self.convertBtn)
		self.mainLayout.addWidget(self.clearBtn)

		self.setCentralWidget(w)

	def enabled(self):
		v = self.srcAmountEdit.value()
		n = self.resultAmountEdit.value()
		if v and n or not v and not n:
			self.convertBtn.setEnabled(False)
		else:
			self.convertBtn.setEnabled(True)

	def onClickConvertBtn(self):
		value_rub = self.srcAmountEdit.value()
		if value_rub:
			self.resultAmountEdit.setValue(value_rub / Course().get())
		value_usd = self.resultAmountEdit.value()
		if value_usd:
			self.srcAmountEdit.setValue(value_usd * Course().get())
		

	def onClickClearBtn(self):
		self.resultAmountEdit.setValue(0)
		self.srcAmountEdit.setValue(0)
	

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Return:
			self.onClickConvertBtn()


if __name__ == "__main__":
	app = QApplication(sys.argv)

	converter = MainWindow()
	converter.show()

	sys.exit(app.exec_())