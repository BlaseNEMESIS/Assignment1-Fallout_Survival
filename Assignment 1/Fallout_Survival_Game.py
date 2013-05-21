#Program: Assignment 1 - Fallout Survival - U Got Died
#File: Fallout Survival Game
#Author: Jonathan Hodder
#Last modified by: Jonathan Hodder
#Date Last Modified: Tuesday May 20th 2013

#Program description:  Welcome to the fallout.  Population you...the rest well.....
#Welcome to the bottom of the food chain.  A storms coming make your choice...
#Shelter....Storm....Either way you'll probably end up dead.

#Version History:
#Version #0 - Added original code from dragon game
#Version #0.1 - Removed extra code
#Version #0.2 - Completed first option and almost finished the next two options
#Version #0.3 - Completed the first two bad ends
#Version #0.4 - Completed all the cave endings - only need to complete 4 more endings

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
    
    #if you choose to enter the cave run the enterCave method
    if choice == '1':
        enterCave()
    #if you choose to head to the town run the enterTown method
    elif choice == '2':
        enterTown()
        
    #if the user pick a different option the storm kills the player
    else:
        print ('Your indecisiveness has cost you greatly the wind has consumed your body and tore your very soul from its frail shell.')
        print ('Your soul will join in the screaming of the winds as it searches to consume organic weakness for the rest of eternity.')
        gameOver()
    
#enter the cave method choice    
def enterCave():
    choice = ''
    #ask the user if they want to continue onwards or use their light first
    print ('You choose to enter into the dark imposing cave.')
    time.sleep(2)
    print ('There is small illumination from the outside that is dissapearing from the storm.')   
    time.sleep(5)
    print ('As the sand is torn from the ground by the storm the cave is devoured by darkness so thick that when you bring your scarred hands upwards it feels as if there is a resistance to your movement.')
    time.sleep(5)
    print ('You can not see... Your mind was able to map out a direction in the cave to begin your travels.')
    time.sleep(5)
    print ('There is a lighter in your pocket you could use it to light the way but any creatures in the cave. Will become aware of you.')
    time.sleep(5)
    
    #If the user does not enter 1 or 2 continue to loop
    while choice != '1' and choice != '2':
        print ('Continue onwards into the unknown.(1)')
        time.sleep(2)
        print ('Use your lighter to take stock of the situation.(2)')
        time.sleep(2)
        print ('Decide...')  
        choice = raw_input()
    #if you choose to continue into the cave run the continue into the cave method
    if choice == '1':
        continueIntoCave()
    #if you choose to turn on the lighter run the turn on lighter method
    elif choice == '2':
        turnOnLighter()

#continue into the cave choice
def continueIntoCave():
    choice = ''
    print ('You continue into the murky darkness pushing through the heavy thickness around you.')
    time.sleep(5)
    print ('You are not sure how long it has been as the weight around you seems to warp all your senses.')
    time.sleep(5)
    print ('As time passes the darkness seems to tighten around you.  It is subtle but your muscless begin to scream and your bones weep from the pressure.')
    time.sleep(5)
    print ('You panic but salvation is near there is a light near you that seems to have the shadows shirk away from them in fear.')
    time.sleep(5)
    print ('You realize that the darkness seems to be in pain from the light.')
    time.sleep(3)
    print ('Your mind comes up with two options to counter the darkness')
    time.sleep(3)
    
    #If the user does not enter 1 or 2 continue to loop
    while choice != '1' and choice != '2':
        print ('Reach for your lighter to protect yourself (1)')
        time.sleep(2)
        print ('Pursue the light at the end of the tunnel (2)')
        time.sleep(2)
        print ('The darkness is not patient Decide...')
        choice = raw_input()
        
    #if you choose to reach for your lighter run the reachForLighter method
    if choice == '1':
        reachForLighter()
    #if you choose to head into the light run the intoTheLight method
    elif choice == '2':
        intoTheLight()
    
#reach for lighter method choice
def reachForLighter():
    #bad end you have died
    print ('You desperately reach for your lighter but it is too late.')
    time.sleep(5)
    print ('The darkness crushes your bones and your fluids leaks from multiple punctures.')
    time.sleep(5)
    print ('Even in death the darkness still crushes you.')
    time.sleep(5)
    print ('In a bestial roar of triumph the darkness disintegrates bones and flesh from your body')
    time.sleep(5)
    print ('With another grunt even your escaped fluids are pulverised by the intense pressure.')
    time.sleep(5)
    print ('There is not even a piece to bury.')
    #run the game over method
    gameOver()
    
#intoTheLight method choice
def intoTheLight():
    #bad end you have died
    print ('You find renewed strength to rush to the light but it does not matter....')
    time.sleep(5)
    print ('As you near the light you fall')
    time.sleep(3)
    print ('Unfortunately in a vertical descent the thickness of the darkness is equivalent into slamming into concrete repeatedly')
    time.sleep(5)
    print ('You do not even live to see the light to see the light at the bottom as your crumpled body slams into the glowing floor below.')
    #run the game over method
    gameOver()
    
