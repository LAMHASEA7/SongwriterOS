-- Migration: Change projects table to support Domain UUID identity
-- Version: 001

PRAGMA foreign_keys = OFF;


BEGIN TRANSACTION;


CREATE TABLE projects_new (

    id TEXT PRIMARY KEY,

    title TEXT NOT NULL,

    project_type TEXT,

    status TEXT DEFAULT 'Draft',

    description TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);


INSERT INTO projects_new
(
    id,
    title,
    description,
    created_at
)
SELECT
    CAST(id AS TEXT),
    name,
    description,
    created_at
FROM projects;


DROP TABLE projects;


ALTER TABLE projects_new
RENAME TO projects;


COMMIT;


PRAGMA foreign_keys = ON;