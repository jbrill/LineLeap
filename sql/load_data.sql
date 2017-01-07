INSERT INTO User (username, firstname, lastname, password, email)
VALUES ('sportslover', 'Paul', 'Walker', 'sha512$69811fbb9f7b48dbbf47ff282e162982$cf0ccc6d30270a8a77d97f795520511e005857b748bb97761609376d6eab6ea500407353628d11f0ead82070f76508b507141a800e1a1fcba4ab77f22540cb28', 'sportslover@hotmail.com'),
	('traveler', 'Rebecca', 'Travolta', 'sha512$3bbeed5c20dc4e2b94fc0ada560faf8c$50853e54458b5f868acbcea886e133d3d9f8761c340baf945006973b605dcaa4247c43902d68199ae94ad0d8f34a3abb7366bf8879035ed0ad47d0527bb3a2e1', 'rebt@explorer.org'),
	('spacejunkie', 'Bob', 'Spacey', 'sha512$25ec31eb382e4ed8bd55593dfd945a54$fa50fae5a286eaf514bdf330c231b984a5237348d45cf9032bf25106dc907dd053ad55336a1e816bbe62d83e4b3130f7aeb6acea9a17a05b5f17ea95f6ac483e', 'bspace@spacejunkies.net');

INSERT INTO Album (title, created, lastupdated, username, access)
VALUES ("I love sports", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "sportslover", 'public'),
	("I love football", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "sportslover", 'private'),
	("Around The World", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "traveler", 'public'),
	("Cool Space Shots", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "spacejunkie", 'private');


INSERT INTO Photo (picid, format) VALUES ("001025dd643b0eb0661e359de86e3ea9","jpg");
INSERT INTO Photo (picid, format) VALUES ("9a0a7d25af4f7a73f67dde74e8e54cff","jpg");
INSERT INTO Photo (picid, format) VALUES ("c8e60100f13ffe374d59e39dc4b6a318","jpg");
INSERT INTO Photo (picid, format) VALUES ("5e8b6207f007338243d3e29d6b82acab","jpg");
INSERT INTO Photo (picid, format) VALUES ("4ddba6e2f905e9778c6b6a48b6fc8e03","jpg");
INSERT INTO Photo (picid, format) VALUES ("09d8a979fa638125b02ae1578eb943fa","jpg");
INSERT INTO Photo (picid, format) VALUES ("143ba34cb5c7e8f12420be1b576bda1a","jpg");
INSERT INTO Photo (picid, format) VALUES ("e615a10fc4222ede59ca3316c3fb751c","jpg");
INSERT INTO Photo (picid, format) VALUES ("65fb1e2aa4977d9414d1b3a7e4a3badd","jpg");
INSERT INTO Photo (picid, format) VALUES ("b94f256c23dec8a2c0da546849058d9e","jpg");
INSERT INTO Photo (picid, format) VALUES ("01e37cbdd55913df563f527860b364e8","jpg");
INSERT INTO Photo (picid, format) VALUES ("8d554cd1d8bb7b49ca798381d1fc171b","jpg");
INSERT INTO Photo (picid, format) VALUES ("2e9e69e19342b98141789925e5f87f60","jpg");
INSERT INTO Photo (picid, format) VALUES ("298e8943ef1942159ef88be21c4619c9","jpg");
INSERT INTO Photo (picid, format) VALUES ("cefe45eaeaeb599256dda325c2e972da","jpg");
INSERT INTO Photo (picid, format) VALUES ("bf755d13bb78e1deb59ef66b6d5c6a70","jpg");
INSERT INTO Photo (picid, format) VALUES ("5f8d7957874f1303d8300e50f17e46d6","jpg");
INSERT INTO Photo (picid, format) VALUES ("bac4fca50bed35b9a5646f632bf4c2e8","jpg");
INSERT INTO Photo (picid, format) VALUES ("f5b57bd7a2c962c54d55b5ddece37158","jpg");
INSERT INTO Photo (picid, format) VALUES ("b7d833dd3aae203ca618759fc6f4fc01","jpg");
INSERT INTO Photo (picid, format) VALUES ("faa20c04097d40cb10793a19246f2754","jpg");
INSERT INTO Photo (picid, format) VALUES ("aaaadd578c78d21defaa73e7d1f08235","jpg");
INSERT INTO Photo (picid, format) VALUES ("adb5c3af19664129141268feda90a275","jpg");
INSERT INTO Photo (picid, format) VALUES ("abf97ffd1f964f42790fb358e5258e8d","jpg");
INSERT INTO Photo (picid, format) VALUES ("ea2db8b970671856e43dd011d7df5fad","jpg");
INSERT INTO Photo (picid, format) VALUES ("76d79b81b9073a2323f0790965b00a68","jpg");
INSERT INTO Photo (picid, format) VALUES ("6510a4add59ef655ae3f0b6cdb24e140","jpg");
INSERT INTO Photo (picid, format) VALUES ("28d38afca913a728b2a6bcf01aa011cd","jpg");
INSERT INTO Photo (picid, format) VALUES ("5fb04eb11cbf99429a05c12ce2f50615","jpg");
INSERT INTO Photo (picid, format) VALUES ("39ee267d13ccd32b50c1de7c2ece54d6","jpg");

INSERT INTO Contain (sequencenum, albumid, picid)
VALUES (0, 2, "001025dd643b0eb0661e359de86e3ea9"),
(1, 2, "9a0a7d25af4f7a73f67dde74e8e54cff"),
(2, 2, "c8e60100f13ffe374d59e39dc4b6a318"),
(3, 2, "5e8b6207f007338243d3e29d6b82acab"),
(4, 4, "4ddba6e2f905e9778c6b6a48b6fc8e03"),
(5, 4, "09d8a979fa638125b02ae1578eb943fa"),
(6, 4, "143ba34cb5c7e8f12420be1b576bda1a"),
(7, 4, "e615a10fc4222ede59ca3316c3fb751c"),
(8, 4, "65fb1e2aa4977d9414d1b3a7e4a3badd"),
(9, 1, "b94f256c23dec8a2c0da546849058d9e"),
(10, 1, "01e37cbdd55913df563f527860b364e8"),
(11, 1, "8d554cd1d8bb7b49ca798381d1fc171b"),
(12, 1, "2e9e69e19342b98141789925e5f87f60"),
(13, 1, "298e8943ef1942159ef88be21c4619c9"),
(14, 1, "cefe45eaeaeb599256dda325c2e972da"),
(15, 1, "bf755d13bb78e1deb59ef66b6d5c6a70"),
(16, 1, "5f8d7957874f1303d8300e50f17e46d6"),
(17, 3, "bac4fca50bed35b9a5646f632bf4c2e8"),
(18, 3, "f5b57bd7a2c962c54d55b5ddece37158"),
(19, 3, "b7d833dd3aae203ca618759fc6f4fc01"),
(20, 3, "faa20c04097d40cb10793a19246f2754"),
(21, 3, "aaaadd578c78d21defaa73e7d1f08235"),
(22, 3, "adb5c3af19664129141268feda90a275"),
(23, 3, "abf97ffd1f964f42790fb358e5258e8d"),
(24, 3, "ea2db8b970671856e43dd011d7df5fad"),
(25, 3, "76d79b81b9073a2323f0790965b00a68"),
(26, 3, "6510a4add59ef655ae3f0b6cdb24e140"),
(27, 3, "28d38afca913a728b2a6bcf01aa011cd"),
(28, 3, "5fb04eb11cbf99429a05c12ce2f50615"),
(29, 3, "39ee267d13ccd32b50c1de7c2ece54d6");
