# importar o módulo unittest
import unittest
import utils

# Crear unha clase TestUtils que estenda de unittest.TestCase.
# Recoméndase usar nomes significativos para o nome da clase
class TestUtils(unittest.TestCase):
    def test_e_primo(self):
        self.assertFalse(utils.is_prime(4))
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertFalse(utils.is_prime(8))
        self.assertFalse(utils.is_prime(10))
        self.assertTrue(utils.is_prime(7))
        self.assertEqual(
        utils.is_prime(-3), "Os números negativos non están permitidos"
    )
    
if __name__ == "__main__":
unittest.main(