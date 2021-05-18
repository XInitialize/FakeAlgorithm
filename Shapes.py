import math


class Point2D:
    def __init__(self, X=0, Y=0) -> None:
        self.X = X
        self.Y = Y

    def fix_int(self):
        self.X = int(self.X)
        self.Y = int(self.Y)

    def __str__(self) -> str:
        return f"({self.X}, {self.Y})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point2D):
            raise TypeError(f"Wrong type for Point2D and {type(o)}")
        else:
            if self.X == o.X and self.Y == o.Y:
                return True
            else:
                return False


class Point3D:
    def __init__(self, X=0, Y=0, Z=0) -> None:
        self.X = X
        self.Y = Y
        self.Z = Z

    def fix_int(self):
        self.X = int(self.X)
        self.Y = int(self.Y)
        self.Z = int(self.Z)

    def __str__(self) -> str:
        return f"({self.X}, {self.Y}, {self.Y})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point3D):
            raise TypeError(f"Wrong type for Point3D and {type(o)}")
        else:
            if self.X == o.X and self.Y == o.Y and self.Z == o.Z:
                return True
            else:
                return False


def PointDistance2D(PointA, PointB):
    return math.sqrt((PointA.X-PointB.X)**2+(PointA.Y-PointB.Y)**2)


def PointDistance3D(PointA, PointB):
    return math.sqrt((PointA.X-PointB.X)**2+(PointA.Y-PointB.Y)**2+(PointA.Z-PointB.Z)**2)


def _recall_instance(instanceA, instanceB, object):
    if type(instanceA) != type(instanceB):
        raise TypeError(
            f"Different instance types. Instance_A's type is {type(instanceA)}, but Instance_B's type is {type(instanceB)}")
    else:
        if isinstance(instanceA, object):
            return True
        else:
            return False


def PointDistance(PointA, PointB):
    if _recall_instance(PointA, PointB, Point2D):
        return PointDistance2D(PointA, PointB)
    elif _recall_instance(PointA, PointB, Point3D):
        return PointDistance3D(PointA, PointB)
    else:
        raise TypeError(
            f"Wrong type to calculate distance, Use 'Point2D'/'Point3D' instead.")


def CalculatePointDelta(PointA, PointB):
    if _recall_instance(PointA, PointB, Point2D):
        deltax = abs(PointA.X-PointB.X)
        deltay = abs(PointA.Y-PointB.Y)
        return deltax, deltay
    elif _recall_instance(PointA, PointB, Point3D):
        deltax = abs(PointA.X-PointB.X)
        deltay = abs(PointA.Y-PointB.Y)
        deltaz = abs(PointA.Z-PointB.Z)
        return deltax, deltay, deltaz
    else:
        raise TypeError(
            f"Wrong type to calculate distance, Use 'Point2D'/'Point3D' instead.")


class CoordinateError(Exception):
    pass


def CompareCoordinate(p1, p2):
    # TODO: verify performance and broadcast to all coordination
    if _recall_instance(p1, p2, Point2D):
        if p1.X != p2.X:
            if p1.X < p2.X:
                return p1, p2
            else:
                return p2, p1
        else:
            if p1.Y != p2.Y:
                if p1.Y < p2.Y:
                    return p1, p2
                else:
                    return p2, p1
            else:
                return p1, p2
    else:
        raise TypeError(
            f"Wrong type to calculate distance, Use 'Point2D'/'Point3D' instead.")


class Line2D:
    def __init__(self, point1: Point2D, point2: Point2D, int_point_mode=True) -> None:
        if int_point_mode:
            self.CenterPoint, self.Length = self.form_line_int(point1, point2)
        else:
            self.CenterPoint, self.Length = self._calculate_center_length(
                point1, point2)

    @staticmethod
    def _calculate_center_length(p1, p2):
        if _recall_instance(p1, p2, Point2D):
            return (
                Point2D((p1.X+p2.X)/2, (p1.Y+p2.Y)/2),
                PointDistance(p1, p2)
            )
        else:
            raise TypeError(
                f"Wrong type to calculate, Use 'Point2D'/'Point3D' instead.")

    def form_line_int(self, p1, p2):
        cP, length = self._calculate_center_length(p1, p2)
        cP.fix_int()
        return cP, length

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Line2D):
            raise TypeError(f"Wrong type for Line2D and {type(o)}")
        else:
            if self.CenterPoint == o.CenterPoint and self.Length == o.Length:
                return True
            else:
                return False


class Rectangle_Grid2D:
    def __init__(self, point1: Point2D, point2: Point2D, int_point_type=True) -> None:
        if int_point_type:
            self.CenterPoint, self.Height, self.Width = self.form_rect_int(
                point1, point2)
        else:
            self.CenterPoint, self.Height, self.Width = self._calculate_rect(
                point1, point2)

    @staticmethod
    def _calculate_rect(p1: Point2D, p2: Point2D):
        if _recall_instance(p1, p2, Point2D):
            if (p1.X == p2.X) or (p1.Y == p2.Y):
                raise CoordinateError("Point in a same grid line")
            else:
                return (
                    Line2D(p1, p2).CenterPoint, abs(p1.Y-p2.Y), abs(p1.X-p2.X)
                )
        else:
            raise TypeError(
                f"Wrong type to calculate, Use 'Point2D'/'Point3D' instead.")

    def form_rect_int(self, p1: Point2D, p2: Point2D):
        cP, height, width = self._calculate_rect(p1, p2)
        cP.fix_int()
        return cP, height, width

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Rectangle_Grid2D):
            raise TypeError(f"Wrong type for Rectangle_Grid2D and {type(o)}")
        else:
            if self.CenterPoint == o.CenterPoint and self.Height == o.Height and self.Width == o.Width:
                return True
            else:
                return False


def Calculate_I_U(rect1: Rectangle_Grid2D, rect2: Rectangle_Grid2D):
    # TODO: broadcast to other dimention
    if _recall_instance(rect1, rect2, Rectangle_Grid2D):
        IoU = 0
        dx, dy = CalculatePointDelta(rect1.CenterPoint, rect2.CenterPoint)
        Ew, Eh = (rect1.Width + rect2.Width), (rect1.Height + rect2.Height)
        if (Ew - 2*dx) > 0 and (Eh - 2*dy) > 0:
            Intersection = (Ew-2 * dx) * (Eh-2 * dy)
            Union = 4 * rect1.Width * rect2.Width + 4 * rect1.Height * rect2.Height - Intersection
            return Intersection, Union
    else:
        raise TypeError(
            f"Wrong type to calculate, Use 'Rectangle_Grid2D' instead.")
