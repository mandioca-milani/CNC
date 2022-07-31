# Document

for doc in App.listDocuments():
    App.closeDocument(doc)

docs = [
    '/Parts/Sketches.FCStd',
]

for doc in docs:
    App.openDocument(os.getcwd() + doc, hidden=True)

if os.path.isfile(os.getcwd() + '/Axis/AxisEngine.FCStd'):
    App.openDocument(os.getcwd() + '/Axis/AxisEngine.FCStd')
else:
    App.newDocument('AxisEngine')
    App.ActiveDocument.saveAs(os.getcwd() + '/Axis/AxisEngine.FCStd')

Gui.activateWorkbench("PartDesignWorkbench")


# Body001Nema17

if App.ActiveDocument.getObject('Body001Nema17'):
    App.ActiveDocument.getObject('Body001Nema17').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body001Nema17')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body001Nema17'))


# Sketch001Body001Nema17

if App.ActiveDocument.getObject('Sketch001Body001Nema17'):
    App.ActiveDocument.removeObject('Sketch001Body001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').newObject('Sketcher::SketchObject', 'Sketch001Body001Nema17')
App.ActiveDocument.getObject('Sketch001Body001Nema17').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body001Nema17').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body001Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.LineSegment(App.Vector(-1, 1, 0), App.Vector(1, 1, 0)))  # 0
geoList.append(Part.LineSegment(App.Vector(1, 1, 0), App.Vector(1, -1, 0)))  # 1
geoList.append(Part.LineSegment(App.Vector(1, -1, 0), App.Vector(-1, -1, 0)))  # 2
geoList.append(Part.LineSegment(App.Vector(-1, -1, 0), App.Vector(-1, 1, 0)))  # 3
App.ActiveDocument.getObject('Sketch001Body001Nema17').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))  # 1
conList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))  # 2
conList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))  # 3
conList.append(Sketcher.Constraint('Horizontal', 0))  # 4
conList.append(Sketcher.Constraint('Vertical', 1))  # 5
conList.append(Sketcher.Constraint('Symmetric', 2, 1, 2, 2, -2))  # 6
conList.append(Sketcher.Constraint('Symmetric', 0, 1, 2, 2, -1))  # 7
conList.append(Sketcher.Constraint('Distance', 0, 42))  # 8
conList.append(Sketcher.Constraint('Equal', 1, 0))  # 9
App.ActiveDocument.getObject('Sketch001Body001Nema17').addConstraint(conList)

geoList = []
geoList.append(Part.Circle(App.Vector(-1, 1, 0), App.Vector(0, 0, 1), 1))  # 4
geoList.append(Part.Circle(App.Vector(1, 1, 0), App.Vector(0, 0, 1), 1))  # 5
geoList.append(Part.Circle(App.Vector(-1, -1, 0), App.Vector(0, 0, 1), 1))  # 6
geoList.append(Part.Circle(App.Vector(1, -1, 0), App.Vector(0, 0, 1), 1))  # 7
App.ActiveDocument.getObject('Sketch001Body001Nema17').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Symmetric', 4, 3, 5, 3, -2))  # 10
conList.append(Sketcher.Constraint('Symmetric', 4, 3, 6, 3, -1))  # 11
conList.append(Sketcher.Constraint('Symmetric', 6, 3, 7, 3, -2))  # 12
conList.append(Sketcher.Constraint('Distance', 4, 3, 5, 3, 31))  # 13
conList.append(Sketcher.Constraint('Distance', 6, 3, 4, 3, 31))  # 14
conList.append(Sketcher.Constraint('Diameter', 4, 3))  # 15
conList.append(Sketcher.Constraint('Equal', 4, 5))  # 16
conList.append(Sketcher.Constraint('Equal', 5, 6))  # 17
conList.append(Sketcher.Constraint('Equal', 6, 7))  # 18
App.ActiveDocument.getObject('Sketch001Body001Nema17').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body001Nema17

if App.ActiveDocument.getObject('Pad001Body001Nema17'):
    App.ActiveDocument.removeObject('Pad001Body001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').newObject('PartDesign::Pad', 'Pad001Body001Nema17')
