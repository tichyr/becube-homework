from spriteok.figura import Figura
from spriteok.jatekos import Jatekos


class Lada(Figura):

    kep = "img/box.png"

    def __init__(self, x, y, targylista = [], allapot = False):
        super().__init__(x, y)
        self.tartalom = targylista
        self.nyitva = allapot

    def tartalom_kiiras(self):
        if self.nyitva == True:
            print("A láda nyitva van, tartalma:")
            for targy in self.tartalom:
                print(targy)
        else:
            print("A láda zárva van")

    def kifoszt(self, jatekos):
        if self.nyitva:
            self.kill()
            self.tartalom_kiiras()
            for targy in self.tartalom:
                jatekos.targyat_talal(targy)
        else:
            self.tartalom_kiiras()