#turn on the lighter method choice             
def turnOnLighter():
    choice = ''
    print ('As you reach for your lighter the darkness seems to increase in pressure.')
    time.sleep(5)
    print ('Fortunately you reach your lighter and with a click a flame is summoned into being.')
    time.sleep(5)
    print ('The darkness seems to melt and warp upon itself as it screams at you.')
    time.sleep(5)
    print ('While the darkness seems to flee from the light the light begins to dominate the cavern')
    time.sleep(5)
    print ('The cave seems to be much smaller then you though as there only seems to be one small room.')
    time.sleep(5)
    print ('Inside the room there is a pulsing object that seems to glow a dark red around the room.')
    time.sleep(5)
    print ('You take a closer look... The object seems to be a pulsating heart with green veins pumping around it.')
    time.sleep(5)
    print ('The items begs for you to touch it to posses it. Whisper sweet love into your ear.  Promises, threats, lies.. You must have it.')
    time.sleep(5)
    
    #while the user does not pick 1 or 2 continue to run the options
    while choice != '1' and choice != '2':
        print ('Pick up the heart.(1)')
        time.sleep(2)
        print ('Wrap the heart up in a cloth (2)')
        time.sleep(2)
        print ('Grab IT!!!')
        choice = raw_input()
    
    #if you choose to pick up the heart run the pickUpHeart method
    if choice == '1':
        pickUpHeart()
    #if you choose to wrap the heart run the wrapUpHeart method
    elif choice == '2':
        wrapUpHeart()

#pickUpHeart method choice
def pickUpHeart():
    #bad end
    print ('You pick up the beating heart and that is the last thing you ever do.')
    time.sleep(5)
    print ('The whispers drill into your brain and tear every part of you from its recesses.')
    time.sleep(5)
    print ('You are now nothing but abomination of flesh, a mindless slaves to powers you could not fathom.')
    gameOver()
    
#wrapUpHeart choice
def wrapUpHeart():
    choice = ''  
    print ('You wrap the heart in a cloth and the whispers almost dissapear but their urgency increases.')
    time.sleep(5)
    print ('A headache causes you to shut your eyes to attempt to block out the desperate pleas.')
    time.sleep(5)
    print ('When you open your eyes you are in a house.') 
    time.sleep(3)
    print ('There is a haunting meoldy coming from the basement but your body screams at you to head upstairs before it is silenced ruthlessy.')
    time.sleep(5)
    
    #while the user does not pick 1 or 2 continue to run the options
    while choice != '1' and choice != '2':
        print ('Head down to the basement (1)')
        time.sleep(2)
        print ('Head upstairs (2)') 
        time.sleep(2)
        print ('Choose quickly..')
        choice = raw_input()    
    
    #if you choose to head down to the basement run the headToBasement method
    if choice == '1':
        headToBasement()
    #if you choose to head upstairs run the headUpstairs method
    elif choice == '2':
        headUpstairs()
 
def headToBasement():
    #bad true end
    print('You choose to head downstairs while the whisper whisper pleased sounds to you.')
    time.sleep(5)
    print('Downstairs is filled with thick shadows the obscur creatures that are incomprehensible to the mortal mind')
    time.sleep(5)
    print('You walk down the steps and kneel at a dais of a an array of tentacles that form a collasping human face.')
    time.sleep(5)
    print('You place the heart at the dais and tentacles from the darkness grab the heart.')
    time.sleep(5)
    print('For providing the forces of darkness with the heart you are gifted anything you wish.')
    time.sleep(5)
    print('But you will forever serve the dark creatures that scurry in the darkness.')
    time.sleep(5)
    print('You will forever be a champion of EVIL.')
    #run the gameOver method
    gameOver()
    
def headUpstairs():
    #good true end
    print('You choose to ignore the whisper and head upstairs.')
    time.sleep(3)
    print('The whispers increase in frequency begging you to turn around')
    time.sleep(3)
    print('You continue to move to the last door in the hallway where there is a beatiful dagger adorned with angels.')
    time.sleep(5)
    print('Your ears bleed and organs rupture as the whispers become screams.')
    time.sleep(4)
    print('You grab the dagger and throw the heart to the ground in a defiant scream of rage.')
    time.sleep(5)
    print('You stab the heart repeatedly even as your body fails you and your consciousness falls apart.')
    time.sleep(5)
    print('The screams cease as heart leaks black blood.  As your body fails the house collaspes around you.')
    time.sleep(5)
    print('You die with a smile on your lips.')
    time.sleep(3)
    print('You are rewarded for your valor and determination and ascend to one of the highest honors.')
    time.sleep(3)
    print('A champion of justice...')
    time.sleep(3)
    print('But remember evil is always out there champion of GOOD')
    gameOver()
    
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
    print ('You breathe deeply as the howls of the storm slowly decrease before they vanish from your hearing.')
    time.sleep(5)
    print ('As you look around the house has a foreboding taint to it as if it tempting you to action.')
    time.sleep(5)
    print ('You feel as if you will fracture as your body and mind conflict with each other.')
    time.sleep(5)
    print ('Your mind screams at you to explore this feeling, that it will provide you with answers.')
    time.sleep(5)
    print ('Your body moans as your blood shivers and your bones scream at you, a primal fear wells up inside to flee.')
    time.sleep(5)
    print ('Explore the house (1)')
    time.sleep(2)
    print ('Leave the town now(2)')
    time.sleep(2)
    print ('Hurry...')

#gameOver method
def gameOver():
    #created playAgain string
    playAgain = ''
    #Ask the player if they wish to play again
    print ('Your mortal journey has ended...')
    time.sleep(5)
    print ('But... There are multiple possibilities in this corrupted world will you replace another and choose differently.')
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
