import arcade

MEZO_MERET = 32


class Figura(arcade.Sprite):

    kep = None

    def __init__(self, x, y):
        super().__init__(self.kep)
        self.center_x, self.center_y = self.koordinatak_szamolasa(x, y)

    def koordinatak_szamolasa(self, x_mezo, y_mezo):
        x = MEZO_MERET * x_mezo + MEZO_MERET / 2
        y = MEZO_MERET * y_mezo + MEZO_MERET / 2
        return x, y
