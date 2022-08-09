import time
import random
from teams import teams
from actions import actions
from events.penalty import penalty

from colorama import Fore
from colorama import Style

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def generateRandomEvent(action):
    if action == 'attack':
        weights = [0.15, 0.05, 0.1, 0.2, 0.5]
        event = random.choice(random.choices(actions['attack'], weights))
    elif action == 'defense':
        weights = [0.2, 0.05, 0.15, 0.2, 0.2, 0.3]
        event = random.choice(random.choices(actions['defense'], weights))

    return event

def generateAction():
    actions = ['attack', 'defense']
    action = random.choice(actions)
    return action

def addScore(score,team):
    score[team] = score[team]+1
    print(f'Score: {score}')

def generateRandomTeam(team1, team2):
    teams = [team1, team2]
    team = random.choice(teams)
    return team

def drawATeam():
    teamsInList = random.sample(teams, 2)
    return teamsInList[0], teamsInList[1]

def foulEvent(event):
    possibilities = ['Red Card', 'Yellow Card', 'Free Kick', 'Penalty', '']
    weights = [0.05, 0.3, 0.2, 0.05, 0.4]
    event = random.choice(random.choices(possibilities, weights))
    if event == '':
        print('Referee starts game after foul')
    else:
        print(f'Referee decide to: {event}')
        time.sleep(0.5)

def freeKickEvent(score, team):
    randomNumber = random.randint(1,10)
    if randomNumber == 10:
        print('Co za piekna bramka z rzutu wolnego!')
        addScore(score, team)
    else:
        print('Niestety zmarnowali okazje na bramke z rzutu wolnego!')

def checkForEvent(event, score, team, player_team):
    if event == "Foul":
        foulEvent(event)

    if event == "Goal":
        addScore(score, team)
            
    if event == "Free Kick":
        freeKickEvent(score,team)

    if event == "Penalty":
        sides = ['left', 'center', 'right']
        if team == player_team:
            penalty(score, team, sides, 'Shoot', addScore)
        else:
            penalty(score, team, sides, 'Save', addScore)

def timeout(score):
    print('Przerwa!')
    print(score)
    time.sleep(3)

def generateActionTeamEvent(team1,team2):
    action = generateAction() # attack or defense
    event = generateRandomEvent(action) # foul, shoot, penalty ...
    team = generateRandomTeam(team1, team2) # which team has the action
    return event, team

def overtime(team1, team2, score, player_team):
    i = 91
    while i < 121:
        event, team = generateActionTeamEvent(team1,team2)
        time.sleep(0.5)

        if event != '':
            if team == player_team:
                print(f'{Fore.YELLOW}{i}{Style.RESET_ALL}.{Fore.GREEN}{team}: {event}{Style.RESET_ALL}')
            else:
                print(f'{Fore.YELLOW}{i}{Style.RESET_ALL}.{Fore.RED}{team}: {event}{Style.RESET_ALL}')
                    
        checkForEvent(event, score, team, player_team)

        if i == 105:
            timeout(score)

        #karne
        if i == 120 and score[team1] == score[team2]:
            pass
            #penalty_score = {team1:0, team2:0}
            #isAWin = False
            #while isAWin:

        i+=1

def app():

    team1, team2 = drawATeam()
    player_team = input(f'Which team you choose? | {team1}, {team2}: ')

    if player_team == team1 or player_team == team2:
        
        score = {team1:0, team2:0}
        print(f'Match Start! {team1} vs {team2}')
        time.sleep(0.5)

        i = 1
        while i < 91:
            event, team = generateActionTeamEvent(team1,team2)
            time.sleep(0.5)

            if event != '':
                if team == player_team:
                    print(f'{Fore.YELLOW}{i}{Style.RESET_ALL}.{Fore.GREEN}{team}: {event}{Style.RESET_ALL}')
                else:
                    print(f'{Fore.YELLOW}{i}{Style.RESET_ALL}.{Fore.RED}{team}: {event}{Style.RESET_ALL}')

            checkForEvent(event, score, team, player_team)

            if i == 45:
                timeout(score)

            i+=1
            
        #Dogrywka
            if i == 90 and score[team1] == score[team2]:
                print('Overtime!')
                overtime(team1, team2, score, player_team)

        print(f'Wygrywa: {max(score, key=score.get)}, {score}')
    else:
        print('You must enter the correct name of the team')
        return

app()