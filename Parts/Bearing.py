import FreeCAD
import FreeCADGui
import Part


class Bearing:
    ActiveDocument = FreeCAD.ActiveDocument
    ActiveView = FreeCADGui.ActiveDocument.ActiveView

    def __init__(self):
        self.Part001 = self.create(self.Part001)
        self.Body001 = self.create(self.Body001)
        self.Sketch001Body001 = self.create(self.Sketch001Body001)
        self.Pad001Body001 = self.create(self.Pad001Body001)
        self.Body002 = self.create(self.Body002)
        self.Sketch001Body002 = self.create(self.Sketch001Body002)
        self.Pad001Body002 = self.create(self.Pad001Body002)
        self.Body003 = self.create(self.Body003)
        self.Sketch001Body003 = self.create(self.Sketch001Body003)
        self.Pad001Body003 = self.create(self.Pad001Body003)

        self.Body002.ViewObject.ShapeColor = (0.2, 0.2, 0.2, 0.0)

    def create(self, method):
        property = method(self.__class__.__name__ + method.__name__)
        self.ActiveDocument.recompute()
        return(property)

    def Part001(self, name):
        if self.ActiveDocument.getObject(name):
            self.ActiveDocument.getObject(name).removeObjectsFromDocument()
            self.ActiveDocument.removeObject(name)

        Part001 = self.ActiveDocument.addObject('App::Part', name)
        Part001.Origin = self.ActiveDocument.addObject('App::Origin', name + 'Origin')
        self.ActiveDocument.removeObject('Origin')
        return(Part001)

    def Body001(self, name):
        Body001 = self.Part001.newObject('PartDesign::Body', name)
        Body001.Origin = self.ActiveDocument.addObject('App::Origin', name + 'Origin')
        self.ActiveDocument.removeObject('Origin')
        return(Body001)

    def Sketch001Body001(self, name):
        Sketch001Body001 = self.Body001.newObject('Sketcher::SketchObject', name)
        Sketch001Body001.Support = self.Body001.Origin.OriginFeatures[3] # XY_Plane
        Sketch001Body001.MapMode = 'FlatFace'
        Sketch001Body001.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 8/2),
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 12/2),
        ], False)
        Sketch001Body001.Visibility = False
        return(Sketch001Body001)

    def Pad001Body001(self, name):
        Pad001Body001 = self.Body001.newObject('PartDesign::Pad', name)
        Pad001Body001.Profile = self.Sketch001Body001
        Pad001Body001.Midplane = True
        Pad001Body001.Length = 7
        return(Pad001Body001)

    def Body002(self, name):
        Body002 = self.Part001.newObject('PartDesign::Body', name)
        Body002.Origin = self.ActiveDocument.addObject('App::Origin', name + 'Origin')
        self.ActiveDocument.removeObject('Origin')
        return(Body002)

    def Sketch001Body002(self, name):
        Sketch001Body002 = self.Body002.newObject('Sketcher::SketchObject', name)
        Sketch001Body002.Support = self.Body002.Origin.OriginFeatures[3] # XY_Plane
        Sketch001Body002.MapMode = 'FlatFace'
        Sketch001Body002.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 12/2),
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 19/2),
        ], False)
        Sketch001Body002.Visibility = False
        return(Sketch001Body002)

    def Pad001Body002(self, name):
        Pad001Body002 = self.Body002.newObject('PartDesign::Pad', name)
        Pad001Body002.Profile = self.Sketch001Body002
        Pad001Body002.Midplane = True
        Pad001Body002.Length = 6.8
        return(Pad001Body002)

    def Body003(self, name):
        Body003 = self.Part001.newObject('PartDesign::Body', name)
        Body003.Origin = self.ActiveDocument.addObject('App::Origin', name + 'Origin')
        self.ActiveDocument.removeObject('Origin')
        self.ActiveDocument.recompute()
        return(Body003)

    def Sketch001Body003(self, name):
        Sketch001Body003 = self.Body003.newObject('Sketcher::SketchObject', name)
        Sketch001Body003.Support = self.Body003.Origin.OriginFeatures[3] # XY_Plane
        Sketch001Body003.MapMode = 'FlatFace'
        Sketch001Body003.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 19/2),
            Part.Circle(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 22/2),
        ], False)
        Sketch001Body003.Visibility = False
        return(Sketch001Body003)

    def Pad001Body003(self, name):
        Pad001Body003 = self.Body003.newObject('PartDesign::Pad', name)
        Pad001Body003.Profile = self.Sketch001Body003
        Pad001Body003.Midplane = True
        Pad001Body003.Length = 7
        return(Pad001Body003)


