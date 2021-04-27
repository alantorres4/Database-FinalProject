import sys
import os
import csv
import random
import os.path
import mysql.connector
from tabulate import tabulate

def menu(option_choosed):
#	menu_options = "\n\t1) Add a Team\n\t2) Add a Game\n\t3) Add a Result\n\t4) View all Teams\n\t5) Results for a Team\n\t6) Results in a Date\n\t7) Quit"
#	print(menu_options)
#	option_choosed = input(f"{os.linesep}Please select an option: ")

		if option_choosed == "1":
			add_team()

		elif option_choosed == "2":
			add_game()

		elif option_choosed == "3":
			add_result()

		elif option_choosed == "4":
			view_teams()

		elif option_choosed == "5":
			results_for_team()

		elif option_choosed == "6":
			results_for_date()

		elif option_choosed == "7":
			close_db()
			print("Quitting...")
			sys.exit()
		else:
			print(f"{os.linesep}The option you selected is not valid.{os.linesep}")


def open_database (hostname,user_name,mysql_pw,database_name):
      global conn
      conn= mysql.connector.connect(host= hostname, 
      user= user_name,  
      password= mysql_pw, 
      database= database_name 
    ) 
      global cursor
      cursor = conn.cursor() 

def printFormat(result):
    header=[]
    for cd in cursor.description: # get headers
        header.append(cd[0])
    return(tabulate(result, headers=header, tablefmt="html")) # print results in table format

# select and display query
def executeSelect(query):
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    res = res.split('\n')
    for i in range (len(res)):
      print(res[i])

#modified version that returns the first value of the query as a variable
def executeSelectOption (query):
    cursor.execute(query)
    results = cursor.fetchall()
    #printFormat(results)
    return results[0][0]

def insert(table,values):
	if table == 'TEAM':
		table = "TEAM (TEAM_NAME, NICKNAME, WINS, LOSSES, RANK)"
	elif table == 'GAME':
		table = "GAME (TEAM_ID_1, TEAM_ID_2, LOCATION, DATE, PLAYED)"
	else: 
		table = "RESULT"
	query ="INSERT into " + table + " values (" + values + ")" +';'
	cursor.execute(query)
	conn.commit()


def executeUpdate(query): # use this function for delete and update
    cursor.execute(query)
    conn.commit()


def close_db ():  # use this function to close db
    cursor.close()
    conn.close()


def add_team():
	global conn
	global cursor
	print(' ')
	name_select = sys.argv[2]
	name_select = name_select.upper()
	try:
		name_check = executeSelectOption(f"SELECT TEAM_NAME FROM TEAM WHERE TEAM_NAME = '{name_select}';")
		print(f"Invalid name. Already exisisting team. Try again later...{os.linesep}")
		return False
	except:
		nickname_select = sys.argv[3]
		wins_select = sys.argv[4]
		losses_select = sys.argv[5]
		rank_select = sys.argv[6]
		values = "'" + name_select + "', '" + nickname_select +"', '" + str(wins_select) + "', '" + str(losses_select) +"', '" + str(rank_select) +"'"
		insert('TEAM',values)
		print(f"Team added to the TEAM table: {os.linesep}")
		executeSelect(f"SELECT * FROM TEAM WHERE TEAM_NAME = '{name_select}';")

	
def add_game():
	global conn
	global cursor
	print(' ')
	print(f"Available teams: {os.linesep}")
	executeSelect(f"SELECT TEAM_NAME AS 'Name', TEAM_ID AS 'ID' FROM TEAM")
	try:
		team_id_1_select = sys.argv[2]
		team_id_1_check = executeSelectOption(f"SELECT TEAM_ID FROM TEAM WHERE TEAM_ID = '{team_id_1_select}';")
		team_id_2_select = sys.argv[3]
		team_id_2_check = executeSelectOption(f"SELECT TEAM_ID FROM TEAM WHERE TEAM_ID = '{team_id_2_select}';")
		location_select = sys.argv[4]
		date_select = sys.argv[5]
		date_select = "STR_TO_DATE('" + date_select + "','%Y-%m-%d')"
		values = "'" + str(team_id_1_select) + "', '" + str(team_id_2_select) +"', '" + location_select +"'," + date_select +", 'NO'"
		print("Values :", values)
		insert('GAME',values)
		print(f"Game added to the GAME table: {os.linesep}")
		executeSelect(f"SELECT * FROM GAME WHERE TEAM_ID_1 = '{team_id_1_select}' AND TEAM_ID_2 = '{team_id_2_select}';")
	except:
		print(f"Invalid ID. Please, try again with a valid team ID.{os.linesep}")
		return False


