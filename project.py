import arcade

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_TITLE = "Starting Template"

names = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
pieces = []

valid_choice = False  
index = 0 #Could I make this better

motion_x = None
motion_y = None

turn = "WHITE" #Do I have to define variable up here?

class chess_piece():

    def __init__(self, piece, colour, x, y):
        self.piece = piece
        self.colour = colour
        self.x = x
        self.y = y
    
    @classmethod
    def make_pieces(cls):
        for x, name in enumerate(names):
            pieces.append(chess_piece (name, "WHITE", (100 * x) + 50, 50))
            pieces.append(chess_piece (name, "BLACK", (100 * x) + 50, 750))
            pieces.append(chess_piece ("Pawn", "WHITE", (100 * x) + 50, 150))
            pieces.append(chess_piece ("Pawn", "BLACK", (100 * x) + 50, 650))

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):

        chess_piece.make_pieces()

    def on_draw(self):

        arcade.start_render()
        #Print chess-board
        z = 0
        for y in range(0, 701, 100):
            for x in range(0 + z, 701 + z, 100):
                if x % 200 == 0:
                    arcade.draw_xywh_rectangle_filled(x - z, y, 100, 100, arcade.color.BLACK)
                else:
                    arcade.draw_xywh_rectangle_filled(x - z, y, 100, 100, arcade.color.WHITE)
            z += 100

        #print pieces
        for piece in pieces:
            if piece.colour == 'WHITE':
                arcade.draw_text(piece.piece, piece.x, piece.y, arcade.color.BLUE)
            elif piece.colour == 'BLACK':
                arcade.draw_text(piece.piece, piece.x, piece.y, arcade.color.RED)

    #def on_update(self, delta_time):

    #def on_key_press(self, key, key_modifiers):
        
        #pass

    #def on_key_release(self, key, key_modifiers):


    def on_mouse_motion(self, x, y, delta_x, delta_y):

        global pieces, index, motion_x, motion_y

        if valid_choice == True:
            motion_x = x
            motion_y = y

            pieces[index].x = motion_x
            pieces[index].y = motion_y

    def on_mouse_press(self, x, y, button, key_modifiers):

        global valid_choice, index

        for i, piece in enumerate(pieces):
            if x in range(piece.x - 50, piece.x + 50) and y in range(piece.y - 50, piece.y + 50):
                if piece.colour == turn:
                    valid_choice = True
                    index = i

            
    def on_mouse_release(self, x, y, button, key_modifiers):
        
        global pieces, index, motion_x, motion_y, valid_choice, turn

        motion_x = None
        motion_y = None

        if valid_choice == True:
            if (x - (x % 50)) % 100 == 0:
                pieces[index].x = x - (x % 50) + 50
            else:
                pieces[index].x = x - (x % 50)

            if (y - (y % 50)) % 100 == 0:
                pieces[index].y = y - (y % 50) + 50
            else:
                pieces[index].y = y - (y % 50)

            if turn == "WHITE":
                turn = "BLACK"
            else:
                turn = "WHITE"
        
        valid_choice = False

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
