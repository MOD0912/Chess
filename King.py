import ursina as ur

class King(ur.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional King-specific initialization can go here

    def on_click(self):
        print(f"King clicked at {self.position}")
        # King-specific click logic