App.ActiveDocument.getObject('Pad001Body001Nema17').Profile = App.ActiveDocument.getObject('Sketch001Body001Nema17')
App.ActiveDocument.getObject('Pad001Body001Nema17').Length = 22
App.ActiveDocument.getObject('Pad001Body001Nema17').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body001Nema17').Visibility = False


# Local00xPad001Body001Nema17

if App.ActiveDocument.getObject('Local001Body001Nema17'):
    App.ActiveDocument.removeObject('Local001Body001Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Local002Body001Nema17'):
    App.ActiveDocument.removeObject('Local002Body001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').newObject('PartDesign::CoordinateSystem', 'Local001Body001Nema17')
App.ActiveDocument.getObject('Local001Body001Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body001Nema17'), 'Face10')]
App.ActiveDocument.getObject('Local001Body001Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').newObject('PartDesign::CoordinateSystem', 'Local002Body001Nema17')
App.ActiveDocument.getObject('Local002Body001Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body001Nema17'), 'Face9')]
App.ActiveDocument.getObject('Local002Body001Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Local001Body001Nema17').Visibility = False
App.ActiveDocument.getObject('Local002Body001Nema17').Visibility = False


# Chamfer001Body001Nema17

if App.ActiveDocument.getObject('Chamfer001Body001Nema17'):
    App.ActiveDocument.removeObject('Chamfer001Body001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').newObject('PartDesign::Chamfer', 'Chamfer001Body001Nema17')
App.ActiveDocument.getObject('Chamfer001Body001Nema17').Base = (
    App.ActiveDocument.getObject('Pad001Body001Nema17'), ["Edge1", "Edge2", "Edge5", "Edge8", ])
App.ActiveDocument.getObject('Chamfer001Body001Nema17').Size = 5
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').ViewObject.ShapeColor = (0.2, 0.2, 0.2, 0.0)
Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Body002Nema17

if App.ActiveDocument.getObject('Body002Nema17'):
    App.ActiveDocument.getObject('Body002Nema17').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body002Nema17')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body002Nema17'))


# Binder001Body002Nema17

if App.ActiveDocument.getObject('Binder001Body002Nema17'):
    App.ActiveDocument.removeObject('Binder001Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::SubShapeBinder', 'Binder001Body002Nema17')
App.ActiveDocument.getObject('Binder001Body002Nema17').Support = FreeCAD.ActiveDocument.getObject('Sketch001Body001Nema17')
App.ActiveDocument.getObject('Binder001Body002Nema17').Placement *= App.ActiveDocument.getObject('Local001Body001Nema17').Placement
App.ActiveDocument.recompute()


# Pad001Body002Nema17

if App.ActiveDocument.getObject('Pad001Body002Nema17'):
    App.ActiveDocument.removeObject('Pad001Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Pad', 'Pad001Body002Nema17')
App.ActiveDocument.getObject('Pad001Body002Nema17').Profile = App.ActiveDocument.getObject('Binder001Body002Nema17')
App.ActiveDocument.getObject('Pad001Body002Nema17').Length = 8
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body002Nema17').Visibility = False


# Local001Body002Nema17

if App.ActiveDocument.getObject('Local001Body002Nema17'):
    App.ActiveDocument.removeObject('Local001Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::CoordinateSystem', 'Local001Body002Nema17')
App.ActiveDocument.getObject('Local001Body002Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body002Nema17'), 'Face10')]
App.ActiveDocument.getObject('Local001Body002Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Local001Body002Nema17').Visibility = False


# Sketch001Body002Nema17

if App.ActiveDocument.getObject('Sketch001Body002Nema17'):
    App.ActiveDocument.removeObject('Sketch001Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('Sketcher::SketchObject', 'Sketch001Body002Nema17')
App.ActiveDocument.getObject('Sketch001Body002Nema17').Support = (App.ActiveDocument.getObject('Pad001Body002Nema17'), ['Face10'])
App.ActiveDocument.getObject('Sketch001Body002Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch001Body002Nema17').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 3, -1, 1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 22))  # 3
conList.append(Sketcher.Constraint('Diameter', 1, 8))  # 3
App.ActiveDocument.getObject('Sketch001Body002Nema17').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad002Body002Nema17

