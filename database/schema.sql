-- SongwriterOS Database Schema
-- Version 0.1.0


CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE styles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    tempo INTEGER,
    instruments TEXT
);


CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    style_id INTEGER,
    title TEXT NOT NULL,
    genre TEXT,
    status TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(project_id)
    REFERENCES projects(id),

    FOREIGN KEY(style_id)
    REFERENCES styles(id)
);


CREATE TABLE lyrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER,
    version INTEGER,
    content TEXT,
    score REAL,

    FOREIGN KEY(song_id)
    REFERENCES songs(id)
);


CREATE TABLE ai_agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    responsibility TEXT
);


CREATE TABLE prompts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER,
    version TEXT,
    prompt_text TEXT,

    FOREIGN KEY(agent_id)
    REFERENCES ai_agents(id)
);