-- SongwriterOS Database Schema
-- Version 0.1.0

CREATE TABLE projects (

    id TEXT PRIMARY KEY,

    title TEXT NOT NULL,

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

    id TEXT PRIMARY KEY,

    project_id TEXT,

    style_id TEXT,

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

    id TEXT PRIMARY KEY,

    song_id TEXT,

    content TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

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

CREATE TABLE works (

    id TEXT PRIMARY KEY,

    project_id TEXT,

    title TEXT NOT NULL,

    work_type TEXT,

    content TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(project_id)
    REFERENCES projects(id)

);