CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venue_id INT,
    timestamp DATETIME,
    temperature FLOAT,
    relative_humidity FLOAT,
    dewpoint FLOAT,
    apparent_temperature FLOAT,
    precipitation FLOAT,
    rain FLOAT,
    showers FLOAT,
    snowfall FLOAT,
    snow_depth FLOAT,
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
