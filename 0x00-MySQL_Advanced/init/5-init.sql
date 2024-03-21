-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    valid_email BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("techie@gold.com", "techiegold");
INSERT INTO users (email, name, valid_email) VALUES ("lady@g.com", "ladyg", 1);
INSERT INTO users (email, name, valid_email) VALUES ("praise@felix.com", "praise", 1);