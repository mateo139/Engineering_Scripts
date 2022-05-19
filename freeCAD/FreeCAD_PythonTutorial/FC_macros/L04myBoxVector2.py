from PySide import QtGui
val = QtGui.QInputDialog.getText(None, "Enter a value", "Please enter a value")[0]
splitValues = val.split(',')

if len(splitValues) == 3:
	(x, y, z)= splitValues
	FreeCAD.Console.PrintMessage(y)
else:
	FreeCAD.Console.PrintMessage("Max/Min length must equal 3")


