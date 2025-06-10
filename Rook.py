import ursina as ur

class Rook(ur.Button):
    def __init__(self, *args, game=None, pos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game
        self.pos = pos
        self.name = 'rook'

    def on_click(self):
        print(f"Rook clicked at {self.position}")
        if self.game:
            self.game.rook(self)
