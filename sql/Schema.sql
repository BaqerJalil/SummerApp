CREATE TABLE Users (

    user_id SERIAL PRIMARY KEY,

    username VARCHAR(50) NOT NULL,

     VARCHAR(100) UNIQUE NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


CREATE TABLE Restaurants (

    restaurant_id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    latitude DECIMAL(9,6),

    longitude DECIMAL(9,6),

    rating DECIMAL(2,1),

    tags TEXT[],

    address TEXT

);


CREATE TABLE Events (

    event_id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    start_time TIMESTAMP,

    end_time TIMESTAMP,

    venue TEXT,

    latitude DECIMAL(9,6),

    longitude DECIMAL(9,6),

    tags TEXT[],

    organizer TEXT,

    source VARCHAR(50)

);


CREATE TABLE Attractions (

    attraction_id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    description TEXT,

    latitude DECIMAL(9,6),

    longitude DECIMAL(9,6),

    rating DECIMAL(2,1),

    tags TEXT[]

);


-- Bookmark Join Tables

CREATE TABLE user_restaurant_bookmarks (

    user_id INT REFERENCES Users(user_id),

    restaurant_id INT REFERENCES Restaurants(restaurant_id),

    PRIMARY KEY(user_id, restaurant_id)

);


CREATE TABLE user_event_bookmarks (

    user_id INT REFERENCES Users(user_id),

    event_id INT REFERENCES Events(event_id),

    PRIMARY KEY(user_id, event_id)

);


CREATE TABLE user_attraction_bookmarks (

    user_id INT REFERENCES Users(user_id),

    attraction_id INT REFERENCES Attractions(attraction_id),

    PRIMARY KEY(user_id, attraction_id)

);
