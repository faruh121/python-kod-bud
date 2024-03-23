# Реализовать в графическом окне анимацию персонажа при движении влево-вправо.
#  В состоянии покоя должен отображаться обычный спрайт, а при движении происходить смена спрайтов для анимации.
import arcade

SPRITE_SCALING = 0.5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        self.player_sprite = arcade.Sprite("img/playerShip1_green.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        
        self.player_sprites_walk = [arcade.Sprite("img/playerShip1_orange.png", SPRITE_SCALING),
                                    arcade.Sprite("img/playerShip1_green.png", SPRITE_SCALING)]
        self.current_sprite = 0
        
        self.set_update_rate(1/10)  # Частота обновления анимации
        
    def on_draw(self):
        arcade.start_render()
        
        if self.player_sprite.change_x == 0:
            self.player_sprite.draw()
        else:
            self.player_sprites_walk[self.current_sprite].center_x = self.player_sprite.center_x
            self.player_sprites_walk[self.current_sprite].center_y = self.player_sprite.center_y
            self.player_sprites_walk[self.current_sprite].draw()
        
    def on_update(self, delta_time):
        self.player_sprite.update()
        
        if self.player_sprite.change_x != 0:
            self.current_sprite += 1
            if self.current_sprite >= len(self.player_sprites_walk):
                self.current_sprite = 0
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    window = MyGame(800, 600)
    arcade.run()

if __name__ == "__main__":
    main()













#cсылка на мой гит хаб https://github.com/faruh121/python-kod-bud