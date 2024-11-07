import mysql.connector
from mysql.connector import Error

class MySQLModule:
    def __init__(self, hostname='localhost', username='root', password='', database=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    # Function to connect to the MySQL database
    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.hostname,
                user=self.username,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print(f"Connected to MySQL Server version {db_info}")
                if self.database:
                    print(f"Connected to database: {self.database}")
                return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    # Function to close the connection safely
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

    # functoin to check first the database is it exists or not then alow to create 
    def check_database_exists(self, database_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
            result = cursor.fetchone()
            return result is not None
        except Error as e:
            print(f"Error checking database: {e}")
            return False

    # function to create basically the database
    def create_database(self, database_name):
        if self.check_database_exists(database_name):
            print(f"Database '{database_name}' already exists. Creation not allowed.")
        else:
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"CREATE DATABASE {database_name}")
                print(f"Database '{database_name}' created successfully.")
            except Error as e:
                print(f"Error creating database: {e}")

    # functoin to check first the table is it exists or not then alow to create 
    def check_table_exists(self, table_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = cursor.fetchone()
            return result is not None
        except Error as e:
            print(f"Error checking table: {e}")
            return False

    # function to create basically the tables
    def create_table(self, create_table_query, table_name):
        if self.check_table_exists(table_name):
            print(f"Table '{table_name}' already exists in the database. Creation not allowed.")
        else:
            try:
                cursor = self.connection.cursor()
                cursor.execute(create_table_query)
                print(f"Table '{table_name}' created successfully.")
            except Error as e:
                print(f"Error creating table: {e}")

    # function to show you your all databases
    def show_databases(self):
        try:
            cursor = self.connection.cursor()
            show_databases_query = "SHOW DATABASES"
            cursor.execute(show_databases_query)
            databases = cursor.fetchall()
            return databases
        except Error as e:
            print(f"Error fetching databases: {e}")
            return None

    # Function to show tables in a specific database based on user input
    def show_tables(self):
        try:
            # Ask the user for the database name
            database_name = input("Which database's tables would you like to see? Give here in the enter here the database name here ans press enter : ")
            
            # Use the provided database name
            use_database_query = f"USE {database_name}"
            cursor = self.connection.cursor()
            cursor.execute(use_database_query)
            
            # Query to show tables in the selected database
            show_tables_query = "SHOW TABLES"
            cursor.execute(show_tables_query)
            
            # Fetch and return the tables
            tables = cursor.fetchall()
            if tables:
                print(f"Tables in the '{database_name}' database:")
                for table in tables:
                    print(table[0])
            else:
                print(f"No tables found in the '{database_name}' database.")
            return tables
        except Error as e:
            print(f"Error fetching tables: {e}")
            return None


    # here we created this method only for to the builtin functions   
    def insert_data_only_with_builtins(self, table_name, columns, values):
        try:
            cursor = self.connection.cursor()
            # Prepare the SQL INSERT statement
            placeholders = ', '.join(['%s'] * len(values))
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

            # Convert values to the correct type if necessary
            converted_values = []
            for value in values:
                if isinstance(value, int):
                    converted_values.append(value)  # keep as is if it's an int
                elif isinstance(value, float):
                    converted_values.append(value)  # keep as is if it's a float
                else:
                    converted_values.append(str(value))  # convert other types to string

            # Execute the query with converted values
            cursor.execute(query, converted_values)  # Using the converted values
            self.connection.commit()
            print("Data inserted successfully")
        except Error as e:
            print(f"Error inserting data: {e}")
    

    # method used for to the python built-in functions and with string method 
    def insert_data_with_builtins_with_methods(self, table_name, columns, values, string_methods=None):
        try:
            cursor = self.connection.cursor()
            # Prepare the SQL INSERT statement
            placeholders = ', '.join(['%s'] * len(values))
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

            # Convert values to the correct type like int , append, float and str
            converted_values = []
            for value in values:
                if isinstance(value, int):
                    converted_values.append(value) 
                elif isinstance(value, float):
                    converted_values.append(value)
                else:
                    str_value = str(value)

                    # Apply user-defined string methods
                    if string_methods:
                        for method in string_methods:
                            if method == 'lower':
                                str_value = str_value.lower()
                            elif method == 'upper':
                                str_value = str_value.upper()
                            elif method == 'replace':
                                str_value = str_value.replace(' ', '_')  # example as replacement
                            elif method == 'strip':
                                str_value = str_value.strip()
                            elif method == 'find':
                                position = str_value.find('-')
                                print(f"Position of '-' in '{value}': {position}")

                    converted_values.append(str_value)

            #execute the query with converted values
            cursor.execute(query, converted_values)
            self.connection.commit()
            print("Data inserted successfully")
        except Error as e:
            print(f"Error inserting data: {e}")

     # Function for inserting multiple rows of data into a table without builtin functions
    def insert_mul_val_data_without(self, table_name, columns, values_list):
        try:
            cursor = self.connection.cursor()
            # Constructing the INSERT query with placeholders for values
            placeholders = ', '.join(['%s'] * len(columns))
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

            # Execute the query for each set of values in values_list
            cursor.executemany(query, values_list)  # Use executemany for multiple rows
            self.connection.commit()  # Committing the transaction
            print("Data inserted successfully")
        except Error as e:
            print(f"Error inserting data: {e}")


    # here i used the set () built-in function and also here we applied
    # the methods of set () on to this built-in function
    def insert_mul_val_data_with(self, table_name, columns, values_list):
        try:
            cursor = self.connection.cursor()

            # Using set() to remove duplicates from values_list
            unique_values_set = set(values_list)

            # Print initial unique set
            print("Initial Set of Unique Values:")
            print(unique_values_set)

            # Asking user which set method to apply, including "skipall"
            method = input("Enter set methods to apply (comma-separated, options: add, remove, union, intersection, difference, update, discard, pop, clear, issubset, skipall): ")
            method_list = method.split(",")

            # Check if the user entered "skipall"
            if "skipall" in method_list:
                print("Skipping all set operations and directly inserting the values.")
            else:
                for method in method_list:
                    method = method.strip()
                    if method == "add":
                        new_value = input("Enter a new tuple to add to the set: ")
                        try:
                            new_tuple = eval(new_value)
                            unique_values_set.add(new_tuple)
                            print(f"Updated set after add: {unique_values_set}")
                        except Exception as e:
                            print(f"Error adding to set: {e}")

                    elif method == "remove":
                        value_to_remove = input("Enter a tuple to remove from the set: ")
                        try:
                            remove_tuple = eval(value_to_remove)
                            unique_values_set.remove(remove_tuple)
                            print(f"Updated set after remove: {unique_values_set}")
                        except KeyError:
                            print(f"Tuple {value_to_remove} not found in set.")
                        except Exception as e:
                            print(f"Error removing from set: {e}")

                    elif method == "union":
                        new_values = input("Enter a set of tuples to perform union: ")
                        try:
                            new_set = eval(new_values)
                            union_result = unique_values_set.union(new_set)
                            print(f"Result of union: {union_result}")
                        except Exception as e:
                            print(f"Error performing union: {e}")

                    elif method == "intersection":
                        new_values = input("Enter a set of tuples to perform intersection: ")
                        try:
                            new_set = eval(new_values)
                            intersection_result = unique_values_set.intersection(new_set)
                            print(f"Result of intersection: {intersection_result}")
                        except Exception as e:
                            print(f"Error performing intersection: {e}")

                    elif method == "difference":
                        new_values = input("Enter a set of tuples to perform difference: ")
                        try:
                            new_set = eval(new_values)
                            difference_result = unique_values_set.difference(new_set)
                            print(f"Result of difference: {difference_result}")
                        except Exception as e:
                            print(f"Error performing difference: {e}")

                    elif method == "update":
                        new_values = input("Enter a list of tuples to update the set: ")
                        try:
                            new_list = eval(new_values)
                            unique_values_set.update(new_list)
                            print(f"Updated set after update: {unique_values_set}")
                        except Exception as e:
                            print(f"Error performing update: {e}")

                    elif method == "discard":
                        value_to_discard = input("Enter a tuple to discard from the set: ")
                        try:
                            discard_tuple = eval(value_to_discard)
                            unique_values_set.discard(discard_tuple)
                            print(f"Updated set after discard: {unique_values_set}")
                        except Exception as e:
                            print(f"Error performing discard: {e}")

                    elif method == "pop":
                        try:
                            popped_value = unique_values_set.pop()
                            print(f"Popped value: {popped_value}")
                            print(f"Updated set after pop: {unique_values_set}")
                        except KeyError:
                            print("The set is empty, cannot pop.")
                        except Exception as e:
                            print(f"Error performing pop: {e}")

                    elif method == "clear":
                        unique_values_set.clear()
                        print(f"Set cleared: {unique_values_set}")

                    elif method == "issubset":
                        new_values = input("Enter a set of tuples to check if the original set is a subset: ")
                        try:
                            new_set = eval(new_values)
                            print("Original Set (unique_values_set):", unique_values_set)
                            if unique_values_set.issubset(new_set):
                                print("Original set is a subset of the entered set.")
                            else:
                                print("Original set is NOT a subset of the entered set.")
                        except Exception as e:
                            print(f"Error performing issubset: {e}")

            # Convert the updated set back to a list (if needed for further operations)
            unique_values_list = list(unique_values_set)

            # Construct the INSERT query with placeholders for values
            placeholders = ', '.join(['%s'] * len(columns))
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

            # Insert each row individually from the unique values list
            for values in unique_values_list:
                try:
                    print("Executing query:", query)
                    print("With values:", values)
                    cursor.execute(query, values)
                    self.connection.commit()
                    print("Row inserted successfully:", values)
                except Error as e:
                    print(f"Error inserting row {values}: {e}")

        except Error as e:
            print(f"Error in insert_mul_val_data_with: {e}")


    # here we used the sorted built-in function 
    def select_and_sort_data(self, table_name, sort_column):
        try:
            cursor = self.connection.cursor()
            # Select all data from the specified table
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
        
            # Filter out rows where the sort column is None
            filtered_data = [row for row in data if row[sort_column] is not None]
        
            # Sort the filtered data
            sorted_data = sorted(filtered_data, key=lambda row: row[sort_column])
        
            # Print the sorted data
            for row in sorted_data:
                print(row)
        
            return sorted_data  # Return sorted data for further use if needed

        except Error as e:
            print(f"Error selecting and sorting data: {e}")

    # here we are used only the list() built-in function 
    def print_data_as_list_only(self, table_name):
        try:
            cursor = self.connection.cursor()
            # Query to select all data from the table
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            data = cursor.fetchall()

            # Convert data to a list using the list() function
            data_list = list(data)

            # Print the list of data
            print(f"Data from {table_name} as list:")
            for row in data_list:
                print(row)
        except Error as e:
            print(f"Error printing data: {e}")

    # here we used the list built-in function and we apply the list methods on list () built-in function 
    def print_data_as_list_with_M(self, table_name, list_methods):
        try:
            cursor = self.connection.cursor()
            # Query to select all data from the table
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            data = cursor.fetchall()

            # Convert data to a list using the list() function
            data_list = list(data)

            # Print the original list of data
            print(f"Original data from {table_name} as list:")
            for row in data_list:
                print(row)

            # Apply the user's chosen list methods
            for method in list_methods:
                if method == "append":
                    # Append a user-defined value to the list
                    value_to_append = input("Enter a value to append (as a tuple): ")
                    data_list.append(eval(value_to_append))

                elif method == "extend":
                    # Extend the list by another list
                    value_to_extend = input("Enter a list to extend with (as a list of tuples): ")
                    data_list.extend(eval(value_to_extend))

                elif method == "pop":
                    # Pop an element from the list at the user-specified index
                    index_to_pop = int(input("Enter an index to pop: "))
                    data_list.pop(index_to_pop)

                elif method == "remove":
                    # Remove the first occurrence of a value
                    value_to_remove = input("Enter a value to remove (as a tuple): ")
                    data_list.remove(eval(value_to_remove))

                elif method == "sort":
                    # Sort the list (this assumes it's sortable)
                    data_list.sort()

                elif method == "reverse":
                    # Reverse the list
                    data_list.reverse()

                elif method == "index":
                    # Get the index of a value
                    value_to_find = input("Enter a value to find (as a tuple): ")
                    index = data_list.index(eval(value_to_find))
                    print(f"Index of {value_to_find}: {index}")

                # New Methods
                elif method == "insert":
                    # Insert a value at the specified index
                    index_to_insert = int(input("Enter the index where you want to insert: "))
                    value_to_insert = input("Enter the value to insert (as a tuple): ")
                    data_list.insert(index_to_insert, eval(value_to_insert))

                elif method == "count":
                    # Count the number of occurrences of a value
                    value_to_count = input("Enter the value to count (as a tuple): ")
                    count = data_list.count(eval(value_to_count))
                    print(f"Count of {value_to_count}: {count}")

                elif method == "clear":
                    # Clear all elements from the list
                    confirm_clear = input("Are you sure you want to clear the list? (yes/no): ")
                    if confirm_clear.lower() == 'yes':
                        data_list.clear()
                        print("The list has been cleared.")

            # Print the modified list of data
            print("\nModified list of data:")
            for row in data_list:
                print(row)

        except Error as e:
            print(f"Error printing data: {e}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")


    # Function for using SQL aggregate functions (e.g., SUM, MAX, MIN, COUNT, AVG) and with pthon len() builtin function
    def aggregate_functions(self, query, values=None):
        try:
            cursor = self.connection.cursor()

            # Executing the query
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            # Fetching all results
            result = cursor.fetchall()

            # Use SQL COUNT function to get the count of rows
            cursor.execute("SELECT COUNT(*) FROM ({}) AS subquery".format(query))
            count_result = cursor.fetchone()[0]  # This gives the count of rows

            # Use the len() function to get the length of the result
            length_of_result = len(result)

            # Returning both the count and the length
            return {"count": count_result, "length": length_of_result, "result": result}
        except Error as e:
            print(f"Error with aggregate functions: {e}")
            return None

    # here we used the abs(), tuple(), float and int built-in function of python 
    def select_with_conditions_with_M(self, table_name, column, condition, value):
        try:
            cursor = self.connection.cursor()

            # Formulate the query based on the condition selected
            query = f"SELECT * FROM {table_name} WHERE {column} {condition} %s"
            cursor.execute(query, (value,))
            results = cursor.fetchall()

            # Print data using abs() to handle any negative numbers
            for row in results:
                row_with_abs = tuple(abs(item) if isinstance(item, (int, float)) else item for item in row)
                print(row_with_abs)

        except Error as e:
            print(f"Error in select_with_conditions_with_M: {e}")

    # here i used this method for to the round () built-in function 
    def round_column_values(self, table_name, column_name, decimal_places):
        try:
            cursor = self.connection.cursor()

            # Fetching values from the column to round
            query = f"SELECT id, {column_name} FROM {table_name}"
            cursor.execute(query)
            data = cursor.fetchall()

            # Rounding values and updating the table
            for row in data:
                rounded_value = round(row[1], decimal_places)
                update_query = f"UPDATE {table_name} SET {column_name} = %s WHERE id = %s"
                cursor.execute(update_query, (rounded_value, row[0]))

            self.connection.commit()
            print(f"Rounded values in column '{column_name}' to {decimal_places} decimal places.")

        except Error as e:
            print(f"Error in round_column_values: {e}")

    # Example of a SELECT with INNER JOIN and with the used of ZIP() , Enumerate () built-in funnctions 
    def inner_join_tables(self, table1, table2, join_condition, columns1, columns2):
        try:
            cursor = self.connection.cursor()

            # Using zip() to combine columns from both tables
            columns = ', '.join([f"{table1}.{col1}, {table2}.{col2}" for col1, col2 in zip(columns1, columns2)])
            query = f"SELECT {columns} FROM {table1} INNER JOIN {table2} ON {join_condition}"
            cursor.execute(query)
            results = cursor.fetchall()

            # Using enumerate() to print results with index
            for idx, row in enumerate(results):
                print(f"{idx}: {row}")

        except Error as e:
            print(f"Error in join_tables: {e}")

    # Example of a SELECT with LEFT JOIN and with the used of ZIP() , Enumerate () built-in funnctions
    def left_join_tables(self, table1, table2, join_condition, columns1, columns2):
        try:
            cursor = self.connection.cursor()

            # Using zip() to combine columns from both tables
            columns = ', '.join([f"{table1}.{col1}, {table2}.{col2}" for col1, col2 in zip(columns1, columns2)])
            query = f"SELECT {columns} FROM {table1} LEFT JOIN {table2} ON {join_condition}"
            cursor.execute(query)
            results = cursor.fetchall()

            # Using enumerate() to print results with index
            for idx, row in enumerate(results):
                print(f"{idx}: {row}")

        except Error as e:
            print(f"Error in join_tables: {e}")
    
    # Example of a SELECT with RIGHT JOIN and with the used of ZIP() , Enumerate () built-in funnctions
    def right_join_tables(self, table1, table2, join_condition, columns1, columns2):
        try:
            cursor = self.connection.cursor()

            # Using zip() to combine columns from both tables
            columns = ', '.join([f"{table1}.{col1}, {table2}.{col2}" for col1, col2 in zip(columns1, columns2)])
            query = f"SELECT {columns} FROM {table1} RIGHT JOIN {table2} ON {join_condition}"
            cursor.execute(query)
            results = cursor.fetchall()

            # Using enumerate() to print results with index
            for idx, row in enumerate(results):
                print(f"{idx}: {row}")

        except Error as e:
            print(f"Error in join_tables: {e}")

    # here we wright this method for to that to delete the inserted values and the 
    # type() builtin function: to check the type of the value being deleted.
    def delete_record(self, table_name, column, operator, value):
        try:
            cursor = self.connection.cursor()

            # Ensure correct operator
            if operator not in ['=', '>', '<', '>=', '<=', '!=']:
                raise ValueError(f"Invalid operator: {operator}. Expected '=', '>', '<', '>=', '<=', '!='")

            # Ensure correct value type using type()
            if type(value) not in [int, float, str]:
                raise ValueError(f"Invalid value type: {type(value)}. Expected int, float, or str.")

            # Create the SQL query with the operator and placeholder for the value
            query = f"DELETE FROM {table_name} WHERE {column} {operator} %s"
            cursor.execute(query, (value,))
        
            # Commit the transaction
            self.connection.commit()

            # Output confirmation of deletion
            print(f"Record(s) deleted where {column} {operator} {value}")
    
        except Exception as e:
            print(f"Error occurred: {str(e)}")


    # Example of DROP TABLE using with dict() built-in functioin for flexible query construction
    def drop_table(self, table_name):
        try:
            cursor = self.connection.cursor()

            # Creating a dictionary to store table information
            table_info = dict(name=table_name, action='DROP')
            query = f"{table_info['action']} TABLE IF EXISTS {table_info['name']}"
            cursor.execute(query)
            self.connection.commit()
            print(f"Table '{table_name}' dropped if it existed.")

        except Error as e:
            print(f"Error in drop_table: {e}")
    
    # Example of ALTER TABLE with range() for batch alterations
    def alter_table_add_columns(self, table_name, column_name, column_type, count):
        try:
            cursor = self.connection.cursor()

            # Using range() to add multiple columns
            for i in range(count):
                query = f"ALTER TABLE {table_name} ADD COLUMN {column_name}_{i} {column_type}"
                cursor.execute(query)
                print(f"Added column: {column_name}_{i} with type {column_type}")

            self.connection.commit()
            print(f"{count} columns added to '{table_name}'.")

        except Error as e:
            print(f"Error in alter_table_add_columns: {e}")

    # i am using tuple() to convert each row from the result into a tuple where each value is paired with its type. 
    # here only i used this method only for to this builtin functions
    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            # Use type() to determine the type of each column
            for row in results:
                typed_row = tuple((item, type(item)) for item in row)
                print(typed_row)

        except Error as e:
            print(f"Error in execute_query: {e}")

    # here we are used this method code for to the enumerate() is used to keep track 
    # of the row index (or position) while iterating through the rows in the result set
    def complex_operation(self, table_name):
        try:
            cursor = self.connection.cursor()

            # Example complex operation where type() is used
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            results = cursor.fetchall()

            # Use enumerate() to print row index with the data
            for index, row in enumerate(results):
                typed_row = [f"Row {index}:"] + [f"{item} (type: {type(item)})" for item in row]
                print(', '.join(typed_row))

        except Error as e:
            print(f"Error in complex_operation: {e}")

    # here we are used the coalesce key word of mysql to handle the null values
    # and dict() builtin function with the dict() methods 
    def select_with_coalesce(self, table_name, column_name, default_value):
        try:
            cursor = self.connection.cursor()

            # Use dict() to store query details
            query_info = dict(column=column_name, default=default_value)
        
            # Construct the query using COALESCE with values from the dict
            query = f"SELECT COALESCE({query_info.get('column')}, %s) FROM {table_name}"
            cursor.execute(query, (query_info.get('default'),))
            results = cursor.fetchall()

            # Store results in a dictionary
            results_dict = {i: result[0] for i, result in enumerate(results, start=1)}

            # Apply dict() methods
            print("Results using dict().keys():", results_dict.keys())  # Print all keys (row numbers)
            print("Results using dict().values():", results_dict.values())  # Print all values (fetched results)
            print("Results using dict().items():", results_dict.items())  # Print key-value pairs (rows and results)
        
            # Use dict().pop() to remove a specific row (if row 1 exists)
            popped_value = results_dict.pop(1, None)
            if popped_value:
                print(f"Popped row 1: {popped_value}")
            else:
                print("Row 1 not found or already popped")

        except Error as e:
            print(f"Error in select_with_coalesce: {e}")
            
    # DISTINCT: Used to eliminate duplicate rows from the result set, returning only unique values.
    # and dict() builtin function with the dict() methods 
    def select_with_distinct(self, table_name, column_name):
        try:
            cursor = self.connection.cursor()

            # Use dict() to store query details
            query_info = dict(column=column_name)
        
            # Construct the query using DISTINCT with values from the dict
            query = f"SELECT DISTINCT {query_info.get('column')} FROM {table_name}"
            cursor.execute(query)
            results = cursor.fetchall()

            # Store distinct results in a dictionary
            results_dict = {i: result[0] for i, result in enumerate(results, start=1)}

            # Apply dict() methods
            print("Results using dict().keys():", results_dict.keys())  # Print all keys (row numbers)
            print("Results using dict().values():", results_dict.values())  # Print all values (fetched results)
            print("Results using dict().items():", results_dict.items())  # Print key-value pairs (rows and results)
        
            # Use dict().pop() to remove a specific row (if row 1 exists)
            popped_value = results_dict.pop(1, None)
            if popped_value:
                print(f"Popped row 1: {popped_value}")
            else:
                print("Row 1 not found or already popped")

        except Error as e:
            print(f"Error in select_with_distinct: {e}")


    # here we used this method for to  that to use for to the between , and key words as in range 
    def select_in_range(self, table_name, column, start, end):
        try:
            cursor = self.connection.cursor()

            # Using range() to filter values between start and end
            query = f"SELECT * FROM {table_name} WHERE {column} BETWEEN %s AND %s"
            cursor.execute(query, (start, end))
            results = cursor.fetchall()

            for row in results:
                print(row)

        except Error as e:
            print(f"Error in select_in_range: {e}")

    # here we used this method for to  that to use for to the like key word
    def select_with_like(self, table_name, column, pattern):
        try:
            cursor = self.connection.cursor()

            # Using LIKE keyword to search for patterns
            query = f"SELECT * FROM {table_name} WHERE {column} LIKE %s"
            cursor.execute(query, (pattern,))
            results = cursor.fetchall()
            
            for row in results:
                print(row)

        except Error as e:
            print(f"Error in select_with_like: {e}")




    
    def update_data(self, update_query, values_list):
        try:
            # Ensure the query starts with 'UPDATE' using startswith()
            if not update_query.strip().upper().startswith("UPDATE"):
                raise ValueError("Query must start with 'UPDATE'.")

            # Example: Use replace() to modify placeholder table names or field names if needed
            sanitized_query = update_query.replace("owner", "actual_table_name_if_needed")

            # Process the values list: apply isalnum() and capitalize() on names
            cleaned_values_list = []
            for name, o_id in values_list:
                if not name.replace(" ", "").isalnum():  # Allowing spaces while checking if the rest is alphanumeric
                    raise ValueError(f"Name '{name}' contains invalid characters.")
                
                # Capitalize the name before updating
                cleaned_name = name.capitalize()
                cleaned_values_list.append((cleaned_name, o_id))

            cursor = self.connection.cursor()
            cursor.executemany(sanitized_query, cleaned_values_list)
            self.connection.commit()
            print(f"{cursor.rowcount} rows updated successfully.")

        except Error as e:
            print(f"Error updating data: {e}")
        except ValueError as ve:
            print(f"Validation Error: {ve}")
        finally:
            if self.connection.is_connected():
                cursor.close()



        


    # IN THE BELLOW CODE I DOES NOT USED ANY IMPORTANT FUNCTIONALITIES OF PYTHON
    # Function to select data from a table
    def select_data(self, select_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error selecting data: {e}")
            return None

    # here are the alter key word is using for to that to add , change, replace, delete, drop and modify the table  
    def alter_table(self, alter_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(alter_query)
            self.connection.commit()
            print("Table altered successfully")
        except mysql.connector.Error as err:
            print(f"Error altering table: {err}")

    # Function to update data of tables
    def update_data(self, update_query, values_list):
        try:
            cursor = self.connection.cursor()
            cursor.executemany(update_query, values_list)
            self.connection.commit()
            print(f"{cursor.rowcount} rows updated successfully.")
        except Error as e:
            print(f"Error updating data: {e}")

    # create a view table from an other table
    def update_data_view(self, query, values_list=None):
        try:
            cursor = self.connection.cursor()
            if values_list:
                cursor.execute(query, values_list)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")

    # the use of to the DESC KEY word for to the tables
    def describe_table(self, table_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DESC {table_name}")  # Using DESC to describe the table structure
            result = cursor.fetchall()  # Fetch all the result of the query
            return result
        except Error as e:
            print(f"Error describing table: {e}")
            return None

    # if ou want to drop the view created table use this code method
    def drop_view(self, view_name):
        try:
            cursor = self.connection.cursor()
            drop_view_query = f"DROP VIEW IF EXISTS {view_name}"
            cursor.execute(drop_view_query)
            self.connection.commit()
            print(f"View '{view_name}' dropped successfully.")
        except Error as e:
            print(f"Error dropping view: {e}")

    # Function to delete data
    def delete_data(self, delete_query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query, values)
            self.connection.commit()
            print("Data deleted successfully.")
        except Error as e:
            print(f"Error deleting data: {e}")

    # Function to check connection is ready
    def is_connected(self):
        return self.connection.is_connected() if self.connection else False

    # Function to select data with specific conditions like (e.g., WHERE, LIKE, BETWEEN, AND, IN, >, < ,!=, =)
    def select_with_conditions_with_out(self, select_query, values=None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(select_query, values)
            else:
                cursor.execute(select_query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error selecting data: {e}")
            return None
