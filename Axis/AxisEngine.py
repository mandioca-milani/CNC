# Document

for doc in App.listDocuments():
    App.closeDocument(doc)

docs = [
    '/Parts/Sketches.FCStd',
    '/Parts/Fasteners.FCStd',
]

for doc in docs:
    App.openDocument(os.getcwd() + doc, hidden=True)

if os.path.isfile(os.getcwd() + '/Axis/AxisEngine.FCStd'):
    App.openDocument(os.getcwd() + '/Axis/AxisEngine.FCStd')
else:
    App.newDocument('AxisEngine')
    App.ActiveDocument.saveAs(os.getcwd() + '/Axis/AxisEngine.FCStd')

Gui.activateWorkbench('PartDesignWorkbench')


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
    App.ActiveDocument.getObject('Pad001Body001Nema17'), ['Edge1', 'Edge2', 'Edge5', 'Edge8', ])
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
App.ActiveDocument.getObject('Binder001Body002Nema17').Support = App.ActiveDocument.getObject('Sketch001Body001Nema17')
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


# PointSpacer00xBody002Nema17

if App.ActiveDocument.getObject('PointSpacer001Body002Nema17'):
    App.ActiveDocument.removeObject('PointSpacer001Body002Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointSpacer002Body002Nema17'):
    App.ActiveDocument.removeObject('PointSpacer002Body002Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointSpacer003Body002Nema17'):
    App.ActiveDocument.removeObject('PointSpacer003Body002Nema17')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointSpacer004Body002Nema17'):
    App.ActiveDocument.removeObject('PointSpacer004Body002Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Point', 'PointSpacer001Body002Nema17')
App.ActiveDocument.getObject('PointSpacer001Body002Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body002Nema17'), 'Edge24')]
App.ActiveDocument.getObject('PointSpacer001Body002Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Point', 'PointSpacer002Body002Nema17')
App.ActiveDocument.getObject('PointSpacer002Body002Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body002Nema17'), 'Edge21')]
App.ActiveDocument.getObject('PointSpacer002Body002Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Point', 'PointSpacer003Body002Nema17')
App.ActiveDocument.getObject('PointSpacer003Body002Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body002Nema17'), 'Edge18')]
App.ActiveDocument.getObject('PointSpacer003Body002Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Nema17').newObject('PartDesign::Point', 'PointSpacer004Body002Nema17')
App.ActiveDocument.getObject('PointSpacer004Body002Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body002Nema17'), 'Edge15')]
App.ActiveDocument.getObject('PointSpacer004Body002Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('PointSpacer001Body002Nema17').Visibility = False
App.ActiveDocument.getObject('PointSpacer002Body002Nema17').Visibility = False
App.ActiveDocument.getObject('PointSpacer003Body002Nema17').Visibility = False
App.ActiveDocument.getObject('PointSpacer004Body002Nema17').Visibility = False


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
    App.ActiveDocument.getObject('Pad002Body002Nema17'), ['Edge1', 'Edge2', 'Edge5', 'Edge8', ])
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
App.ActiveDocument.getObject('Binder001Body003Nema17').Support = App.ActiveDocument.getObject('Sketch001Body001Nema17')
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


# Sketch001Body003Nema17

if App.ActiveDocument.getObject('Sketch001Body003Nema17'):
    App.ActiveDocument.removeObject('Sketch001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('Sketcher::SketchObject', 'Sketch001Body003Nema17')
App.ActiveDocument.getObject('Sketch001Body003Nema17').Support = (App.ActiveDocument.getObject('Pad001Body003Nema17'), ['Face1'])
App.ActiveDocument.getObject('Sketch001Body003Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.LineSegment(App.Vector(-1, 1, 0), App.Vector(1, 1, 0)))  # 0
geoList.append(Part.LineSegment(App.Vector(1, 1, 0), App.Vector(1, 0, 0)))  # 1
geoList.append(Part.LineSegment(App.Vector(1, 0, 0), App.Vector(-1, 0, 0)))  # 2
geoList.append(Part.LineSegment(App.Vector(-1, 0, 0), App.Vector(-1, 1, 0)))  # 3
App.ActiveDocument.getObject('Sketch001Body003Nema17').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))  # 1
conList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))  # 2
conList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))  # 3
conList.append(Sketcher.Constraint('Horizontal', 0))  # 4
conList.append(Sketcher.Constraint('Vertical', 1))  # 5
conList.append(Sketcher.Constraint('Vertical', 3))  # 6
conList.append(Sketcher.Constraint('Symmetric', 2, 1, 2, 2, -2))  # 6
conList.append(Sketcher.Constraint('PointOnObject', 1, 2, -1))  # 6
conList.append(Sketcher.Constraint('Distance', 0, 16))  # 8
conList.append(Sketcher.Constraint('Distance', 3, 10))  # 9
App.ActiveDocument.getObject('Sketch001Body003Nema17').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad002Body003Nema17

if App.ActiveDocument.getObject('Pad002Body003Nema17'):
    App.ActiveDocument.removeObject('Pad002Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Pad', 'Pad002Body003Nema17')
App.ActiveDocument.getObject('Pad002Body003Nema17').Profile = App.ActiveDocument.getObject('Sketch001Body003Nema17')
App.ActiveDocument.getObject('Pad002Body003Nema17').Length = 5
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body003Nema17').Visibility = False


# Chamfer001Body003Nema17

if App.ActiveDocument.getObject('Chamfer001Body003Nema17'):
    App.ActiveDocument.removeObject('Chamfer001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Chamfer', 'Chamfer001Body003Nema17')
App.ActiveDocument.getObject('Chamfer001Body003Nema17').Base = (
    App.ActiveDocument.getObject('Pad002Body003Nema17'), ['Edge26', 'Edge31', 'Edge4', 'Edge29', ])
App.ActiveDocument.getObject('Chamfer001Body003Nema17').Size = 3
App.ActiveDocument.recompute()


# Hole001Body003Nema17

if App.ActiveDocument.getObject('Hole001Body003Nema17'):
    App.ActiveDocument.removeObject('Hole001Body003Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Hole', 'Hole001Body003Nema17')
App.ActiveDocument.getObject('Hole001Body003Nema17').Profile = (
    App.ActiveDocument.getObject('Chamfer001Body003Nema17'), ['Edge32', 'Edge31', 'Edge34', 'Edge33', ])
App.ActiveDocument.getObject('Hole001Body003Nema17').Diameter = 6
App.ActiveDocument.getObject('Hole001Body003Nema17').Depth = 3
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
App.ActiveDocument.getObject('Point001Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge47')]
App.ActiveDocument.getObject('Point001Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point002Body003Nema17')
App.ActiveDocument.getObject('Point002Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge45')]
App.ActiveDocument.getObject('Point002Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point003Body003Nema17')
App.ActiveDocument.getObject('Point003Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge51')]
App.ActiveDocument.getObject('Point003Body003Nema17').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Nema17').newObject('PartDesign::Point', 'Point004Body003Nema17')
App.ActiveDocument.getObject('Point004Body003Nema17').Support = [(App.ActiveDocument.getObject('Hole001Body003Nema17'), 'Edge49')]
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


# Binder001Body004Nema17

if App.ActiveDocument.getObject('Binder001Body004Nema17'):
    App.ActiveDocument.removeObject('Binder001Body004Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Nema17').newObject('PartDesign::ShapeBinder', 'Binder001Body004Nema17')
App.ActiveDocument.getObject('Binder001Body004Nema17').Support = App.ActiveDocument.getObject('Local001Body002Nema17')
App.ActiveDocument.getObject('Binder001Body004Nema17').Placement *= App.ActiveDocument.getObject('Local001Body002Nema17').Placement
App.ActiveDocument.recompute()


# Sketch001Body004Nema17

if App.ActiveDocument.getObject('Sketch001Body004Nema17'):
    App.ActiveDocument.removeObject('Sketch001Body004Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Nema17').newObject('Sketcher::SketchObject', 'Sketch001Body004Nema17')
App.ActiveDocument.getObject('Sketch001Body004Nema17').Support = (App.ActiveDocument.getObject('Binder001Body004Nema17'), [''])
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


# Local001Body004Nema17

if App.ActiveDocument.getObject('Local001Body004Nema17'):
    App.ActiveDocument.removeObject('Local001Body004Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Nema17').newObject('PartDesign::CoordinateSystem', 'Local001Body004Nema17')
App.ActiveDocument.getObject('Local001Body004Nema17').Support = [(App.ActiveDocument.getObject('Pad001Body004Nema17'), 'Face3')]
App.ActiveDocument.getObject('Local001Body004Nema17').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Local001Body004Nema17').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Compound001Nema17

if App.ActiveDocument.getObject('Compound001Nema17'):
    App.ActiveDocument.removeObject('Compound001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject("Part::Compound", "Compound001Nema17")
App.ActiveDocument.getObject('Compound001Nema17').Links = [
    App.ActiveDocument.getObject('Body001Nema17'),
    App.ActiveDocument.getObject('Body002Nema17'),
    App.ActiveDocument.getObject('Body003Nema17'),
    App.ActiveDocument.getObject('Body004Nema17'), ]
App.ActiveDocument.recompute()


# Part001Nema17

if App.ActiveDocument.getObject('Part001Nema17'):
    App.ActiveDocument.getObject('Part001Nema17').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part001Nema17')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part001Nema17'))
App.ActiveDocument.recompute()


# Compound001Nema17Part001Nema17

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Compound001Nema17Part001Nema17')
App.ActiveDocument.getObject('Compound001Nema17Part001Nema17').LinkedObject = App.ActiveDocument.getObject('Compound001Nema17')
App.ActiveDocument.recompute()

# App.ActiveDocument.getObject('Compound001Nema17').Visibility = False


# Link00xM3x50xScrewPart001Nema17

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link001M3x50xScrewPart001Nema17')
App.ActiveDocument.getObject('Link001M3x50xScrewPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x45-Screw')[0]
App.ActiveDocument.getObject('Link001M3x50xScrewPart001Nema17').Placement *= App.ActiveDocument.getObject('Point001Body003Nema17').Placement
App.ActiveDocument.getObject('Link001M3x50xScrewPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link002M3x50xScrewPart001Nema17')
App.ActiveDocument.getObject('Link002M3x50xScrewPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x45-Screw')[0]
App.ActiveDocument.getObject('Link002M3x50xScrewPart001Nema17').Placement *= App.ActiveDocument.getObject('Point002Body003Nema17').Placement
App.ActiveDocument.getObject('Link002M3x50xScrewPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link003M3x50xScrewPart001Nema17')
App.ActiveDocument.getObject('Link003M3x50xScrewPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x45-Screw')[0]
App.ActiveDocument.getObject('Link003M3x50xScrewPart001Nema17').Placement *= App.ActiveDocument.getObject('Point003Body003Nema17').Placement
App.ActiveDocument.getObject('Link003M3x50xScrewPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link004M3x50xScrewPart001Nema17')
App.ActiveDocument.getObject('Link004M3x50xScrewPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x45-Screw')[0]
App.ActiveDocument.getObject('Link004M3x50xScrewPart001Nema17').Placement *= App.ActiveDocument.getObject('Point004Body003Nema17').Placement
App.ActiveDocument.getObject('Link004M3x50xScrewPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()


# Link00xM3x5xCustomSpacerPart001Nema17

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link001M3x5xCustomSpacerPart001Nema17')
App.ActiveDocument.getObject('Link001M3x5xCustomSpacerPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5xCustom-Spacer')[0]
App.ActiveDocument.getObject('Link001M3x5xCustomSpacerPart001Nema17').Placement *= App.ActiveDocument.getObject('PointSpacer001Body002Nema17').Placement
App.ActiveDocument.getObject('Link001M3x5xCustomSpacerPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, -90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link002M3x5xCustomSpacerPart001Nema17')
App.ActiveDocument.getObject('Link002M3x5xCustomSpacerPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5xCustom-Spacer')[0]
App.ActiveDocument.getObject('Link002M3x5xCustomSpacerPart001Nema17').Placement *= App.ActiveDocument.getObject('PointSpacer002Body002Nema17').Placement
App.ActiveDocument.getObject('Link002M3x5xCustomSpacerPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, -90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link003M3x5xCustomSpacerPart001Nema17')
App.ActiveDocument.getObject('Link003M3x5xCustomSpacerPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5xCustom-Spacer')[0]
App.ActiveDocument.getObject('Link003M3x5xCustomSpacerPart001Nema17').Placement *= App.ActiveDocument.getObject('PointSpacer003Body002Nema17').Placement
App.ActiveDocument.getObject('Link003M3x5xCustomSpacerPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, -90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Nema17').newObject('App::Link', 'Link004M3x5xCustomSpacerPart001Nema17')
App.ActiveDocument.getObject('Link004M3x5xCustomSpacerPart001Nema17').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5xCustom-Spacer')[0]
App.ActiveDocument.getObject('Link004M3x5xCustomSpacerPart001Nema17').Placement *= App.ActiveDocument.getObject('PointSpacer004Body002Nema17').Placement
App.ActiveDocument.getObject('Link004M3x5xCustomSpacerPart001Nema17').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, -90))
App.ActiveDocument.recompute()


