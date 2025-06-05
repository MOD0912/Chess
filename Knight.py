import ursina as ur

class Knight(ur.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional Knight-specific initialization can go here

    def on_click(self):
        print(f"Knight clicked at {self.position}")
        # Knight-specific click logic
