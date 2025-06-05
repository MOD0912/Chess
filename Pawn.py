import ursina as ur

class Pawn(ur.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional Pawn-specific initialization can go here

    def on_click(self):
        print(f"Pawn clicked at {self.position}")
        # Pawn-specific click logic
