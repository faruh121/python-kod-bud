# Создать графическое приложение размерами 600 на 480. Указать заголовок "Моя первая игра". Установить желтый цвет фона.

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Моя первая игра"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(SCREEN_TITLE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.BLACK, 12, anchor_x="center")

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()


#cсылка на мой гит хаб https://github.com/faruh121/python-kod-bud