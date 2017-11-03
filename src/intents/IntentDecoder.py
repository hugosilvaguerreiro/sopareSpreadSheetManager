import sys
sys.path.insert(0, '../skills')
sys.path.insert(0, '../storage')
from Intent import *
from ClassifierSkill import *
from GreetIntent import *
from SpreadsheetIntent import *
from SpamIntent import *
from StorageAccesser import *


class IntentDecoder(Intent):
	def __init__(self, label=None):
		self.label = label
		self.storageAccesser = StorageAccesser()
		self.classifier = ClassifierSkill()
		self.intents = {"greet": GreetIntent("greet"), "spreadsheet" : SpreadsheetIntent("spreadsheet"),
						"spam" : SpamIntent("spam")}

	def execute(self, linus, inputReceived):
		label = self.classifier.classify(inputReceived)
		return self.intents[label]
