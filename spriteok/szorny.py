from spriteok.figura import Figura


class Szorny(Figura):

    eletero = None
    sebzes = None

    def __init__(self, x, y,):
        super().__init__(x, y)

    def megjelenit(self):
        print("Szörny: koordináták: (" + str(self.center_x) + ", " + str(self.center_y) + "), életerő: " + str(self.eletero) + ", sebzés: " + str(self.sebzes))
