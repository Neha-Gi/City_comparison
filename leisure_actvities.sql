\c city_comparison ; 
CREATE TABLE leisure_activities (
    Activity_id SERIAL PRIMARY KEY,
    Leisure_Activity VARCHAR(100),
    Cost_per_activity INT CHECK (Cost_per_activity >= 0),
    salary_id INT REFERENCES salary(salary_id),
    city_id INT REFERENCES city_comparison(city_id),
    year VARCHAR(10) NOT NULL
);

INSERT INTO leisure_activities (Leisure_Activity, Cost_per_activity, salary_id, city_id, year)
SELECT 
    la.Leisure_Activity,
    la.Cost_per_activity,
    s.salary_id,
    cc.city_id,
    la.year
FROM (
    VALUES
        ('Gym Membership', 10, 'Pune', '2023'),
        ('Gym Membership', 25, 'Berlin', '2023'),
        ('Movie Night', 10, 'Pune', '2023'),
        ('Movie Night', 15, 'Berlin', '2023'),
        ('Dining Out', 15, 'Pune', '2023'),
        ('Dining Out', 20, 'Berlin', '2023'),
        ('Boating and kayaking', 20, 'Pune', '2023'),
        ('Boating and Kayaking', 25, 'Berlin', '2023')
) AS la (Leisure_Activity, Cost_per_activity, City_name, year)
JOIN salary s ON s.year = la.year
JOIN city_comparison cc ON cc.City_name = la.City_name AND cc.Year = la.year;


