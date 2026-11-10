import unittest

from blockchain import Blockchain


class BlockchainTests(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain(difficulty=2)
        self.bc.add_block("first")
        self.bc.add_block("second")

    def test_valid_chain(self):
        self.assertTrue(self.bc.is_valid())

    def test_blocks_are_linked(self):
        self.assertEqual(self.bc.chain[1].previous_hash, self.bc.chain[0].hash)
        self.assertEqual(self.bc.chain[2].previous_hash, self.bc.chain[1].hash)

    def test_proof_of_work(self):
        for block in self.bc.chain:
            self.assertTrue(block.hash.startswith("00"))

    def test_tampering_is_detected(self):
        self.bc.chain[1].data = "changed"
        self.assertFalse(self.bc.is_valid())

    def test_broken_link_is_detected(self):
        self.bc.chain[2].previous_hash = "0" * 64
        self.assertFalse(self.bc.is_valid())


if __name__ == "__main__":
    unittest.main()
