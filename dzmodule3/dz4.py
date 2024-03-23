import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALE = 0.5
COIN_SCALE = 0.5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "My Arcade Game")
        self.character = arcade.Sprite("character.png", CHARACTER_SCALE)
        self.character.center_x = 100
        self.character.center_y = 100
        self.coins = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        self.character.draw()
        self.coins.draw()

    def on_update(self, delta_time):
        self.character.update()

        for coin in self.coins:
            if arcade.check_for_collision(self.character, coin):
                coin.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.character.change_y = 5
        elif key == arcade.key.DOWN:
            self.character.change_y = -5
        elif key == arcade.key.LEFT:
            self.character.change_x = -5
        elif key == arcade.key.RIGHT:
            self.character.change_x = 5

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.character.change_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.character.change_x = 0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()

#cсылка на мой гит хаб https://github.com/faruh121/python-kod-bud