if App.ActiveDocument.getObject('Pad002Body002Nema17'):
    App.ActiveDocument.removeObject('Pad002Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Pad', 'Pad002Body002Nema17')
App.ActiveDocument.getObject('Pad002Body002Nema17').Profile = App.ActiveDocument.getObject('Sketch001Body002Nema17')
App.ActiveDocument.getObject('Pad002Body002Nema17').Length = 2
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body002Nema17').Visibility = False


# Chamfer001Body002Nema17

if App.ActiveDocument.getObject('Chamfer001Body002Nema17'):
    App.ActiveDocument.removeObject('Chamfer001Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Chamfer', 'Chamfer001Body002Nema17')
App.ActiveDocument.getObject('Chamfer001Body002Nema17').Base = (
    App.ActiveDocument.getObject('Pad002Body002Nema17'), ["Edge1", "Edge2", "Edge5", "Edge8", ])
App.ActiveDocument.getObject('Chamfer001Body002Nema17').Size = 3
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Body003Nema17

if App.ActiveDocument.getObject('Body003Nema17'):
    App.ActiveDocument.getObject('Body003Nema17').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body003Nema17')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body003Nema17'))


# Binder001Body003Nema17

if App.ActiveDocument.getObject('Binder001Body003Nema17'):
    App.ActiveDocument.removeObject('Binder001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::SubShapeBinder', 'Binder001Body003Nema17')
App.ActiveDocument.getObject('Binder001Body003Nema17').Support = FreeCAD.ActiveDocument.getObject('Sketch001Body001Nema17')
App.ActiveDocument.getObject('Binder001Body003Nema17').Placement *= App.ActiveDocument.getObject('Local002Body001Nema17').Placement
App.ActiveDocument.recompute()


# Pad001Body003Nema17

if App.ActiveDocument.getObject('Pad001Body003Nema17'):
    App.ActiveDocument.removeObject('Pad001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Pad', 'Pad001Body003Nema17')
App.ActiveDocument.getObject('Pad001Body003Nema17').Profile = App.ActiveDocument.getObject('Binder001Body003Nema17')
App.ActiveDocument.getObject('Pad001Body003Nema17').Length = 10
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body003Nema17').Visibility = False


# Chamfer001Body003Nema17

if App.ActiveDocument.getObject('Chamfer001Body003Nema17'):
    App.ActiveDocument.removeObject('Chamfer001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Chamfer', 'Chamfer001Body003Nema17')
App.ActiveDocument.getObject('Chamfer001Body003Nema17').Base = (
    App.ActiveDocument.getObject('Pad001Body003Nema17'), ["Edge1", "Edge2", "Edge5", "Edge8", ])
App.ActiveDocument.getObject('Chamfer001Body003Nema17').Size = 3
App.ActiveDocument.recompute()


# Hole001Body003Nema17

if App.ActiveDocument.getObject('Hole001Body003Nema17'):
    App.ActiveDocument.removeObject('Hole001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Hole', 'Hole001Body003Nema17')
App.ActiveDocument.getObject('Hole001Body003Nema17').Profile = (
    App.ActiveDocument.getObject('Chamfer001Body003Nema17'), ['Edge25', 'Edge26', 'Edge28', 'Edge27', ])
App.ActiveDocument.getObject('Hole001Body003Nema17').Diameter = 6
App.ActiveDocument.getObject('Hole001Body003Nema17').Depth = 6
App.ActiveDocument.getObject('Hole001Body003Nema17').Reversed = True
App.ActiveDocument.getObject('Hole001Body003Nema17').DrillPoint = 'Flat'
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Point00xHoleBody003Nema17

if App.ActiveDocument.getObject('Point001Body003Nema17'):
    App.ActiveDocument.removeObject('Point001Body003Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Point002Body003Nema17'):
    App.ActiveDocument.removeObject('Point002Body003Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Point003Body003Nema17'):
    App.ActiveDocument.removeObject('Point003Body003Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Point004Body003Nema17'):
    App.ActiveDocument.removeObject('Point004Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point001Body003Nema17')
