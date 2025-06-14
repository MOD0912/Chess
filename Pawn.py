import ursina as ur

class Pawn(ur.Button):
    def __init__(self, *args, game=None, pos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.pos = pos
        self.game = game  # Save reference to the main game
        self.name = 'pawn'

    def click(self):
        print(f"Pawn clicked at {self.position}")
        if self.game:
            self.game.clear_points()
        self.game.summon_point(self.position, self)

    def move(self, new_position):
        """Move the pawn to a new position."""
        print(f"Moving pawn from {self.position} to {new_position}")
        self.position = new_position
    

if __name__ == "__main__":
    import main