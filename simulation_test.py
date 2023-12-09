import unittest
from logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_log.txt"
        self.logger = Logger(self.log_file)

    def test_write_metadata(self):
        self.logger.write_metadata(100000, 0.9, "Ebola", 0.7, 0.25)
        with open(self.log_file, 'r') as file:
            content = file.read()
            self.assertIn("Population Size: 100000", content)
            self.assertIn("Vaccination Percentage: 0.9", content)
            self.assertIn("Virus Name: Ebola", content)
            self.assertIn("Mortality Rate: 0.7", content)
            self.assertIn("Basic Reproduction Number: 0.25", content)

    def test_log_interactions(self):
        self.logger.log_interactions(1, 50, 5)
        with open(self.log_file, 'r') as file:
            content = file.read()
            self.assertIn("Step 1: Interactions - 50, New Infections - 5", content)

    def test_log_infection_survival(self):
        self.logger.log_infection_survival(1, 95000, 500)
        with open(self.log_file, 'r') as file:
            content = file.read()
            self.assertIn("Step 1: Population - 95000, New Fatalities - 500", content)

if __name__ == "__main__":
    unittest.main()

