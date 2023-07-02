import mysql.connector
from mysql.connector import Error, errorcode

# Database config object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    # Try/catch block for handling potential MySQL database errors
    db = mysql.connector.connect(**config)  # Connect to the pysports database

    # Output the connection status
    print(f"\nDatabase user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

    input("\n\nPress any key to continue...")

except Error as err:
    # On error code
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

finally:
    # Close the connection to MySQL
    if 'db' in locals() or 'db' in globals():
        db.close()
