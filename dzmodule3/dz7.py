



# Добавить в игру из прошлого домашнего задания звуки. 
# Звуки можно найти в стандартной библиотеке arcade, либо загрузить свои.
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALING = 1
COIN_SCALING = 0.5
ENEMY_SCALING = 1

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.character_list = None
        self.coin_list = None
        self.enemy_list = None
        self.character_sprite = None
        self.coin_sound = arcade.load_sound("sound/coin_sound.wav")
        self.hit_sound = arcade.load_sound("sound/hit_sound.wav")

    def setup(self):
        self.character_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.character_sprite = arcade.Sprite("img/playerShip1_green.pngcharacter.png", CHARACTER_SCALING)
        self.character_sprite.center_x = 50
        self.character_sprite.center_y = 50
        self.character_list.append(self.character_sprite)

        coin = arcade.Sprite("img/meteorGrey_big2.png", COIN_SCALING)
        coin.center_x = 200
        coin.center_y = 200
        self.coin_list.append(coin)

        enemy = arcade.Sprite("img/meteorGrey_big2.png", ENEMY_SCALING)
        enemy.center_x = 300
        enemy.center_y = 300
        self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.character_list.draw()
        self.coin_list.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        self.character_list.update()

        hit_list = arcade.check_for_collision_with_list(self.character_sprite, self.enemy_list)
        if hit_list:
            arcade.close_window()
            arcade.play_sound(self.hit_sound)
            arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.coin_sound)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

#cсылка на мой гит хаб https://github.com/faruh121/python-kod-bud