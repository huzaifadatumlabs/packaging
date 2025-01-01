import pymysql
import json
import argparse

# Function to connect to MySQL
def create_connection(host, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,           # MySQL host
            user=user,           # MySQL username
            password=password,   # MySQL password
            database=database    # The database to connect to
        )
        print("Connected to MySQL database")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to create a table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    );
    """)
    print("Table 'person' created successfully")
    cursor.close()

# Function to insert data from JSON into the table
def insert_data_from_json(connection, json_file):
    cursor = connection.cursor()

    # Open and read the JSON data from the file
    with open(json_file, 'r') as file:
        data = json.load(file)  # Load the JSON data into a Python list

    # Iterate over the JSON data and insert into the table
    for person in data:
        query = "INSERT INTO person (name, email) VALUES (%s, %s)"
        values = (person['name'], person['email'])
        cursor.execute(query, values)
        connection.commit()  # Commit the transaction
        print(f"Inserted {cursor.rowcount} row(s) into the persons table")

    cursor.close()

# Main script to demonstrate CRUD operations
def main():
    # Set up argparse to get database connection information from the command line
    parser = argparse.ArgumentParser(description="Connect to MySQL and perform CRUD operations.")
    parser.add_argument('--host', type=str, required=True, help='MySQL host (e.g., localhost or IP)')
    parser.add_argument('--user', type=str, required=True, help='MySQL username')
    parser.add_argument('--password', type=str, required=True, help='MySQL password')
    parser.add_argument('--database', type=str, required=True, help='The database to connect to')
    parser.add_argument('--json', type=str, required=True, help='Path to the JSON file for data insertion')

    # Parse the arguments
    args = parser.parse_args()

    # Create the database connection using the parsed arguments
    connection = create_connection(args.host, args.user, args.password, args.database)
    if connection:
        create_table(connection)  # Create table if it doesn't exist
        
        # Insert data from the JSON file
        insert_data_from_json(connection, args.json)

        connection.close()  # Close the connection

if __name__ == "__main__":
    main()
