import ursina as ur
class Piece(ur.Button):
    def __init__(self, texture, position, scale, *args, **kwargs):
        super().__init__(position=position, highlight_color=ur.color.light_gray, pressed_color=ur.color.gray, *args, **kwargs)
        self.model = ur.Quad()
        self.position = position + (-0.01, 0, 0)
        self.texture = texture
        self.scale = scale
        self.name = texture.split('-')[1]
    
    def on_click(self):
        print(f"Clicked on {self.name} at position {self.position}")
        # Here you can add logic for what happens when the piece is clicked
        # For example, you might want to select the piece or show its possible moves



if __name__ == '__main__':
    import main