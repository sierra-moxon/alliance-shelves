

CREATE TABLE "Couch" (
	id TEXT, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	color VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id, name, description, image, color)
);

CREATE TABLE "KitchenTable" (
	id TEXT, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	color TEXT, 
	PRIMARY KEY (id, name, description, image, color)
);

CREATE TABLE "Shelf" (
	id TEXT, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	color TEXT, 
	height INTEGER, 
	width TEXT, 
	number_of_shelves TEXT, 
	PRIMARY KEY (id, name, description, image, color, height, width, number_of_shelves)
);
