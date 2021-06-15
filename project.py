import arcade

#Chessboard
HEIGHT = 800
WIDTH = 800

pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
white_pieces = []
black_pieces = []

class chess_piece():

    def __init__(self, piece, colour, x, y):
        self.piece = piece
        self.colour = colour
        self.x = x
        self.y = y
    
    @classmethod
    def pieces(cls):
        for x, name in enumerate(pieces):
            white_pieces.append(chess_piece (name, "White", (100 * x) + 50, 50))
            black_pieces.append(chess_piece (name, "Black", (100 * x) + 50, 750))
        
chess_piece.pieces()

arcade.open_window(WIDTH, HEIGHT,"chess")
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
for i in range(8):
    arcade.draw_text(white_pieces[i].piece, white_pieces[i].x, white_pieces[i].y, arcade.color.RED)
    arcade.draw_text(black_pieces[i].piece, black_pieces[i].x, black_pieces[i].y, arcade.color.BLUE)

arcade.finish_render()
arcade.run()
