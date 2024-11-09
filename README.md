Project Descriptions

MySQL-DataBridge

MySQL-DataBridge is a lightweight Python module designed to simplify MySQL database connections, database creation, and table management. With easy-to-use methods, you can streamline interactions with MySQL databases in your projects.

## Installation

To install MySQL-DataBridge, use the following command:

```bash

pip install MySQL-DataBridge

```

Follow these steps to get started with MySQL-DataBridge:

# Import the Module

```python

from MySQL-DataBridge import MySQLModule

```

# Initialize the Module

Create an instance of the MySQLModule class, providing your MySQL hostname, username, and password:

```python

db = MySQLModule(hostname="localhost", username="root", password="your_password")

```

# Connect to the MySQL Server

Establish a connection to your MySQL server:

```python

connection = db.connect_to_database()

```

# Create a New Database

Use the create_database method to create a new database:

```python

db.create_database("your_database_name")

```

# Set the Database and Reconnect

After creating or selecting a database, specify it and reconnect:

```python

db.database = "your_database_name_here" 
db.connect_to_database()

```

    Replace 'your_database_name_here' with your database name

# Create a Table

Define a table schema using an SQL CREATE TABLE statement and use the create_table method to create it:

```python

create_my_table = """
CREATE TABLE IF NOT EXISTS your_table_name (
    # Replace with your table columns
    # Example:
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
"""

# Confirm the table name here as well
my_table_name = "your_table_name"

# Create the table
db.create_table(create_my_table, my_table_name)

```

## Important Notes

    Database Name: Replace "your_database_name_here" with the name of your desired database.
    Table Name: Replace "your_table_name" in both the CREATE TABLE statement and my_table_name variable.
    Columns: Customize the CREATE TABLE statement to include all columns and data types your table needs.


# Displaying All Databases

```python

databases = db.show_databases()
if databases:
    print("Databases:")
    for db_name in databases:
        print(db_name[0])

```

# Explanation:
   This code snippet calls the show_databases() method to retrieve a list of all databases available on the connected MySQL server. It checks if the result is not empty and then iterates through the list, printing each database name. Ensure that you have an active connection to the MySQL server before running this code.

# Connecting to the Database and Showing Tables

```python

if db.connect_to_database():
    print("Connected to the MySQL server successfully!")
    # Call the show_tables method to show tables in the selected database
    db.show_tables()  # This will prompt the user for the database name
else:
    print("Failed to connect to the MySQL server.")

```

# Explanation:
   This code first attempts to connect to the MySQL server using the connect_to_database() method. If the connection is successful, it prints a confirmation message and calls the show_tables() method, which will display the tables within the selected database. If the connection fails, an error message is displayed.

# Inserting Data Using String Methods

```python

table_name = "your_table_name_here"
columns = ["column_name_1", "column_name_2", "column_name_3", ...] 
values = ["value_1", "value_2", "value_3"]  
# Write float and integer values without double (") quotation marks, but separate by commas.

# Insert data with string methods (e.g., 'lower', 'upper', etc.)
db.insert_data_with_builtins_methods(table_name, columns, values)

```

# Explanation:
   This snippet demonstrates how to insert a single row of data into a specified table using string transformation methods (e.g., converting strings to lowercase or uppercase). Replace table_name, columns, and values with the appropriate table and data values for your database. Ensure that numeric data is written without quotation marks.

# Inserting Data Without String Transformations

```python

table_name = "your_table_name_here"
columns = ["column_name_1", "column_name_2", "column_name_3", ...] 
values = ["value_1", "value_2", "value_3"]  
# Write float and integer values without double (") quotation marks, but separate by commas.

# Insert the data
db.insert_data_only_with_builtins(table_name, columns, values)

```

# Explanation:

  This code shows how to insert a single row of data without applying any string methods. Replace table_name, columns, and values with your specific table and data. Ensure that numerical values are unquoted.

