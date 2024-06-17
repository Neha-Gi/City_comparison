\c city_comparison ; 
CREATE TABLE currencies (
    Currency_ID SERIAL PRIMARY KEY,
    Currency VARCHAR(10) NOT NULL
    
);

INSERT INTO currencies (Currency)
VALUES
    ('Euro'),
    ('INR');