Gui.ActiveDocument.ActiveView.setActiveObject('part', None)


# Group001Nema17

if App.ActiveDocument.getObject('Group001Nema17'):
    App.ActiveDocument.removeObject('Group001Nema17')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::DocumentObjectGroup', 'Group001Nema17')
App.ActiveDocument.getObject('Group001Nema17').addObject(App.ActiveDocument.getObject('Body001Nema17'))
App.ActiveDocument.getObject('Group001Nema17').addObject(App.ActiveDocument.getObject('Body002Nema17'))
App.ActiveDocument.getObject('Group001Nema17').addObject(App.ActiveDocument.getObject('Body003Nema17'))
App.ActiveDocument.getObject('Group001Nema17').addObject(App.ActiveDocument.getObject('Body004Nema17'))
App.ActiveDocument.getObject('Group001Nema17').addObject(App.ActiveDocument.getObject('Compound001Nema17'))
App.ActiveDocument.getObject('Group001Nema17').addObject(App.ActiveDocument.getObject('Part001Nema17'))

App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject('Group001Nema17').Group:
    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

App.ActiveDocument.getObject('Group001Nema17').Visibility = True

objs = [
    App.ActiveDocument.getObject('Compound001Nema17'),
    App.ActiveDocument.getObject('Part001Nema17'),
]

# XAxis

for i in range(1, len(objs)):
    objs[i].Placement.Base.x = \
        objs[i-1].Placement.Base.x + (
            objs[i-1].Shape.BoundBox.XLength +
            objs[i].Shape.BoundBox.XLength)*75/100

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


# Local001Body001Coupling

if App.ActiveDocument.getObject('Local001Body001Coupling'):
    App.ActiveDocument.removeObject('Local001Body001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Coupling').newObject('PartDesign::CoordinateSystem', 'Local001Body001Coupling')
App.ActiveDocument.getObject('Local001Body001Coupling').Support = [(App.ActiveDocument.getObject('Hole001Body001Coupling'), 'Edge7')]
App.ActiveDocument.getObject('Local001Body001Coupling').AttachmentOffset = App.Placement(App.Vector(0, 0, 7.5), App.Vector(0, 0, 1), 90)
App.ActiveDocument.getObject('Local001Body001Coupling').MapMode = 'InertialCS'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Local001Body001Coupling').Visibility = False


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


# Part001Coupling

if App.ActiveDocument.getObject('Part001Coupling'):
    App.ActiveDocument.getObject('Part001Coupling').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part001Coupling')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part001Coupling'))
App.ActiveDocument.recompute()

# Link00xBody00xBearing

App.ActiveDocument.getObject('Part001Coupling').newObject('App::Link', 'Link001Body001Coupling')
App.ActiveDocument.getObject('Link001Body001Coupling').LinkedObject = App.ActiveDocument.getObject('Body001Coupling')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('part', None)


# Group001Coupling

if App.ActiveDocument.getObject('Group001Coupling'):
    App.ActiveDocument.removeObject('Group001Coupling')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::DocumentObjectGroup', 'Group001Coupling')
App.ActiveDocument.getObject('Group001Coupling').addObject(App.ActiveDocument.getObject('Body001Coupling'))
App.ActiveDocument.getObject('Group001Coupling').addObject(App.ActiveDocument.getObject('Part001Coupling'))

App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject('Group001Coupling').Group:
    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

App.ActiveDocument.getObject('Group001Nema17').Visibility = True
App.ActiveDocument.getObject('Group001Coupling').Visibility = True

objs = [
    App.ActiveDocument.getObject('Body001Coupling'),
    App.ActiveDocument.getObject('Part001Coupling'),
]


# XAxis

objs[0].Placement.Base.x = App.ActiveDocument.getObject('Group001Nema17').Shape.BoundBox.Center.x + \
    (App.ActiveDocument.getObject('Group001Nema17').Shape.BoundBox.XLength + objs[0].Shape.BoundBox.XLength)*75/100

for i in range(1, len(objs)):
    objs[i].Placement.Base.x = \
        objs[i-1].Placement.Base.x + (
            objs[i-1].Shape.BoundBox.XLength +
            objs[i].Shape.BoundBox.XLength)*75/100

App.ActiveDocument.recompute()

del objs


# Body001Bearing

if App.ActiveDocument.getObject('Body001Bearing'):
    App.ActiveDocument.getObject('Body001Bearing').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body001Bearing')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body001Bearing'))


# Sketch001Body001Bearing

if App.ActiveDocument.getObject('Sketch001Body001Bearing'):
    App.ActiveDocument.removeObject('Sketch001Body001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Bearing').newObject('Sketcher::SketchObject', 'Sketch001Body001Bearing')
App.ActiveDocument.getObject('Sketch001Body001Bearing').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body001Bearing').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body001Bearing').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch001Body001Bearing').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 3, -1, 1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 22))  # 3
conList.append(Sketcher.Constraint('Diameter', 1, 18))  # 3
App.ActiveDocument.getObject('Sketch001Body001Bearing').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body001Bearing

if App.ActiveDocument.getObject('Pad001Body001Bearing'):
    App.ActiveDocument.removeObject('Pad001Body001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Bearing').newObject('PartDesign::Pad', 'Pad001Body001Bearing')
App.ActiveDocument.getObject('Pad001Body001Bearing').Profile = App.ActiveDocument.getObject('Sketch001Body001Bearing')
App.ActiveDocument.getObject('Pad001Body001Bearing').Length = 7
App.ActiveDocument.getObject('Pad001Body001Bearing').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body001Bearing').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Local001Pad001Body001Bearing

if App.ActiveDocument.getObject('Local001Pad001Body001Bearing'):
    App.ActiveDocument.removeObject('Local001Pad001Body001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Bearing').newObject('PartDesign::CoordinateSystem', 'Local001Pad001Body001Bearing')
App.ActiveDocument.getObject('Local001Pad001Body001Bearing').Support = [(App.ActiveDocument.getObject('Pad001Body001Bearing'), '')]
App.ActiveDocument.getObject('Local001Pad001Body001Bearing').MapMode = 'ObjectXY'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Local001Pad001Body001Bearing').Visibility = False


# Body002Bearing

if App.ActiveDocument.getObject('Body002Bearing'):
    App.ActiveDocument.getObject('Body002Bearing').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body002Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body002Bearing')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body002Bearing'))


# Sketch001Body002Bearing

if App.ActiveDocument.getObject('Sketch001Body002Bearing'):
    App.ActiveDocument.removeObject('Sketch001Body002Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Bearing').newObject('Sketcher::SketchObject', 'Sketch001Body002Bearing')
App.ActiveDocument.getObject('Sketch001Body002Bearing').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body002Bearing').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body002Bearing').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch001Body002Bearing').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 3, -1, 1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 18))  # 3
conList.append(Sketcher.Constraint('Diameter', 1, 12))  # 3
App.ActiveDocument.getObject('Sketch001Body002Bearing').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body002Bearing

if App.ActiveDocument.getObject('Pad001Body002Bearing'):
    App.ActiveDocument.removeObject('Pad001Body002Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Bearing').newObject('PartDesign::Pad', 'Pad001Body002Bearing')
App.ActiveDocument.getObject('Pad001Body002Bearing').Profile = App.ActiveDocument.getObject('Sketch001Body002Bearing')
App.ActiveDocument.getObject('Pad001Body002Bearing').Length = 7
App.ActiveDocument.getObject('Pad001Body002Bearing').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body002Bearing').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# ShapeColor

App.ActiveDocument.getObject('Body002Bearing').ViewObject.ShapeColor = (0.2, 0.2, 0.2, 0.0)


# Body003Bearing

if App.ActiveDocument.getObject('Body003Bearing'):
    App.ActiveDocument.getObject('Body003Bearing').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body003Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body003Bearing')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body003Bearing'))


# Sketch001Body003Bearing

if App.ActiveDocument.getObject('Sketch001Body003Bearing'):
    App.ActiveDocument.removeObject('Sketch001Body003Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Bearing').newObject('Sketcher::SketchObject', 'Sketch001Body003Bearing')
App.ActiveDocument.getObject('Sketch001Body003Bearing').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body003Bearing').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body003Bearing').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch001Body003Bearing').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 3, -1, 1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 12))  # 3
conList.append(Sketcher.Constraint('Diameter', 1, 8))  # 3
App.ActiveDocument.getObject('Sketch001Body003Bearing').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad00xBody003Bearing

if App.ActiveDocument.getObject('Pad001Body003Bearing'):
    App.ActiveDocument.removeObject('Pad001Body003Bearing')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Pad002Body003Bearing'):
    App.ActiveDocument.removeObject('Pad002Body003Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Bearing').newObject('PartDesign::Pad', 'Pad001Body003Bearing')
App.ActiveDocument.getObject('Pad001Body003Bearing').Profile = App.ActiveDocument.getObject('Sketch001Body003Bearing')
App.ActiveDocument.getObject('Pad001Body003Bearing').Length = 7
App.ActiveDocument.getObject('Pad001Body003Bearing').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Bearing').newObject('PartDesign::Pad', 'Pad002Body003Bearing')
App.ActiveDocument.getObject('Pad002Body003Bearing').Profile = (App.ActiveDocument.getObject('Pad001Body003Bearing'), ['Face4', ])
App.ActiveDocument.getObject('Pad002Body003Bearing').Length = 4
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body003Bearing').Visibility = False
App.ActiveDocument.getObject('Pad001Body003Bearing').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Compound001Bearing

if App.ActiveDocument.getObject('Compound001Bearing'):
    App.ActiveDocument.removeObject('Compound001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject("Part::Compound", "Compound001Bearing")
App.ActiveDocument.getObject('Compound001Bearing').Links = [
    App.ActiveDocument.getObject('Body001Bearing'),
    App.ActiveDocument.getObject('Body002Bearing'),
    App.ActiveDocument.getObject('Body003Bearing'), ]
App.ActiveDocument.recompute()


# Part001Bearing

if App.ActiveDocument.getObject('Part001Bearing'):
    App.ActiveDocument.getObject('Part001Bearing').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part001Bearing')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part001Bearing'))
App.ActiveDocument.recompute()

# Compound001BearingPart001Bearing

