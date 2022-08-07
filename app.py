import time
import random
from teams import teams

def generateRandomEvent():
    event = ''
    randomNumber = random.randint(1,10)

    if randomNumber == 1 or randomNumber == 2 or randomNumber == 3:
        event = ''
    elif randomNumber == 4:
        event = 'Zółta Kartka'
    elif randomNumber == 5:
        event = 'Czerwona Kartka'
    elif randomNumber == 6:
        event = 'Aut'
    elif randomNumber == 7:
        event = 'Rzut Wolny'
    elif randomNumber == 8:
        event = 'Rzut Karny'
    elif randomNumber == 9:
        event = 'BRAMKA!'
    
    return event

def generateAction():
    action = ''
    randomNumber = random.randint(1,2)
    if randomNumber == 1:
        action = 'attack'
    elif randomNumber == 2:
        action = 'defense'
    
    return action


def generateRandomTeam(team1, team2):
    randomTeam = random.randint(1,2)
    if randomTeam == 1:
        team = team1
    else: 
        team = team2

    return team

def app():
    team1 = random.choice(teams)
    team2 = random.choice(teams)
    if team1 == team2:
        team2 = random.choice(teams)

    score = {team1:0, team2:0}

    i = 1
    while i < 91:
        action = generateAction()
        event = generateRandomEvent()
        time.sleep(0.5)
        team = generateRandomTeam(team1, team2)
        print(f'{i}.{team}: {event}')

        if event == "BRAMKA!":
            score[team] = score[team]+1
            print(f'Wynik: {score}')
        
        if event == "Rzut Wolny":
            randomNumber = random.randint(1,10)
            if randomNumber == 10:
                score[team] = score[team]+1
                print('Co za piekna bramka z rzutu wolnego!')
                print(f'Wynik: {score}')
            else:
                print('Niestety zmarnowali okazje na bramke z rzutu wolnego!')

        if event == "Rzut Karny":
            randomNumber = random.randint(1,2)
            if randomNumber == 1:
                score[team] = score[team]+1
                print('BRAMKA!')
                print(f'Wynik: {score}')
            else:
                print("Nietrafiony Karny!")

        if i == 45:
            print('Przerwa!')
            print(score)
            time.sleep(3)
        i+=1
    print(score)

app()