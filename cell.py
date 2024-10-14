from graphics import Line, Point


class Cell:
    def __init__(self, window=None) -> None:
        self.x1 = None
        self.x1 = None
        self.x2 = None
        self.y2 = None
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.window = window

    def draw(self, x1, y1, x2, y2):
        if self.window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line, "black")
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line, "black")

    def center(self):
        return Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def draw_move(self, to_cell, undo=False):
        if self.window is None:
            return
        color = "gray" if undo else "red"
        point1 = self.center()
        point2 = to_cell.center()
        line = Line(point1, point2)
        self.window.draw_line(line, color)
