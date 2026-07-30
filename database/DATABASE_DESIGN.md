# SongwriterOS Database Design

Version: 0.1.0

Status: Draft

---

# 1. Database Purpose

The database stores songwriting knowledge,
creative projects, AI processes,
and generated results.

---

# 2. Core Tables


## projects

Purpose:
Store songwriting projects.

Fields:

- id
- project_name
- description
- created_at


## songs

Purpose:
Store songs.

Fields:

- id
- project_id
- title
- genre
- style
- status
- created_at


## lyrics

Purpose:
Store lyric versions.

Fields:

- id
- song_id
- version
- content
- analysis_score


## styles

Purpose:
Store music style DNA.

Fields:

- id
- name
- description
- tempo
- instruments


## rhyme_rules

Purpose:
Store songwriting rules.

Fields:

- id
- rule_name
- description


## melody_patterns

Purpose:
Store melody structures.

Fields:

- id
- pattern_name
- description


## ai_agents

Purpose:
Store AI team definitions.

Fields:

- id
- agent_name
- responsibility


## prompts

Purpose:
Store prompt versions.

Fields:

- id
- agent_id
- prompt_text
- version