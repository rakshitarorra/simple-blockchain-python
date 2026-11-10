from blockchain import Blockchain


def show(chain):
    for b in chain.chain:
        print(f"Block {b.index} | nonce={b.nonce} | hash={b.hash[:16]}... | data={b.data}")


if __name__ == "__main__":
    bc = Blockchain(difficulty=4)
    bc.add_block("Alice pays Bob 5")
    bc.add_block("Bob pays Carol 2")
    show(bc)
    print("Valid chain?", bc.is_valid())

    print("\nTampering with block 1...")
    bc.chain[1].data = "Alice pays Bob 500"
    print("Valid chain?", bc.is_valid())
