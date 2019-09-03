# Importok
from irany import Irany
from jatek_fuggvenyek import *
from random import randint
from spriteok.kard import Kard
from spriteok.erme import Erme
from spriteok.lada import Lada
from spriteok.vampir import Vampir
from spriteok.szellem import Szellem
from spriteok.ork import Ork
from spriteok.jatekos import Jatekos
from spriteok.fal import Fal

import arcade  # A jatek grafikáját oldja meg

# --- Konstansok ---
KEP_SZELESSEG = 640
KEP_MAGASSAG = 480

MEZO_MERET = 32 # Ekkora egy "kocka"
BAL_HATAR = 48 # Eddig mehet a játékos (képének középpontja) balra
JOBB_HATAR = 592 # Eddig mehet a játékos (képének középpontja) jobbra
FELSO_HATAR = 432 # Eddig mehet a játékos (képének középpontja) felfele
ALSO_HATAR = 48 # Eddig mehet a játékos (képének középpontja) lefele


class LovagJatek(arcade.Window):

    def __init__(self):
        super().__init__(KEP_SZELESSEG, KEP_MAGASSAG, "Lovagjáték")

        # Ezek a valtozok tartalmazzak a sprite listakat
        self.jatekos_lista = None
        self.eletero_lista = None
        self.eletero_lista2 = None
        self.erme_jelzo_lista = None
        self.erme_jelzo_sprite = None
        self.erme_jelzo_sprite2 = None
        self.erme_lista = None
        self.kard_lista = None
        self.lada_lista = None
        self.szorny_lista = None
        self.fal_lista = None
        self.jatekos = None
        self.jatekos2 = None

        self.kesz = False

    def on_key_press(self, megnyomott_gomb, modositok):
        """
        Ez a függvény tartalmazza azt, hogy mit kell gombnyomáskor csinálni.

        Automatikusan meghívódik minden gombnyomáskor. Ezt az úgynevezett
        eseményekkel (event) oldjuk majd meg: az 'on_key_press' esemény mindig megtörténik ('elsül'), ha valaki megnyom egy gombot,
        bármelyiket. Ez a függvény az 'on_key_press' esemény kezelő függvénye (event handler).

        A 'megnyomott_gomb' paraméter tartalmazza majd a megnyomott gomb kódját, így el tudjuk dönteni, hogy melyik gombot
        nyomták meg.

        A 'modositok' paramétert is megkapjuk, de nem használjuk. Ezzel lehetne vizsgálni a shift, alt, ctrl, stb. gombok
        lenyomását az eredetielg lenyomott gombbal együtt. Nem használjuk, de az esemény szerkezete miatt meg kell adni.
        """

        # A gombnyomásnak megfelelően odéb tesszük a játékost
        self.mozgasd_a_jatekost(megnyomott_gomb)

    def on_draw(self):
        """
        Ez a függvény is automatikusan hívódik meg. A játék bizonyos időközönként kirajzolja a képernyőt.
        Ide kell befoglalni mindent, amit meg szeretnénk jelentíteni.
        Mindig az arcade.start_render-rel kell kezdeni.
        """
        arcade.start_render()
        self.jelenitsd_meg_a_hatteret()

        self.jatekos_lista.draw()
        self.erme_jelzo_lista.draw()
        self.erme_lista.draw()
        self.kard_lista.draw()
        self.lada_lista.draw()
        self.szorny_lista.draw()
        self.jelenitsd_meg_az_aranymennyiseget()
        self.eletero_lista.draw()
        self.fal_lista.draw()

        if self.jatekos2 is not None:
            self.eletero_lista2.draw()

    def inditas(self):
        self.grafika_init()

        # Kezdeti üzenetek kiírása
        udvozlet()

        # Valójában itt indul el az ismétlődő ciklus
        arcade.run()

        # Ha vége a játéknak
        print("")
        print("-------------------------")
        print("Játékos1 eredményei")
        print("")
        viszlat(self.jatekos.tavolsag, self.jatekos.arany)
        kiir_fejlett(self.jatekos.targylista)

        if self.jatekos2 is not None:
            print("")
            print("-------------------------")
            print("Játékos2 eredményei")
            print("")
            viszlat(self.jatekos2.tavolsag, self.jatekos2.arany)
            kiir_fejlett(self.jatekos2.targylista)

    def grafika_init(self):

        # Hatter poziciojanak beallitasa
        self.hatter_pozicio_x, self.hatter_pozicio_y = KEP_SZELESSEG / 2, KEP_MAGASSAG / 2
        self.hatter_kep = arcade.load_texture("img/palya.png")

        self.jatekos_sprite_init()
        self.erme_jelzo_init()
        self.erme_sprite_init()
        self.kard_sprite_init()
        self.szorny_sprite_init()
        self.lada_sprite_init()
        self.fal_sprite_init()

        self.eletek_kirajzolasa()

    def jatekos_sprite_init(self):
        self.jatekos_lista = arcade.SpriteList()
        self.jatekos = Jatekos(randint(1, 18), randint(1, 12), 5)
        # self.jatekos2 = Jatekos(randint(1, 18), randint(1, 12), 5)
        self.jatekos_lista.append(self.jatekos)
        # self.jatekos_lista.append(self.jatekos2)

    def erme_jelzo_init(self):
        # Erme az erme jelzohoz
        self.erme_jelzo_sprite = arcade.Sprite("img/Coin1.png")
        self.erme_jelzo_sprite.center_x = MEZO_MERET / 2
        self.erme_jelzo_sprite.center_y = KEP_MAGASSAG - 1.5 * MEZO_MERET
        self.erme_jelzo_lista = arcade.SpriteList()
        self.erme_jelzo_lista.append(self.erme_jelzo_sprite)

        if self.jatekos2 is not None:
            self.erme_jelzo_sprite2 = arcade.Sprite("img/Coin1.png")
            self.erme_jelzo_sprite2.center_x = JOBB_HATAR + MEZO_MERET
            self.erme_jelzo_sprite2.center_y = KEP_MAGASSAG - 1.5 * MEZO_MERET
            self.erme_jelzo_lista.append(self.erme_jelzo_sprite2)

    def erme_sprite_init(self):
        self.erme_lista = arcade.SpriteList()
        for i in range(1,5):
            self.erme_lista.append(Erme(randint(1, 18), randint(1, 12), randint(1, 5)))

    def kard_sprite_init(self):
        self.kard_lista = arcade.SpriteList()
        self.kard_lista.append(Kard(randint(1, 18), randint(1, 12)))

    def szorny_sprite_init(self):
        self.szorny_lista = arcade.SpriteList()
        self.szorny_lista.append(Vampir(randint(1, 18), randint(1, 12)))
        self.szorny_lista.append(Szellem(randint(1, 18), randint(1, 12)))
        self.szorny_lista.append(Ork(randint(1, 18), randint(1, 12)))

    def lada_sprite_init(self):
        self.lada_lista = arcade.SpriteList()
        self.lada_lista.append(Lada(randint(1, 18), randint(1, 12), ["balta", "páncél"], False))
        self.lada_lista.append(Lada(randint(1, 18), randint(1, 12), ["pajzs", "sisak", "kard"], True))

    def fal_sprite_init(self):
        self.fal_lista = arcade.SpriteList()
        for i in range(4, 15):
            self.fal_lista.append(Fal(i, 11))
            self.fal_lista.append(Fal(i, 3))

    def update(self, delta_time: float):

        for jatekos in self.jatekos_lista:

            erintett_ermek = arcade.check_for_collision_with_list(jatekos, self.erme_lista)
            erintett_kardok = arcade.check_for_collision_with_list(jatekos, self.kard_lista)
            erintett_szornyek = arcade.check_for_collision_with_list(jatekos, self.szorny_lista)
            erintett_ladak = arcade.check_for_collision_with_list(jatekos, self.lada_lista)

            for erme in erintett_ermek:
                erme.kill()
                jatekos.aranyat_talal(erme.ertek)
                Erme.szamlalo -= 1

            for kard in erintett_kardok:
                kard.kill()
                jatekos.targyat_talal("kard")

            for szorny in erintett_szornyek:
                szorny.kill()
                jatekos.eletek -= szorny.sebzes

            for lada in erintett_ladak:
                lada.kifoszt(jatekos)

        self.eletek_kirajzolasa()

        if (Erme.szamlalo == 0) or (self.jatekos.eletek < 1) or (
                (self.jatekos2 is not None) and (self.jatekos2.eletek < 1)):
            self.close()

    def mozgasd_a_jatekost(self, megnyomott_gomb):

        # If-elif szerkezettel megvizsgáljuk, hogy a megnyomott gomb valamelyik nyíl-e a négy nyíl közül

        # Ha a lenyomott gomb a balra gomb
        if megnyomott_gomb == arcade.key.LEFT:
            if self.jatekos.center_x > BAL_HATAR:
                self.jatekos.balra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.RIGHT:
            if self.jatekos.center_x < JOBB_HATAR:
                self.jatekos.jobbra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.UP:
            if self.jatekos.center_y < FELSO_HATAR:
                self.jatekos.felfele_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.DOWN:
            if self.jatekos.center_y > ALSO_HATAR:
                self.jatekos.lefele_lep(self.fal_lista)

        if self.jatekos2 is not None:
            if megnyomott_gomb == arcade.key.A:
                if self.jatekos2.center_x > BAL_HATAR:
                    self.jatekos2.balra_lep(self.fal_lista)

            elif megnyomott_gomb == arcade.key.D:
                if self.jatekos2.center_x < JOBB_HATAR:
                    self.jatekos2.jobbra_lep(self.fal_lista)

            elif megnyomott_gomb == arcade.key.W:
                if self.jatekos2.center_y < FELSO_HATAR:
                    self.jatekos2.felfele_lep(self.fal_lista)

            elif megnyomott_gomb == arcade.key.S:
                if self.jatekos2.center_y > ALSO_HATAR:
                    self.jatekos2.lefele_lep(self.fal_lista)

    def jelenitsd_meg_a_hatteret(self):
        arcade.draw_texture_rectangle(
            self.hatter_pozicio_x,
            self.hatter_pozicio_y,
            self.hatter_kep.width,
            self.hatter_kep.height,
            self.hatter_kep)

    def jelenitsd_meg_az_aranymennyiseget(self):
        arcade.draw_text(
            str(self.jatekos.arany),
            MEZO_MERET,
            KEP_MAGASSAG - 2 * MEZO_MERET,
            arcade.color.WHITE,
            30)

        if self.jatekos2 is not None:
            arcade.draw_text(
                str(self.jatekos2.arany),
                JOBB_HATAR,
                KEP_MAGASSAG - 2 * MEZO_MERET,
                arcade.color.WHITE,
                30)

    def eletek_kirajzolasa(self):
        self.eletero_lista = arcade.SpriteList()
        for i in range(self.jatekos.eletek):
            uj_elet_sprite = arcade.Sprite("img/heart.png")
            uj_elet_sprite.center_x = i * MEZO_MERET + MEZO_MERET / 2
            uj_elet_sprite.center_y = KEP_MAGASSAG - MEZO_MERET / 2
            self.eletero_lista.append(uj_elet_sprite)

        if self.jatekos2 is not None:
            self.eletero_lista2 = arcade.SpriteList()
            for i in range(self.jatekos2.eletek):
                uj_elet_sprite = arcade.Sprite("img/heart.png")
                uj_elet_sprite.center_x = JOBB_HATAR - (i * MEZO_MERET - MEZO_MERET)
                uj_elet_sprite.center_y = KEP_MAGASSAG - MEZO_MERET / 2
                self.eletero_lista2.append(uj_elet_sprite)


if __name__ == "__main__":
    jatek = LovagJatek()
    jatek.inditas()