# Inserting Multiple Rows of Data

```python

table_name = "your_table_name_here"
# Write your column names below
columns = ["your_column_name_1", "your_column_name_2", "your_column_name_3", "your_column_name_4"] 
values_list = [
    ("your_value_1", "your_value_2", "your_value_3", "your_value_4"),
    ("your_value_1", "your_value_2", "your_value_3", "your_value_4"),
    # Add more rows as needed
]
# Write float and integer values without double (") quotation marks, but separate by commas.

# Insert multiple rows
db.insert_mul_val_data_without(table_name, columns, values_list)

```

# Explanation:

  This snippet inserts multiple rows of data into the specified table. Customize table_name, columns, and values_list with your data. This method is ideal for bulk inserts. Ensure that numeric data does not have quotation marks.
 
#  Inserting Multiple Rows with Error Handling

```python

table_name = "your_table_name_here"
# Write your column names below
columns = ["your_column_name_1", "your_column_name_2", "your_column_name_3", "your_column_name_4"] 
values_list = [
    ("your_value_1", "your_value_2", "your_value_3", "your_value_4"),
    ("your_value_1", "your_value_2", "your_value_3", "your_value_4"),
    # Add more rows as needed
]
# Write float and integer values without double (") quotation marks, but separate by commas.

# Insert data with error handling
try:
    db.insert_mul_val_data_with(table_name, columns, values_list)
except Exception as e:
    print(f"Error occurred while inserting data: {e}")

```

# Explanation:

  This example is similar to the previous one but includes error handling. The try-except block ensures that any issues during the data insertion process (e.g., database errors or constraint violations) are caught, and a descriptive error message is printed.

# Inserting Multiple Rows of Data with Set Operations

```python

table_name = "your_table_name_here"
# Write your column names below
columns = ["your_column_name_1", "your_column_name_2", "your_column_name_3", "your_column_name_4"] 
values_list = [
    ("your_value_1", "your_value_2", "your_value_3", "your_value_4"),
    ("your_value_1", "your_value_2", "your_value_3", "your_value_4"),
    # Add more rows as needed
]
# Write float and integer values without double (") quotation marks, but separate by commas.

# Insert the data with set operations
db.insert_mul_val_data_with(table_name, columns, values_list)

```

# Explanation:

    This code inserts multiple rows into a table using set operations. Replace table_name, columns, and values_list with your specific table name, column names, and data. Ensure numeric data types are entered without quotes.

# Selecting and Sorting Data

```python

db.select_and_sort_data("your_table_name_here", 3)  # Replace '3' with the column number or index you want to sort by.

```

# Explanation:

    This snippet calls the select_and_sort_data() method to retrieve and sort data from a specific table. Replace "your_table_name_here" with your table's name, and 3 with the appropriate column index for sorting.

# Printing Data as a List

```python

db.print_data_as_list_only("your_table_name_here")

```

# Explanation:

    The print_data_as_list_only() function prints the data from a specified table in a simple list format. Replace "your_table_name_here" with the name of your table to view its data.

# Applying List Methods to Print Data

```python

table_name = "your_table_name_here"
# Call the function to apply list methods
print("=== Applying List Methods ===")
db.print_data_as_list_with_M(table_name)

```

# Explanation:

    This function prints data from a table while applying list-specific methods for formatting or transformation. Replace table_name with your actual table name.

# Executing an Aggregate Query

```python

# Define your aggregate query

aggregate_query = "SELECT your_column_name_1, AVG(your_column_name_2) FROM your_table_name GROUP BY your_column_name_1"

# Execute the query using the aggregate_functions method
result = db.aggregate_functions(aggregate_query)

# Print the result
print(result)

```

# Explanation:

    Use this code to run aggregate queries, such as calculating averages or sums, grouped by specific columns. Replace your_column_name_1, your_column_name_2, and your_table_name with appropriate values from your database schema.

# Interactive MySQL Query Options

