from cell import Cell
import random
import time


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ) -> None:
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_enterance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self.num_cols):
            col_cells = []
            for _ in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = i * self.cell_size_x + self.x1
        x2 = x1 + self.cell_size_x
        y1 = j * self.cell_size_y + self.y1
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells = []
            if i > 1 and not self._cells[i - 1][j].visited:
                cells.append((i - 1, j, "left"))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                cells.append((i + 1, j, "right"))
            if j >= 1 and not self._cells[i][j - 1].visited:
                cells.append((i, j - 1, "top"))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                cells.append((i, j + 1, "bottom"))
            if len(cells) == 0:
                self._draw_cell(i, j)
                return
            next_cell = cells[random.randrange(len(cells))]
            if next_cell[2] == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
                self._break_walls_r(i - 1, j)
            if next_cell[2] == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)
            if next_cell[2] == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)
            if next_cell[2] == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)

    def _break_enterance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
