import arcade

#Chessboard
HEIGHT = 800
WIDTH = 800

names = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
pieces = []

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
        
chess_piece.make_pieces()

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
for i in range(32):
    if pieces[i].colour == 'WHITE':
        arcade.draw_text(pieces[i].piece, pieces[i].x, pieces[i].y, arcade.color.BLUE)
    elif pieces[i].colour == 'BLACK':
        arcade.draw_text(pieces[i].piece, pieces[i].x, pieces[i].y, arcade.color.RED)

arcade.finish_render()
arcade.run()