App.ActiveDocument.getObject('Part001Bearing').newObject('App::Link', 'Compound001BearingPart001Bearing')
App.ActiveDocument.getObject('Compound001BearingPart001Bearing').LinkedObject = App.ActiveDocument.getObject('Compound001Bearing')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('part', None)


# Group001Bearing

if App.ActiveDocument.getObject('Group001Bearing'):
    App.ActiveDocument.removeObject('Group001Bearing')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::DocumentObjectGroup', 'Group001Bearing')
App.ActiveDocument.getObject('Group001Bearing').addObject(App.ActiveDocument.getObject('Body001Bearing'))
App.ActiveDocument.getObject('Group001Bearing').addObject(App.ActiveDocument.getObject('Body002Bearing'))
App.ActiveDocument.getObject('Group001Bearing').addObject(App.ActiveDocument.getObject('Body003Bearing'))
App.ActiveDocument.getObject('Group001Bearing').addObject(App.ActiveDocument.getObject('Compound001Bearing'))
App.ActiveDocument.getObject('Group001Bearing').addObject(App.ActiveDocument.getObject('Part001Bearing'))

App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject('Group001Bearing').Group:
    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

App.ActiveDocument.getObject('Group001Coupling').Visibility = True
App.ActiveDocument.getObject('Group001Bearing').Visibility = True

objs = [
    App.ActiveDocument.getObject('Compound001Bearing'),
    App.ActiveDocument.getObject('Part001Bearing'),
]


# XAxis

objs[0].Placement.Base.x = App.ActiveDocument.getObject('Group001Coupling').Shape.BoundBox.Center.x + \
    (App.ActiveDocument.getObject('Group001Coupling').Shape.BoundBox.XLength + objs[0].Shape.BoundBox.XLength)*75/100

for i in range(1, len(objs)):
    objs[i].Placement.Base.x = \
        objs[i-1].Placement.Base.x + (
            objs[i-1].Shape.BoundBox.XLength +
            objs[i].Shape.BoundBox.XLength)*75/100

App.ActiveDocument.recompute()

del objs


# SquareProfileSketch001Spacer

if App.ActiveDocument.getObject('SquareProfileSketch001Spacer'):
    App.ActiveDocument.removeObject('SquareProfileSketch001Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject("Part::Feature", "SquareProfileSketch001Spacer")
App.ActiveDocument.getObject('SquareProfileSketch001Spacer').Shape = \
    Part.Compound(App.getDocument('Sketches').getObject('BodySquareProfileSketch').Shape.slice(App.Vector(0, 1, 0), 0))
App.ActiveDocument.recompute()


App.ActiveDocument.getObject('SquareProfileSketch001Spacer').Visibility = False


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

App.ActiveDocument.getObject('Body001Spacer').newObject('PartDesign::ShapeBinder', 'Binder001Body001Spacer')
App.ActiveDocument.getObject('Binder001Body001Spacer').Support = App.ActiveDocument.getObject('SquareProfileSketch001Spacer')
App.ActiveDocument.recompute()


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


# Local00xBody001Spacer

if App.ActiveDocument.getObject('Local001Body001Spacer'):
    App.ActiveDocument.removeObject('Local001Body001Spacer')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Local002Body001Spacer'):
    App.ActiveDocument.removeObject('Local002Body001Spacer')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Local003Body001Spacer'):
    App.ActiveDocument.removeObject('Local003Body001Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Spacer').newObject('PartDesign::CoordinateSystem', 'Local001Body001Spacer')
App.ActiveDocument.getObject('Local001Body001Spacer').Support = [(App.ActiveDocument.getObject('Pad001Body001Spacer'), '')]
App.ActiveDocument.getObject('Local001Body001Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180)
App.ActiveDocument.getObject('Local001Body001Spacer').MapMode = 'ObjectXZ'
App.ActiveDocument.getObject('Local001Body001Spacer').Visibility = False
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Spacer').newObject('PartDesign::CoordinateSystem', 'Local002Body001Spacer')
App.ActiveDocument.getObject('Local002Body001Spacer').Support = [(App.ActiveDocument.getObject('Pad001Body001Spacer'), 'Face18')]
App.ActiveDocument.getObject('Local002Body001Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 180)
App.ActiveDocument.getObject('Local002Body001Spacer').MapMode = 'FlatFace'
App.ActiveDocument.getObject('Local002Body001Spacer').Visibility = False
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Spacer').newObject('PartDesign::CoordinateSystem', 'Local003Body001Spacer')
App.ActiveDocument.getObject('Local003Body001Spacer').Support = [(App.ActiveDocument.getObject('Pad001Body001Spacer'), 'Face17')]
App.ActiveDocument.getObject('Local003Body001Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180)
App.ActiveDocument.getObject('Local003Body001Spacer').MapMode = 'FlatFace'
App.ActiveDocument.getObject('Local003Body001Spacer').Visibility = False
App.ActiveDocument.recompute()


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

App.ActiveDocument.getObject('Body002Spacer').newObject('PartDesign::ShapeBinder', 'Binder001Body002Spacer')
App.ActiveDocument.getObject('Binder001Body002Spacer').Support = App.ActiveDocument.getObject('SquareProfileSketch001Spacer')
App.ActiveDocument.recompute()


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


# Local00xBody002Spacer

if App.ActiveDocument.getObject('Local001Body002Spacer'):
    App.ActiveDocument.removeObject('Local001Body002Spacer')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Local002Body002Spacer'):
    App.ActiveDocument.removeObject('Local002Body002Spacer')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('Local003Body002Spacer'):
    App.ActiveDocument.removeObject('Local003Body002Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Spacer').newObject('PartDesign::CoordinateSystem', 'Local001Body002Spacer')
App.ActiveDocument.getObject('Local001Body002Spacer').Support = [(App.ActiveDocument.getObject('Pad001Body002Spacer'), '')]
App.ActiveDocument.getObject('Local001Body002Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180)
App.ActiveDocument.getObject('Local001Body002Spacer').MapMode = 'ObjectXZ'
App.ActiveDocument.getObject('Local001Body002Spacer').Visibility = False
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Spacer').newObject('PartDesign::CoordinateSystem', 'Local002Body002Spacer')
App.ActiveDocument.getObject('Local002Body002Spacer').Support = [(App.ActiveDocument.getObject('Pad001Body002Spacer'), 'Face18')]
App.ActiveDocument.getObject('Local002Body002Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 180)
App.ActiveDocument.getObject('Local002Body002Spacer').MapMode = 'FlatFace'
App.ActiveDocument.getObject('Local002Body002Spacer').Visibility = False
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Spacer').newObject('PartDesign::CoordinateSystem', 'Local003Body002Spacer')
App.ActiveDocument.getObject('Local003Body002Spacer').Support = [(App.ActiveDocument.getObject('Pad001Body002Spacer'), 'Face17')]
App.ActiveDocument.getObject('Local003Body002Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180)
App.ActiveDocument.getObject('Local003Body002Spacer').MapMode = 'FlatFace'
App.ActiveDocument.getObject('Local003Body002Spacer').Visibility = False
App.ActiveDocument.recompute()


# Body003Spacer

if App.ActiveDocument.getObject('Body003Spacer'):
    App.ActiveDocument.getObject('Body003Spacer').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body003Spacer')
App.ActiveDocument.getObject('Body003Spacer').BaseFeature = App.ActiveDocument.getObject('Body001Spacer')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body003Spacer'))


# Sketch001Body003Spacer

if App.ActiveDocument.getObject('Sketch001Body003Spacer'):
    App.ActiveDocument.removeObject('Sketch001Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Spacer').newObject('Sketcher::SketchObject', 'Sketch001Body003Spacer')
App.ActiveDocument.getObject('Sketch001Body003Spacer').Support = (App.ActiveDocument.getObject(
    'YZ_Plane' + App.ActiveDocument.getObject('Body003Spacer').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body003Spacer').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1))  # 0
App.ActiveDocument.getObject('Sketch001Body003Spacer').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Diameter', 0, 5/16*25.4))  # 1
App.ActiveDocument.getObject('Sketch001Body003Spacer').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket001Body003Spacer

if App.ActiveDocument.getObject('Pocket001Body003Spacer'):
    App.ActiveDocument.removeObject('Pocket001Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Spacer').newObject('PartDesign::Pocket', 'Pocket001Body003Spacer')
App.ActiveDocument.getObject('Pocket001Body003Spacer').Profile = App.ActiveDocument.getObject('Sketch001Body003Spacer')
App.ActiveDocument.getObject('Pocket001Body003Spacer').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body003Spacer').Visibility = False


# PointNut001Body003Spacer

if App.ActiveDocument.getObject('PointNut001Body003Spacer'):
    App.ActiveDocument.removeObject('PointNut001Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Spacer').newObject('PartDesign::Point', 'PointNut001Body003Spacer')
App.ActiveDocument.getObject('PointNut001Body003Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body003Spacer'), 'Edge45')]
App.ActiveDocument.getObject('PointNut001Body003Spacer').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('PointNut001Body003Spacer').Visibility = False


# LocalSupport001Body003Spacer

if App.ActiveDocument.getObject('LocalSupport001Body003Spacer'):
    App.ActiveDocument.removeObject('LocalSupport001Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Spacer').newObject('PartDesign::CoordinateSystem', 'LocalSupport001Body003Spacer')
App.ActiveDocument.getObject('LocalSupport001Body003Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body003Spacer'), 'Edge39')]
App.ActiveDocument.getObject('LocalSupport001Body003Spacer').MapMode = 'SectionOfRevolution'
App.ActiveDocument.getObject('LocalSupport001Body003Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Rotation(-90, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('LocalSupport001Body003Spacer').Visibility = False


# Sketch002Body003Spacer

if App.ActiveDocument.getObject('Sketch002Body003Spacer'):
    App.ActiveDocument.removeObject('Sketch002Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Spacer').newObject('Sketcher::SketchObject', 'Sketch002Body003Spacer')
App.ActiveDocument.getObject('Sketch002Body003Spacer').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body003Spacer').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch002Body003Spacer').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 1, 0), App.Vector(0, 0, 1), 1))  # 0
geoList.append(Part.Circle(App.Vector(0, -1, 0), App.Vector(0, 0, 1), 1))  # 1
App.ActiveDocument.getObject('Sketch002Body003Spacer').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('PointOnObject', 1, 3, -2))  # 0
conList.append(Sketcher.Constraint('Distance', 1, 3, 0, 3, 16))  # 3
conList.append(Sketcher.Constraint('Symmetric', 0, 3, 1, 3, -1))  # 1
conList.append(Sketcher.Constraint('Diameter', 0, 1/4*25.4))  # 4
conList.append(Sketcher.Constraint('Equal', 1, 0))  # 5
App.ActiveDocument.getObject('Sketch002Body003Spacer').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket002Body003Spacer

if App.ActiveDocument.getObject('Pocket002Body003Spacer'):
    App.ActiveDocument.removeObject('Pocket002Body003Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Spacer').newObject('PartDesign::Pocket', 'Pocket002Body003Spacer')
App.ActiveDocument.getObject('Pocket002Body003Spacer').Profile = App.ActiveDocument.getObject('Sketch002Body003Spacer')
App.ActiveDocument.getObject('Pocket002Body003Spacer').Reversed = True
App.ActiveDocument.getObject('Pocket002Body003Spacer').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch002Body003Spacer').Visibility = False


# Body004Spacer

if App.ActiveDocument.getObject('Body004Spacer'):
    App.ActiveDocument.getObject('Body004Spacer').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body004Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body004Spacer')
App.ActiveDocument.getObject('Body004Spacer').BaseFeature = App.ActiveDocument.getObject('Body002Spacer')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body004Spacer'))


# Binder001Body004Spacer

if App.ActiveDocument.getObject('Binder001Body004Spacer'):
    App.ActiveDocument.removeObject('Binder001Body004Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Spacer').newObject('PartDesign::ShapeBinder', 'Binder001Body004Spacer')
App.ActiveDocument.getObject('Binder001Body004Spacer').Support = App.ActiveDocument.getObject('Sketch001Body003Spacer')
App.ActiveDocument.recompute()


# Pocket001Body004Spacer

if App.ActiveDocument.getObject('Pocket001Body004Spacer'):
    App.ActiveDocument.removeObject('Pocket001Body004Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Spacer').newObject('PartDesign::Pocket', 'Pocket001Body004Spacer')
App.ActiveDocument.getObject('Pocket001Body004Spacer').Profile = App.ActiveDocument.getObject('Binder001Body004Spacer')
App.ActiveDocument.getObject('Pocket001Body004Spacer').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body004Spacer').Visibility = False


# PointNut001Body004Spacer

if App.ActiveDocument.getObject('PointNut001Body004Spacer'):
    App.ActiveDocument.removeObject('PointNut001Body004Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Spacer').newObject('PartDesign::Point', 'PointNut001Body004Spacer')
App.ActiveDocument.getObject('PointNut001Body004Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body004Spacer'), 'Edge45')]
App.ActiveDocument.getObject('PointNut001Body004Spacer').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('PointNut001Body004Spacer').Visibility = False


