import pydot
import Part
import Sketcher


graph = pydot.Dot('Nema 17', graph_type='digraph', rankdir='BT')

cluster = pydot.Cluster('Cluster'+'BodyBase', label='BodyBase')
cluster.add_node(pydot.Node('BodyBaseSketch'))
cluster.add_node(pydot.Node('BodyBasePad'))
cluster.add_node(pydot.Node('BodyBaseSketch001'))
cluster.add_node(pydot.Node('BodyBasePad001'))
cluster.add_node(pydot.Node('BodyBaseChamfer'))
cluster.add_node(pydot.Node('BodyBaseHole'))
graph.add_subgraph(cluster)
graph.add_edge(pydot.Edge('BodyBasePad', 'BodyBaseSketch'))
graph.add_edge(pydot.Edge('BodyBaseSketch001', 'BodyBasePad'))
graph.add_edge(pydot.Edge('BodyBasePad001', 'BodyBaseSketch001'))
graph.add_edge(pydot.Edge('BodyBaseChamfer', 'BodyBasePad'))
graph.add_edge(pydot.Edge('BodyBaseHole', 'BodyBasePad'))

cluster = pydot.Cluster('Cluster'+'BodyMeio', label='BodyMeio')
cluster.add_node(pydot.Node('BodyMeioBinder'))
cluster.add_node(pydot.Node('BodyMeioPad002'))
cluster.add_node(pydot.Node('BodyMeioChamfer001'))
graph.add_subgraph(cluster)
graph.add_edge(pydot.Edge('BodyMeioBinder', 'BodyBasePad'))
graph.add_edge(pydot.Edge('BodyMeioPad002', 'BodyMeioBinder'))
graph.add_edge(pydot.Edge('BodyMeioChamfer001', 'BodyMeioPad002'))

cluster = pydot.Cluster('Cluster'+'BodyTopo', label='BodyTopo')
cluster.add_node(pydot.Node('BodyTopoBinder001'))
cluster.add_node(pydot.Node('BodyTopoPad003'))
cluster.add_node(pydot.Node('BodyTopoDatumPlane'))
cluster.add_node(pydot.Node('BodyTopoChamfer002'))
cluster.add_node(pydot.Node('BodyTopoSketch002'))
cluster.add_node(pydot.Node('BodyTopoPad004'))
graph.add_subgraph(cluster)
graph.add_edge(pydot.Edge('BodyTopoBinder001', 'BodyMeioPad002'))
graph.add_edge(pydot.Edge('BodyTopoPad003', 'BodyTopoBinder001'))
graph.add_edge(pydot.Edge('BodyTopoDatumPlane', 'BodyTopoPad003'))
graph.add_edge(pydot.Edge('BodyTopoChamfer002', 'BodyTopoPad003'))
graph.add_edge(pydot.Edge('BodyTopoSketch002', 'BodyTopoPad003'))
graph.add_edge(pydot.Edge('BodyTopoPad004', 'BodyTopoSketch002'))

cluster = pydot.Cluster('Cluster'+'BodyFuso', label='BodyFuso')
cluster.add_node(pydot.Node('BodyFusoSketch003'))
cluster.add_node(pydot.Node('BodyFusoPad005'))
graph.add_subgraph(cluster)
graph.add_edge(pydot.Edge('BodyFusoSketch003', 'BodyTopoDatumPlane'))
graph.add_edge(pydot.Edge('BodyFusoPad005', 'BodyFusoSketch003'))

graph.write_svg('./Nema 17.svg', prog='dot')


try:
    App.getDocument('Nema_17')
    App.closeDocument('Nema_17')
except:
    pass

App.newDocument('Nema_17')


# BodyBase
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyBase')
App.ActiveDocument.recompute()

