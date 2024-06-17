import json
from city_comp_db import (
    insert_data,  # CREATE
    get_city_name,  # READ
    update_city,  # UPDATE
    delete_city,  # DELETE
    fetch_highest_avg_monthly_salary_net,  # AGGREGATION
    other_expenses_with_salary,  # JOIN
)


def main():
    while True:
        print("\nCity Comparison Database")
        print("1. Add City")
        print("2. View Cities")
        print("3. Update City data")
        print("4. Delete City")
        print("5. View Highest Average Monthly Salary City")
        print(
            "6. View Other expenses such as Leisure activities with average monthly salary"
        )
        print("7. Exit")
        # print("8.. View Safety percentage from all the cities")
        # print("9. View Education cost and cost of living for the year 2023 from all the cities")
        # print("10. View Currency details")

        choice = input("Enter your choice: ")

        if choice == "1":  # CREATE
            Year = input("Enter a year for which the data is to be entered : ")  # 2023
            City_name = input("Enter city name : ")  # Munich
            Cost_of_Living_Monthly = float(
                input("Enter Cost of living monthly : ")
            )  # 3000
            Average_monthly_Salary_Net = float(
                input("Enter average monthly salary in Euro : ")
            )  # 3500
            Education_Quality_percent = float(
                input("Enter quality of education percentage: ")
            )  # 94
            Safety_percent = float(input("Enter percentage of safety:"))  # 89
            Public_Transport_Monthly_Pass = float(
                input("Enter the cost of public transport per month : ")
            )  # 29
            Weather_data = input(
                'Enter min and max temperature throughout year as JSON (e.g., {"min": -2, "max": 30}): '
            )  # {"min":-10,"max":29}
            Weather = json.loads(Weather_data)
            insert_data(
                Year,
                City_name,
                Cost_of_Living_Monthly,
                Average_monthly_Salary_Net,
                Education_Quality_percent,
                Safety_percent,
                Public_Transport_Monthly_Pass,
                Weather,
            )

        elif choice == "2":  # READ
            get_city_name()
        elif choice == "3":  # UPDATE
            city_id = int(input("Enter city ID to update: "))  # input option(1 to 12)
            leisure_activity = input("Enter leisure activity: ")
            cost_per_activity = int(input("Enter the cost per activity: "))
            update_city(city_id, leisure_activity, cost_per_activity)
        elif choice == "4":  # DELETE
            city_id = int(input("Enter city ID to delete: "))
            delete_city(city_id)
        elif choice == "5":  # AGGREGATION
            fetch_highest_avg_monthly_salary_net()
        elif choice == "6":  # JOIN
            other_expenses_with_salary()  # input option(47 or 48)
        elif choice == "7":

            print("\n" + "*" * 50)
            print(" " * 10 + "THANK YOU FOR USING OUR DATABASE")
            print(" " * 15 + "\U0001F600   \U0001F600   \U0001F600")
            print("*" * 50 + "\n")

            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
