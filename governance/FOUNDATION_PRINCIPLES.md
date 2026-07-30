# CreativeOS Foundation Principles

Version: 0.1

## Purpose

This document defines the fundamental principles
that govern the architecture of CreativeOS.

SongwriterOS is the first application built on top
of this foundation.

---

# Principle 1: Core First

The Core must never depend on applications.

Core provides reusable capabilities.

Applications consume Core services.

---

# Principle 2: Domain Driven Design

The system is organized by business domains,
not technical layers.

Examples:

- Writing
- Knowledge
- Emotion
- Evaluation
- Workflow

---

# Principle 3: Provider Independence

The Core must not depend on external vendors.

AI providers, databases, and external services
must connect through adapters.

---

# Principle 4: Knowledge and Rules Separation

Knowledge represents information.

Rules represent decisions and evaluation logic.

They must evolve independently.

---

# Principle 5: AI Is A Capability Provider

AI generates possibilities.

The system evaluates,
and humans make final creative decisions.

---

# Principle 6: Everything Has Version

The following must support versioning:

- Prompt
- Agent
- Rule
- Workflow
- Knowledge
- Generated Content

---

# Principle 7: Explainability

Every important decision should provide:

- Result
- Reason
- Evidence
- Confidence

---

# Principle 8: Plugin Architecture

New capabilities should be added through plugins,
not by modifying the Core.

---

# Principle 9: Human Creative Authority

Creative ownership always belongs to humans.

AI enhances creativity.

AI does not replace creativity.

---

# Principle 10: Long Term Compatibility

Architecture decisions must consider future systems:

- NovelOS
- ScreenplayOS
- MovieOS
- ArticleOS
- KnowledgeOS