# BodyBaseSketch
App.ActiveDocument.getObject('BodyBase').newObject('Sketcher::SketchObject','BodyBaseSketch')
App.ActiveDocument.getObject('BodyBaseSketch').Support = (App.ActiveDocument.getObject('XY_Plane'),[''])
App.ActiveDocument.getObject('BodyBaseSketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.LineSegment(App.Vector(-1,1,0),App.Vector(1,1,0)))
geoList.append(Part.LineSegment(App.Vector(1,1,0),App.Vector(1,-1,0)))
geoList.append(Part.LineSegment(App.Vector(1,-1,0),App.Vector(-1,-1,0)))
geoList.append(Part.LineSegment(App.Vector(-1,-1,0),App.Vector(-1,1,0)))
App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(geoList,False)

conList = []
conList.append(Sketcher.Constraint('Coincident',0,2,1,1))
conList.append(Sketcher.Constraint('Coincident',1,2,2,1))
conList.append(Sketcher.Constraint('Coincident',2,2,3,1))
conList.append(Sketcher.Constraint('Coincident',3,2,0,1))
conList.append(Sketcher.Constraint('Horizontal',2))
conList.append(Sketcher.Constraint('Vertical',3))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(conList)

App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Symmetric',0,1,0,2,-2))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Symmetric',0,2,1,2,-1))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Distance',0,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(8,App.Units.Quantity('42.000000 mm'))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Distance',1,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(9,App.Units.Quantity('42.000000 mm'))
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(Part.Circle(App.Vector(-1,1,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(Part.Circle(App.Vector(1,1,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(Part.Circle(App.Vector(-1,-1,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyBaseSketch').addGeometry(Part.Circle(App.Vector(1,-1,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Symmetric',4,3,5,3,-2))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Symmetric',4,3,6,3,-1))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Symmetric',6,3,7,3,-2))

App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Distance',4,3,5,3,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(13,App.Units.Quantity('31.000000 mm'))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Distance',6,3,4,3,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(14,App.Units.Quantity('31.000000 mm'))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Diameter',4,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch').setDatum(15,App.Units.Quantity('3.000000 mm'))

App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Equal',4,5))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Equal',5,6))
App.ActiveDocument.getObject('BodyBaseSketch').addConstraint(Sketcher.Constraint('Equal',6,7))

# BodyBasePad
App.ActiveDocument.getObject('BodyBase').newObject('PartDesign::Pad','BodyBasePad')
App.ActiveDocument.getObject('BodyBasePad').Profile = App.ActiveDocument.getObject('BodyBaseSketch')
App.ActiveDocument.getObject('BodyBasePad').Length = 10.000000
App.ActiveDocument.getObject('BodyBaseSketch').Visibility = False
App.ActiveDocument.recompute()

# BodyBaseSketch001
App.ActiveDocument.getObject('BodyBase').newObject('Sketcher::SketchObject','BodyBaseSketch001')
App.ActiveDocument.getObject('BodyBaseSketch001').Support = (App.ActiveDocument.getObject('BodyBasePad'),['Face2',])
App.ActiveDocument.getObject('BodyBaseSketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.LineSegment(App.Vector(-1,1,0),App.Vector(1,1,0)))
geoList.append(Part.LineSegment(App.Vector(1,1,0),App.Vector(1,-1,0)))
geoList.append(Part.LineSegment(App.Vector(1,-1,0),App.Vector(-1,-1,0)))
geoList.append(Part.LineSegment(App.Vector(-1,-1,0),App.Vector(-1,1,0)))
App.ActiveDocument.getObject('BodyBaseSketch001').addGeometry(geoList,False)

conList = []
conList.append(Sketcher.Constraint('Coincident',0,2,1,1))
conList.append(Sketcher.Constraint('Coincident',1,2,2,1))
conList.append(Sketcher.Constraint('Coincident',2,2,3,1))
conList.append(Sketcher.Constraint('Coincident',3,2,0,1))
conList.append(Sketcher.Constraint('Horizontal',2))
conList.append(Sketcher.Constraint('Vertical',1))
conList.append(Sketcher.Constraint('Vertical',3))
App.ActiveDocument.getObject('BodyBaseSketch001').addConstraint(conList)
App.ActiveDocument.getObject('BodyBaseSketch001').addConstraint(Sketcher.Constraint('PointOnObject',1,2,-1))

App.ActiveDocument.getObject('BodyBaseSketch001').addConstraint(Sketcher.Constraint('Symmetric',0,1,0,2,-2))
App.ActiveDocument.getObject('BodyBaseSketch001').addConstraint(Sketcher.Constraint('Distance',0,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch001').setDatum(9,App.Units.Quantity('16.000000 mm'))
App.ActiveDocument.getObject('BodyBaseSketch001').addConstraint(Sketcher.Constraint('Distance',1,2.000000))
App.ActiveDocument.getObject('BodyBaseSketch001').setExpression('Constraints[10]', u'BodyBasePad.Shape.BoundBox.ZLength')
App.ActiveDocument.recompute()

# BodyBasePad001
App.ActiveDocument.getObject('BodyBase').newObject('PartDesign::Pad','BodyBasePad001')
App.ActiveDocument.getObject('BodyBasePad001').Profile = App.ActiveDocument.getObject('BodyBaseSketch001')
App.ActiveDocument.getObject('BodyBasePad001').Length = 5.000000
App.ActiveDocument.getObject('BodyBaseSketch001').Visibility = False
App.ActiveDocument.recompute()

# BodyBaseChamfer
App.ActiveDocument.getObject('BodyBase').newObject('PartDesign::Chamfer','BodyBaseChamfer')
App.ActiveDocument.getObject('BodyBaseChamfer').Base = (App.ActiveDocument.getObject('BodyBasePad'),['Edge1','Edge2','Edge5','Edge8',])
App.ActiveDocument.getObject('BodyBaseChamfer').Size = 4.000000
App.ActiveDocument.getObject('BodyBasePad').Visibility = False
App.ActiveDocument.recompute()

# BodyBaseHole
App.ActiveDocument.getObject('BodyBase').newObject('PartDesign::Hole','BodyBaseHole')
App.ActiveDocument.getObject('BodyBaseHole').Profile = (App.ActiveDocument.getObject('BodyBasePad'), ['Edge14','Edge17','Edge20','Edge23',])
App.ActiveDocument.getObject('BodyBaseHole').DrillPoint = 0
App.ActiveDocument.getObject('BodyBaseHole').Reversed = True
App.ActiveDocument.getObject('BodyBaseHole').Diameter = 6.000000
App.ActiveDocument.getObject('BodyBaseHole').Depth = 3.000000
App.ActiveDocument.getObject('BodyBasePad001').Visibility = False
App.ActiveDocument.recompute()


# BodyMeio
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyMeio')
App.ActiveDocument.recompute()

# BodyMeioBinder
App.ActiveDocument.getObject('BodyMeio').newObject('PartDesign::SubShapeBinder','BodyMeioBinder')
App.ActiveDocument.getObject('BodyMeioBinder').Support = (App.ActiveDocument.getObject('BodyBasePad'),['Face10'])
App.ActiveDocument.recompute()

# BodyMeioPad002
App.ActiveDocument.getObject('BodyMeio').newObject('PartDesign::Pad','BodyMeioPad002')
App.ActiveDocument.getObject('BodyMeioPad002').Profile = App.ActiveDocument.getObject('BodyMeioBinder')
App.ActiveDocument.getObject('BodyMeioPad002').Length = 22.000000
App.ActiveDocument.getObject('BodyMeioBinder').Visibility = False
App.ActiveDocument.recompute()

# BodyMeioChamfer001
App.ActiveDocument.getObject('BodyMeio').newObject('PartDesign::Chamfer','BodyMeioChamfer001')
App.ActiveDocument.getObject('BodyMeioChamfer001').Base = (App.ActiveDocument.getObject('BodyMeioPad002'),['Edge1','Edge2','Edge5','Edge8',])
App.ActiveDocument.getObject('BodyMeioChamfer001').Size = 6.000000
App.ActiveDocument.getObject('BodyMeioPad002').Visibility = False
App.ActiveDocument.recompute()

# Shape Color
App.ActiveDocument.getObject('BodyMeio').ViewObject.ShapeColor = (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.0)


# BodyTopo
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyTopo')
App.ActiveDocument.recompute()

# BodyTopoBinder001
App.ActiveDocument.getObject('BodyTopo').newObject('PartDesign::SubShapeBinder','BodyTopoBinder001')
App.ActiveDocument.getObject('BodyTopoBinder001').Support = (App.ActiveDocument.getObject('BodyMeioPad002'),['Face10'])
App.ActiveDocument.recompute()

# BodyTopoPad003
App.ActiveDocument.getObject('BodyTopo').newObject('PartDesign::Pad','BodyTopoPad003')
App.ActiveDocument.getObject('BodyTopoPad003').Profile = App.ActiveDocument.getObject('BodyTopoBinder001')
App.ActiveDocument.getObject('BodyTopoPad003').Length = 8.000000
App.ActiveDocument.getObject('BodyTopoBinder001').Visibility = False
App.ActiveDocument.recompute()

# BodyTopoDatumPlane
App.ActiveDocument.getObject('BodyTopo').newObject('PartDesign::Plane','BodyTopoDatumPlane')
App.ActiveDocument.getObject('BodyTopoDatumPlane').Support = [(App.ActiveDocument.getObject('BodyTopoPad003'),'Face10')]
App.ActiveDocument.getObject('BodyTopoDatumPlane').MapMode = 'FlatFace'
App.ActiveDocument.getObject('BodyTopoDatumPlane').Visibility = False
App.ActiveDocument.recompute()

# BodyTopoChamfer002
App.ActiveDocument.getObject('BodyTopo').newObject('PartDesign::Chamfer','BodyTopoChamfer002')
App.ActiveDocument.getObject('BodyTopoChamfer002').Base = (App.ActiveDocument.getObject('BodyTopoPad003'),['Edge1','Edge2','Edge5','Edge8',])
App.ActiveDocument.getObject('BodyTopoChamfer002').Size = App.ActiveDocument.getObject('BodyBaseChamfer').Size
App.ActiveDocument.getObject('BodyTopoPad003').Visibility = False
App.ActiveDocument.recompute()

# BodyTopoSketch002
App.ActiveDocument.getObject('BodyTopo').newObject('Sketcher::SketchObject','BodyTopoSketch002')
App.ActiveDocument.getObject('BodyTopoSketch002').Support = (App.ActiveDocument.getObject('BodyTopoPad003'),['Face10',])
App.ActiveDocument.getObject('BodyTopoSketch002').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyTopoSketch002').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyTopoSketch002').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),1.000000),False)

App.ActiveDocument.getObject('BodyTopoSketch002').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
App.ActiveDocument.getObject('BodyTopoSketch002').addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1))

