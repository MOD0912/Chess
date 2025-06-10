import ursina as ur

class Bishop(ur.Button):
    def __init__(self, *args, game=None, pos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game
        self.pos = pos
        self.name = 'bishop'

    def on_click(self):
        print(f"Bishop clicked at {self.position}")
        if self.game:
            self.game.bishop(self)