# LocalSupport001Body004Spacer

if App.ActiveDocument.getObject('LocalSupport001Body004Spacer'):
    App.ActiveDocument.removeObject('LocalSupport001Body004Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Spacer').newObject('PartDesign::CoordinateSystem', 'LocalSupport001Body004Spacer')
App.ActiveDocument.getObject('LocalSupport001Body004Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body004Spacer'), 'Edge39')]
App.ActiveDocument.getObject('LocalSupport001Body004Spacer').MapMode = 'SectionOfRevolution'
App.ActiveDocument.getObject('LocalSupport001Body004Spacer').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Rotation(-90, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('LocalSupport001Body004Spacer').Visibility = False


# Body005Spacer

if App.ActiveDocument.getObject('Body005Spacer'):
    App.ActiveDocument.getObject('Body005Spacer').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body005Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body005Spacer')
App.ActiveDocument.getObject('Body005Spacer').BaseFeature = App.ActiveDocument.getObject('Body001Spacer')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body005Spacer'))


# Binder001Body005Spacer

if App.ActiveDocument.getObject('Binder001Body005Spacer'):
    App.ActiveDocument.removeObject('Binder001Body005Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body005Spacer').newObject('PartDesign::ShapeBinder', 'Binder001Body005Spacer')
App.ActiveDocument.getObject('Binder001Body005Spacer').Support = App.ActiveDocument.getObject('Sketch001Body003Spacer')
App.ActiveDocument.recompute()


# Pocket001Body005Spacer

if App.ActiveDocument.getObject('Pocket001Body005Spacer'):
    App.ActiveDocument.removeObject('Pocket001Body005Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body005Spacer').newObject('PartDesign::Pocket', 'Pocket001Body005Spacer')
App.ActiveDocument.getObject('Pocket001Body005Spacer').Profile = App.ActiveDocument.getObject('Binder001Body005Spacer')
App.ActiveDocument.getObject('Pocket001Body005Spacer').Midplane = True
App.ActiveDocument.getObject('Pocket001Body005Spacer').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body005Spacer').Visibility = False


# PointNut00xBody005Spacer

if App.ActiveDocument.getObject('PointNut001Body005Spacer'):
    App.ActiveDocument.removeObject('PointNut001Body005Spacer')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointNut002Body005Spacer'):
    App.ActiveDocument.removeObject('PointNut002Body005Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body005Spacer').newObject('PartDesign::Point', 'PointNut001Body005Spacer')
App.ActiveDocument.getObject('PointNut001Body005Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body005Spacer'), 'Edge46')]
App.ActiveDocument.getObject('PointNut001Body005Spacer').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body005Spacer').newObject('PartDesign::Point', 'PointNut002Body005Spacer')
App.ActiveDocument.getObject('PointNut002Body005Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body005Spacer'), 'Edge51')]
App.ActiveDocument.getObject('PointNut002Body005Spacer').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()


App.ActiveDocument.getObject('PointNut001Body005Spacer').Visibility = False
App.ActiveDocument.getObject('PointNut002Body005Spacer').Visibility = False


# Binder002Body005Spacer

if App.ActiveDocument.getObject('Binder002Body005Spacer'):
    App.ActiveDocument.removeObject('Binder002Body005Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body005Spacer').newObject('PartDesign::ShapeBinder', 'Binder002Body005Spacer')
App.ActiveDocument.getObject('Binder002Body005Spacer').Support = App.ActiveDocument.getObject('Sketch002Body003Spacer')
App.ActiveDocument.recompute()


# Pocket002Body005Spacer

if App.ActiveDocument.getObject('Pocket002Body005Spacer'):
    App.ActiveDocument.removeObject('Pocket002Body005Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body005Spacer').newObject('PartDesign::Pocket', 'Pocket002Body005Spacer')
App.ActiveDocument.getObject('Pocket002Body005Spacer').Profile = App.ActiveDocument.getObject('Binder002Body005Spacer')
App.ActiveDocument.getObject('Pocket002Body005Spacer').Reversed = True
App.ActiveDocument.getObject('Pocket002Body005Spacer').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder002Body005Spacer').Visibility = False


# Body006Spacer

if App.ActiveDocument.getObject('Body006Spacer'):
    App.ActiveDocument.getObject('Body006Spacer').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body006Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body006Spacer')
App.ActiveDocument.getObject('Body006Spacer').BaseFeature = App.ActiveDocument.getObject('Body002Spacer')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body006Spacer'))


# Binder001Body006Spacer

if App.ActiveDocument.getObject('Binder001Body006Spacer'):
    App.ActiveDocument.removeObject('Binder001Body006Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body006Spacer').newObject('PartDesign::ShapeBinder', 'Binder001Body006Spacer')
App.ActiveDocument.getObject('Binder001Body006Spacer').Support = App.ActiveDocument.getObject('Sketch001Body003Spacer')
App.ActiveDocument.recompute()


# Pocket001Body006Spacer

if App.ActiveDocument.getObject('Pocket001Body006Spacer'):
    App.ActiveDocument.removeObject('Pocket001Body006Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body006Spacer').newObject('PartDesign::Pocket', 'Pocket001Body006Spacer')
App.ActiveDocument.getObject('Pocket001Body006Spacer').Profile = App.ActiveDocument.getObject('Binder001Body006Spacer')
App.ActiveDocument.getObject('Pocket001Body006Spacer').Midplane = True
App.ActiveDocument.getObject('Pocket001Body006Spacer').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Binder001Body006Spacer').Visibility = False


# PointNut00xBody006Spacer

if App.ActiveDocument.getObject('PointNut001Body006Spacer'):
    App.ActiveDocument.removeObject('PointNut001Body006Spacer')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointNut002Body006Spacer'):
    App.ActiveDocument.removeObject('PointNut002Body006Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body006Spacer').newObject('PartDesign::Point', 'PointNut001Body006Spacer')
App.ActiveDocument.getObject('PointNut001Body006Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body006Spacer'), 'Edge46')]
App.ActiveDocument.getObject('PointNut001Body006Spacer').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body006Spacer').newObject('PartDesign::Point', 'PointNut002Body006Spacer')
App.ActiveDocument.getObject('PointNut002Body006Spacer').Support = [(App.ActiveDocument.getObject('Pocket001Body006Spacer'), 'Edge51')]
App.ActiveDocument.getObject('PointNut002Body006Spacer').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()


App.ActiveDocument.getObject('PointNut001Body006Spacer').Visibility = False
App.ActiveDocument.getObject('PointNut002Body006Spacer').Visibility = False


# Group001Spacer

if App.ActiveDocument.getObject('Group001Spacer'):
    App.ActiveDocument.removeObject('Group001Spacer')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::DocumentObjectGroup', 'Group001Spacer')
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('SquareProfileSketch001Spacer'))
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('Body001Spacer'))
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('Body002Spacer'))
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('Body003Spacer'))
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('Body004Spacer'))
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('Body005Spacer'))
App.ActiveDocument.getObject('Group001Spacer').addObject(App.ActiveDocument.getObject('Body006Spacer'))
App.ActiveDocument.recompute()


# ShapeColor

App.ActiveDocument.getObject('Body001Spacer').ViewObject.ShapeColor = (0.3, 0.3, 1.0, 0.0)
App.ActiveDocument.getObject('Body002Spacer').ViewObject.ShapeColor = (0.3, 0.3, 1.0, 0.0)
App.ActiveDocument.getObject('Body003Spacer').ViewObject.ShapeColor = (0.3, 0.3, 1.0, 0.0)
App.ActiveDocument.getObject('Body004Spacer').ViewObject.ShapeColor = (0.3, 0.3, 1.0, 0.0)
App.ActiveDocument.getObject('Body005Spacer').ViewObject.ShapeColor = (0.3, 0.3, 1.0, 0.0)
App.ActiveDocument.getObject('Body006Spacer').ViewObject.ShapeColor = (0.3, 0.3, 1.0, 0.0)


# Placement

for obj in App.ActiveDocument.getObject('Group001Spacer').Group:
    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))


# YAxis

for i in range(1, len(App.ActiveDocument.getObject('Group001Spacer').Group)):
    App.ActiveDocument.getObject('Group001Spacer').Group[i].Placement.Base.y = \
        App.ActiveDocument.getObject('Group001Nema17').Shape.BoundBox.Center.y - (
        App.ActiveDocument.getObject('Group001Nema17').Shape.BoundBox.YLength +
        App.ActiveDocument.getObject('Group001Spacer').Shape.BoundBox.YLength)*75/100


# XAxis

for i in range(2, len(App.ActiveDocument.getObject('Group001Spacer').Group)):
    App.ActiveDocument.getObject('Group001Spacer').Group[i].Placement.Base.x = \
        App.ActiveDocument.getObject('Group001Spacer').Group[i-1].Placement.Base.x + (
        App.ActiveDocument.getObject('Group001Spacer').Group[i-1].Shape.BoundBox.XLength +
        App.ActiveDocument.getObject('Group001Spacer').Group[i].Shape.BoundBox.XLength)*75/100


App.ActiveDocument.recompute()


# Body001Support

if App.ActiveDocument.getObject('Body001Support'):
    App.ActiveDocument.getObject('Body001Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body001Support')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body002Support'))


# Binder001Body002Support

if App.ActiveDocument.getObject('Binder001Body001Support'):
    App.ActiveDocument.removeObject('Binder001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::ShapeBinder', 'Binder001Body001Support')
App.ActiveDocument.getObject('Binder001Body001Support').Support = App.ActiveDocument.getObject('Sketch001Body001Nema17')
App.ActiveDocument.recompute()


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


# Local001Body001Support

if App.ActiveDocument.getObject('Local001Body001Support'):
    App.ActiveDocument.removeObject('Local001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::CoordinateSystem', 'Local001Body001Support')
App.ActiveDocument.getObject('Local001Body001Support').Support = [(App.ActiveDocument.getObject('Pad001Body001Support'), 'Face9')]
App.ActiveDocument.getObject('Local001Body001Support').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(180, 0, 0), 180)
App.ActiveDocument.getObject('Local001Body001Support').MapMode = 'FlatFace'
App.ActiveDocument.getObject('Local001Body001Support').Visibility = False
App.ActiveDocument.recompute()


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


# Point001Body001Support

