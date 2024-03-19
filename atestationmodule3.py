import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Platformer Game")
        self.player = arcade.Sprite("character.png")
        self.player.center_x = 50
        self.player.center_y = 50

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time):
        self.player.center_x += MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player.center_y += 100

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()