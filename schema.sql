-- CREATE TABLE IF NOT EXISTS products 
-- (
-- 	id INTEGER PRIMARY KEY,
-- 	is_customizable INTEGER NOT NULL,
-- 	delivery TEXT NOT NULL,
-- 	kids INTEGER NOT NULL,
-- 	name TEXT NOT NULL,
-- 	sizes TEXT NOT NULL,
-- 	kid_adult INTEGER NOT NULL,
-- 	free_porto INTEGER NOT NULL,
-- 	image TEXT NOT NULL,
-- 	package INTEGER NOT NULL,
-- 	price REAL NOT NULL,
-- 	url TEXT NOT NULL,
-- 	online INTEGER NOT NULL,
-- 	price_old REAL NOT NULL,
-- 	currency TEXT NOT NULL,
-- 	img_url TEXT NOT NULL,
-- 	women INTEGER NOT NULL 
-- );

CREATE TABLE IF NOT EXISTS products 
(
	id INTEGER PRIMARY KEY,
	is_customizable TEXT NOT NULL,
	delivery TEXT NOT NULL,
	kids TEXT NOT NULL,
	name TEXT NOT NULL,
	sizes TEXT NOT NULL,
	kid_adult TEXT NOT NULL,
	free_porto TEXT NOT NULL,
	image TEXT NOT NULL,
	package TEXT NOT NULL,
	price REAL NOT NULL,
	url TEXT NOT NULL,
	online TEXT NOT NULL,
	price_old REAL NOT NULL,
	currency TEXT NOT NULL,
	img_url TEXT NOT NULL,
	women TEXT NOT NULL 
);
