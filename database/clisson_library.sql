CREATE DATABASE IF NOT EXISTS clisson_library CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE clisson_library;

CREATE TABLE IF NOT EXISTS user_types (
    id INT NOT NULL AUTO_INCREMENT,
    user_type VARCHAR(64) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(128) NOT NULL,
    username VARCHAR(128) NOT NULL,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    password VARCHAR(64) NOT NULL,
    user_type_id INT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE INDEX (email),
    INDEX user_type_id_idx (user_type_id),
    FOREIGN KEY (user_type_id) REFERENCES user_types(id)
) ENGINE=INNODB; 

CREATE TABLE IF NOT EXISTS books(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(128) NOT NULL,
    author_name VARCHAR(256) NOT NULL,
    number_of_copies INT NOT NULL, 
    isbn VARCHAR(32) NOT NULL, 
    book_cover MEDIUMBLOB,
    book_cover_mimetype VARCHAR(64),
    published_date DATETIME NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE INDEX (isbn)
) ENGINE=INNODB;  

CREATE TABLE IF NOT EXISTS genre(
    id INT NOT NULL AUTO_INCREMENT,
    genre_type VARCHAR(128) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (id)
) ENGINE=INNODB;  

CREATE TABLE IF NOT EXISTS holds(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id), 
    FOREIGN KEY (book_id) REFERENCES books(id)
) ENGINE=INNODB;  

CREATE TABLE IF NOT EXISTS checkouts(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    checkout_date DATETIME NOT NULL,
    due_date DATETIME NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id), 
    FOREIGN KEY (book_id) REFERENCES books(id)
) ENGINE=INNODB; 
 
CREATE TABLE IF NOT EXISTS book_genre(
    id INT NOT NULL AUTO_INCREMENT,
    book_id INT NOT NULL,
    genre_id INT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (genre_id) REFERENCES genre(id), 
    FOREIGN KEY (book_id) REFERENCES books(id)
) ENGINE=INNODB;  