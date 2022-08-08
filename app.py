import time
import random
from teams import teams
from actions import actions

def generateRandomEvent(action):
    event = ''
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
    randomTeam = random.randint(1,2)
    if randomTeam == 1:
        team = team1
    else: 
        team = team2

    return team

def penalty(score, team, sides, action):
    if action == 'Shoot':
        player_shoot = input('Where you want to shoot? (left, center, right) ')
        if player_shoot != "left" or "center" or "right":
            player_shoot = "left"
            print(f'You didnt choose. I shot {player_shoot}')
        goalkeeper = random.choice(sides)
        if player_shoot == goalkeeper:
            print('Goalkeeper defends the penalty!!')
            print(f'Goalkeeper go to: {goalkeeper}')
        else:
            print('Goal!')
            print(f'Goalkeeper go to: {goalkeeper}')
            addScore(score, team)

    elif action == 'Save':
        playerGoalkeeper = input('Where you want to go with your goalkeeper? (left, center, right) ')
        if playerGoalkeeper != "left" or "center" or "right":
            playerGoalkeeper = "left"
            print(f'You didnt choose. I go {playerGoalkeeper}')
        computerShoot = random.choice(sides)
        if computerShoot == playerGoalkeeper:
            print('Goalkeeper defends the penalty!!')
            print(f'Shooter shoot to: {computerShoot}')
        else:
            print('Goal!')
            print(f'Shooter shoot to: {computerShoot}')
            addScore(score, team)

def app():
    team1 = random.choice(teams)
    team2 = random.choice(teams)
    if team1 == team2:
        team2 = random.choice(teams)

    player_team = input(f'Which team you choose? | {team1}, {team2}: ')

    if player_team == team1 or player_team == team2:
        
        score = {team1:0, team2:0}
        print(f'Match Start! {team1} vs {team2}')
        time.sleep(0.5)
        i = 1
        while i < 91:
            action = generateAction()
            event = generateRandomEvent(action)
            team = generateRandomTeam(team1, team2)

            time.sleep(0.5)

            if event == '':
                pass
            else:
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
        if score[team1] == score[team2]:
            while i < 121:
                if i == 105:
                    print('Przerwa!')
                    print(score)
                    time.sleep(3)
            i+=1
        print(score)
    else:
        print('You must enter the correct name of the team')
        return

app()