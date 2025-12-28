# SPEC-HASH Schema

SPEC-HASH defines the minimum information required to anchor a document
under 512.

Required fields:
- Document identifier
- Hash algorithm
- Hash value
- UTC timestamp
- Reference to the genesis hash (if descendant)

Optional fields:
- Repository URL
- Commit identifier
- Human-readable notes

SPEC-HASH does not define:
- storage format
- transport protocol
- enforcement mechanism

Its sole function is to make lineage explicit and verifiable.
