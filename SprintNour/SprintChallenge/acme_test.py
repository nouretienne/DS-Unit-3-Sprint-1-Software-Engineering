import unittest
from acme import Product
from acme_report import generate_products, adj, name


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
    
    def test_product_explode(self):
        """Test Product Explode function on a glove"""
        self.assertEqual(BoxingGlove('Punchy the Third').explode(), "...it's a glove.")



if __name__ == '__main__':
    unittest.main()