# Event Model

Version: 0.1


## Purpose

Represents a change or occurrence
inside CreativeOS.


## Event Structure

Event:

- id
- type
- timestamp
- source
- payload
- version


## Examples

ProjectCreated

ConceptGenerated

ContentCreated

ReviewCompleted

ApprovalGranted


## Rules

Events are immutable.

Events represent facts,
not commands.