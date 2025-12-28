PROMPTS — Interface Layer

This directory contains optional prompt interfaces for loading the 512 constraint kernel into AI workspaces.

These prompts do not define, modify, or extend the 512 kernel.
They exist solely to provide a clean, repeatable way to apply the kernel as a reasoning constraint.

Available modes:

- LOAD_512_KERNEL.md  
  Use when no external repository is available. Loads the kernel only.

- LOAD_512_REPOSITORY.md  
  Use when referencing the canonical text repository. Loads the kernel and binds interpretation to specific documents.

In all cases:
- The kernel text is authoritative.
- Implementations, infrastructure, and enforcement are out of scope.
- Prompts are optional and voluntary.

> Developer note: to locate repository URL bindings, search for the canonical URL string across prompt files.
