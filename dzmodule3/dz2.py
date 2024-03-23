import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Snegovik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x, self.y + 40, 20, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x, self.y + 70, 15, arcade.color.WHITE)

def on_draw(delta_time):
    arcade.start_render()
    snegovik.draw()

snegovik = Snegovik(400, 300)

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Snegovik")
arcade.set_background_color(arcade.color.RED)

arcade.schedule(on_draw, 1/60)

arcade.run()