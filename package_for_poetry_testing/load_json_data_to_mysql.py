import pymysql
import json

# Function to connect to MySQL
def create_connection():
    try:
        connection = pymysql.connect(
            host="localhost",         # MySQL host (e.g., localhost or IP)
            user="root",              # MySQL username
            password="123456",        # MySQL password
            database="test"           # The database to connect to
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
    connection = create_connection()
    if connection:
        create_table(connection)  # Create table if it doesn't exist
        
        # Path to the JSON file
        json_file = 'data.json'

        # Insert data from the JSON file
        insert_data_from_json(connection, json_file)

        connection.close()  # Close the connection

if __name__ == "__main__":
    main()
