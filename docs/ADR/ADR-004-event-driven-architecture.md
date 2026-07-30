# ADR-004 Event Driven Architecture

Status: Accepted


## Decision

CreativeOS uses event-driven
communication between modules.


## Reason

The platform must support:

- Multiple applications
- Multiple agents
- Plugin expansion


## Benefits

- Loose coupling
- Better scalability
- Easier extension


## Consequence

Modules must publish and consume
events instead of direct calls.