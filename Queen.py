import ursina as ur

class Queen(ur.Button):
    def __init__(self, *args, game=None, pos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game
        self.pos = pos
        self.name = 'queen'

    def on_click(self):
        print(f"Queen clicked at {self.position}")
        if self.game:
            self.game.queen(self)
            
if __name__ == "__main__":
    import main
