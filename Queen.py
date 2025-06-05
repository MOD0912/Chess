import ursina as ur

class Queen(ur.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional Queen-specific initialization can go here

    def on_click(self):
        print(f"Queen clicked at {self.position}")
        # Queen-specific click logic
