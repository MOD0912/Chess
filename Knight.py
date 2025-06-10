import ursina as ur

class Knight(ur.Button):
    def __init__(self, *args, game=None, pos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game
        self.pos = pos
        self.name = 'knight'

    def on_click(self):
        print(f"Knight clicked at {self.position}")
        if self.game:
            self.game.knight(self)
            

if __name__ == "__main__":
    import main
