import json
import psycopg as pg

CONN = pg.connect(user="postgres", password="postgres", dbname="city_comparison")


# CREATE
def insert_data(
    Year,
    City_name,
    Cost_of_Living_Monthly,
    Average_monthly_Salary_Net,
    Education_Quality_percent,
    Safety_percent,
    Public_Transport_Monthly_Pass,
    Weather,
):
    """Insert new data of the city"""
    Weather_json = json.dumps(Weather)
    insert_query = """
    INSERT INTO city_comparison (Year, City_name, Cost_of_Living_Monthly, Average_Monthly_Salary_Net, Education_Quality_percent, Safety_percent, Public_Transport_Monthly_Pass, Weather)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    with CONN.cursor() as cursor:
        cursor.execute(
            insert_query,
            (
                Year,
                City_name,
                Cost_of_Living_Monthly,
                Average_monthly_Salary_Net,
                Education_Quality_percent,
                Safety_percent,
                Public_Transport_Monthly_Pass,
                Weather_json,
            ),
        )

        print(f"\nInserted successfully|{insert_query}")
        CONN.commit()


# READ
def get_city_name():
    """fetch all cities"""
    city_name_query = """SELECT DISTINCT city_name FROM city_comparison

"""
    with CONN.cursor() as cursor:
        cursor.execute(city_name_query)
        city_names = cursor.fetchall()
        print(f"\nThis data has comparitive data from following cities:")
        for city in city_names:
            print(city[0])
        print()
        CONN.commit()


# UPDATE
def update_city(city_id,leisure_activity,cost_per_activity):
    """Update a specific row of a city."""
    update_query = """UPDATE leisure_activities 
                    SET cost_per_activity = %s 
                    WHERE city_id = %s AND leisure_activity = %s;"""
    with CONN.cursor() as cursor:
        cursor.execute(update_query, (cost_per_activity,city_id,leisure_activity))
        CONN.commit()
        print(f"Updated cost per activity to {cost_per_activity} for city_id {city_id} and leisure_activity {leisure_activity}")


# DELETE
def delete_city(city_id):
    """Delete a city by its ID."""
    delete_query = "DELETE FROM city_comparison WHERE city_id = %s;"
    with CONN.cursor() as cursor:
        cursor.execute(delete_query, (city_id,))
        print(f"Deleted row from city_id : {city_id}")
        CONN.commit()


# Aggregation
def fetch_highest_avg_monthly_salary_net():
    """fetch highest avg monthly salary"""
    highest_avg_mnthly_salary_query = """SELECT MAX(Average_Monthly_Salary_Net) 
    FROM city_comparison """

    highest_salary_city_query = """SELECT city_name FROM city_comparison WHERE Average_Monthly_Salary_Net =
    (SELECT MAX(Average_Monthly_Salary_Net) FROM city_comparison);"""

    with CONN.cursor() as cursor:
        cursor.execute(highest_avg_mnthly_salary_query)
        highest_avg_salary = cursor.fetchone()[0]
        cursor.execute(highest_salary_city_query)
        highest_salary_cities = cursor.fetchone()[0]
    print(
        f"\nHighest monthly average salary is {highest_avg_salary} EURO from {highest_salary_cities} city\n"
    )
    CONN.commit()

#JOIN
def other_expenses_with_salary():
    """Join the tables for expenses and salary"""
    city_id = int(input("Enter City ID to filter by: ")) 
    join_query = """
    SELECT s.salary_id, s.monthly_salary, l.leisure_activity, l.cost_per_activity, s.city_id, c.city_name
    FROM salary s
    JOIN leisure_activities l ON s.salary_id = l.salary_id AND s.city_id = l.city_id
    JOIN city_comparison c ON s.city_id = c.city_id
    WHERE s.city_id = %s; ;
    """
    with CONN.cursor() as cursor:
        cursor.execute(join_query,(city_id,))
        join_data = cursor.fetchall()
        print("Leisure Activities with monthly salary:")
        print(join_data)
        #for row in join_data:
         #   print(row)
