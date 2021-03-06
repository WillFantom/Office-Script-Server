-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
  admin BIT NOT NULL
);

CREATE TABLE list (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  uid INTEGER NOT NULL,
  added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  uri TEXT NOT NULL,
  FOREIGN KEY (uid) REFERENCES user (id)
);