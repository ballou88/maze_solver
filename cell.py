from graphics import Line, Point


class Cell:
    def __init__(
        self,
        window,
        point1,
        point2,
        has_top_wall=True,
        has_right_wall=True,
        has_bottom_wall=True,
        has_left_wall=True,
    ) -> None:
        self.point1 = point1
        self.point2 = point2
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall
        self.window = window

    def draw(self):
        if self.has_top_wall:
            self.draw_top()
        if self.has_right_wall:
            self.draw_right()
        if self.has_bottom_wall:
            self.draw_bottom()
        if self.has_left_wall:
            self.draw_left()

    def draw_top(self):
        line = Line(self.point1, Point(self.point2.x, self.point1.y))
        self.window.draw_line(line, "black")

    def draw_right(self):
        line = Line(Point(self.point2.x, self.point1.y), self.point2)
        self.window.draw_line(line, "black")

    def draw_bottom(self):
        line = Line(Point(self.point1.x, self.point2.y), self.point2)
        self.window.draw_line(line, "black")

    def draw_left(self):
        line = Line(self.point1, Point(self.point1.x, self.point2.y))
        self.window.draw_line(line, "black")