App.ActiveDocument.getObject('Point001Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge41')]
App.ActiveDocument.getObject('Point001Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point002Body003Nema17')
App.ActiveDocument.getObject('Point002Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge43')]
App.ActiveDocument.getObject('Point002Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point003Body003Nema17')
App.ActiveDocument.getObject('Point003Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge45')]
App.ActiveDocument.getObject('Point003Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point004Body003Nema17')
App.ActiveDocument.getObject('Point004Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge47')]
App.ActiveDocument.getObject('Point004Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Point001Body003Nema17').Visibility = False
App.ActiveDocument.getObject('Point002Body003Nema17').Visibility = False
App.ActiveDocument.getObject('Point003Body003Nema17').Visibility = False
App.ActiveDocument.getObject('Point004Body003Nema17').Visibility = False


# Body004Nema17

if App.ActiveDocument.getObject('Body004Nema17'):
    App.ActiveDocument.getObject('Body004Nema17').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body004Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body004Nema17')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body004Nema17'))


# Sketch001Body004Nema17

if App.ActiveDocument.getObject('Sketch001Body004Nema17'):
    App.ActiveDocument.removeObject('Sketch001Body004Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Nema17').newObject('Sketcher::SketchObject', 'Sketch001Body004Nema17')
App.ActiveDocument.getObject('Sketch001Body004Nema17').Support = (App.ActiveDocument.getObject('Local001Body002Nema17'), [''])
App.ActiveDocument.getObject('Sketch001Body004Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body004Nema17').addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2), False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Diameter', 0, 5))  # 1
App.ActiveDocument.getObject('Sketch001Body004Nema17').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body004Nema17

if App.ActiveDocument.getObject('Pad001Body004Nema17'):
    App.ActiveDocument.removeObject('Pad001Body004Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Nema17').newObject('PartDesign::Pad', 'Pad001Body004Nema17')
App.ActiveDocument.getObject('Pad001Body004Nema17').Profile = App.ActiveDocument.getObject('Sketch001Body004Nema17')
App.ActiveDocument.getObject('Pad001Body004Nema17').Length = 24
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body004Nema17').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Part001Nema17

if App.ActiveDocument.getObject('Part001Nema17'):
    App.ActiveDocument.getObject('Part001Nema17').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part001Nema17')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part001Nema17'))
App.ActiveDocument.recompute()

# Link00xBody00xNema17

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link001Body001Nema17')
App.ActiveDocument.getObject('Link001Body001Nema17').LinkedObject = App.ActiveDocument.getObject('Body001Nema17')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link002Body001Nema17')
App.ActiveDocument.getObject('Link002Body001Nema17').LinkedObject = App.ActiveDocument.getObject('Body002Nema17')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link003Body001Nema17')
App.ActiveDocument.getObject('Link003Body001Nema17').LinkedObject = App.ActiveDocument.getObject('Body003Nema17')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link004Body001Nema17')
App.ActiveDocument.getObject('Link004Body001Nema17').LinkedObject = App.ActiveDocument.getObject('Body004Nema17')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Nema17').Visibility = False
App.ActiveDocument.getObject('Body002Nema17').Visibility = False
App.ActiveDocument.getObject('Body003Nema17').Visibility = False
App.ActiveDocument.getObject('Body004Nema17').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('part', None)


# Group001Nema17

if App.ActiveDocument.getObject('Group001Nema17'):
    App.ActiveDocument.removeObject('Group001Nema17')
    App.ActiveDocument.recompute()

App.activeDocument().addObject('App::DocumentObjectGroup', 'Group001Nema17')
App.ActiveDocument.getObject("Group001Nema17").addObject(App.ActiveDocument.getObject("Body001Nema17"))
App.ActiveDocument.getObject("Group001Nema17").addObject(App.ActiveDocument.getObject("Body002Nema17"))
App.ActiveDocument.getObject("Group001Nema17").addObject(App.ActiveDocument.getObject("Body003Nema17"))
App.ActiveDocument.getObject("Group001Nema17").addObject(App.ActiveDocument.getObject("Body004Nema17"))
App.ActiveDocument.getObject("Group001Nema17").addObject(App.ActiveDocument.getObject("Part001Nema17"))

App.ActiveDocument.recompute()


# Body001Coupling

