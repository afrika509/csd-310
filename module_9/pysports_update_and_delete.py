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
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Insert a new record for Smeagol
    cursor.execute("INSERT INTO player(player_id, first_name, last_name, team_id) VALUES (21, 'Smeagol', 'Shire Folk', 1)")
    db.commit()

    # Display player records with team names after insert
    cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player.player_id")
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER INSERT --")
    for i in players:
        print(f"\nPlayer ID: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nTeam Name: {i[3]}\n")

    # Update the record for Smeagol
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE player_id = 21")
    db.commit()

    # Display all records in the player table after update
    cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player.player_id")
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")
    for i in players:
        print(f"\nPlayer ID: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nTeam Name: {i[3]}\n")

    # Delete the record for Gollum
    cursor.execute("DELETE FROM player WHERE player_id = 21")
    db.commit()

    # Display all records in the player table after delete
    cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player.player_id")
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER DELETE --")
    for i in players:
        print(f"\nPlayer ID: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nTeam Name: {i[3]}\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
    input("Press Enter to continue...")
