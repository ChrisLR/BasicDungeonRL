class Room(object):
    def __init__(self, x, y, design_piece):
        self.design_piece = design_piece
        self.x = x
        self.y = y
        self.width = design_piece.get_width()
        self.height = design_piece.get_height()
