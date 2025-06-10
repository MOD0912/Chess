import ursina as ur

class King(ur.Button):
    def __init__(self, *args, game=None, pos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game
        self.pos = pos
        self.name = 'king'

    def on_click(self):
        print(f"King clicked at {self.position}")
        if self.game:
            self.game.king(self)
