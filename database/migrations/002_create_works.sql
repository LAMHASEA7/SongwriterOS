-- Migration: Create creative works table
-- Version: 002


CREATE TABLE works (

    id TEXT PRIMARY KEY,

    title TEXT NOT NULL,

    work_type TEXT,

    content TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);