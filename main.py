from graphics import Window, Point
from cell import Cell


def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    point2 = Point(40, 40)
    cell1 = Cell(win, point1, point2, True, False)
    cell1.draw()
    point1 = Point(60, 60)
    point2 = Point(110, 110)
    cell2 = Cell(win, point1, point2, False)
    cell2.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