if App.ActiveDocument.getObject('Point001Body001Support'):
    App.ActiveDocument.removeObject('Point001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Point', 'Point001Body001Support')
App.ActiveDocument.getObject('Point001Body001Support').Support = [(App.ActiveDocument.getObject('Pocket001Body001Support'), 'Face11')]
App.ActiveDocument.getObject('Point001Body001Support').MapMode = 'CenterOfMass'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Point001Body001Support').Visibility = False


# Hole001Body001Support

if App.ActiveDocument.getObject('Hole001Body001Support'):
    App.ActiveDocument.removeObject('Hole001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Hole', 'Hole001Body001Support')
App.ActiveDocument.getObject('Hole001Body001Support').Profile = (App.ActiveDocument.getObject('Pocket001Body001Support'), ['Face12', ])
App.ActiveDocument.getObject('Hole001Body001Support').DepthType = 'ThroughAll'
App.ActiveDocument.getObject('Hole001Body001Support').Diameter = 10
App.ActiveDocument.recompute()


# Hole002Body001Support

if App.ActiveDocument.getObject('Hole002Body001Support'):
    App.ActiveDocument.removeObject('Hole002Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Hole', 'Hole002Body001Support')
App.ActiveDocument.getObject('Hole002Body001Support').Profile = (
    App.ActiveDocument.getObject('Hole001Body001Support'), ['Edge20', 'Edge22', 'Edge18', 'Edge19', ])
App.ActiveDocument.getObject('Hole002Body001Support').Diameter = 6
App.ActiveDocument.getObject('Hole002Body001Support').Depth = 3
App.ActiveDocument.getObject('Hole002Body001Support').DrillPoint = 'Flat'
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# PointScrew00xBody001Support

if App.ActiveDocument.getObject('PointScrew001Body001Support'):
    App.ActiveDocument.removeObject('PointScrew001Body001Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointScrew002Body001Support'):
    App.ActiveDocument.removeObject('PointScrew002Body001Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointScrew003Body001Support'):
    App.ActiveDocument.removeObject('PointScrew003Body001Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointScrew004Body001Support'):
    App.ActiveDocument.removeObject('PointScrew004Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Point', 'PointScrew001Body001Support')
App.ActiveDocument.getObject('PointScrew001Body001Support').Support = [(App.ActiveDocument.getObject('Hole002Body001Support'), 'Edge28')]
App.ActiveDocument.getObject('PointScrew001Body001Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Point', 'PointScrew002Body001Support')
App.ActiveDocument.getObject('PointScrew002Body001Support').Support = [(App.ActiveDocument.getObject('Hole002Body001Support'), 'Edge32')]
App.ActiveDocument.getObject('PointScrew002Body001Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Point', 'PointScrew003Body001Support')
App.ActiveDocument.getObject('PointScrew003Body001Support').Support = [(App.ActiveDocument.getObject('Hole002Body001Support'), 'Edge24')]
App.ActiveDocument.getObject('PointScrew003Body001Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Point', 'PointScrew004Body001Support')
App.ActiveDocument.getObject('PointScrew004Body001Support').Support = [(App.ActiveDocument.getObject('Hole002Body001Support'), 'Edge26')]
App.ActiveDocument.getObject('PointScrew004Body001Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('PointScrew001Body001Support').Visibility = False
App.ActiveDocument.getObject('PointScrew002Body001Support').Visibility = False
App.ActiveDocument.getObject('PointScrew003Body001Support').Visibility = False
App.ActiveDocument.getObject('PointScrew004Body001Support').Visibility = False


# Chamfer001Body001Support

if App.ActiveDocument.getObject('Chamfer001Body001Support'):
    App.ActiveDocument.removeObject('Chamfer001Body001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body001Support').newObject('PartDesign::Chamfer', 'Chamfer001Body001Support')
App.ActiveDocument.getObject('Chamfer001Body001Support').Base = (
    App.ActiveDocument.getObject('Hole002Body001Support'), ['Edge1', 'Edge2', 'Edge5', 'Edge8', ])
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

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::ShapeBinder', 'Binder001Body002Support')
App.ActiveDocument.getObject('Binder001Body002Support').Support = App.ActiveDocument.getObject('Sketch001Body001Nema17')
App.ActiveDocument.recompute()


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


# Local001Body002Support

if App.ActiveDocument.getObject('Local001Body002Support'):
    App.ActiveDocument.removeObject('Local001Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::CoordinateSystem', 'Local001Body002Support')
App.ActiveDocument.getObject('Local001Body002Support').Support = [(App.ActiveDocument.getObject('Pad001Body002Support'), 'Face9')]
App.ActiveDocument.getObject('Local001Body002Support').MapMode = 'FlatFace'
App.ActiveDocument.getObject('Local001Body002Support').Visibility = False
App.ActiveDocument.recompute()


# PointSpacer00xBody002Support

if App.ActiveDocument.getObject('PointSpacer001Body002Support'):
    App.ActiveDocument.removeObject('PointSpacer001Body002Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointSpacer002Body002Support'):
    App.ActiveDocument.removeObject('PointSpacer002Body002Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointSpacer003Body002Support'):
    App.ActiveDocument.removeObject('PointSpacer003Body002Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointSpacer004Body002Support'):
    App.ActiveDocument.removeObject('PointSpacer004Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointSpacer001Body002Support')
App.ActiveDocument.getObject('PointSpacer001Body002Support').Support = [(App.ActiveDocument.getObject('Pad001Body002Support'), 'Edge23')]
App.ActiveDocument.getObject('PointSpacer001Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointSpacer002Body002Support')
App.ActiveDocument.getObject('PointSpacer002Body002Support').Support = [(App.ActiveDocument.getObject('Pad001Body002Support'), 'Edge20')]
App.ActiveDocument.getObject('PointSpacer002Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointSpacer003Body002Support')
App.ActiveDocument.getObject('PointSpacer003Body002Support').Support = [(App.ActiveDocument.getObject('Pad001Body002Support'), 'Edge17')]
App.ActiveDocument.getObject('PointSpacer003Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointSpacer004Body002Support')
App.ActiveDocument.getObject('PointSpacer004Body002Support').Support = [(App.ActiveDocument.getObject('Pad001Body002Support'), 'Edge14')]
App.ActiveDocument.getObject('PointSpacer004Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('PointSpacer001Body002Support').Visibility = False
App.ActiveDocument.getObject('PointSpacer002Body002Support').Visibility = False
App.ActiveDocument.getObject('PointSpacer003Body002Support').Visibility = False
App.ActiveDocument.getObject('PointSpacer004Body002Support').Visibility = False


# Hole001Body002Support

if App.ActiveDocument.getObject('Hole001Body002Support'):
    App.ActiveDocument.removeObject('Hole001Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Hole', 'Hole001Body002Support')
App.ActiveDocument.getObject('Hole001Body002Support').Profile = (
    App.ActiveDocument.getObject('Pad001Body002Support'), ['Edge24', 'Edge21', 'Edge18', 'Edge15', ])
App.ActiveDocument.getObject('Hole001Body002Support').Diameter = 6
App.ActiveDocument.getObject('Hole001Body002Support').Depth = 3
App.ActiveDocument.getObject('Hole001Body002Support').DrillPoint = 'Flat'
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# PointScrew00xBody002Support

if App.ActiveDocument.getObject('PointScrew001Body002Support'):
    App.ActiveDocument.removeObject('PointScrew001Body002Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointScrew002Body002Support'):
    App.ActiveDocument.removeObject('PointScrew002Body002Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointScrew003Body002Support'):
    App.ActiveDocument.removeObject('PointScrew003Body002Support')
    App.ActiveDocument.recompute()

if App.ActiveDocument.getObject('PointScrew004Body002Support'):
    App.ActiveDocument.removeObject('PointScrew004Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointScrew001Body002Support')
App.ActiveDocument.getObject('PointScrew001Body002Support').Support = [(App.ActiveDocument.getObject('Hole001Body002Support'), 'Edge28')]
App.ActiveDocument.getObject('PointScrew001Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointScrew002Body002Support')
App.ActiveDocument.getObject('PointScrew002Body002Support').Support = [(App.ActiveDocument.getObject('Hole001Body002Support'), 'Edge26')]
App.ActiveDocument.getObject('PointScrew002Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointScrew003Body002Support')
App.ActiveDocument.getObject('PointScrew003Body002Support').Support = [(App.ActiveDocument.getObject('Hole001Body002Support'), 'Edge24')]
App.ActiveDocument.getObject('PointScrew003Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Point', 'PointScrew004Body002Support')
App.ActiveDocument.getObject('PointScrew004Body002Support').Support = [(App.ActiveDocument.getObject('Hole001Body002Support'), 'Edge22')]
App.ActiveDocument.getObject('PointScrew004Body002Support').MapMode = 'CenterOfCurvature'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('PointScrew001Body002Support').Visibility = False
App.ActiveDocument.getObject('PointScrew002Body002Support').Visibility = False
App.ActiveDocument.getObject('PointScrew003Body002Support').Visibility = False
App.ActiveDocument.getObject('PointScrew004Body002Support').Visibility = False


# Chamfer001Body002Support

if App.ActiveDocument.getObject('Chamfer001Body002Support'):
    App.ActiveDocument.removeObject('Chamfer001Body002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body002Support').newObject('PartDesign::Chamfer', 'Chamfer001Body002Support')
App.ActiveDocument.getObject('Chamfer001Body002Support').Base = (
    App.ActiveDocument.getObject('Hole001Body002Support'), ['Edge2', 'Edge8', 'Edge1', 'Edge5', ])
App.ActiveDocument.getObject('Chamfer001Body002Support').Size = 3
App.ActiveDocument.recompute()


# ShapeColor

App.ActiveDocument.getObject('Body002Support').ViewObject.ShapeColor = App.ActiveDocument.getObject('Body001Support').ViewObject.ShapeColor


# Placement

App.ActiveDocument.getObject('Body002Support').Placement.Base.x = (
    App.ActiveDocument.getObject('Body001Support').Shape.BoundBox.XLength +
    App.ActiveDocument.getObject('Body002Support').Shape.BoundBox.XLength)*75/100
App.ActiveDocument.recompute()


# Part001Support

if App.ActiveDocument.getObject('Part001Support'):
    App.ActiveDocument.getObject('Part001Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part001Support')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part001Support'))
App.ActiveDocument.recompute()


# Link001Body001Support

App.ActiveDocument.getObject('Part001Support').newObject('App::Link', 'Link001Body001Support')
App.ActiveDocument.getObject('Link001Body001Support').LinkedObject = App.ActiveDocument.getObject('Body001Support')
App.ActiveDocument.recompute()


# Link001Part001Bearing

App.ActiveDocument.getObject('Part001Support').newObject('App::Link', 'Link001Part001Bearing')
App.ActiveDocument.getObject('Link001Part001Bearing').LinkedObject = App.ActiveDocument.getObject('Part001Bearing')
App.ActiveDocument.getObject('Link001Part001Bearing').Placement *= App.ActiveDocument.getObject('Local001Pad001Body001Bearing').Placement
App.ActiveDocument.getObject('Link001Part001Bearing').Placement *= App.ActiveDocument.getObject('Point001Body001Support').Placement
App.ActiveDocument.recompute()


# Link00xM3x20_Screw

App.ActiveDocument.getObject('Part001Support').newObject('App::Link', 'Link001M3x20_Screw')
App.ActiveDocument.getObject('Link001M3x20_Screw').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x20-Screw')[0]
App.ActiveDocument.getObject('Link001M3x20_Screw').Placement *= App.ActiveDocument.getObject('PointScrew001Body001Support').Placement
App.ActiveDocument.getObject('Link001M3x20_Screw').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Support').newObject('App::Link', 'Link002M3x20_Screw')
App.ActiveDocument.getObject('Link002M3x20_Screw').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x20-Screw')[0]
App.ActiveDocument.getObject('Link002M3x20_Screw').Placement *= App.ActiveDocument.getObject('PointScrew002Body001Support').Placement
App.ActiveDocument.getObject('Link002M3x20_Screw').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Support').newObject('App::Link', 'Link003M3x20_Screw')
App.ActiveDocument.getObject('Link003M3x20_Screw').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x20-Screw')[0]
App.ActiveDocument.getObject('Link003M3x20_Screw').Placement *= App.ActiveDocument.getObject('PointScrew003Body001Support').Placement
App.ActiveDocument.getObject('Link003M3x20_Screw').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part001Support').newObject('App::Link', 'Link004M3x20_Screw')
App.ActiveDocument.getObject('Link004M3x20_Screw').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x20-Screw')[0]
App.ActiveDocument.getObject('Link004M3x20_Screw').Placement *= App.ActiveDocument.getObject('PointScrew004Body001Support').Placement
App.ActiveDocument.getObject('Link004M3x20_Screw').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()


Gui.ActiveDocument.ActiveView.setActiveObject('part', None)


# Part002Support

if App.ActiveDocument.getObject('Part002Support'):
    App.ActiveDocument.getObject('Part002Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part002Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part002Support')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part002Support'))
App.ActiveDocument.recompute()


# Link001Body002Support

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link001Body002Support')
App.ActiveDocument.getObject('Link001Body002Support').LinkedObject = App.ActiveDocument.getObject('Body002Support')
App.ActiveDocument.recompute()


# Link00xM3x15ScrewPart002Support

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link001M3x15ScrewPart002Support')
App.ActiveDocument.getObject('Link001M3x15ScrewPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x15-Screw')[0]
App.ActiveDocument.getObject('Link001M3x15ScrewPart002Support').Placement *= App.ActiveDocument.getObject('PointScrew001Body002Support').Placement
App.ActiveDocument.getObject('Link001M3x15ScrewPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link002M3x15ScrewPart002Support')
App.ActiveDocument.getObject('Link002M3x15ScrewPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x15-Screw')[0]
App.ActiveDocument.getObject('Link002M3x15ScrewPart002Support').Placement *= App.ActiveDocument.getObject('PointScrew002Body002Support').Placement
App.ActiveDocument.getObject('Link002M3x15ScrewPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link003M3x15ScrewPart002Support')
App.ActiveDocument.getObject('Link003M3x15ScrewPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x15-Screw')[0]
App.ActiveDocument.getObject('Link003M3x15ScrewPart002Support').Placement *= App.ActiveDocument.getObject('PointScrew003Body002Support').Placement
App.ActiveDocument.getObject('Link003M3x15ScrewPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link004M3x15ScrewPart002Support')
App.ActiveDocument.getObject('Link004M3x15ScrewPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x15-Screw')[0]
App.ActiveDocument.getObject('Link004M3x15ScrewPart002Support').Placement *= App.ActiveDocument.getObject('PointScrew004Body002Support').Placement
App.ActiveDocument.getObject('Link004M3x15ScrewPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()


# Link00xM3x5x35SpacerPart002Support

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link001M3x5x35SpacerPart002Support')
App.ActiveDocument.getObject('Link001M3x5x35SpacerPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5x35-Spacer')[0]
App.ActiveDocument.getObject('Link001M3x5x35SpacerPart002Support').Placement *= App.ActiveDocument.getObject('PointSpacer001Body002Support').Placement
App.ActiveDocument.getObject('Link001M3x5x35SpacerPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link002M3x5x35SpacerPart002Support')
App.ActiveDocument.getObject('Link002M3x5x35SpacerPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5x35-Spacer')[0]
App.ActiveDocument.getObject('Link002M3x5x35SpacerPart002Support').Placement *= App.ActiveDocument.getObject('PointSpacer002Body002Support').Placement
App.ActiveDocument.getObject('Link002M3x5x35SpacerPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link003M3x5x35SpacerPart002Support')
App.ActiveDocument.getObject('Link003M3x5x35SpacerPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5x35-Spacer')[0]
App.ActiveDocument.getObject('Link003M3x5x35SpacerPart002Support').Placement *= App.ActiveDocument.getObject('PointSpacer003Body002Support').Placement
App.ActiveDocument.getObject('Link003M3x5x35SpacerPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Support').newObject('App::Link', 'Link004M3x5x35SpacerPart002Support')
App.ActiveDocument.getObject('Link004M3x5x35SpacerPart002Support').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('M3x5.5x35-Spacer')[0]
App.ActiveDocument.getObject('Link004M3x5x35SpacerPart002Support').Placement *= App.ActiveDocument.getObject('PointSpacer004Body002Support').Placement
App.ActiveDocument.getObject('Link004M3x5x35SpacerPart002Support').Placement *= App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 90))
App.ActiveDocument.recompute()


Gui.ActiveDocument.ActiveView.setActiveObject('part', None)


# Body003Support

if App.ActiveDocument.getObject('Body003Support'):
    App.ActiveDocument.getObject('Body003Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body003Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body003Support')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body003Support'))


# Sketch001Body003Support

if App.ActiveDocument.getObject('Sketch001Body003Support'):
    App.ActiveDocument.removeObject('Sketch001Body003Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Support').newObject('Sketcher::SketchObject', 'Sketch001Body003Support')
App.ActiveDocument.getObject('Sketch001Body003Support').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body003Support').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body003Support').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.LineSegment(App.Vector(-1, 1, 0), App.Vector(1, 1, 0)))  # 0
geoList.append(Part.LineSegment(App.Vector(1, 1, 0), App.Vector(1, -1, 0)))  # 1
geoList.append(Part.LineSegment(App.Vector(1, -1, 0), App.Vector(-1, -1, 0)))  # 2
geoList.append(Part.LineSegment(App.Vector(-1, -1, 0), App.Vector(-1, 1, 0)))  # 3
App.ActiveDocument.getObject('Sketch001Body003Support').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))  # 1
conList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))  # 2
conList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))  # 3
conList.append(Sketcher.Constraint('Horizontal', 0))  # 4
conList.append(Sketcher.Constraint('Vertical', 1))  # 5
conList.append(Sketcher.Constraint('Symmetric', 2, 1, 2, 2, -2))  # 6
conList.append(Sketcher.Constraint('Symmetric', 0, 1, 2, 2, -1))  # 7
conList.append(Sketcher.Constraint('Distance', 0, App.ActiveDocument.getObject('Body001Spacer').Shape.BoundBox.XLength))  # 8
conList.append(Sketcher.Constraint('Distance', 1, App.ActiveDocument.getObject('Body001Spacer').Shape.BoundBox.YLength))  # 9
App.ActiveDocument.getObject('Sketch001Body003Support').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body003Support

