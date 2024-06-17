# City Comparison Database

## Mission Statement

To provide information to the people of Pune city to aid in making relocation decisions by offering a comprehensive data-driven comparison between Pune and Berlin, facilitating the identification of the best environment for growth and prosperity.

## Mission Objectives

- **Maintain Data of Two Cities**: Store and manage comprehensive data sets for Pune and Berlin, covering various aspects of city life.
  
- **Provide Estimated Cost of Living**: Offer yearly estimates of the cost of living in both cities, helping individuals assess financial feasibility.

- **Track Data Over Time**: Maintain historical records to track changes and trends in city metrics over time, allowing for informed decision-making.

- **Recommend Other Cities for Relocation**: Use comparative analysis to recommend alternative cities for relocation based on user preferences and criteria.

## Database Structure

The database consists of the following tables:

- **city_comparison**: Contains information about cities such as city_id, city_name, and other general details.
  
- **salary**: Stores data related to salaries, including salary_id, monthly_salary, and city_id.

- **leisure_activities**: Tracks leisure activities available in each city, including details like activity name, cost_per_activity, and city_id.

- **currency**: Provides currency details for each city, specifying the currency used (e.g., Euro).

- **education_cost**: Stores education-related costs for each city, including expenses like tuition fees and related costs.

## Usage

### Setting Up the Database

1. **Database Setup**: Ensure PostgreSQL is installed. Use the provided SQL scripts to create the database and tables.

```postgresql
\i city_comparison.sql
```
```postgresql
\i education_cost.sql
```
```postgresql
\i salary.sql
```
```postgresql
\i leisure_activities.sql
```
```postgresql
\i currency.sql
```


2.  **Run main**: Execute the Python script main.py to interact with the database and perform operations such as adding cities, viewing data, updating city information, and more.
   
   

```python
python3 src/main.py
```