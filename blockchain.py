"""A minimal blockchain: hash-linked blocks, proof-of-work and chain validation."""

import hashlib
import json
import time


class Block:
    def __init__(self, index, data, previous_hash, timestamp=None, nonce=0):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = timestamp if timestamp is not None else time.time()
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """SHA-256 over every field of the block except the hash itself."""
        payload = json.dumps(
            {
                "index": self.index,
                "data": self.data,
                "previous_hash": self.previous_hash,
                "timestamp": self.timestamp,
                "nonce": self.nonce,
            },
            sort_keys=True,
        )
        return hashlib.sha256(payload.encode()).hexdigest()

    def mine(self, difficulty):
        """Proof-of-work: find a nonce so the hash starts with `difficulty` zeros."""
        prefix = "0" * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()


class Blockchain:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        genesis = Block(0, "Genesis Block", "0" * 64, timestamp=0)
        genesis.mine(difficulty)
        self.chain = [genesis]

    def add_block(self, data):
        previous = self.chain[-1]
        block = Block(previous.index + 1, data, previous.hash)
        block.mine(self.difficulty)
        self.chain.append(block)
        return block

    def is_valid(self):
        """Check every block's hash, proof-of-work and link to the previous block."""
        prefix = "0" * self.difficulty
        for i, block in enumerate(self.chain):
            if block.hash != block.compute_hash():
                return False
            if not block.hash.startswith(prefix):
                return False
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False
        return True
