import ursina as ur

class Bishop(ur.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional Bishop-specific initialization can go here

    def on_click(self):
        print(f"Bishop clicked at {self.position}")
        # Bishop-specific click logic
