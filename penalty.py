import random
def penalty(score, team, sides, action, addScore):
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