if App.ActiveDocument.getObject('Pad001Body003Support'):
    App.ActiveDocument.removeObject('Pad001Body003Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Support').newObject('PartDesign::Pad', 'Pad001Body003Support')
App.ActiveDocument.getObject('Pad001Body003Support').Profile = App.ActiveDocument.getObject('Sketch001Body003Support')
App.ActiveDocument.getObject('Pad001Body003Support').Length = 22/2 + 1*25.4/2
App.ActiveDocument.getObject('Pad001Body003Support').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body003Support').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Sketch002Body003Support

if App.ActiveDocument.getObject('Sketch002Body003Support'):
    App.ActiveDocument.removeObject('Sketch002Body003Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Support').newObject('Sketcher::SketchObject', 'Sketch002Body003Support')
App.ActiveDocument.getObject('Sketch002Body003Support').Support = (App.ActiveDocument.getObject('Pad001Body003Support'), ['Face6'])
App.ActiveDocument.getObject('Sketch002Body003Support').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
App.ActiveDocument.getObject('Sketch002Body003Support').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Diameter', 0, 5/16*25.4))  # 1
App.ActiveDocument.getObject('Sketch002Body003Support').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket001Body003Support

if App.ActiveDocument.getObject('Pocket001Body003Support'):
    App.ActiveDocument.removeObject('Pocket001Body003Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Support').newObject('PartDesign::Pocket', 'Pocket001Body003Support')
App.ActiveDocument.getObject('Pocket001Body003Support').Profile = App.ActiveDocument.getObject('Sketch002Body003Support')
App.ActiveDocument.getObject('Pocket001Body003Support').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch002Body003Support').Visibility = False


# LocalSpacer001Body003Support

if App.ActiveDocument.getObject('LocalSpacer001Body003Support'):
    App.ActiveDocument.removeObject('LocalSpacer001Body003Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body003Support').newObject('PartDesign::CoordinateSystem', 'LocalSpacer001Body003Support')
App.ActiveDocument.getObject('LocalSpacer001Body003Support').Support = [(App.ActiveDocument.getObject('Pocket001Body003Support'), 'Edge12')]
App.ActiveDocument.getObject('LocalSpacer001Body003Support').MapMode = 'SectionOfRevolution'
App.ActiveDocument.getObject('LocalSpacer001Body003Support').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 90)
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('LocalSpacer001Body003Support').Visibility = False


# ShapeColor

App.ActiveDocument.getObject('Body003Support').ViewObject.ShapeColor = (0.0, 0.6, 0.5, 0.0)


# Body004Support

if App.ActiveDocument.getObject('Body004Support'):
    App.ActiveDocument.getObject('Body004Support').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Body004Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('PartDesign::Body', 'Body004Support')
App.ActiveDocument.recompute()

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', App.ActiveDocument.getObject('Body004Support'))


# Sketch001Body004Support

if App.ActiveDocument.getObject('Sketch001Body004Support'):
    App.ActiveDocument.removeObject('Sketch001Body004Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Support').newObject('Sketcher::SketchObject', 'Sketch001Body004Support')
App.ActiveDocument.getObject('Sketch001Body004Support').Support = (App.ActiveDocument.getObject(
    'XY_Plane' + App.ActiveDocument.getObject('Body004Support').Origin.Name.replace('Origin', '')), [''])
App.ActiveDocument.getObject('Sketch001Body004Support').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.LineSegment(App.Vector(-1, 1, 0), App.Vector(1, 1, 0)))  # 0
geoList.append(Part.LineSegment(App.Vector(1, 1, 0), App.Vector(1, -1, 0)))  # 1
geoList.append(Part.LineSegment(App.Vector(1, -1, 0), App.Vector(-1, -1, 0)))  # 2
geoList.append(Part.LineSegment(App.Vector(-1, -1, 0), App.Vector(-1, 1, 0)))  # 3
App.ActiveDocument.getObject('Sketch001Body004Support').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))  # 0
conList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))  # 1
conList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))  # 2
conList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))  # 3
conList.append(Sketcher.Constraint('Horizontal', 0))  # 4
conList.append(Sketcher.Constraint('Vertical', 1))  # 5
conList.append(Sketcher.Constraint('Symmetric', 2, 1, 2, 2, -2))  # 6
conList.append(Sketcher.Constraint('Symmetric', 0, 1, 2, 2, -1))  # 7
conList.append(Sketcher.Constraint('Distance', 0, App.ActiveDocument.getObject('Body002Spacer').Shape.BoundBox.XLength))  # 8
conList.append(Sketcher.Constraint('Distance', 1, App.ActiveDocument.getObject('Body002Spacer').Shape.BoundBox.YLength))  # 9
App.ActiveDocument.getObject('Sketch001Body004Support').addConstraint(conList)

App.ActiveDocument.recompute()


# Pad001Body004Support

if App.ActiveDocument.getObject('Pad001Body004Support'):
    App.ActiveDocument.removeObject('Pad001Body004Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Support').newObject('PartDesign::Pad', 'Pad001Body004Support')