```python

# Don't change this code. Use it as you see and follow the explanation below the code.

while True:
    print("\n--- MySQL Query Options ---")
    print("1. Select with conditions")
    print("2. Select in a range")
    print("3. Select with LIKE")
    print("4. Round column values")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        table_name, column, condition, value = db.get_select_conditions_input()
        db.select_with_conditions_with_M(table_name, column, condition, value)

    elif choice == "2":
        table_name, column, start, end = db.get_select_in_range_input()
        db.select_in_range(table_name, column, start, end)

    elif choice == "3":
        table_name, column, pattern = db.get_select_with_like_input()
        db.select_with_like(table_name, column, pattern)

    elif choice == "4":
        table_name, column_name, decimal_places = db.get_round_column_values_input()
        db.round_column_values(table_name, column_name, decimal_places)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


```

# Explanation: 

    This interactive script provides users with options to perform various MySQL queries. Users can:

    Select with specific conditions.
    Select data within a specific range.
    Use LIKE to search for patterns.
    Round column values to a specified number of decimal places.

# Joining Two Tables

```python

table1 = 'your_table_1_name_here'
table2 = 'your_table_2_name_here'
join_condition = 'your_table_1_name_here.your_table_1_column_name = your_table_2_name_here.your_table_2_column_name'
columns1 = ['your_table_1_column_1', 'your_table_1_column_2', ...]

```

# Explanation:
     This snippet sets up a join between two tables based on a specified condition. Replace table1, table2, join_condition, and columns1 with your table names, join condition, and column names. Use this when combining data from multiple tables using an SQL JOIN operation.

# INNER JOIN

The join_tables() function can be used to perform an INNER JOIN, which retrieves only the rows where there is a match between the specified columns in both tables.

    Purpose: Returns only the rows that have matching values in both table1 and table2. Rows without matches are not included in the result.

# LEFT JOIN

The left_join_tables() function performs a LEFT JOIN, which returns all rows from table1 (left table) and matched rows from table2 (right table). Rows in table1 without a corresponding match in table2 will show NULL values for columns from table2.

    Purpose: Retrieves all rows from table1 and matched rows from table2. Non-matching rows from table2 will have NULL values.

# RIGHT JOIN
The right_join_tables() function performs a RIGHT JOIN, which returns all rows from table2 (right table) and matched rows from table1 (left table). Rows in table2 without a corresponding match in table1 will show NULL values for columns from table1.

    Purpose: Retrieves all rows from table2 and matched rows from table1. Non-matching rows from table1 will have NULL values.


## Note: 

     Make sure to replace placeholders like your_table_1_name_here, your_table_1_column_name, etc., with actual table and column names relevant to your database.


# DROP Table Operation

The drop_table() function is used to delete an entire table from the database. Use this function carefully, as dropping a table will remove all the data and its structure permanently.

```python

table_name_for_drop = 'your_table_here_to_drop'

# Perform DROP operation
db.drop_table(table_name_for_drop)

```

# Explanation:

     This snippet demonstrates how to drop a table from your database using the drop_table() function. Replace 'your_table_here_to_drop' with the name of the table you wish to remove. Use this when you need to delete an entire table from your database.

# Execute a Custom SELECT Query

The execute_query() function allows you to run a custom SQL query. This can be useful for retrieving specific data from your table.

```python

# Define your table name and query
table_name = "your_table_name"  # Replace with your table name
query = f"SELECT column1, column2, column3 FROM {table_name}"  # Replace with your columns

# Execute the custom query
db.execute_query(query)

```

# Explanation:

    This code is used for executing a custom SELECT query. Replace column1, column2, column3, and your_table_name with your desired columns and table name. This allows you to retrieve specific columns from a table.

# Complex Operations

The complex_operation() function performs advanced operations on the specified table. This could involve a series of custom operations or data transformations defined within the method.

```python

db.complex_operation(table_name)

```

