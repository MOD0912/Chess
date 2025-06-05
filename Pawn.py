import ursina as ur

class Pawn(ur.Button):
    def __init__(self, *args, game=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game  # Save reference to the main game

    def on_click(self):
        print(f"Pawn clicked at {self.position}")
        if self.game:
            self.game.piece_clicked(self)
