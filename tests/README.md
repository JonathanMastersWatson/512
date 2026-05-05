# Tests

This folder contains deterministic test cases for the 512 boundary.

## Purpose

- Validate correctness of constraint evaluation
- Ensure consistent ALLOW / DENY outcomes
- Prevent unintended behavior changes

## Principles

- Every test must be deterministic
- Every input must produce a single fixed output
- No randomness
- No external dependencies

## Structure

Each test should define:

- input (action, constraints, state)
- expected result (ALLOW or DENY)

## Goal

Given the same input, 512 must always return the same result.
