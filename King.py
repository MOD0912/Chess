import ursina as ur

class King(ur.Button):
    def __init__(self, *args, game=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def on_click(self):
        print(f"King clicked at {self.position}")
        if self.game:
            self.game.piece_clicked(self)
