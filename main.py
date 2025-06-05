import ursina as ur
import os

from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King

class Main:
    def __init__(self):
        super().__init__()
        self.pieces = []
        for i in range(8):
            self.pieces.append([])
        self.scale_y = 0.75
        self.scale_x = 0.75
        self.your_color = "black"
        self.enemy_color = "white" if self.your_color == "black" else "black"
        print(self.pieces)
        self.board = ur.Entity(
            position=(-2.1, -2.1, -0.1),
            scale=(8*self.scale_x, 8*self.scale_y, -0.01),
            color=ur.color.white
        )
        self.create_board()
        self.create_pieces()
    
    def create_board(self):
        for x in range(0, 8):
            for y in range(0, 8):
                if (x + y) % 2 == 0:
                    color = ur.color.white
                else:
                    color = ur.color.rgba32(170, 90, 30)
                board = ur.Entity(  
                    parent=self.board,
                    model="quad",
                    position=(x*0.1, y*0.1, -0.01),
                    scale=(0.1, 0.1, -0.01),
                    color=color,
                )
                #self.pieces[0].append(board)

    def create_pieces(self):

        
        # top pieces
        # pawns:
        for i in range(0, 8):
            pawn = Pawn(parent=self.board, 
                        texture=self.enemy_color+"-pawn",
                        position=(i/10+0.01, 0.6, 0), 
                        color=ur.color.white,
                        scale=(.1, .1)
            )

            self.pieces[-2].append(pawn)
            
        # rooks:
        lr = Rook(parent=self.board, 
                  texture=self.enemy_color+"-rook", 
                  position=(0, 0.7, 0), 
                  color=ur.color.white,
                  scale=(.1, .1)
                  )
        rr = Rook(parent=self.board,
                  texture=self.enemy_color+"-rook", 
                  position=(0.7, 0.7, 0), 
                  color=ur.color.white,
                  scale=(.1, .1)
                  )
        
        # knights:
        lk = Knight(parent=self.board, 
                    texture=self.enemy_color+"-knight", 
                    position=(0.1, 0.7, 0), 
                    color=ur.color.white,
                    scale=(.1, .1)
                   )
        rk = Knight(parent=self.board,
                   texture=self.enemy_color+"-knight", 
                   position=(0.6, 0.7, 0), 
                   color=ur.color.white,
                   scale=(.1, .1)
                    )
        
        # bishops:
        lb = Bishop(parent=self.board,
                    texture=self.enemy_color+"-bishop", 
                    position=(0.2, 0.7, 0), 
                    color=ur.color.white,
                    scale=(.1, .1)
                    )
        rb = Bishop(parent=self.board,
                    texture=self.enemy_color+"-bishop", 
                    position=(0.5, 0.7, 0), 
                    color=ur.color.white,
                    scale=(.1, .1)
                    )
        # queen and king:
        queen = Queen(parent=self.board, 
                     texture=self.enemy_color+"-queen", 
                     position=(0.3, 0.7, 0), 
                     color=ur.color.white,
                     scale=(.1, .1)
                      )
        king = King(parent=self.board,
                   texture=self.enemy_color+"-king", 
                   position=(0.4, 0.7, 0), 
                   color=ur.color.white,
                   scale=(.1, .1)
                   )
        self.pieces[-1].extend([lr, lk, lb, queen, king, rb, rk, rr])
        
        
        
        # bottom pieces
        # pawns:
        for i in range(0, 8):
            pawn = Pawn(parent=self.board, 
                        texture=self.your_color+"-pawn", 
                        position=(i/10, 0.1, 0),
                        color=ur.color.white,
                        scale=(.1, .1))
            self.pieces[1].append(pawn)
        
        # rooks:
        lr = Rook(parent=self.board, 
                  texture=self.your_color+"-rook", 
                  position=(0, 0, 0), 
                  color=ur.color.white,
                  scale=(.1, .1))
        rr = Rook(parent=self.board, 
                  texture=self.your_color+"-rook", 
                  position=(0.7, 0, 0), 
                  color=ur.color.white,
                  scale=(.1, .1))

        # knights:
        lk = Knight(parent=self.board, 
                    texture=self.your_color+"-knight", 
                    position=(0.1, 0, 0), 
                    color=ur.color.white,
                    scale=(.1, .1))
        rk = Knight(parent=self.board,
                   texture=self.your_color+"-knight", 
                   position=(0.6, 0, 0), 
                   color=ur.color.white,
                   scale=(.1, .1))
        
        # bishops:
        lb = Bishop(parent=self.board, 
                    texture=self.your_color+"-bishop", 
                    position=(0.2, 0, 0), 
                    color=ur.color.white,
                    scale=(.1, .1))
        rb = Bishop(parent=self.board,
                    texture=self.your_color+"-bishop", 
                    position=(0.5, 0, 0), 
                    color=ur.color.white,
                    scale=(.1, .1))
        
        # queen and king:
        queen = Queen(parent=self.board, 
                     texture=self.your_color+"-queen", 
                     position=(0.3, 0, 0), 
                     color=ur.color.white,
                     scale=(.1, .1))
        king = King(parent=self.board, 
                   texture=self.your_color+"-king", 
                   position=(0.4, 0, 0), 
                   color=ur.color.white,
                   scale=(.1, .1))

        self.pieces[0].extend([lr, lk, lb, queen, king, rb, rk, rr])
        
        
        for i in self.pieces:
            #print(i)
            print(len(i))

def input(key):
    if key == "control":
        exit()
        
        
app = ur.Ursina()
Main()
ur.EditorCamera()
app.run()