# Explanation:

    The complex_operation() function is designed to execute complex SQL operations on a specified table. Replace table_name with the name of your table. This function is ideal for running pre-defined complex SQL tasks that involve multiple steps.

# SELECT with COALESCE

The select_with_coalesce() function is used to select values from a column, replacing any NULL values with a default value.

```python

# Define your table name, column name, and default value
table_name = "your_table_name"  
column_name = "your_column_name" 
default_value = "your_default_value" 

# Execute the query with COALESCE
db.select_with_coalesce(table_name, column_name, default_value)

```

# Explanation:
    
     This code block retrieves data from a specified column, using COALESCE to return a default value when NULL is encountered. Replace your_table_name, your_column_name, and your_default_value as needed.

# SELECT Distinct Values

The select_with_distinct() function retrieves distinct values from a specified column, eliminating duplicate results.

```python

# Define your table name and the column from which you want distinct values
table_name = "your_table_name"  
column_name_for_distinct = "your_column_name"  

# Execute the query to select distinct values
db.select_with_distinct(table_name, column_name_for_distinct)

```

# Explanation:
     This snippet fetches unique values from a specified column in a table. Replace your_table_name and your_column_name to customize it for your needs. Use this to eliminate duplicate entries in your query results.

# UPDATE Data in a Table

The update_data() function is used to update specific rows in a table based on a given condition.

```python

# Define your UPDATE query and the values you want to update
update_query = "UPDATE your_table_name SET your_column_name = %s WHERE your_id_column = %s"

# List of values to update (new values, identifier for the row)
values_list = [
    ("new_value_1", 1),  
    ("new_value_2", 2),  
    ("new_value_3", 3), 
]

# Execute the update query with the values
db.update_data(update_query, values_list)

```

# Explanation: 
    This code updates data in a specified table. Replace your_table_name, your_column_name, and your_id_column with the appropriate table and column names. The values_list specifies the new data and the row to update.

# Fetch All Data from a Table

The select_data() function is used to execute a SELECT query and print all the retrieved records.

```python

# Define your SELECT query to fetch all data from a specified table
select_query = "SELECT * FROM your_table_name"

# Execute the query and store the results
results = db.select_data(select_query)

# Iterate through the results and print each row
for row in results:
    print(row)

```

# Explanation:

    This snippet retrieves all rows and columns from a specified table. Replace your_table_name with the name of the table you want to query. The results are printed row by row.

# Concatenate Columns in a SELECT Query

The select_data() function can also be used to concatenate columns for formatted output, such as full names.

```python

# Define your SELECT query to concatenate first and last names into a single string
concat_query = "SELECT CONCAT('your_table_name_here: ', column_name_1, ' ', column_name_2) AS full_Name_here FROM your_table_name"

# Execute the query and store the results
results = db.select_data(concat_query)

# Iterate through the results and print each concatenated full name
for row in results:
    print(row[0])  # Access the first column from each row, which contains the concatenated result

```

# Explanation:
    
    This code uses the CONCAT function to merge columns into a single string. Replace your_table_name_here, column_name_1, and column_name_2 as needed. This is helpful for formatting full names or similar combinations.

# SELECT with Conditions

The select_data() function can be used to fetch data based on specific conditions.

```python

# Define your SELECT query with conditions to filter results
select_query = "SELECT * FROM your_table_name WHERE monthly_salary > your_salary_value OR age < your_age_value OR your_id_column = your_id_value"

# Execute the query and store the results
results = db.select_data(select_query)

# Iterate through the results and print each row
for row in results:
    print(row)  # Each row represents a record meeting the specified conditions

```

# Explanation:
    
    This code filters results based on specific conditions. Replace your_table_name, your_salary_value, your_age_value, and your_id_value with the actual table name and filter criteria. This is ideal for retrieving conditional data from your table.

# SELECT Query to Filter Names Starting with a Specific Letter

