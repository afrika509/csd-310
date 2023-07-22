-- drop test user if exists
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- drop constraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

/*
    insert book records 
*/
INSERT INTO book (book_name, author, details)
VALUES ('The Alchemist', 'Paulo Coelho', 'A philosophical novel about following your dreams');

INSERT INTO book (book_name, author, details)
VALUES ('To Kill a Mockingbird', 'Harper Lee', 'A classic American novel tackling themes of racial injustice');

INSERT INTO book (book_name, author, details)
VALUES ('1984', 'George Orwell', 'A dystopian novel depicting a totalitarian society');

INSERT INTO book (book_name, author, details)
VALUES ('Pride and Prejudice', 'Jane Austen', 'A romantic novel exploring themes of social class and prejudice');

INSERT INTO book (book_name, author, details)
VALUES ('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', 'A comedic science fiction series');

INSERT INTO book (book_name, author)
VALUES ('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book (book_name, author)
VALUES ('The Catcher in the Rye', 'J.D. Salinger');

INSERT INTO book (book_name, author)
VALUES ('To the Lighthouse', 'Virginia Woolf');

INSERT INTO book (book_name, author)
VALUES ('Moby-Dick', 'Herman Melville');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name)
VALUES ('Tracy','Atkins');

INSERT INTO user(first_name, last_name)
VALUES ('Frank','Sinatra');

INSERT INTO user(first_name, last_name)
VALUES ('Kelly','Rowland');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id)
VALUES (
    (SELECT user_id FROM user WHERE first_name = 'Tracy'),
    (SELECT book_id FROM book WHERE book_name = 'The Alchemist')
);

INSERT INTO wishlist(user_id, book_id)
VALUES (
    (SELECT user_id FROM user WHERE first_name = 'Frank'),
    (SELECT book_id FROM book WHERE book_name = '1984')
);

INSERT INTO wishlist(user_id, book_id)
VALUES (
    (SELECT user_id FROM user WHERE first_name = 'Kelly'),
    (SELECT book_id FROM book WHERE book_name = 'To Kill a Mockingbird')
);
