create table word_collection(id INTEGER PRIMARY KEY AUTOINCREMENT, letter varchar(10), word varchar(100), meaning varchar(255));
create table users(id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(55), email varchar(100));
create table processed(id INTEGER PRIMARY KEY AUTOINCREMENT, word_id INTEGER, user_id INTEGER);