class BearingKFL8(Bearing):
    def __init__(self):
        self.Part001 = self.create(self.Part001)
        self.Body001 = self.create(self.Body001)
        self.Sketch001Body001 = self.create(self.Sketch001Body001)
        self.Pad001Body001 = self.create(self.Pad001Body001)
        self.Pad002Body001 = self.create(self.Pad002Body001)
        self.Sketch002Body001 = self.create(self.Sketch002Body001)
        self.Pocket001Body001 = self.create(self.Pocket001Body001)
        self.Sketch003Body001 = self.create(self.Sketch003Body001)
        self.Pocket002Body001 = self.create(self.Pocket002Body001)
        self.Body002 = self.create(self.Body002)
        self.Sketch001Body002 = self.create(self.Sketch001Body002)
        self.Pad001Body002 = self.create(self.Pad001Body002)
        self.Body003 = self.create(self.Body003)
        self.Sketch001Body003 = self.create(self.Sketch001Body003)
        self.Revolution001Body003 = self.create(self.Revolution001Body003)

        self.Body002.ViewObject.ShapeColor = (0.2, 0.2, 0.2, 0.0)

    def Part001(self, name):
        return(super().Part001(name))

    def Body001(self, name):
        return(super().Body001(name))

    def Sketch001Body001(self, name):
        return(super().Sketch001Body001(name))

    def Pad001Body001(self, name):
        return(super().Pad001Body001(name))

    def Pad002Body001(self, name):
        Pad002Body001 = self.Body001.newObject('PartDesign::Pad', name)
        Pad002Body001.Profile = (self.Pad001Body001, ['Face4'])
        Pad002Body001.Length = 4
        return(Pad002Body001)

    def Sketch002Body001(self, name):
        Sketch002Body001 = self.Body001.newObject('Sketcher::SketchObject', name)
        Sketch002Body001.Support = self.Body001.Origin.OriginFeatures[4] # XZ_Plane
        Sketch002Body001.MapMode = 'FlatFace'
        Sketch002Body001.addGeometry([
            Part.Circle(FreeCAD.Vector(0, 7/2+4/2, 0), FreeCAD.Vector(0, 0, 1), 3/2),
        ], False)
        Sketch002Body001.Visibility = False
        return(Sketch002Body001)

    def Pocket001Body001(self, name):
        Pocket001Body001 = self.Body001.newObject('PartDesign::Pocket', name)
        Pocket001Body001.Profile = self.Sketch002Body001
        Pocket001Body001.Reversed = True
        Pocket001Body001.Type = 'ThroughAll'
        return(Pocket001Body001)

    def Sketch003Body001(self, name):
        Sketch003Body001 = self.Body001.newObject('Sketcher::SketchObject', name)
        Sketch003Body001.Support = self.Sketch002Body001.Support
        Sketch003Body001.MapMode = self.Sketch002Body001.MapMode
        Sketch003Body001.AttachmentOffset = FreeCAD.Placement(
            FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(App.Vector(0, 1, 0), 80)
        )
        Sketch003Body001.Geometry = self.Sketch002Body001.Geometry
        Sketch003Body001.Visibility = self.Sketch002Body001.Visibility
        return(Sketch003Body001)

    def Pocket002Body001(self, name):
        Pocket002Body001 = self.Body001.newObject('PartDesign::Pocket', name)
        Pocket002Body001.Profile = self.Sketch003Body001
        Pocket002Body001.Reversed = True
        Pocket002Body001.Type = 'ThroughAll'
        return(Pocket002Body001)

    def Body002(self, name):
        return(super().Body002(name))

    def Sketch001Body002(self, name):
        return(super().Sketch001Body002(name))

    def Pad001Body002(self, name):
        return(super().Pad001Body002(name))

    def Body003(self, name):
        return(super().Body003(name))

    def Sketch001Body003(self, name):
        Sketch001 = self.Body003.newObject('Sketcher::SketchObject', name)
        Sketch001.Support = self.Body003.Origin.OriginFeatures[4] # XZ_Plane
        Sketch001.MapMode = 'FlatFace'
        Sketch001.Visibility = False
        Sketch001.addGeometry([
            Part.ArcOfParabola(Part.Parabola(
                    FreeCAD.Vector(22/4, 0, 0),
                    FreeCAD.Vector(22/2, 0, 0),
                    FreeCAD.Vector(0, 0, 1),
                ), -7/2, 7/2), # 0
            Part.LineSegment(
                FreeCAD.Vector(19/2, 7/2, 0),
                FreeCAD.Vector(19/2, -7/2, 0)
            ), # 1
        ], False)
        Sketch001.addGeometry([
            Part.LineSegment(FreeCAD.Vector(
                Sketch001.Geometry[0].StartPoint.x,
                Sketch001.Geometry[0].StartPoint.y, 0),
                FreeCAD.Vector(19/2, 7/2, 0)
            ), # 3
            Part.LineSegment(FreeCAD.Vector(
                Sketch001.Geometry[0].EndPoint.x,
                Sketch001.Geometry[0].EndPoint.y, 0),
                FreeCAD.Vector(19/2, -7/2, 0)
            ), # 4
        ], False)
        self.ActiveDocument.recompute()
        return(Sketch001)

    def Revolution001Body003(self, name):
        Revolution001 = self.Body003.newObject('PartDesign::Revolution', name)
        Revolution001.ReferenceAxis = (self.Sketch001Body003, ['V_Axis'])
        Revolution001.Profile = self.Sketch001Body003
        self.ActiveDocument.recompute()
        return(Revolution001)


if __name__ == '__main__':
    # Bearing()
    BearingKFL8()
