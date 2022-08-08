import time
import random
from teams import teams
from actions import actions

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

def penalty(score, team, sides, action):
    if action == 'Shoot':
        player_shoot = input('Where you want to shoot? (left, center, right) ')
        player_shoot.lower()
        #If player dont choose direction
        if player_shoot == "left" or player_shoot == "center" or player_shoot == "right":
            pass
        else:
            player_shoot = random.choice(['left', 'center', 'right'])
            print(f'You didnt choose. I shot {player_shoot}')

        goalkeeper = random.choice(sides)
        if player_shoot == goalkeeper:
            print('Goalkeeper defends the penalty!!')
        else:
            print('Goal!')
            addScore(score, team)
        print(f'Goalkeeper go to: {goalkeeper}')

    elif action == 'Save':
        playerGoalkeeper = input('Where you want to go with your goalkeeper? (left, center, right) ')
        playerGoalkeeper.lower()
        
        #If player dont choose direction
        if playerGoalkeeper == "left" or playerGoalkeeper == "center" or playerGoalkeeper == "right":
            pass
        else:
            playerGoalkeeper = random.choice(['left', 'center', 'right'])
            print(f'You didnt choose. I go {playerGoalkeeper}')

        computerShoot = random.choice(sides)
        if computerShoot == playerGoalkeeper:
            print('Goalkeeper defends the penalty!!')
        else:
            print('Goal!')
            addScore(score, team)
        print(f'Shooter shoot to: {computerShoot}')

def drawATeam():
    teamsInList = random.sample(teams, 2)
    return teamsInList[0], teamsInList[1]

def checkForEvent():
    #TODO Dodac ify z eventami zeby nie zasmiecac app
    pass

def app():

    team1, team2 = drawATeam()
    player_team = input(f'Which team you choose? | {team1}, {team2}: ')

    if player_team == team1 or player_team == team2:
        
        score = {team1:0, team2:0}
        print(f'Match Start! {team1} vs {team2}')
        time.sleep(0.5)

        i = 1
        while i < 91:
            action = generateAction() # attack or defense
            event = generateRandomEvent(action) # foul, shoot, penalty ...
            team = generateRandomTeam(team1, team2) # which team has the action
            time.sleep(0.5)

            if event != '':
                print(f'{i}.{team}: {event}')

            if event == "Foul":
                possibilities = ['Red Card', 'Yellow Card', 'Free Kick', 'Penalty', '']
                weights = [0.05, 0.3, 0.2, 0.05, 0.4]
                event = random.choice(random.choices(possibilities, weights))
                if event == '':
                    print('Referee starts game after foul')
                else:
                    print(f'Referee decide to: {event}')
                    time.sleep(0.5)

            if event == "Goal":
                addScore(score, team)
            
            if event == "Free Kick":
                randomNumber = random.randint(1,10)
                if randomNumber == 10:
                    print('Co za piekna bramka z rzutu wolnego!')
                    addScore(score, team)
                else:
                    print('Niestety zmarnowali okazje na bramke z rzutu wolnego!')

            if event == "Penalty":
                sides = ['left', 'center', 'right']
                if team == player_team:
                    penalty(score, team, sides, 'Shoot')
                else:
                    penalty(score, team, sides, 'Save')

            if i == 45:
                print('Przerwa!')
                print(score)
                time.sleep(3)
            i+=1
            
        #Dogrywka
            if i == 90 and score[team1] == score[team2]:
                print('Rozpoczynam dogrywke')
                i = 91
                while i < 121:
                    action = generateAction() # attack or defense
                    event = generateRandomEvent(action) # foul, shoot, penalty ...
                    team = generateRandomTeam(team1, team2) # which team has the action
                    time.sleep(0.5)
                    if event != '':
                        print(f'{i}.{team}: {event}')
                        time.sleep(0.1)
                    if i == 105:
                        print('Przerwa!')
                        print(score)
                        time.sleep(3)
                    i+=1

                    #Penalties
                    if i == 120 and score[team1] == score[team2]:
                        time.sleep(0.1)
                        print('Rozpoczynamy rzuty karne')

        print(f'Wygrywa: {max(score, key=score.get)}, {score}')
    else:
        print('You must enter the correct name of the team')
        return

app()