App.ActiveDocument.getObject('Pad001Body004Support').Profile = App.ActiveDocument.getObject('Sketch001Body004Support')
App.ActiveDocument.getObject('Pad001Body004Support').Length = 22/2 + 1*25.4/2
App.ActiveDocument.getObject('Pad001Body004Support').Midplane = True
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch001Body004Support').Visibility = False

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)


# Sketch002Body004Support

if App.ActiveDocument.getObject('Sketch002Body004Support'):
    App.ActiveDocument.removeObject('Sketch002Body004Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Support').newObject('Sketcher::SketchObject', 'Sketch002Body004Support')
App.ActiveDocument.getObject('Sketch002Body004Support').Support = (App.ActiveDocument.getObject('Pad001Body004Support'), ['Face6'])
App.ActiveDocument.getObject('Sketch002Body004Support').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 2))  # 0
App.ActiveDocument.getObject('Sketch002Body004Support').addGeometry(geoList, False)

conList = []
conList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))  # 0
conList.append(Sketcher.Constraint('Diameter', 0, 5/16*25.4))  # 1
App.ActiveDocument.getObject('Sketch002Body004Support').addConstraint(conList)

App.ActiveDocument.recompute()


# Pocket001Body004Support

if App.ActiveDocument.getObject('Pocket001Body004Support'):
    App.ActiveDocument.removeObject('Pocket001Body004Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Support').newObject('PartDesign::Pocket', 'Pocket001Body004Support')
App.ActiveDocument.getObject('Pocket001Body004Support').Profile = App.ActiveDocument.getObject('Sketch002Body004Support')
App.ActiveDocument.getObject('Pocket001Body004Support').Type = 'ThroughAll'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Sketch002Body004Support').Visibility = False


# LocalSpacer001Body004Support

if App.ActiveDocument.getObject('LocalSpacer001Body004Support'):
    App.ActiveDocument.removeObject('LocalSpacer001Body004Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Body004Support').newObject('PartDesign::CoordinateSystem', 'LocalSpacer001Body004Support')
App.ActiveDocument.getObject('LocalSpacer001Body004Support').Support = [(App.ActiveDocument.getObject('Pocket001Body004Support'), 'Edge12')]
App.ActiveDocument.getObject('LocalSpacer001Body004Support').MapMode = 'SectionOfRevolution'
App.ActiveDocument.getObject('LocalSpacer001Body004Support').AttachmentOffset = App.Placement(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 90)
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('LocalSpacer001Body004Support').Visibility = False


# ShapeColor

App.ActiveDocument.getObject('Body004Support').ViewObject.ShapeColor = (0.0, 0.6, 0.5, 0.0)


# Group001Support

if App.ActiveDocument.getObject('Group001Support'):
    App.ActiveDocument.removeObject('Group001Support')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::DocumentObjectGroup', 'Group001Support')
App.ActiveDocument.getObject('Group001Support').addObject(App.ActiveDocument.getObject('Body001Support'))
App.ActiveDocument.getObject('Group001Support').addObject(App.ActiveDocument.getObject('Body002Support'))
App.ActiveDocument.getObject('Group001Support').addObject(App.ActiveDocument.getObject('Part001Support'))
App.ActiveDocument.getObject('Group001Support').addObject(App.ActiveDocument.getObject('Part002Support'))
App.ActiveDocument.getObject('Group001Support').addObject(App.ActiveDocument.getObject('Body003Support'))
App.ActiveDocument.getObject('Group001Support').addObject(App.ActiveDocument.getObject('Body004Support'))
App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject('Group001Support').Group:
    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

App.ActiveDocument.getObject('Group001Spacer').Visibility = True
App.ActiveDocument.getObject('Group001Support').Visibility = True

# YAxis

for obj in App.ActiveDocument.getObject('Group001Support').Group:
    obj.Placement.Base.y = App.ActiveDocument.getObject('Group001Spacer').Shape.BoundBox.Center.y - (
        App.ActiveDocument.getObject('Group001Spacer').Shape.BoundBox.YLength +
        App.ActiveDocument.getObject('Group001Support').Shape.BoundBox.YLength)*75/100


# XAxis

for i in range(1, len(App.ActiveDocument.getObject('Group001Support').Group)):
    App.ActiveDocument.getObject('Group001Support').Group[i].Placement.Base.x = \
        App.ActiveDocument.getObject('Group001Support').Group[i-1].Placement.Base.x + (
            App.ActiveDocument.getObject('Group001Support').Group[i-1].Shape.BoundBox.XLength +
            App.ActiveDocument.getObject('Group001Support').Group[i].Shape.BoundBox.XLength)*75/100

App.ActiveDocument.recompute()


# Part001Engine

if App.ActiveDocument.getObject('Part001Engine'):
    App.ActiveDocument.getObject('Part001Engine').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part001Engine')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part001Engine')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part001Engine'))
App.ActiveDocument.recompute()


# Link001Body003Spacer

App.ActiveDocument.getObject('Part001Engine').newObject('App::Link', 'Link001Body003Spacer')
App.ActiveDocument.getObject('Link001Body003Spacer').LinkedObject = App.ActiveDocument.getObject('Body003Spacer')
App.ActiveDocument.getObject('Link001Body003Spacer').Placement *= App.ActiveDocument.getObject('Local001Body001Spacer').Placement
App.ActiveDocument.recompute()


# Link001Part001Nema17

App.ActiveDocument.getObject('Part001Engine').newObject('App::Link', 'Link001Part001Nema17')
App.ActiveDocument.getObject('Link001Part001Nema17').LinkedObject = App.ActiveDocument.getObject('Part001Nema17')
App.ActiveDocument.getObject('Link001Part001Nema17').Placement *= App.ActiveDocument.getObject('Link001Body003Spacer').Placement
App.ActiveDocument.getObject('Link001Part001Nema17').Placement *= App.ActiveDocument.getObject('Local002Body001Spacer').Placement
App.ActiveDocument.getObject('Link001Part001Nema17').Placement *= App.ActiveDocument.getObject('Local001Body002Nema17').Placement.inverse()
App.ActiveDocument.recompute()

# Part001CouplingPart001Engine

App.ActiveDocument.getObject('Part001Engine').newObject('App::Link', 'Part001CouplingPart001Engine')
App.ActiveDocument.getObject('Part001CouplingPart001Engine').LinkedObject = App.ActiveDocument.getObject('Part001Coupling')
App.ActiveDocument.getObject('Part001CouplingPart001Engine').Placement *= App.ActiveDocument.getObject('Link001Part001Nema17').Placement
App.ActiveDocument.getObject('Part001CouplingPart001Engine').Placement *= App.ActiveDocument.getObject('Local001Body004Nema17').Placement
App.ActiveDocument.getObject('Part001CouplingPart001Engine').Placement *= App.ActiveDocument.getObject('Local001Body001Coupling').Placement.inverse()
App.ActiveDocument.recompute()


# Link001Part001Support

App.ActiveDocument.getObject('Part001Engine').newObject('App::Link', 'Link001Part001Support')
App.ActiveDocument.getObject('Link001Part001Support').LinkedObject = App.ActiveDocument.getObject('Part001Support')
App.ActiveDocument.getObject('Link001Part001Support').Placement *= App.ActiveDocument.getObject('Link001Body003Spacer').Placement
App.ActiveDocument.getObject('Link001Part001Support').Placement *= App.ActiveDocument.getObject('Local003Body001Spacer').Placement
App.ActiveDocument.getObject('Link001Part001Support').Placement *= App.ActiveDocument.getObject('Local001Body001Support').Placement.inverse()
App.ActiveDocument.recompute()


# Body003SupportPart001Support

App.ActiveDocument.getObject('Part001Engine').newObject('App::Link', 'Body003SupportPart001Support')
App.ActiveDocument.getObject('Body003SupportPart001Support').LinkedObject = App.ActiveDocument.getObject('Body003Support')
App.ActiveDocument.getObject('Body003SupportPart001Support').Placement *= App.ActiveDocument.getObject('Link001Body003Spacer').Placement
App.ActiveDocument.getObject('Body003SupportPart001Support').Placement *= App.ActiveDocument.getObject('LocalSupport001Body003Spacer').Placement
App.ActiveDocument.getObject('Body003SupportPart001Support').Placement *= App.ActiveDocument.getObject('LocalSpacer001Body003Support').Placement.inverse()
App.ActiveDocument.recompute()


# LinkNut001Body003Spacer

App.ActiveDocument.getObject('Part001Engine').newObject('App::Link', 'LinkNut001Body003Spacer')
App.ActiveDocument.getObject('LinkNut001Body003Spacer').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('5/16in-Nut')[0]
App.ActiveDocument.getObject('LinkNut001Body003Spacer').Placement *= App.ActiveDocument.getObject('Link001Body003Spacer').Placement
App.ActiveDocument.getObject('LinkNut001Body003Spacer').Placement *= App.ActiveDocument.getObject('PointNut001Body003Spacer').Placement
App.ActiveDocument.getObject('LinkNut001Body003Spacer').Placement *= App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90)
App.ActiveDocument.recompute()


# Part002Engine

if App.ActiveDocument.getObject('Part002Engine'):
    App.ActiveDocument.getObject('Part002Engine').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part002Engine')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part002Engine')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part002Engine'))
App.ActiveDocument.recompute()


# Body004SpacerPart002Engine

App.ActiveDocument.getObject('Part002Engine').newObject('App::Link', 'Body004SpacerPart002Engine')
App.ActiveDocument.getObject('Body004SpacerPart002Engine').LinkedObject = App.ActiveDocument.getObject('Body004Spacer')
App.ActiveDocument.getObject('Body004SpacerPart002Engine').Placement *= App.ActiveDocument.getObject('Local001Body002Spacer').Placement
App.ActiveDocument.recompute()


# Part00xSupportPart002Engine

App.ActiveDocument.getObject('Part002Engine').newObject('App::Link', 'Part002SupportPart002Engine')
App.ActiveDocument.getObject('Part002SupportPart002Engine').LinkedObject = App.ActiveDocument.getObject('Part002Support')
App.ActiveDocument.getObject('Part002SupportPart002Engine').Placement *= App.ActiveDocument.getObject('Body004SpacerPart002Engine').Placement
App.ActiveDocument.getObject('Part002SupportPart002Engine').Placement *= App.ActiveDocument.getObject('Local002Body002Spacer').Placement
App.ActiveDocument.getObject('Part002SupportPart002Engine').Placement *= App.ActiveDocument.getObject('Local001Body002Support').Placement
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part002Engine').newObject('App::Link', 'Part001SupportPart002Engine')
App.ActiveDocument.getObject('Part001SupportPart002Engine').LinkedObject = App.ActiveDocument.getObject('Part001Support')
App.ActiveDocument.getObject('Part001SupportPart002Engine').Placement *= App.ActiveDocument.getObject('Body004SpacerPart002Engine').Placement
App.ActiveDocument.getObject('Part001SupportPart002Engine').Placement *= App.ActiveDocument.getObject('Local003Body002Spacer').Placement
App.ActiveDocument.getObject('Part001SupportPart002Engine').Placement *= App.ActiveDocument.getObject('Local001Body001Support').Placement.inverse()
App.ActiveDocument.recompute()

# Body004SupportPart001Support

App.ActiveDocument.getObject('Part002Engine').newObject('App::Link', 'Body004SupportPart001Support')
App.ActiveDocument.getObject('Body004SupportPart001Support').LinkedObject = App.ActiveDocument.getObject('Body004Support')
App.ActiveDocument.getObject('Body004SupportPart001Support').Placement *= App.ActiveDocument.getObject('Body004SpacerPart002Engine').Placement
App.ActiveDocument.getObject('Body004SupportPart001Support').Placement *= App.ActiveDocument.getObject('LocalSupport001Body004Spacer').Placement
App.ActiveDocument.getObject('Body004SupportPart001Support').Placement *= App.ActiveDocument.getObject('LocalSpacer001Body004Support').Placement.inverse()
App.ActiveDocument.recompute()


