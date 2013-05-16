#Program: Assignment 1 - Fallout Survival - U Got Died
#File: Fallout Survival Game
#Author: Jonathan Hodder
#Last modified by: Jonathan Hodder
#Date Last Modified: Wednesday May 15th 2013

#Program description:  Welcome to the fallout.  Population you...the rest well.....
#Welcome to the bottom of the food chain.  A storms coming make your choice...
#Shelter....Storm....Either way you'll probably end up dead.

#Version History:
#Version #1 - Added original code from dragon game
#Version #1.1 - Removed extra code


import time

#display introduction method
def displayIntro():
    #print the introduction of the Fallout
    print ('Welcome to the fallout.  Population you...')
    time.sleep(3)
    print ('the rest well.....Welcome to the bottom of the food chain. ')
    time.sleep(3)
    print ('Shelter....Storm....Either way youll probably end up dead.')
    time.sleep(3)
    print

#First option method
def CaveOrTown():
    #string choice is set to blank
    choice = ''
    #provide two options to the player the cave or the twon
    print ('The storm is coming...')
    time.sleep(2)
    print ('You see a dark foreboding cave where ichor drips around the jagged protusions of the mouths entrance.')
    time.sleep(5)
    print ('Past the cave is a derilict town in the distance.  The town looks to be in ruin and seems to be falling apart at the seams.')
    time.sleep(5)
    print ('Make your decision soon as the storm is coming.  If you do not find shelter soon the winds will consume your body so viciously that not even the bones of your corspe will survive.')
    time.sleep(5)
    print ('Enter the ichor drooping cave (1)')
    time.sleep(2)
    print ('Hurry to the decrepit town(2)')
    time.sleep(2)
    print ('Make your choice!!!!!!')
    choice = raw_input()
    
    #if you enter the cave this happens run the enterCave method
    if choice == '1':
        enterCave()
    
    else if choice == '2':
        
        enter Town()
    #if the user pick a different option the storm kills the player
    else:
        print ('Your indecisiveness has cost you greatly the wind has consumed your body and tore your very soul from its frail shell.')
        print ('Your soul will join in the screaming of the winds as it searches to consume organic weakness for the rest of eternity.')
        gameOver()
    
#enter the cave method choice    
def enterCave():
    #ask the user if they want to continue onwards or use their light first
    print ('You choose to enter into the dark imposing cave.')
    time.sleep(2)
    print ('There is small illumination from the outside that is dissapearing in the storm.')   
    time.sleep(5)
    print ('As the sand is torn from the ground by the storm the cave is devoured by darkness so thick that when you bring your scarred hands upwards it feels as if there is a resistance to your movement.')
    time.sleep(5)
    print ('You can not see... Your mind was able to map out a direction in the cave to begin your travels.')
    time.sleep(5)
    print ('There is a lighter in your pocket you could use it to light the way but any creatures in the cave. Will become aware of you.')
    time.sleep(5)
    print ('Continue onwards into the unknown.(1)')
    time.sleep(2)
    print ('Use your lighter to take stock of the situation.(2)')
    time.sleep(2)
    print ('Decide...')       

#enter the town method choice
def runToTown():
    print ('You run through the sands hoping to outchase the storm.')
    time.sleep(3)
    print ('You are able to make it to the first building a house that sags to the sides as the wood of the frame seems to be breaking apart.')
    time.sleep(5)
    print ('There is no time to look for another house as the sand behind you is thrown into the gaping maw of the whirlwind.')
    time.sleep(5)
    print ('As you open the rotting door the very hinges scream in protest but with a tug you are inside!')
    time.sleep(5)
    print ('You slam the door and slowly back away as a capachony of screams moan and rage as if they are cursing your survival.')
    time.sleep(5)
    print ('Slowly')

#gameOver method
def gameOver():
    #created playAgain string
    playAgain = ''
    #Ask the player if they wish to play again
    print ('Your mortal journey has ended...')
    time.sleep(5)
    print ('But... There are multiple possibilities in this corrupted world will you replace another and choose differently.')
    time.sleep(5)
    print
    time.sleep(5)

    print ('Do you want to play the game of life again? (yes or no)')
    playAgain = raw_input()
    #if the players says yes run main method again
    if playAgain == 'yes' or playAgain == 'y':
        main()

#main method
def main():
    
    #run the game
    displayIntro()
    CaveOrTown()

main()
