# simple-blockchain-python

A small blockchain written from scratch in Python, built to learn how the core ideas work.

## What it does
- **Blocks** store data, a timestamp, the previous block's hash and a nonce.
- **SHA-256 hashing** links each block to the one before it.
- **Proof-of-work**: a block is mined by finding a nonce whose hash starts with a set number of zeros.
- **Validation**: `is_valid()` detects tampered data, broken links and missing proof-of-work.

## Run it
Requires Python 3.8+ and no external packages.

```bash
python demo.py
python -m unittest -v
```

The demo builds a chain, shows it is valid, edits one block, and shows the chain becomes invalid.

## What I learned
- Changing any block changes its hash, which breaks every later block's link.
- Proof-of-work makes rewriting history expensive because each block must be re-mined.

## Limitations
This is a learning project. It has no networking, no consensus between nodes, no digital signatures and no transactions model.

## Ideas for next steps
- Add transactions with public-key signatures.
- Simulate several nodes with the longest-chain rule.