def add_result():
	global conn
	global cursor
	global team_id_1_wins, team_id_2_wins
	print(' ')
	print(f"Available games: {os.linesep}")
	executeSelect(f"SELECT g.GAME_ID, TEAM_ID_1, TEAM_ID_2 FROM GAME g WHERE PLAYED = 'NO'")
	gameid_select = sys.argv[2]
	try:
		game_check = executeSelectOption(f"SELECT GAME_ID FROM GAME WHERE GAME_ID = '{gameid_select}';")

	except:
		print(f"Invalid game ID. Please, first add the game in the GAME table.{os.linesep}")
		return False
	teamoneid_select = sys.argv[3]
	teamtwoid_select = sys.argv[4]
	scoreteamone_select = sys.argv[5]
	scoreteamtwo_select = sys.argv[6]
	values = "'" + str(gameid_select) + "', '" + str(teamoneid_select) +"', '" + str(teamtwoid_select) + "', '" + str(scoreteamone_select) +"', '" + str(scoreteamtwo_select) +"'"
	insert('RESULT',values)
	print(f"Result added to the RESULT table: {os.linesep}")
	executeSelect(f"SELECT * FROM RESULT WHERE GAME_ID = '{gameid_select}';")
	team_id_2_wins = executeSelectOption(f"SELECT WINS FROM TEAM WHERE TEAM_ID = '{teamtwoid_select}';")
	team_id_1_wins = executeSelectOption(f"SELECT WINS FROM TEAM WHERE TEAM_ID = '{teamoneid_select}';")
	if scoreteamone_select > scoreteamtwo_select:
		team_id_1_wins += 1
		team_id_2_losses = executeSelectOption(f"SELECT LOSSES FROM TEAM WHERE TEAM_ID = '{teamtwoid_select}';")
		team_id_2_losses += 1
		executeUpdate(f"UPDATE TEAM set WINS = '{team_id_1_wins}' where TEAM_ID = '{teamoneid_select}' ;")
		executeUpdate(f"UPDATE TEAM set LOSSES = '{team_id_2_losses}' where TEAM_ID = '{teamtwoid_select}' ;")
		rank_modifier(teamoneid_select, team_id_1_wins)
		rank_modifier(teamtwoid_select, team_id_2_wins)
	else:
		team_id_1_losses = executeSelectOption(f"SELECT LOSSES FROM TEAM WHERE TEAM_ID = '{teamoneid_select}';")
		team_id_1_losses += 1
		team_id_2_wins += 1
		executeUpdate(f"UPDATE TEAM set LOSSES = '{team_id_1_losses}' where TEAM_ID = '{teamoneid_select}' ;")
		executeUpdate(f"UPDATE TEAM set WINS = '{team_id_2_wins}' where TEAM_ID = '{teamtwoid_select}' ;")
		rank_modifier(teamoneid_select, team_id_1_wins)
		rank_modifier(teamtwoid_select, team_id_2_wins)


def view_teams():
	executeSelect(f"SELECT TEAM_NAME, NICKNAME, WINS, LOSSES, RANK FROM TEAM ORDER BY RANK ASC")

def results_for_team():
	team_chosen = sys.argv[2]
	team_chosen = team_chosen.upper()
	try:
		executeSelect(f"SELECT A.TEAM_NAME AS 'HOST', B.TEAM_NAME AS 'GUEST', DATE, SCOREONE AS 'HOME RESULT', SCORETWO AS 'GUEST RESULT', IF(SCOREONE>SCORETWO, A.TEAM_NAME, B.TEAM_NAME) AS 'WINNER' FROM TEAM A INNER JOIN TEAM B INNER JOIN GAME ON A.TEAM_ID = TEAM_ID_1 AND B.TEAM_ID = TEAM_ID_2 INNER JOIN RESULT ON GAME.GAME_ID = RESULT.GAME_ID WHERE A.TEAM_NAME = '{team_chosen}' OR B.TEAM_NAME = '{team_chosen}';")
	except:
		print(f"  [-] {team_chosen} was not a valid team name.");



def results_for_date():
	date_chosen = sys.argv[2];
	try:
		executeSelect(f"SELECT A.TEAM_NAME AS 'HOST', B.TEAM_NAME AS 'GUEST', LOCATION, SCOREONE AS 'HOME RESULT', SCORETWO 'GUEST RESULT', IF(SCOREONE>SCORETWO, A.TEAM_NAME, B.TEAM_NAME) AS 'WINNER' FROM TEAM A INNER JOIN TEAM B LEFT JOIN GAME ON A.TEAM_ID = TEAM_ID_1 AND B.TEAM_ID = TEAM_ID_2 LEFT JOIN RESULT ON GAME.GAME_ID = RESULT.GAME_ID WHERE DATE = '{date_chosen}';")

	except:
		print(f"  [-] {date_chosen} was not a valid date. Make sure it is in this format: YYYY-MM-DD.")


def rank_modifier(TEAM_ID, WINS):
	global team_id_1_wins, team_id_2_wins
	rank_team = executeSelectOption(f"SELECT RANK FROM TEAM WHERE TEAM_ID = '{TEAM_ID}';")
	sup_rank_team = rank_team + 1
	low_rank_team = rank_team - 1
	wins_sup_team = executeSelectOption(f"SELECT WINS FROM TEAM WHERE RANK = '{sup_rank_team}';")
	wins_low_team = executeSelectOption(f"SELECT WINS FROM TEAM WHERE RANK = '{low_rank_team}';")
	if WINS >= wins_sup_team:
		executeUpdate(f"UPDATE TEAM set RANK = '00' where RANK = '{sup_rank_team}' ;")
		executeUpdate(f"UPDATE TEAM set RANK = '{sup_rank_team}' where TEAM_ID = '{TEAM_ID}' ;")
		executeUpdate(f"UPDATE TEAM set RANK = '{rank_team}' where RANK = '00' ;")
	elif WINS <= wins_low_team:
		executeUpdate(f"UPDATE TEAM set RANK = '00' where RANK = '{low_rank_team}' ;")
		executeUpdate(f"UPDATE TEAM set RANK = '{low_rank_team}' where TEAM_ID = '{TEAM_ID}' ;")
		executeUpdate(f"UPDATE TEAM set RANK = '{rank_team}' where RANK = '00' ;")
	else:
		return False


##### Test #######
mysql_username = 'ajtorres' # please change to your username
mysql_password = 'Aiba4ioz'  # please change to your MySQL password

open_database('localhost',mysql_username,mysql_password,mysql_username) # open database   
option_choosed = sys.argv[1] # Gets the argument from command line. Ex: '$python3 main_file.py 4 etc etc....', so optioned_choosed will be 4
menu(option_choosed)

