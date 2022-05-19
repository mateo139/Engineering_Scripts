import FreeCAD
import Part

App.newDocument()
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")

box = App.ActiveDocument.addObject("Part::Box","Box")
box.Placement = App.Placement(App.Vector(1,1,1),App.Rotation(0,0,0,1))
box.Height = 5.00
box.Length = 5.00
box.Width = 5.00

sphere = App.ActiveDocument.addObject("Part::Sphere","Sphere")
sphere.Placement = App.Placement(App.Vector(5,5,5),App.Rotation(0,0,0,1))

App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")