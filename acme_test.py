import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

PossibleNames=[]

for x in range (0, len(ADJECTIVES)):
    for y in range (0, len(NOUNS)):
        PossibleNames.append(ADJECTIVES[x] + " " + NOUNS[y])

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_weight(self):
        prod = Product("Test Product")
        self.assertEqual(prod.weight,20)
    def test_default_product_steability(self):
        prod =Product("Test Product")
        if self.price/self.weight < 0.5:
            self.assertEqual(self.steability, "Not so stealable...")

        elif self.price/self.weight >= 0.5 and self.price/self.weight < 1 :
            self.assertEqual(self.steability, "Kinda stealable")
        else:
            self.assertEqual(self.steability, "Very stealable")
    def test_default_product_explode (self):
        prod =Product("Test Product")
        if self.flammability*self.weight < 10:
            self.assertEqual(self.explode, "...fizzle")
        elif self.flammability*self.weight >=10 and self.flammability*self.weight < 50:
            self.assertEqual(self.explode, "...boom!")
        else:
            self.assertEqual(self.explode, "...BABOOM!!")
class AcmeProductTests(unittest.TestCase):
    def test_default_num_products(self):
        prod=generate_products()
        self.assertEqual(len(prod),30)
    def test_legal_names(self):
        prod = generate_products()
        names=[]
        for x in range (0, len(prod)):
            names.append(prod[x].name)
            self.assertIn(names, PossibleNames)
          




if __name__ == '__main__':
    unittest.main()
