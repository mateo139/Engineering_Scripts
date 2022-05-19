# Hyperbola Creator - Version 0.7
'''
***************************************************************************
*   Copyright (c) 2015 <quick61>                                          *
*                                                                         *
*   This file is a supplement to the FreeCAD CAx development system.      *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU  General Public License (GPL)           *
*   as published by the Free Software Foundation; either version 3 of     *
*   the License, or (at your option) any later version.                   *
*   for detail see the LICENCE text file.                                 *
*                                                                         *
*   This software is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU Library General Public License for more details.                  *
*                                                                         *
*   You should have received a copy of the GNU General Public License     *
*   License along with this macro; if not, write to the Free Software     *
*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
*   USA                                                                   *
***************************************************************************
'''


_Title__="Hyperbola Creator"
__Author__ = "Quick61"
__Version__ = "00.11"
__Date__    = "16/06/2015"


__Comment__ = "This macro creates ..."


__Web__ = "http://forum.freecadweb.org/viewtopic.php?f=22&t=11328"
__Wiki__ = "http://www.freecadweb.org"
__Icon__  = "/usr/lib/freecad/Mod/plugins/FreeCAD-macros/icons/HyperbolaIcon.png"
__IconW__  = "C:/Documents and Settings/YourUserName/Application Data/FreeCAD"
__Help__ = "start the macro and follow the instructions"
__Status__ = ""
__Requires__ = ""
__Communication__ = "https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=2030"


import FreeCAD, FreeCADGui, Part, PySide
from FreeCAD import Base
from PySide import QtCore, QtGui
from PySide.QtGui import QLineEdit, QRadioButton
App=FreeCAD

#+ hack
import sys,traceback
def sayexc(mess=''):
	exc_type, exc_value, exc_traceback = sys.exc_info()
	ttt=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
	lls=eval(ttt)
	l=len(lls)
	l2=lls[(l-3):]
	FreeCAD.Console.PrintError(mess + "\n" +"-->  ".join(l2))

class p():

    def makeHyp(self):

        if self.radio1.isChecked():
            try:

                Mi = float(self.r1.text())
                Ma = float(self.r2.text())
                tS1 = float(self.s1.text())
                tS2 = float(self.s2.text())

                hyp=Part.Hyperbola()
                hyp.MinorRadius=Mi
                hyp.MajorRadius=Ma

                shape=hyp.toShape(tS1,tS2)
                Part.show(shape)

            except:
                sayexc()
                FreeCAD.Console.PrintError("Unable to complete task")

            self.close()


        if self.radio2.isChecked():
            try:

                Mi = float(self.r1.text())
                Ma = float(self.r2.text())
                tS1 = float(self.s1.text())
                tS2 = float(self.s2.text())
                Dg = float(self.Dg.text())

                hyp=Part.Hyperbola()
                hyp.MinorRadius=Mi
                hyp.MajorRadius=Ma

                shape=hyp.toShape(tS1,tS2)
                rev=shape.revolve(App.Vector(0,0,0),App.Vector(0,1,0),Dg) # revolve around Y axis by number of degrees
                Part.show(rev)
            except:
                sayexc()
                FreeCAD.Console.PrintError("Unable to complete task")

            self.close()

    def close(self):
        self.dialog.hide()



    def __init__(self):
        self.dialog = None

        self.dialog = QtGui.QDialog()
        self.dialog.resize(280,110)

        self.dialog.setWindowTitle("Hyperbola Creator")
        la = QtGui.QVBoxLayout(self.dialog)

        self.radio1 = QRadioButton("Make 2D Shape")
        self.radio2 = QRadioButton("Make 3D Revolution")

# # # #
# set default to "Make 2D Shape" & make radio buttons - Change self.radio1.setChecked(True) to
# self.radio2.setChecked(True) to set "Make 3D Revolution" as default
# # # #

        self.radio1.setChecked(True)
        la.addWidget(self.radio1)
        la.addWidget(self.radio2)

        iN1 = QtGui.QLabel("Minor Radius")
        la.addWidget(iN1)
        self.r1 = QtGui.QLineEdit()
        la.addWidget(self.r1)
        self.r1.setText('2')

        iN2 = QtGui.QLabel("Major Radius")
        la.addWidget(iN2)
        self.r2 = QtGui.QLineEdit()
        la.addWidget(self.r2)
        self.r2.setText('3')

        iN3 = QtGui.QLabel("Range Of Curve - Minimum")
        la.addWidget(iN3)
        self.s1 = QtGui.QLineEdit()
        la.addWidget(self.s1)
        self.s1.setText('-2')

        iN4 = QtGui.QLabel("Range Of Curve - Maximum")
        la.addWidget(iN4)
        self.s2 = QtGui.QLineEdit()
        la.addWidget(self.s2)
        self.s2.setText('2')

        iN5 = QtGui.QLabel("Degrees of Revolve (Only valid for 3D Revolution)")
        la.addWidget(iN5)
        self.Dg = QtGui.QLineEdit()
        self.Dg.insert("360")
        la.addWidget(self.Dg)

        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        la.addWidget(okbox)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.makeHyp)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()

p()