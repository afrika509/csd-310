import mysql.connector
from mysql.connector import errorcode

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

    cursor = db.cursor()

    # Select query for the team table
    team_query = "SELECT team_id, team_name, mascot FROM team"
    cursor.execute(team_query)
    teams = cursor.fetchall()

    print("\n-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print(f"Team ID: {team[0]}\nTeam Name: {team[1]}\nMascot: {team[2]}\n")

    # Select query for the player table
    player_query = "SELECT player_id, first_name, last_name, team_id FROM player"
    cursor.execute(player_query)
    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam ID: {player[3]}\n")

except mysql.connector.Error as err:
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
