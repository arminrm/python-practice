import arcade

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_TITLE = "Starting Template"

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # If you have sprite lists, you should create them here,
         # and set them to None

    def setup(self):
       #""" Set up the game variables. Call to re-start the game. """
       # Create your sprites and sprite lists here
        #pass

    def on_draw(self):
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        arcade.start_render()
        z = 0
        for y in range(0, 701, 100):
            for x in range(0 + z, 701 + z, 100):
                if x % 200 == 0:
                    arcade.draw_xywh_rectangle_filled(x - z, y, 100, 100, arcade.color.BLACK)
                else:
                    arcade.draw_xywh_rectangle_filled(x - z, y, 100, 100, arcade.color.WHITE)

                #White pieces
                if (x,y) == (0, 0) or (x,y) == (700, 0):
                    arcade.draw_text("Rook", x + 50, y + 50, arcade.color.YELLOW)
                elif (x,y) == (100, 0) or (x,y) == (600, 0):
                    arcade.draw_text("Knight", x + 50, y + 50, arcade.color.YELLOW)
                elif (x, y) == (200, 0) or (x,y) == (500, 0):
                    arcade.draw_text("Bishop", x + 50, y + 50, arcade.color.YELLOW)
                elif (x, y) == (300, 0):
                    arcade.draw_text("Queen", x + 50, y + 50, arcade.color.YELLOW)
                elif (x, y) == (400, 0):
                    arcade.draw_text("King", x + 50, y + 50, arcade.color.YELLOW)
                elif y == 100:
                    arcade.draw_text("Pawn", x - z + 50, y + 50, arcade.color.YELLOW)

                #Black pieces
                if (x, y) == (700, 700) or (x,y) == (1400, 700):
                    arcade.draw_text("Rook", x - z + 50, y + 50, arcade.color.BLUE)
                elif (x, y) == (800, 700) or (x, y) == (1300, 700):
                    arcade.draw_text("Knight", x - z + 50, y + 50, arcade.color.BLUE)
                elif (x, y) == (900, 700) or (x, y) == (1200, 700):
                    arcade.draw_text("Bishop", x - z + 50, y + 50, arcade.color.BLUE)
                elif (x, y) == (1000, 700):
                    arcade.draw_text("Queen", x - z + 50, y + 50, arcade.color.BLUE)
                elif (x, y) == (1100, 700):
                    arcade.draw_text("King", x - z + 50, y + 50, arcade.color.BLUE)
                elif y == 600:
                    arcade.draw_text("Pawn", x - z + 50, y + 50, arcade.color.BLUE)
                z += 100
        arcade.finish_render()

       # This command should happen before we start drawing. It will clear
       # the screen to the background color, and erase what we drew last frame.
       
       

        # Call draw() on all your sprite lists below

     #def on_update(self, delta_time):

        #pass

    #def on_key_press(self, key, key_modifiers):
        
        #pass

    #def on_key_release(self, key, key_modifiers):

        #pass

    #def on_mouse_motion(self, x, y, delta_x, delta_y):

        #pass

    #def on_mouse_press(self, x, y, button, key_modifiers):

        #pass

    #def on_mouse_release(self, x, y, button, key_modifiers):

        #pass

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
