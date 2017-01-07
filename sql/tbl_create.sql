SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS Contain, Photo, Album, User, AlbumAccess;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE User
(
  username varchar(20) primary key,
  firstname varchar(20),
  lastname varchar(20),
  password varchar(256),
  email varchar(40)
);

CREATE TABLE Album
(
  albumid int NOT NULL primary key AUTO_INCREMENT,
  title varchar(50),
  created timestamp default CURRENT_TIMESTAMP,
  lastupdated timestamp default CURRENT_TIMESTAMP,
  username varchar(255),
  access ENUM('public', 'private'),
  FOREIGN KEY (username) REFERENCES User(username)
);

CREATE TABLE AlbumAccess
(
  albumid int,
  username varchar(255),
  FOREIGN KEY (albumid) REFERENCES Album(albumid),
  FOREIGN KEY (username) REFERENCES User(username)
);

CREATE TABLE Photo
(
  picid varchar(40) primary key,
  format char(3),
  date timestamp default CURRENT_TIMESTAMP
);

CREATE TABLE Contain
(
  sequencenum int primary key,
  albumid int,
  picid varchar(40),
  caption varchar(255) default "",
  FOREIGN KEY (albumid) REFERENCES Album(albumid),
  FOREIGN KEY (picid) REFERENCES Photo(picid)
);

# SHOW ENGINE INNODB STATUS
