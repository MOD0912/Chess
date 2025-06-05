import ursina as ur

class Rook(ur.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional Rook-specific initialization can go here

    def on_click(self):
        print(f"Rook clicked at {self.position}")
        # Rook-specific click logic
