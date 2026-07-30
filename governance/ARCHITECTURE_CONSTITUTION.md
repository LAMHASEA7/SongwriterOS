# Architecture Constitution

Version: 0.1

---

# System Vision

CreativeOS is a modular creative platform.

SongwriterOS is the first reference application.

---

# Architecture Model


Application Layer

↓

Core Platform

↓

Ports

↓

Adapters

↓

External Providers


---

# Core Rules

## Rule 1

Core cannot import application code.

## Rule 2

Domain logic cannot depend on infrastructure.

## Rule 3

External providers communicate only through adapters.

## Rule 4

Business decisions must not exist in UI.

## Rule 5

Data ownership must be clearly separated.

---

# Control Plane

Responsible for:

- Workflow decisions
- Agent selection
- Provider selection
- Rule selection


# Execution Plane

Responsible for:

- Generation
- Analysis
- Storage
- Processing

---

# Change Management

Major architectural changes require:

- Documentation
- Decision Record
- Impact Analysis