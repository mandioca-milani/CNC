import FreeCAD
import FreeCADGui
import Part


class Bearing:
    _instance = None

    document = None
    view = None

    part001 = None
    body001 = None
    sketch001body001 = None
    revolution001body001 = None
    body002 = None
    sketch001body002 = None
    pad001body002 = None
    body003 = None
    sketch001body003 = None
    pad001body003 = None
    pad002body003 = None
    sketch002body003 = None
    pocket001body003 = None
    sketch003body003 = None
    pocket002body003 = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(__class__, self).__new__(self)
        return self._instance

    def create(self, document=None):
        self.document = FreeCAD.getDocument(document) if document else FreeCAD.ActiveDocument
        self.view = FreeCADGui.getDocument(document).ActiveView if document else FreeCADGui.ActiveDocument.ActiveView

        self.__part001('Part001Bearing')
        self.__body001('Body001Bearing')
        self.__sketch001body001('Sketch001Body001Bearing')
        self.__revolution001body001('Revolution001Body001Bearing')
        self.__body002('Body002Bearing')
        self.__sketch001body002('Sketch001Body002Bearing')
        self.__pad001body002('Pad001Body002Bearing')
        self.__body003('body003Bearing')
        self.__sketch001body003('Sketch001body003Bearing')
        self.__pad001body003('Pad001body003Bearing')
        self.__pad002body003('Pad002body003Bearing')
        self.__sketch002body003('Sketch002body003Bearing')
        self.__pocket001body003('Pocket001body003Bearing')
        self.__sketch003body003('Sketch003body003Bearing')
        self.__pocket002body003('Pocket002body003Bearing')

        self.view.setActiveObject('pdbody', None)
        self.view.setActiveObject('part', None)

        self.body002.ViewObject.ShapeColor = (0.2, 0.2, 0.2, 0.0)

    def __part001(self, name):
        if self.document.getObject(name):
            self.document.getObject(name).removeObjectsFromDocument()
            self.document.removeObject(name)
            self.document.recompute()

        self.part001 = self.document.addObject('App::Part', name)
        self.view.setActiveObject('part', self.part001)
        self.document.recompute()

    def __body001(self, name):
        self.body001 = self.part001.newObject('PartDesign::Body', name)
        self.view.setActiveObject('pdbody', self.body001)
        self.document.recompute()

    def __sketch001body001(self, name):
        self.sketch001body001 = self.body001.newObject('Sketcher::SketchObject', name)
        self.sketch001body001.Support = self.body001.Origin.OriginFeatures[4]  # XZ_Plane
        self.sketch001body001.MapMode = 'FlatFace'
        self.sketch001body001.Visibility = False
        self.document.recompute()

        self.sketch001body001.addGeometry([
            Part.ArcOfParabola(Part.Parabola(
                FreeCAD.Vector(22/4, 0, 0),
                FreeCAD.Vector(22/2, 0, 0),
                FreeCAD.Vector(0, 0, 1)), -7/2, 7/2
            ),  # 0
            Part.LineSegment(FreeCAD.Vector(19/2, 7/2, 0), FreeCAD.Vector(19/2, -7/2, 0)),  # 1
        ], False)
        self.sketch001body001.addGeometry([
            Part.LineSegment(FreeCAD.Vector(
                self.sketch001body001.Geometry[0].StartPoint.x,
                self.sketch001body001.Geometry[0].StartPoint.y, 0),
                FreeCAD.Vector(19/2, 7/2, 0)
            ),  # 3
            Part.LineSegment(FreeCAD.Vector(
                self.sketch001body001.Geometry[0].EndPoint.x,
                self.sketch001body001.Geometry[0].EndPoint.y, 0),
                FreeCAD.Vector(19/2, -7/2, 0)
            ),  # 4
        ], False)
        self.document.recompute()

    def __revolution001body001(self, name):

        self.revolution001body001 = self.body001.newObject('PartDesign::Revolution', name)
        self.revolution001body001.Profile = self.sketch001body001
        self.revolution001body001.ReferenceAxis = (self.sketch001body001, ['V_Axis'])
        self.document.recompute()

    def __body002(self, name):
        self.body002 = self.part001.newObject('PartDesign::Body', name)
        self.view.setActiveObject('pdbody', self.body002)
        self.document.recompute()

    def __sketch001body002(self, name):
        self.sketch001body002 = self.body002.newObject('Sketcher::SketchObject', name)
        self.sketch001body002.Support = self.body002.Origin.OriginFeatures[3]  # XY_Plane
        self.sketch001body002.MapMode = 'FlatFace'
        self.sketch001body002.Visibility = False
        self.document.recompute()

        self.sketch001body002.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 12/2),
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 19/2),
        ], False)
        self.document.recompute()

    def __pad001body002(self, name):
        self.pad001body002 = self.body002.newObject('PartDesign::Pad', name)
        self.pad001body002.Profile = self.sketch001body002
        self.pad001body002.Midplane = True
        self.pad001body002.Length = 6.8
        self.document.recompute()

    def __body003(self, name):
        self.body003 = self.part001.newObject('PartDesign::Body', name)
        self.view.setActiveObject('pdbody', self.body003)
        self.document.recompute()

    def __sketch001body003(self, name):
        self.sketch001body003 = self.body003.newObject('Sketcher::SketchObject', name)
        self.sketch001body003.Support = self.body003.Origin.OriginFeatures[3]  # XY_Plane
        self.sketch001body003.MapMode = 'FlatFace'
        self.sketch001body003.Visibility = False
        self.document.recompute()

        self.sketch001body003.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 8/2),
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 12/2),
        ], False)
        self.document.recompute()

    def __pad001body003(self, name):
        self.pad001body003 = self.body003.newObject('PartDesign::Pad', name)
        self.pad001body003.Profile = self.sketch001body003
        self.pad001body003.Midplane = True
        self.pad001body003.Length = 7
        self.document.recompute()

    def __pad002body003(self, name):
        self.pad002body003 = self.body003.newObject('PartDesign::Pad', name)
        self.pad002body003.Profile = (self.pad001body003, ['Face4'])
        self.pad002body003.Length = 4
        self.document.recompute()

    def __sketch002body003(self, name):
        self.sketch002body003 = self.body003.newObject('Sketcher::SketchObject', name)
        self.sketch002body003.Support = self.body003.Origin.OriginFeatures[5]  # YZ_Plane
        self.sketch002body003.MapMode = 'FlatFace'
        self.sketch002body003.Visibility = False
        self.document.recompute()

        self.sketch002body003.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 7/2+4/2, 0), FreeCAD.Vector(0, 0, 1), 3/2),
        ], False)
        self.document.recompute()

    def __pocket001body003(self, name):
        self.pocket001body003 = self.body003.newObject('PartDesign::Pocket', name)
        self.pocket001body003.Profile = self.sketch002body003
        self.pocket001body003.Reversed = True
        self.pocket001body003.Type = 'ThroughAll'
        self.document.recompute()

    def __sketch003body003(self, name):
        self.sketch003body003 = self.body003.newObject('Sketcher::SketchObject', name)
        self.sketch003body003.Support = self.body003.Origin.OriginFeatures[4]  # XZ_Plane
        self.sketch003body003.MapMode = 'FlatFace'
        self.sketch003body003.Geometry = self.sketch002body003.Geometry
        self.sketch003body003.Visibility = False
        self.document.recompute()

    def __pocket002body003(self, name):
        self.pocket002body003 = self.body003.newObject('PartDesign::Pocket', name)
        self.pocket002body003.Profile = self.sketch003body003
        self.pocket002body003.Reversed = True
        self.pocket002body003.Type = 'ThroughAll'
        self.document.recompute()
