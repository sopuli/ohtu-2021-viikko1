import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_liikaa(self):

        self.varasto.ota_varastosta(15)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_nollasaldo1(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_nollasaldo2(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_saldojen_summat(self):
        self.varasto.lisaa_varastoon(8)

        laskettu_saldo = self.varasto.saldo + self.varasto.paljonko_mahtuu()

        self.assertAlmostEqual(laskettu_saldo, 10)

    def test_nollasaldo3(self):
        self.varasto = Varasto(10, alku_saldo=-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_nollavarasto(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    #def __str__(self):
        #return f"{self.varasto.saldo}" ????



    