App.ActiveDocument.getObject('BodyTopoSketch002').addConstraint(Sketcher.Constraint('Diameter',0,2.000000))
App.ActiveDocument.getObject('BodyTopoSketch002').addConstraint(Sketcher.Constraint('Diameter',1,2.000000))

App.ActiveDocument.getObject('BodyTopoSketch002').setDatum(2,App.Units.Quantity('9.000000 mm'))
App.ActiveDocument.getObject('BodyTopoSketch002').setDatum(3,App.Units.Quantity('22.000000 mm'))
App.ActiveDocument.recompute()

# BodyTopoPad004
App.ActiveDocument.getObject('BodyTopo').newObject('PartDesign::Pad','BodyTopoPad004')
App.ActiveDocument.getObject('BodyTopoPad004').Profile = App.ActiveDocument.getObject('BodyTopoSketch002')
App.ActiveDocument.getObject('BodyTopoPad004').Length = 2.000000
App.ActiveDocument.getObject('BodyTopoSketch002').Visibility = False
App.ActiveDocument.recompute()


# BodyFuso
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyFuso')
App.ActiveDocument.recompute()

# BodyFusoSketch003
App.ActiveDocument.getObject('BodyFuso').newObject('Sketcher::SketchObject','BodyFusoSketch003')
App.ActiveDocument.getObject('BodyFusoSketch003').Support = (App.ActiveDocument.getObject('BodyTopoDatumPlane'),[''])
App.ActiveDocument.getObject('BodyFusoSketch003').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.getObject('BodyFusoSketch003').addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),1.000000),False)
App.ActiveDocument.getObject('BodyFusoSketch003').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
App.ActiveDocument.getObject('BodyFusoSketch003').addConstraint(Sketcher.Constraint('Diameter',0,2.000000))
App.ActiveDocument.getObject('BodyFusoSketch003').setDatum(1,App.Units.Quantity('5.000000 mm'))
App.ActiveDocument.recompute()

# BodyFusoPad005
App.ActiveDocument.getObject('BodyFuso').newObject('PartDesign::Pad','BodyFusoPad005')
App.ActiveDocument.getObject('BodyFusoPad005').Profile = App.ActiveDocument.getObject('BodyFusoSketch003')
App.ActiveDocument.getObject('BodyFusoPad005').Length = 24.000000
App.ActiveDocument.getObject('BodyFusoSketch003').Visibility = False
App.ActiveDocument.recompute()


# Compound
Gui.activateWorkbench('PartWorkbench')
App.ActiveDocument.addObject('Part::Compound','Compound')
App.ActiveDocument.Compound.Links = [App.ActiveDocument.getObject('BodyBase'),App.ActiveDocument.getObject('BodyMeio'),App.ActiveDocument.getObject('BodyTopo'),App.ActiveDocument.getObject('BodyFuso'),]
App.ActiveDocument.recompute()


# View Fit
Gui.ActiveDocument.activeView().setCameraType('Perspective')
Gui.ActiveDocument.activeView().viewTrimetric()
Gui.SendMsgToActiveView('ViewFit')

# Save
App.ActiveDocument.saveAs(u'./Nema 17.FCStd')
