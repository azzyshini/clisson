/*User type data*/
insert into user_types (user_type) values ('student');
insert into user_types (user_type) values ('teacher');

/* Users Table data*/
insert into users (email, username, first_name, last_name, password, user_type_id) values ('parkjimin@clisson.com', 'gotjams', 'Jimin', 'Park', 'bangtan7', 1);
insert into users (email, username, first_name, last_name, password, user_type_id) values ('jeonjungkook@clisson.com', 'musclepig', 'Jungkook', 'Jeon', 'bangtan7', 1);
insert into users (email, username, first_name, last_name, password, user_type_id) values ('kimnamjoon@clisson.com', 'pinkmon', 'Namjoon', 'Kim', 'bangtan7', 2);
insert into users (email, username, first_name, last_name, password, user_type_id) values ('kimseokjin@clisson.com', 'worldwidehandsome', 'Seokjin', 'Kim', 'bangtan7', 2); 

/* Books Table data*/ 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Moby Dick','Herman Melville',1,'0679602909','1851-11-14'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('A Midsummer Night\'s Dream','William Shakespeare',2,'0553213008','1600-01-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Gulliver\'s Travels','Jonathan Swift',2,'0486292738','1726-10-28'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Alice\'s Adventure in Wonderland','Lewis Carroll',2,'0486275434','1865-11-26'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Divine Comedy','Dante Alighieri',2,'0142437220','1555-01-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Don Quixote','Miguel de Cervantes',2,'039397281X','1620-01-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Adventures of Huckleberry Finn','Mark Twain',2,'0486280616','1884-12-10'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('The Three Musketeers','Alexandre Dumas',2,'1849907498','1844-07-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Frankenstein','Mary Shelley',2,'0486282112','1818-01-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Pride and Prejudice','Jane Austen',2,'0393264882','1813-01-28'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Sense and Sensibility','Jane Austen',2,'039397775X','1811-01-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('Philosophiae Naturalis Principia Mathematica','Isaac Newton',1,'1307962403','1728-01-01'); 
insert into books (title, author_name, number_of_copies, isbn, published_date) values ('The Social Contract','Jean-Jacques Rousseau',1,'0140442014','1762-01-01');    

/* Genre Tables data*/ 
insert into genre (genre_type) values ('Non-Fiction'); 
insert into genre (genre_type) values ('Fiction');
insert into genre (genre_type) values ('Fantasy');
insert into genre (genre_type) values ('Poem');
insert into genre (genre_type) values ('Epic');
insert into genre (genre_type) values ('Play');
insert into genre (genre_type) values ('Romance');
insert into genre (genre_type) values ('Mystery');
insert into genre (genre_type) values ('Satire');
insert into genre (genre_type) values ('Adventure');
insert into genre (genre_type) values ('Comedy');
insert into genre (genre_type) values ('Picaresque');
insert into genre (genre_type) values ('Historical');
insert into genre (genre_type) values ('Gothic');
insert into genre (genre_type) values ('Horror');
insert into genre (genre_type) values ('Sci-fi');

/* Books Genre data*/ 
insert into book_genre (book_id, genre_id) values(1,2);
insert into book_genre (book_id, genre_id) values(1,9); 
insert into book_genre (book_id, genre_id) values(1,5); 
insert into book_genre (book_id, genre_id) values(2,2); 
insert into book_genre (book_id, genre_id) values(2,3); 
insert into book_genre (book_id, genre_id) values(2,11); 
insert into book_genre (book_id, genre_id) values(2,6); 
insert into book_genre (book_id, genre_id) values(3,2); 
insert into book_genre (book_id, genre_id) values(3,3); 
insert into book_genre (book_id, genre_id) values(3,9); 
insert into book_genre (book_id, genre_id) values(3,10); 
insert into book_genre (book_id, genre_id) values(4,2); 
insert into book_genre (book_id, genre_id) values(4,3); 
insert into book_genre (book_id, genre_id) values(5,4); 
insert into book_genre (book_id, genre_id) values(5,10); 
insert into book_genre (book_id, genre_id) values(5,2); 
insert into book_genre (book_id, genre_id) values(6,2); 
insert into book_genre (book_id, genre_id) values(6,9); 
insert into book_genre (book_id, genre_id) values(6,10); 
insert into book_genre (book_id, genre_id) values(7,2); 
insert into book_genre (book_id, genre_id) values(7,12); 
insert into book_genre (book_id, genre_id) values(7,9); 
insert into book_genre (book_id, genre_id) values(8,2); 
insert into book_genre (book_id, genre_id) values(8,10); 
insert into book_genre (book_id, genre_id) values(8,13); 
insert into book_genre (book_id, genre_id) values(9,2); 
insert into book_genre (book_id, genre_id) values(9,15); 
insert into book_genre (book_id, genre_id) values(9,14); 
insert into book_genre (book_id, genre_id) values(9,16); 
insert into book_genre (book_id, genre_id) values(10,2); 
insert into book_genre (book_id, genre_id) values(10,11); 
insert into book_genre (book_id, genre_id) values(10,7);
insert into book_genre (book_id, genre_id) values(11,2);
insert into book_genre (book_id, genre_id) values(11,7);
insert into book_genre (book_id, genre_id) values(11,9);
insert into book_genre (book_id, genre_id) values(12,1);
insert into book_genre (book_id, genre_id) values(13,1);