# LinkNut001Body004Spacer

App.ActiveDocument.getObject('Part002Engine').newObject('App::Link', 'LinkNut001Body004Spacer')
App.ActiveDocument.getObject('LinkNut001Body004Spacer').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('5/16in-Nut')[0]
App.ActiveDocument.getObject('LinkNut001Body004Spacer').Placement *= App.ActiveDocument.getObject('Body004SpacerPart002Engine').Placement
App.ActiveDocument.getObject('LinkNut001Body004Spacer').Placement *= App.ActiveDocument.getObject('PointNut001Body004Spacer').Placement
App.ActiveDocument.getObject('LinkNut001Body004Spacer').Placement *= App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90)
App.ActiveDocument.recompute()


# Part003Engine

if App.ActiveDocument.getObject('Part003Engine'):
    App.ActiveDocument.getObject('Part003Engine').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part003Engine')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part003Engine')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part003Engine'))
App.ActiveDocument.recompute()


# Body005SpacerPart003Engine

App.ActiveDocument.getObject('Part003Engine').newObject('App::Link', 'Body005SpacerPart003Engine')
App.ActiveDocument.getObject('Body005SpacerPart003Engine').LinkedObject = App.ActiveDocument.getObject('Body005Spacer')
App.ActiveDocument.getObject('Body005SpacerPart003Engine').Placement *= App.ActiveDocument.getObject('Local001Body001Spacer').Placement
App.ActiveDocument.recompute()


# Part001Nema17Part003Engine

App.ActiveDocument.getObject('Part003Engine').newObject('App::Link', 'Part001Nema17Part003Engine')
App.ActiveDocument.getObject('Part001Nema17Part003Engine').LinkedObject = App.ActiveDocument.getObject('Part001Nema17')
App.ActiveDocument.getObject('Part001Nema17Part003Engine').Placement *= App.ActiveDocument.getObject('Body005SpacerPart003Engine').Placement
App.ActiveDocument.getObject('Part001Nema17Part003Engine').Placement *= App.ActiveDocument.getObject('Local002Body001Spacer').Placement
App.ActiveDocument.getObject('Part001Nema17Part003Engine').Placement *= App.ActiveDocument.getObject('Local001Body002Nema17').Placement.inverse()
App.ActiveDocument.recompute()


# Part001CouplingPart003Engine

App.ActiveDocument.getObject('Part003Engine').newObject('App::Link', 'Part001CouplingPart003Engine')
App.ActiveDocument.getObject('Part001CouplingPart003Engine').LinkedObject = App.ActiveDocument.getObject('Part001Coupling')
App.ActiveDocument.getObject('Part001CouplingPart003Engine').Placement *= App.ActiveDocument.getObject('Part001Nema17Part003Engine').Placement
App.ActiveDocument.getObject('Part001CouplingPart003Engine').Placement *= App.ActiveDocument.getObject('Local001Body004Nema17').Placement
App.ActiveDocument.getObject('Part001CouplingPart003Engine').Placement *= App.ActiveDocument.getObject('Local001Body001Coupling').Placement.inverse()
App.ActiveDocument.recompute()


# Part001SupportPart003Engine

App.ActiveDocument.getObject('Part003Engine').newObject('App::Link', 'Part001SupportPart003Engine')
App.ActiveDocument.getObject('Part001SupportPart003Engine').LinkedObject = App.ActiveDocument.getObject('Part001Support')
App.ActiveDocument.getObject('Part001SupportPart003Engine').Placement *= App.ActiveDocument.getObject('Body005SpacerPart003Engine').Placement
App.ActiveDocument.getObject('Part001SupportPart003Engine').Placement *= App.ActiveDocument.getObject('Local003Body001Spacer').Placement
App.ActiveDocument.getObject('Part001SupportPart003Engine').Placement *= App.ActiveDocument.getObject('Local001Body001Support').Placement.inverse()
App.ActiveDocument.recompute()


# LinkNut00xBody005Spacer

App.ActiveDocument.getObject('Part003Engine').newObject('App::Link', 'LinkNut001Body005Spacer')
App.ActiveDocument.getObject('LinkNut001Body005Spacer').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('5/16in-Nut')[0]
App.ActiveDocument.getObject('LinkNut001Body005Spacer').Placement *= App.ActiveDocument.getObject('Body005SpacerPart003Engine').Placement
App.ActiveDocument.getObject('LinkNut001Body005Spacer').Placement *= App.ActiveDocument.getObject('PointNut001Body005Spacer').Placement
App.ActiveDocument.getObject('LinkNut001Body005Spacer').Placement *= App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90)
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part003Engine').newObject('App::Link', 'LinkNut002Body005Spacer')
App.ActiveDocument.getObject('LinkNut002Body005Spacer').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('5/16in-Nut')[0]
App.ActiveDocument.getObject('LinkNut002Body005Spacer').Placement *= App.ActiveDocument.getObject('Body005SpacerPart003Engine').Placement
App.ActiveDocument.getObject('LinkNut002Body005Spacer').Placement *= App.ActiveDocument.getObject('PointNut002Body005Spacer').Placement
App.ActiveDocument.getObject('LinkNut002Body005Spacer').Placement *= App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
App.ActiveDocument.recompute()


# Part004Engine

if App.ActiveDocument.getObject('Part004Engine'):
    App.ActiveDocument.getObject('Part004Engine').removeObjectsFromDocument()
    App.ActiveDocument.removeObject('Part004Engine')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::Part', 'Part004Engine')
Gui.ActiveDocument.ActiveView.setActiveObject('part', App.ActiveDocument.getObject('Part004Engine'))
App.ActiveDocument.recompute()


# Body006SpacerPart004Engine

App.ActiveDocument.getObject('Part004Engine').newObject('App::Link', 'Body006SpacerPart004Engine')
App.ActiveDocument.getObject('Body006SpacerPart004Engine').LinkedObject = App.ActiveDocument.getObject('Body006Spacer')
App.ActiveDocument.getObject('Body006SpacerPart004Engine').Placement *= App.ActiveDocument.getObject('Local001Body002Spacer').Placement
App.ActiveDocument.recompute()


# Part00xSupportPart004Engine

App.ActiveDocument.getObject('Part004Engine').newObject('App::Link', 'Part002SupportPart004Engine')
App.ActiveDocument.getObject('Part002SupportPart004Engine').LinkedObject = App.ActiveDocument.getObject('Part002Support')
App.ActiveDocument.getObject('Part002SupportPart004Engine').Placement *= App.ActiveDocument.getObject('Body006SpacerPart004Engine').Placement
App.ActiveDocument.getObject('Part002SupportPart004Engine').Placement *= App.ActiveDocument.getObject('Local002Body002Spacer').Placement
App.ActiveDocument.getObject('Part002SupportPart004Engine').Placement *= App.ActiveDocument.getObject('Local001Body002Support').Placement
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part004Engine').newObject('App::Link', 'Part001SupportPart004Engine')
App.ActiveDocument.getObject('Part001SupportPart004Engine').LinkedObject = App.ActiveDocument.getObject('Part001Support')
App.ActiveDocument.getObject('Part001SupportPart004Engine').Placement *= App.ActiveDocument.getObject('Body006SpacerPart004Engine').Placement
App.ActiveDocument.getObject('Part001SupportPart004Engine').Placement *= App.ActiveDocument.getObject('Local003Body002Spacer').Placement
App.ActiveDocument.getObject('Part001SupportPart004Engine').Placement *= App.ActiveDocument.getObject('Local001Body001Support').Placement.inverse()
App.ActiveDocument.recompute()


# LinkNut00xBody006Spacer

App.ActiveDocument.getObject('Part004Engine').newObject('App::Link', 'LinkNut001Body006Spacer')
App.ActiveDocument.getObject('LinkNut001Body006Spacer').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('5/16in-Nut')[0]
App.ActiveDocument.getObject('LinkNut001Body006Spacer').Placement *= App.ActiveDocument.getObject('Body006SpacerPart004Engine').Placement
App.ActiveDocument.getObject('LinkNut001Body006Spacer').Placement *= App.ActiveDocument.getObject('PointNut001Body006Spacer').Placement
App.ActiveDocument.getObject('LinkNut001Body006Spacer').Placement *= App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90)
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('Part004Engine').newObject('App::Link', 'LinkNut002Body006Spacer')
App.ActiveDocument.getObject('LinkNut002Body006Spacer').LinkedObject = App.getDocument('Fasteners').getObjectsByLabel('5/16in-Nut')[0]
App.ActiveDocument.getObject('LinkNut002Body006Spacer').Placement *= App.ActiveDocument.getObject('Body006SpacerPart004Engine').Placement
App.ActiveDocument.getObject('LinkNut002Body006Spacer').Placement *= App.ActiveDocument.getObject('PointNut002Body006Spacer').Placement
App.ActiveDocument.getObject('LinkNut002Body006Spacer').Placement *= App.Placement(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
App.ActiveDocument.recompute()


# Group001Engine

if App.ActiveDocument.getObject('Group001Engine'):
    App.ActiveDocument.removeObject('Group001Engine')
    App.ActiveDocument.recompute()

App.ActiveDocument.addObject('App::DocumentObjectGroup', 'Group001Engine')
App.ActiveDocument.getObject('Group001Engine').addObject(App.ActiveDocument.getObject('Part001Engine'))
App.ActiveDocument.getObject('Group001Engine').addObject(App.ActiveDocument.getObject('Part002Engine'))
App.ActiveDocument.getObject('Group001Engine').addObject(App.ActiveDocument.getObject('Part003Engine'))
App.ActiveDocument.getObject('Group001Engine').addObject(App.ActiveDocument.getObject('Part004Engine'))
App.ActiveDocument.recompute()


# Placement

for obj in App.ActiveDocument.getObject('Group001Engine').Group:
    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))

App.ActiveDocument.getObject('Group001Support').Visibility = True
App.ActiveDocument.getObject('Group001Engine').Visibility = True


# YAxis

for obj in App.ActiveDocument.getObject('Group001Engine').Group:
    obj.Placement.Base.y = App.ActiveDocument.getObject('Group001Support').Shape.BoundBox.Center.y - (
        App.ActiveDocument.getObject('Group001Support').Shape.BoundBox.YLength +
        App.ActiveDocument.getObject('Group001Engine').Shape.BoundBox.YLength)*75/100


# XAxis

for i in range(1, len(App.ActiveDocument.getObject('Group001Engine').Group)):
    App.ActiveDocument.getObject('Group001Engine').Group[i].Placement.Base.x = \
        App.ActiveDocument.getObject('Group001Engine').Group[i-1].Placement.Base.x + (
            App.ActiveDocument.getObject('Group001Engine').Group[i-1].Shape.BoundBox.XLength +
            App.ActiveDocument.getObject('Group001Engine').Group[i].Shape.BoundBox.XLength)*75/100

App.ActiveDocument.recompute()


# Save

import pydot

Gui.ActiveDocument.ActiveView.setActiveObject('pdbody', None)
Gui.ActiveDocument.activeView().viewDefaultOrientation()
Gui.SendMsgToActiveView('ViewFit')

App.ActiveDocument.save()

graph = pydot.graph_from_dot_data(App.ActiveDocument.exportGraphviz())[0]
graph.write_svg(os.getcwd() + '/Axis/AxisEngine.svg')

