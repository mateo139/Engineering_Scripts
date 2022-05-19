from PySide import QtGui
userInputValue = QtGui.QInputDialog.getText(None, "Enter a value", "Please enter a value")[0]
FreeCAD.Console.PrintMessage(userInputValue)