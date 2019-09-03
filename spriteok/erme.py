from spriteok.figura import Figura

class Erme(Figura):

    kep = "img/Coin1.png"
    szamlalo = 0

    def __init__(self, x, y, e):
        super().__init__(x, y)
        self.ertek = e
        Erme.szamlalo += 1