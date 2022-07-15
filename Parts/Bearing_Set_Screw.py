import Part
import Sketcher

try:
    App.getDocument('Bearing_Set_Screw')
    App.closeDocument('Bearing_Set_Screw')
except:
    pass

App.newDocument('Bearing_Set_Screw')

# BodyBase
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyBase')
App.ActiveDocument.recompute()

# BodyBaseSketch
App.ActiveDocument.getObject('BodyBase').newObject('Sketcher::SketchObject','BodyBaseSketch')
App.ActiveDocument.getObject('BodyBaseSketch').Support = (App.ActiveDocument.getObject('XY_Plane'),[''])
App.ActiveDocument.getObject('BodyBaseSketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),2.000000),False)
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Coincident',1,3,0,3))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Diameter',0,4.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(2,App.Units.Quantity('22.000000 mm'))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Diameter',1,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(3,App.Units.Quantity('20.000000 mm'))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyBase').newObject('PartDesign::Pad','Pad')
App.ActiveDocument.getObject('Pad').Profile = App.ActiveDocument.getObject('BodyBaseSketch')
App.ActiveDocument.getObject('Pad').Length = 7.000000
App.ActiveDocument.getObject('BodyBaseSketch').Visibility = False
App.ActiveDocument.recompute()

# BodyCenter
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyCenter')
App.ActiveDocument.recompute()

# BodyCenterSketch
App.ActiveDocument.getObject('BodyCenter').newObject('Sketcher::SketchObject','BodyCenterSketch')
App.ActiveDocument.getObject('BodyCenterSketch').Support = (App.ActiveDocument.getObject('XY_Plane001'),[''])
App.ActiveDocument.getObject('BodyCenterSketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyCenterSketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),2.000000),False)
App.ActiveDocument.getObject('BodyCenterSketch').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
App.ActiveDocument.getObject('BodyCenterSketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyCenterSketch').addConstraint(Sketcher.Constraint('Coincident',1,3,0,3))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyCenterSketch').addConstraint(Sketcher.Constraint('Diameter',0,4.000000))
App.ActiveDocument.getObject('BodyCenterSketch').setDatum(2,App.Units.Quantity('10.000000 mm'))
App.ActiveDocument.getObject('BodyCenterSketch').addConstraint(Sketcher.Constraint('Diameter',1,2.000000))
App.ActiveDocument.getObject('BodyCenterSketch').setDatum(3,App.Units.Quantity('8.000000 mm'))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyCenter').newObject('PartDesign::Pad','Pad001')
App.ActiveDocument.getObject('Pad001').Profile = App.ActiveDocument.getObject('BodyCenterSketch')
App.ActiveDocument.getObject('Pad001').Length = 14.000000
App.ActiveDocument.getObject('BodyCenterSketch').Visibility = False
App.ActiveDocument.recompute()

# BodyFill
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyFill')
App.ActiveDocument.getObject('BodyFill').Placement = App.Placement(App.Vector(0,0,0.250000),App.Rotation(App.Vector(0,0,1),0))
App.ActiveDocument.getObject('BodyFill').ViewObject.ShapeColor = (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.0)
App.ActiveDocument.recompute()

# BodyFillSketch
App.ActiveDocument.getObject('BodyFill').newObject('Sketcher::SketchObject','BodyFillSketch')
App.ActiveDocument.getObject('BodyFillSketch').Support = (App.ActiveDocument.getObject('XY_Plane002'),[''])
App.ActiveDocument.getObject('BodyFillSketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyFillSketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),2.000000),False)
App.ActiveDocument.getObject('BodyFillSketch').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
App.ActiveDocument.getObject('BodyFillSketch').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyFillSketch').addConstraint(Sketcher.Constraint('Coincident',1,3,0,3))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyFillSketch').addConstraint(Sketcher.Constraint('Diameter',0,4.000000))
App.ActiveDocument.getObject('BodyFillSketch').setDatum(2,App.Units.Quantity('20.000000 mm'))
App.ActiveDocument.getObject('BodyFillSketch').addConstraint(Sketcher.Constraint('Diameter',1,2.000000))
App.ActiveDocument.getObject('BodyFillSketch').setDatum(3,App.Units.Quantity('10.000000 mm'))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyFill').newObject('PartDesign::Pad','Pad002')
App.ActiveDocument.getObject('Pad002').Profile = App.ActiveDocument.getObject('BodyFillSketch')
App.ActiveDocument.getObject('Pad002').Length = 6.500000
App.ActiveDocument.getObject('BodyFillSketch').Visibility = False
App.ActiveDocument.recompute()

# Compound
Gui.activateWorkbench('PartWorkbench')
App.ActiveDocument.addObject('Part::Compound','Compound')
App.ActiveDocument.Compound.Links = [App.ActiveDocument.getObject('BodyBase'),
App.ActiveDocument.getObject('BodyCenter'),
App.ActiveDocument.getObject('BodyFill'),]
App.ActiveDocument.recompute()

# View Fit
Gui.ActiveDocument.activeView().setCameraType('Perspective')
Gui.ActiveDocument.activeView().viewTrimetric()
Gui.SendMsgToActiveView('ViewFit')
