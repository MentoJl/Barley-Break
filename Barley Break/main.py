from pyray import *
import random

class BarleyBreak:

    WIDTH = 400
    HEIGHT = 400

    def __init__(self):
        self.recs = {}
        self.window_should_close = False
        self.rec_width = 100
        self.rec_height = 100
        
    def createBoard(self):
        numbers = random.sample(range(16), 16)
        self.board = [numbers[i:i+4] for i in range(0, 16, 4)]

    def drawRecs(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] < 15:
                    x = j * self.rec_width
                    y = i * self.rec_height
                    draw_rectangle(x, y, self.rec_width, self.rec_height, DARKPURPLE)
                    draw_rectangle_lines(x, y, self.rec_width, self.rec_height, BLACK)
                    draw_text(f"{self.board[i][j]+1}", int(x + (self.rec_width / 2) - 10), int(y + (self.rec_height / 2) - 10), 30, WHITE)

    def swap(self, a, b ):
        return b, a

    def cheaker(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if not self.board[i][j - 1] < self.board[i][j] and j != 0:
                    return False
        return True

    def mouseClicked(self):
        mouse = get_mouse_position()
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] < 15:
                    x = j * self.rec_width
                    y = i * self.rec_height
                    if mouse.x > x and mouse.x < x + self.rec_width and mouse.y > y and mouse.y < y + self.rec_height:
                        try:
                            if j-1 >= 0 and self.board[i][j-1] == 15:
                                self.board[i][j], self.board[i][j-1] = self.swap(self.board[i][j], self.board[i][j-1])

                            elif j+1 < 4 and self.board[i][j+1] == 15:
                                self.board[i][j], self.board[i][j+1] = self.swap(self.board[i][j], self.board[i][j+1])

                            elif i-1 >= 0 and self.board[i-1][j] == 15:
                                self.board[i][j], self.board[i-1][j] = self.swap(self.board[i][j], self.board[i-1][j])

                            elif i+1 < 4 and self.board[i+1][j] == 15:
                                self.board[i][j], self.board[i+1][j] = self.swap(self.board[i][j], self.board[i+1][j])
                        except Exception as error:
                            print(f"Error: {error}")

    def closeWindow(self):
        if window_should_close():
            self.window_should_close = True

    def show(self):
        set_target_fps(30)
        self.createBoard()
        print(self.board)
        while not self.window_should_close and not window_should_close():
            begin_drawing()
            clear_background(WHITE)
            if is_mouse_button_pressed(MOUSE_LEFT_BUTTON) and not self.cheaker():
                self.mouseClicked()
            if self.cheaker():
                color = Color(0, 0, 0, 168)
                rec = Rectangle(0, 0, self.WIDTH, self.HEIGHT)
                draw_rectangle_rec(rec, color)
                draw_text("PRESS TO RESTART", 120, 270, 300, WHITE)
                if is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
                    break
            self.drawRecs()
            end_drawing()

init_window(400, 400, "BarleyBreak")
set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)
test = BarleyBreak()
test.show()