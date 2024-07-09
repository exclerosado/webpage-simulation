CREATE DATABASE pageview_simulation;

USE pageview_simulation;

CREATE TABLE web_page_logs(
    transaction_id INT(10) AUTO_INCREMENT PRIMARY KEY,
    clientID VARCHAR(64) NOT NULL,
    landing_page BOOLEAN NOT NULL,
    personal_data BOOLEAN NOT NULL,
    address_data BOOLEAN NOT NULL,
    payment_data BOOLEAN NOT NULL, 
    confirmation BOOLEAN NOT NULL,
    goal BOOLEAN NOT NULL,
    date_time DATETIME NOT NULL
);