The select_data() function can be used to execute a query that retrieves rows where a specified column's values start with a particular letter.

```python

# Define your SELECT query to filter names starting with a specific letter
select_query = "SELECT * FROM your_table_name WHERE your_column_name LIKE 'B%'"

# Execute the query and store the results
results = db.select_data(select_query)

# Print each row matching the condition
for row in results:
    print(row)

```

Purpose: This code filters records in your_table_name where your_column_name starts with 'B'. This function is helpful for identifying and analyzing data with a specific pattern, such as customers or products whose names begin with a specific letter.

# SELECT Query to Filter Ages Within a Range

The select_data() function can be used to execute a query that retrieves rows where a column value falls within a specified range.

```python

# Define your SELECT query to filter ages within a range
select_query = "SELECT * FROM your_table_name WHERE age BETWEEN your_min_age AND your_max_age"

# Execute the query and store the results
results = db.select_data(select_query)

# Print each row that falls within the age range
for row in results:
    print(row)

```

Purpose: This code snippet selects records where the age column value is between your_min_age and your_max_age. It is useful for demographic analysis or filtering data based on specific age criteria.

# SELECT Query to Filter Specific Values

The select_data() function can be used to execute a query that retrieves rows where a column matches any value in a given list.

```python

# Define your SELECT query to filter specific names
select_query = "SELECT * FROM your_table_name WHERE your_column_name IN ('Value1', 'Value2')"

# Execute the query and store the results
results = db.select_data(select_query)

# Print each row matching one of the specified values
for row in results:
    print(row)

```

Purpose: This query helps select records where your_column_name matches any value in the specified list. It is ideal for filtering records for a set of known attributes or categories.

# UNION Query to Combine Results from Two Tables

The select_data() function can be used to execute a UNION query that combines the result sets of two SELECT statements.

```python

# Define a UNION query to combine results from two tables
union_query = """
SELECT your_table_1_column_1, your_table_1_column_2, your_table_1_column_3 FROM your_first_table
UNION
SELECT your_table_2_column_1, your_table_2_column_2, your_table_2_column_3 FROM your_second_table;
"""

# Execute the UNION query
print("Results of UNION query:")
union_results = db.select_data(union_query)

# Print each row of the combined result set
for row in union_results:
    print(row)

```

Purpose: This code snippet uses UNION to combine data from your_first_table and your_second_table into a single result set. Duplicate rows are removed, making it suitable for merging datasets with unique entries.

# Add a New Column to a Table

The alter_table() function is used to modify the structure of a table by adding a new column.

```python

# Define a query to add a new column to your table
add_column_query = "ALTER TABLE your_table_name ADD your_new_column_name VARCHAR(255) AFTER your_existing_column;"
db.alter_table(add_column_query)

```

Purpose: This query adds a new column your_new_column_name to your_table_name, enhancing the table's structure for additional data storage.

# Rename a Column in a Table

The alter_table() function is also used to rename a column in an existing table.

```python

# Query to rename a column in your table
rename_column_query = "ALTER TABLE your_table_name CHANGE old_column_name new_column_name INT AUTO_INCREMENT;"
db.alter_table(rename_column_query)

```

Purpose: This query renames old_column_name to new_column_name and changes its data type to INT with AUTO_INCREMENT, if necessary.

# Set a Default Value for a Column

The alter_table() function can be used to set a default value for an existing column.

```python

# Query to set a default value for a column
default_value_query = "ALTER TABLE your_table_name MODIFY your_column_name INT DEFAULT 0;"
db.alter_table(default_value_query)

```

Purpose: This query sets a default value of 0 for your_column_name in your_table_name, which helps maintain data consistency.

# Change a Column's Data Type


The alter_table() function is used to change the data type of an existing column.

```python

# Query to change a column's data type
change_data_type_query = "ALTER TABLE your_table_name MODIFY your_column_name SMALLINT;"
db.alter_table(change_data_type_query)

```

