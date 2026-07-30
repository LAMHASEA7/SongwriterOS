-- SongwriterOS Seed Data
-- Version 0.1.0


-- Projects

INSERT INTO projects
(name, description)
VALUES
(
'AI Rock Album 2026',
'Collection of AI assisted rock songs'
);



-- Styles

INSERT INTO styles
(name, description, tempo, instruments)
VALUES

(
'Modern Hard Rock',
'Heavy guitar driven emotional rock',
148,
'Electric Guitar, Bass, Live Drums'
),

(
'Alternative Rock',
'2000s emotional alternative rock',
120,
'Guitar, Bass, Drums, Piano'
),

(
'Cinematic Rock',
'Epic emotional soundtrack rock',
110,
'Orchestra, Guitar, Piano'
);



-- AI Agents

INSERT INTO ai_agents
(name, responsibility)
VALUES

(
'Concept Agent',
'Create song concepts and stories'
),

(
'Lyric Writer Agent',
'Write lyrics with emotion and structure'
),

(
'Rhyme Checker Agent',
'Analyze rhyme and word flow'
),

(
'Melody Critic Agent',
'Analyze melody smoothness'
),

(
'Style Director Agent',
'Design music style and production'
);



-- Song

INSERT INTO songs
(
project_id,
style_id,
title,
genre,
status
)
VALUES
(
1,
1,
'ทลายกรอบ',
'Modern Hard Rock',
'Draft'
);