import pydot
import Part
import Sketcher


graph = pydot.Dot('KFL 8', graph_type='digraph', rankdir='BT')

cluster = pydot.Cluster('Cluster'+'BodyFrame', label='BodyFrame')
cluster.add_node(pydot.Node('BodyFrameSketch'))
cluster.add_node(pydot.Node('BodyFramePad'))
cluster.add_node(pydot.Node('BodyFrameFillet'))
cluster.add_node(pydot.Node('BodyFrameFillet001'))
cluster.add_node(pydot.Node('BodyFrameSketch001'))
cluster.add_node(pydot.Node('BodyFramePad001'))
graph.add_subgraph(cluster)
graph.add_edge(pydot.Edge('BodyFramePad', 'BodyFrameSketch'))
graph.add_edge(pydot.Edge('BodyFrameFillet', 'BodyFramePad'))
graph.add_edge(pydot.Edge('BodyFrameFillet001', 'BodyFrameFillet'))
graph.add_edge(pydot.Edge('BodyFrameSketch001', 'BodyFramePad'))
graph.add_edge(pydot.Edge('BodyFramePad001', 'BodyFrameSketch001'))

graph.write_svg('./KFL 8.svg', prog='dot')


try:
    App.getDocument('KFL_8')
    App.closeDocument('KFL_8')
except:
    pass

App.newDocument('KFL_8')


# BodyFrame
Gui.activateWorkbench('PartDesignWorkbench')
App.ActiveDocument.addObject('PartDesign::Body','BodyFrame')
App.ActiveDocument.recompute()

# BodyFrameSketch
App.ActiveDocument.getObject('BodyFrame').newObject('Sketcher::SketchObject','BodyFrameSketch')
App.ActiveDocument.getObject('BodyFrameSketch').Support = (App.ActiveDocument.getObject('XY_Plane'),[''])
App.ActiveDocument.getObject('BodyFrameSketch').MapMode = 'FlatFace'

App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.LineSegment(App.Vector(0,1,0),App.Vector(1,0,0)),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.LineSegment(App.Vector(1,0,0),App.Vector(0,-1,0)),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.LineSegment(App.Vector(0,-1,0),App.Vector(-1,0,0)),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.LineSegment(App.Vector(-1,0,0),App.Vector(0,1,0)),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('PointOnObject',0,1,-2))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('PointOnObject',0,2,-1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Coincident',0,2,1,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Coincident',1,2,2,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Coincident',2,2,3,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Coincident',3,2,0,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Symmetric',0,1,1,2,-1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Symmetric',2,2,0,2,-2))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Distance',0,1,1,2,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch').setDatum(8,App.Units.Quantity('30.000000 mm'))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Distance',2,2,0,2,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch').setDatum(9,App.Units.Quantity('60.000000 mm'))

App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.Circle(App.Vector(1,0,0),App.Vector(0,0,1),1),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.Circle(App.Vector(-1,0,0),App.Vector(0,0,1),2),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('PointOnObject',4,3,-1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Symmetric',5,3,4,3,-2))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Distance',5,3,4,3,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch').setDatum(12,App.Units.Quantity('35.000000 mm'))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Diameter',4,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch').setDatum(13,App.Units.Quantity('5.000000 mm'))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Equal',4,5))

App.getDocument('KFL_8').getObject('BodyFrameSketch').addGeometry(Part.Circle(App.Vector(0,0,0),App.Vector(0,0,1),1.000000),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Coincident',6,3,-1,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch').addConstraint(Sketcher.Constraint('Diameter',6,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch').setDatum(16,App.Units.Quantity('22.000000 mm'))

# BodyFramePad
App.ActiveDocument.getObject('BodyFrame').newObject('PartDesign::Pad','BodyFramePad')
App.ActiveDocument.getObject('BodyFramePad').Profile = App.ActiveDocument.getObject('BodyFrameSketch')
App.ActiveDocument.getObject('BodyFramePad').Length = 4.000000
App.ActiveDocument.getObject('BodyFrameSketch').Visibility = False
App.ActiveDocument.recompute()

# BodyFrameFillet
App.getDocument('KFL_8').getObject('BodyFrame').newObject('PartDesign::Fillet','BodyFrameFillet')
App.getDocument('KFL_8').getObject('BodyFrameFillet').Base = (App.getDocument('KFL_8').getObject('BodyFramePad'),['Edge2','Edge8',])
App.getDocument('KFL_8').getObject('BodyFrameFillet').Radius = 5.000000
App.getDocument('KFL_8').getObject('BodyFramePad').Visibility = False
App.ActiveDocument.recompute()

# BodyFrameFillet001
App.getDocument('KFL_8').getObject('BodyFrame').newObject('PartDesign::Fillet','BodyFrameFillet001')
App.getDocument('KFL_8').getObject('BodyFrameFillet001').Base = (App.getDocument('KFL_8').getObject('BodyFrameFillet'),['Edge3','Edge23',])
App.getDocument('KFL_8').getObject('BodyFrameFillet001').Radius = 10.000000
App.getDocument('KFL_8').getObject('BodyFrameFillet').Visibility = False
App.ActiveDocument.recompute()

# BodyFrameSketch001
App.ActiveDocument.getObject('BodyFrame').newObject('Sketcher::SketchObject','BodyFrameSketch001')
App.ActiveDocument.getObject('BodyFrameSketch001').Support = (App.ActiveDocument.getObject('BodyFramePad'),['Face9'])
App.ActiveDocument.getObject('BodyFrameSketch001').MapMode = 'FlatFace'

App.getDocument('KFL_8').getObject('BodyFrameSketch001').addGeometry(Part.Circle(App.Vector(0,0,0),App.Vector(0,0,1),1.000000),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch001').addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch001').addGeometry(Part.Circle(App.Vector(0,0,0),App.Vector(0,0,1),1.000000),False)
App.getDocument('KFL_8').getObject('BodyFrameSketch001').addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1))
App.getDocument('KFL_8').getObject('BodyFrameSketch001').addConstraint(Sketcher.Constraint('Diameter',0,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch001').addConstraint(Sketcher.Constraint('Diameter',1,2.000000))
App.getDocument('KFL_8').getObject('BodyFrameSketch001').setDatum(2,App.Units.Quantity('22.000000 mm'))
App.getDocument('KFL_8').getObject('BodyFrameSketch001').setDatum(3,App.Units.Quantity('25.000000 mm'))

# BodyFramePad001
App.ActiveDocument.getObject('BodyFrame').newObject('PartDesign::Pad','BodyFramePad001')
App.ActiveDocument.getObject('BodyFramePad001').Profile = App.ActiveDocument.getObject('BodyFrameSketch001')
App.ActiveDocument.getObject('BodyFramePad001').Length = 4.000000
App.ActiveDocument.getObject('BodyFrameSketch001').Visibility = False
App.ActiveDocument.recompute()


# View Fit
Gui.ActiveDocument.activeView().setCameraType('Perspective')
Gui.ActiveDocument.activeView().viewTrimetric()
Gui.SendMsgToActiveView('ViewFit')

# Save
App.ActiveDocument.saveAs(u'./KFL 8.FCStd')