if App.ActiveDocument.getObject('Body001Coupling'):
    App.ActiveDocument.getObject('Body001Coupling').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body001Coupling')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body001Coupling'))


# Sketch001Body001Coupling

if App.ActiveDocument.getObject('Sketch001Body001Coupling'):
    App.ActiveDocument.removeObject('Sketch001Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('Sketcher::SketchObject', 'Sketch001Body001Coupling')
App.ActiveDocument.getObject('Sketch001Body001Coupling').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body001Coupling').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body001Coupling').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch001Body001Coupling').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 3, -1, 1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 19))  # 3
conList.append(Sketcher.Constraint('Diameter', 1, 5))  # 3
App.ActiveDocument.getObject('Sketch001Body001Coupling').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body001Coupling

if App.ActiveDocument.getObject('Pad001Body001Coupling'):
    App.ActiveDocument.removeObject('Pad001Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('PartDesign::Pad', 'Pad001Body001Coupling')
App.ActiveDocument.getObject('Pad001Body001Coupling').Profile = App.ActiveDocument.getObject('Sketch001Body001Coupling')
App.ActiveDocument.getObject('Pad001Body001Coupling').Length = 24
App.ActiveDocument.getObject('Pad001Body001Coupling').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body001Coupling').Visibility = False


# Hole001Body001Coupling

if App.ActiveDocument.getObject('Hole001Body001Coupling'):
    App.ActiveDocument.removeObject('Hole001Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('PartDesign::Hole', 'Hole001Body001Coupling')
App.ActiveDocument.getObject('Hole001Body001Coupling').Profile = (
    App.ActiveDocument.getObject('Pad001Body001Coupling'), ['Edge6', ])
App.ActiveDocument.getObject('Hole001Body001Coupling').Diameter = 8
App.ActiveDocument.getObject('Hole001Body001Coupling').Depth = 18
App.ActiveDocument.getObject('Hole001Body001Coupling').Reversed = False
App.ActiveDocument.getObject('Hole001Body001Coupling').DrillPoint = 'Flat'
App.ActiveDocument.recompute()


# Sketch002Body001Coupling

if App.ActiveDocument.getObject('Sketch002Body001Coupling'):
    App.ActiveDocument.removeObject('Sketch002Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('Sketcher::SketchObject', 'Sketch002Body001Coupling')
App.ActiveDocument.getObject('Sketch002Body001Coupling').Support = (App.ActiveDocument.getObject(
    'YZ_Plane' + App.ActiveDocument.getObject('Body001Coupling').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch002Body001Coupling').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 1, 0), App.Vector(0, 0, 1), 1))  # 0
geoList.append(Part.Circle(App.Vector(0, -1, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch002Body001Coupling').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('PointOnObject', 1, 3, -2))  # 0
conList.append(Sketcher.Constraint('Distance', 1, 3, 0, 3, 16))  # 3
conList.append(Sketcher.Constraint('Symmetric', 0, 3, 1, 3, -1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 4))  # 4
conList.append(Sketcher.Constraint('Diameter', 1, 4))  # 5
App.ActiveDocument.getObject('Sketch002Body001Coupling').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket001Body001Coupling

if App.ActiveDocument.getObject('Pocket001Body001Coupling'):
    App.ActiveDocument.removeObject('Pocket001Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('PartDesign::Pocket', 'Pocket001Body001Coupling')
App.ActiveDocument.getObject('Pocket001Body001Coupling').Profile = App.ActiveDocument.getObject('Sketch002Body001Coupling')
App.ActiveDocument.getObject('Pocket001Body001Coupling').Reversed = True
App.ActiveDocument.getObject('Pocket001Body001Coupling').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch002Body001Coupling').Visibility = False


# Sketch003Body001Coupling

if App.ActiveDocument.getObject('Sketch003Body001Coupling'):
    App.ActiveDocument.removeObject('Sketch003Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('Sketcher::SketchObject', 'Sketch003Body001Coupling')
App.ActiveDocument.getObject('Sketch003Body001Coupling').Support = (App.ActiveDocument.getObject(
    'XZ_Plane' + App.ActiveDocument.getObject('Body001Coupling').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch003Body001Coupling').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 1, 0), App.Vector(0, 0, 1), 1))  # 0
geoList.append(Part.Circle(App.Vector(0, -1, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch003Body001Coupling').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('PointOnObject', 1, 3, -2))  # 0
conList.append(Sketcher.Constraint('Distance', 1, 3, 0, 3, 16))  # 3
conList.append(Sketcher.Constraint('Symmetric', 0, 3, 1, 3, -1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 4))  # 4
conList.append(Sketcher.Constraint('Diameter', 1, 4))  # 5
App.ActiveDocument.getObject('Sketch003Body001Coupling').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket002Body001Coupling

if App.ActiveDocument.getObject('Pocket002Body001Coupling'):
    App.ActiveDocument.removeObject('Pocket002Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('PartDesign::Pocket', 'Pocket002Body001Coupling')
App.ActiveDocument.getObject('Pocket002Body001Coupling').Profile = App.ActiveDocument.getObject('Sketch003Body001Coupling')
App.ActiveDocument.getObject('Pocket002Body001Coupling').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch003Body001Coupling').Visibility = False


# Placement

App.ActiveDocument.getObject('Body001Coupling').Placement.Base.x = (
    App.ActiveDocument.getObject('Part001Nema17').Shape.BoundBox.XLength +
    App.ActiveDocument.getObject('Body001Coupling').Shape.BoundBox.XLength)*75/100
App.ActiveDocument.recompute()


# LinkSquareProfileSketch

if App.ActiveDocument.getObject('LinkSquareProfileSketch'):
    App.ActiveDocument.removeObject('LinkSquareProfileSketch')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Link', 'LinkSquareProfileSketch')
App.ActiveDocument.getObject('LinkSquareProfileSketch').LinkedObject = App.getDocument('Sketches').getObject('SquareProfileSketch')
App.ActiveDocument.recompute()


# Body001Spacer

if App.ActiveDocument.getObject('Body001Spacer'):
    App.ActiveDocument.getObject('Body001Spacer').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body001Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body001Spacer')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body001Spacer'))


# Binder001Body001Spacer

if App.ActiveDocument.getObject('Binder001Body001Spacer'):
    App.ActiveDocument.removeObject('Binder001Body001Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Spacer').newObject('PartDesign::SubShapeBinder', 'Binder001Body001Spacer')
App.ActiveDocument.getObject('Binder001Body001Spacer').Support = App.ActiveDocument.getObject('LinkSquareProfileSketch')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('LinkSquareProfileSketch').Visibility = False


# Pad001Body001Spacer

if App.ActiveDocument.getObject('Pad001Body001Spacer'):
    App.ActiveDocument.removeObject('Pad001Body001Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Spacer').newObject('PartDesign::Pad', 'Pad001Body001Spacer')
App.ActiveDocument.getObject('Pad001Body001Spacer').Profile = App.ActiveDocument.getObject('Binder001Body001Spacer')
App.ActiveDocument.getObject('Pad001Body001Spacer').Length = 45
App.ActiveDocument.getObject('Pad001Body001Spacer').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body001Spacer').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Body002Spacer

if App.ActiveDocument.getObject('Body002Spacer'):
    App.ActiveDocument.getObject('Body002Spacer').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body002Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body002Spacer')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body002Spacer'))


# Binder001Body002Spacer

if App.ActiveDocument.getObject('Binder001Body002Spacer'):
    App.ActiveDocument.removeObject('Binder001Body002Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Spacer').newObject('PartDesign::SubShapeBinder', 'Binder001Body002Spacer')
App.ActiveDocument.getObject('Binder001Body002Spacer').Support = App.ActiveDocument.getObject('LinkSquareProfileSketch')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('LinkSquareProfileSketch').Visibility = False


# Pad001Body002Spacer

if App.ActiveDocument.getObject('Pad001Body002Spacer'):
    App.ActiveDocument.removeObject('Pad001Body002Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Spacer').newObject('PartDesign::Pad', 'Pad001Body002Spacer')
App.ActiveDocument.getObject('Pad001Body002Spacer').Profile = App.ActiveDocument.getObject('Binder001Body002Spacer')
App.ActiveDocument.getObject('Pad001Body002Spacer').Length = 35
App.ActiveDocument.getObject('Pad001Body002Spacer').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body002Spacer').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Placement

App.ActiveDocument.getObject('Body002Spacer').Placement.Base.x = (
    App.ActiveDocument.getObject('Body001Spacer').Shape.BoundBox.XLength +
    App.ActiveDocument.getObject('Body002Spacer').Shape.BoundBox.XLength)*75/100
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body002Spacer').Placement.Base.x = App.ActiveDocument.getObject('Body002Spacer').Placement.Base.x


# Group001Spacer

if App.ActiveDocument.getObject('Group001Spacer'):
    App.ActiveDocument.removeObject('Group001Spacer')
    App.ActiveDocument.recompute()

App.activeDocument().addObject('App::DocumentObjectGroup', 'Group001Spacer')
App.ActiveDocument.getObject("Group001Spacer").addObject(App.ActiveDocument.getObject("LinkSquareProfileSketch"))
App.ActiveDocument.getObject("Group001Spacer").addObject(App.ActiveDocument.getObject("Body001Spacer"))
App.ActiveDocument.getObject("Group001Spacer").addObject(App.ActiveDocument.getObject("Body002Spacer"))
App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject("Group001Spacer").Group:
    obj.Placement.Base.y = -(
        App.ActiveDocument.getObject('Group001Nema17').Shape.BoundBox.YLength +
        App.ActiveDocument.getObject('Group001Spacer').Shape.BoundBox.YLength)*75/100

App.ActiveDocument.recompute()


# Link001Sketch001Body001Nema17Body001Support

if App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support'):
    App.ActiveDocument.removeObject('Link001Sketch001Body001Nema17Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Link', 'Link001Sketch001Body001Nema17Body001Support')
App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support').LinkedObject = App.ActiveDocument.getObject('Sketch001Body001Nema17')
App.ActiveDocument.recompute()


# Body001Support

if App.ActiveDocument.getObject('Body001Support'):
    App.ActiveDocument.getObject('Body001Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body001Support')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body001Support'))


# Binder001Body001Support

if App.ActiveDocument.getObject('Binder001Body001Support'):
    App.ActiveDocument.removeObject('Binder001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::SubShapeBinder', 'Binder001Body001Support')
App.ActiveDocument.getObject('Binder001Body001Support').Support = App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support').Visibility = False


# Pad001Body001Support

if App.ActiveDocument.getObject('Pad001Body001Support'):
    App.ActiveDocument.removeObject('Pad001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Pad', 'Pad001Body001Support')
App.ActiveDocument.getObject('Pad001Body001Support').Profile = App.ActiveDocument.getObject('Binder001Body001Support')
App.ActiveDocument.getObject('Pad001Body001Support').Midplane = True
App.ActiveDocument.getObject('Pad001Body001Support').Length = 15
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body001Support').Visibility = False


# Sketch001Body001Support

if App.ActiveDocument.getObject('Sketch001Body001Support'):
    App.ActiveDocument.removeObject('Sketch001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('Sketcher::SketchObject', 'Sketch001Body001Support')
App.ActiveDocument.getObject('Sketch001Body001Support').Support = (App.ActiveDocument.getObject('Pad001Body001Support'), ['Face10'])
App.ActiveDocument.getObject('Sketch001Body001Support').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body001Support').addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2), False)  # 0

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Diameter', 0, 22))  # 1
App.ActiveDocument.getObject('Sketch001Body001Support').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket001Body001Support

if App.ActiveDocument.getObject('Pocket001Body001Support'):
    App.ActiveDocument.removeObject('Pocket001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Pocket', 'Pocket001Body001Support')
App.ActiveDocument.getObject('Pocket001Body001Support').Profile = App.ActiveDocument.getObject('Sketch001Body001Support')
App.ActiveDocument.getObject('Pocket001Body001Support').Length = 7
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body001Support').Visibility = False


# Hole001Body001Support

if App.ActiveDocument.getObject('Hole001Body001Support'):
    App.ActiveDocument.removeObject('Hole001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Hole', 'Hole001Body001Support')
App.ActiveDocument.getObject('Hole001Body001Support').Profile = (App.ActiveDocument.getObject('Pocket001Body001Support'), ['Face12', ])
App.ActiveDocument.getObject('Hole001Body001Support').DepthType = 'ThroughAll'
App.ActiveDocument.getObject('Hole001Body001Support').Diameter = 10
App.ActiveDocument.recompute()


# Chamfer001Body001Support

if App.ActiveDocument.getObject('Chamfer001Body001Support'):
    App.ActiveDocument.removeObject('Chamfer001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Chamfer', 'Chamfer001Body001Support')
App.ActiveDocument.getObject('Chamfer001Body001Support').Base = (
    App.ActiveDocument.getObject('Hole001Body001Support'), ["Edge1", "Edge2", "Edge5", "Edge8", ])
App.ActiveDocument.getObject('Chamfer001Body001Support').Size = 3
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# ShapeColor

App.ActiveDocument.getObject('Body001Support').ViewObject.ShapeColor = (0.0, 0.6, 1.0, 0.0)


# Body002Support

if App.ActiveDocument.getObject('Body002Support'):
    App.ActiveDocument.getObject('Body002Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body002Support')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body002Support'))


# Binder001Body002Support

if App.ActiveDocument.getObject('Binder001Body002Support'):
    App.ActiveDocument.removeObject('Binder001Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::SubShapeBinder', 'Binder001Body002Support')
App.ActiveDocument.getObject('Binder001Body002Support').Support = App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support')
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support').Visibility = False


# Pad001Body002Support

if App.ActiveDocument.getObject('Pad001Body002Support'):
    App.ActiveDocument.removeObject('Pad001Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Pad', 'Pad001Body002Support')
App.ActiveDocument.getObject('Pad001Body002Support').Profile = App.ActiveDocument.getObject('Binder001Body002Support')
App.ActiveDocument.getObject('Pad001Body002Support').Midplane = True
App.ActiveDocument.getObject('Pad001Body002Support').Length = 10
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body002Support').Visibility = False


# Chamfer001Body002Support

if App.ActiveDocument.getObject('Chamfer001Body002Support'):
    App.ActiveDocument.removeObject('Chamfer001Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Chamfer', 'Chamfer001Body002Support')
App.ActiveDocument.getObject('Chamfer001Body002Support').Base = (
    App.ActiveDocument.getObject('Pad001Body002Support'), ["Edge1", "Edge2", "Edge5", "Edge8", ])
App.ActiveDocument.getObject('Chamfer001Body002Support').Size = 3
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# ShapeColor

App.ActiveDocument.getObject('Body002Support').ViewObject.ShapeColor = App.ActiveDocument.getObject('Body001Support').ViewObject.ShapeColor


# Placement

App.ActiveDocument.getObject('Body002Support').Placement.Base.x = (
    App.ActiveDocument.getObject('Body001Support').Shape.BoundBox.XLength +
    App.ActiveDocument.getObject('Body002Support').Shape.BoundBox.XLength)*75/100
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body002Support').Placement.Base.x = App.ActiveDocument.getObject('Body002Support').Placement.Base.x
App.ActiveDocument.recompute()


# Group001Support

if App.ActiveDocument.getObject('Group001Support'):
    App.ActiveDocument.removeObject('Group001Support')
    App.ActiveDocument.recompute()

App.activeDocument().addObject('App::DocumentObjectGroup', 'Group001Support')
App.ActiveDocument.getObject("Group001Support").addObject(App.ActiveDocument.getObject('Link001Sketch001Body001Nema17Body001Support'))
App.ActiveDocument.getObject("Group001Support").addObject(App.ActiveDocument.getObject("Body001Support"))
App.ActiveDocument.getObject("Group001Support").addObject(App.ActiveDocument.getObject("Body002Support"))
App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject("Group001Support").Group:
    obj.Placement.Base.y = App.ActiveDocument.getObject('Group001Spacer').Shape.BoundBox.Center.y - (
        App.ActiveDocument.getObject('Group001Spacer').Shape.BoundBox.YLength +
        App.ActiveDocument.getObject('Group001Support').Shape.BoundBox.YLength)*75/100

App.ActiveDocument.recompute()


# Save

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.SendMsgToActiveView("ViewFit")

App.ActiveDocument.save()

