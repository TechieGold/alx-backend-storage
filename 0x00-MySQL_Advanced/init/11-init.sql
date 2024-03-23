-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    SCORE INT DEFAULT 0,
    last_meeting DATE NULL
);

INSERT INTO students (name, SCORE) VALUES ("Gold", 199);
INSERT INTO students (name, SCORE) VALUES ("Praise", 119);
INSERT INTO students (name, SCORE) VALUES ("Jean", 60);
INSERT INTO students (name, SCORE) VALUES ("steeve", 59);
INSERT INTO students (name, SCORE) VALUES ("Camilia", 80);
INSERT INTO students (name, SCORE) VALUES ("Alexa", 40);