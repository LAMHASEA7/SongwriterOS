# Application Layer

Responsible for orchestrating user intentions.

## Responsibilities

- Handle Commands
- Execute Use Cases
- Coordinate Domain Logic
- Call Repository Ports

## Rules

Application layer must not depend on Infrastructure.

Flow:

Command
    |
Use Case
    |
Domain
    |
Repository Port