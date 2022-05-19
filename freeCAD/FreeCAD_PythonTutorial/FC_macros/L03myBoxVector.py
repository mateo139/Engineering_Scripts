from PySide import QtGui
val = QtGui.QInputDialog.getText(None, "Enter a value", "Please enter a value")[0]
myBox = FreeCAD.ActiveDocument.getObject("Box")
myTuple = tuple(val.split(','))
myBox.Placement.Base = FreeCAD.Vector(myTuple)

