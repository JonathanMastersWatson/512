# Why a Hash Is Used

A hash is a one-way cryptographic fingerprint of a document.

For 512, hashing serves one purpose only:
to prove that a specific text existed, unchanged, at a specific point
in time.

The ledger does not store the document.
It stores evidence of its existence.

Benefits of hashing:
- immutability without publication
- verifiability without trust
- global consistency
- zero ambiguity

If a single character of the document changes, the hash changes.

This property makes silent modification impossible.
