\c city_comparison ; 
CREATE TABLE salary (
    salary_id SERIAL PRIMARY KEY,
    Year VARCHAR(10) NOT NULL,
    Monthly_Salary INT CHECK (Monthly_Salary > 0),
    Annual_Salary INT CHECK (Annual_Salary>0),
    city_id INT REFERENCES city_comparison(city_id)
);

INSERT INTO salary (Year, Monthly_Salary, Annual_Salary, city_id)
SELECT 
    cc.Year,
    cc.Average_Monthly_Salary_Net AS Monthly_Salary,
    cc.Average_Monthly_Salary_Net * 12 AS Annual_Salary,
    cc.city_id
FROM city_comparison cc;
