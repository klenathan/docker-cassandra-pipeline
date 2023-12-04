CREATE TABLE weatherreport (
  forecastdate TIMESTAMP,
  location TEXT,
  description TEXT,
  temp FLOAT,
  feels_like FLOAT,
  temp_min FLOAT,
  temp_max FLOAT,
  pressure FLOAT,
  humidity FLOAT,
  wind FLOAT,
  sunrise BIGINT,
  sunset BIGINT,
  PRIMARY KEY (location, forecastdate)
);

CREATE TABLE IF NOT EXISTS fakerdata (
  name TEXT,
  address TEXT,
  year INT,
  email TEXT,
  job TEXT,
  date_of_birth TEXT,
  phone TEXT,
  origin TEXT,
  credit_card_num TEXT,
  credit_card_provider TEXT,
  credit_card_expire TEXT,
  PRIMARY KEY (name, address)
);

CREATE TABLE IF NOT EXISTS fakerdata (
  name TEXT,
  address TEXT,
  year INT,
  email TEXT,
  job TEXT,
  date_of_birth TEXT,
  phone TEXT,
  origin TEXT,
  credit_card_num TEXT,
  credit_card_provider TEXT,
  credit_card_expire TEXT,
  PRIMARY KEY (name, address)
);

CREATE TABLE IF NOT EXISTS aqi (
    location TEXT,
    aqi FLOAT,
    time TIMESTAMP,
    PRIMARY KEY (location, time)
);