Purpose: This query modifies your_column_name to have a SMALLINT data type, adjusting the column structure for the desired data format.

# Update a Single Record in a Table

The update_data() function can be used to update specific records in a table.

```python

# Query to update a single record in your table
update_query = "UPDATE your_table_name SET your_column_name = %s WHERE record_id_column = %s"
updated_values = ("your_column_name_value", "record_id_column_value")
db.update_data(update_query, updated_values)

```

Purpose: This code updates your_column_name with a new value for the record identified by record_id_column. This function is useful for targeted updates to maintain or correct data.

## Code Explanations for Database Operations

# Update Multiple Records in Your Table

This function updates multiple records in a table by specifying the new values and the unique identifiers for the records to be updated.


```python

# Query to update multiple records in your table
update_query = "UPDATE your_table_name SET your_column_name = %s WHERE record_id_column = %s"
updated_values = [
    ("your_column_name_value_1", "record_id_column_value_1"),
    ("your_column_name_value_2", "record_id_column_value_2")
]

db.update_data(update_query, updated_values)

```

Purpose: This code is used for batch updating records in a table, ensuring efficient updates of multiple rows in a single function call.

# Alter Table Structure

This function modifies the structure of a table by altering column properties, such as removing a default value.

```python

# Query to alter table structure
alter_query = "ALTER TABLE your_table_name ALTER COLUMN your_column_name DROP DEFAULT"
db.update_data(alter_query)

```

Purpose: This command is essential for changing the schema of a table, allowing for flexible database structure management without dropping and recreating the table.

# Create a View

This function creates a database view to present specific data from a table in a defined format.

```python

# Query to create a view 
create_view_query = """
CREATE VIEW your_view_table_name AS
SELECT your_id_column_1, your_column_name_2, your_column_name_3 FROM your_table_name
WHERE your_column_name < 600; # Replace with columns that have data types such as INT, FLOAT, or DECIMAL.
"""
db.update_data_view(create_view_query)

```

Purpose: Creating views simplifies complex queries and enhances data security by allowing controlled access to specific data in a table.

# Describe Table Structure

This function retrieves the structure of a specified table to help understand its schema.

```python

# Specify the table name you want to describe
table_name = "your_table_name"
table_structure = db.describe_table(table_name)

# Prints the structure of the specified table
print(table_structure)

```

Purpose: Describing a table is crucial for checking column names, data types, and constraints, aiding in database design and debugging.

# Drop a View

This function deletes a view from the database.

```python

# Specify the view name you want to drop
view_name = "your_view_name"
db.drop_view(view_name)

```

Purpose: Dropping a view is useful when it is no longer needed, helping maintain a clean and organized database environment.

# Delete a Record

This function deletes specific records from a table based on a given condition.

```python

# Specify the query to delete a record
delete_query = "DELETE FROM your_table_name WHERE your_column_name = %s"
delete_values = ("Your_column_Value",)
db.delete_data(delete_query, delete_values)

```

Purpose: Deleting records is important for data management, allowing the removal of outdated or irrelevant data.

# Select Records with Conditions

This function retrieves records from a table based on multiple conditions, including data type-specific filtering.

```python

# Query to select records with conditions
select_query = "SELECT * FROM your_table_name WHERE your_column_name_datatype_decimal_int_or_float BETWEEN %s AND %s AND your_column_name_datatype_anytype LIKE %s"
result = db.select_with_conditions_with_out(select_query, (25, 35, 'A%'))

# Note: Replace column names with actual names (e.g., age, salary) and data types (CHAR, INT, etc.)

```

Purpose: This query is valuable for filtering records using complex conditions, which is essential for targeted data analysis and reporting.

# Close Database Connection

This function safely closes the connection to the database.
```python

# Closes the connection to the database
db.close_connection()

```

Purpose: Closing the database connection ensures that resources are released, preventing potential memory leaks and maintaining database integrity.

