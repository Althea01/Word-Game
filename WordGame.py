__author__ = 'LilyDu'

"""globals"""
global name


global TeammateCheck
TeammateCheck = False

global AtticCheck
AtticCheck = False

global DoorCheck
DoorCheck = False

global FishingRodCheck
FishingRodCheck = False

global ShovelCheck
ShovelCheck = False

global SafeCheck
SafeCheck = False


"""globals"""

#In the living room
def LivingRoom():
    print "You are now in the Living Room."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the living room."
    print "Type 'bag' or 'b' to check what is in the bag."
    
    def ActionChoiceL():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Dining room"
            print "Bathroom"
            print "Bedroom"
            print "Balcony"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Television"
            print "Table"
            print "Sofa"
            ObjectChoiceL()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            LivingRoom()
    ActionChoiceL()

#In the dining room
def DiningRoom():
    print "You are now in the dining room."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the dining room."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceD():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Living room"
            print "Study room"
            print "Kitchen"
            print "Bedroom"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Droplight"
            print "Dining table"
            if DoorCheck is True:
                print "Opened door"
            elif DoorCheck is False:
                print "Locked door"
            ObjectChoiceD()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            DiningRoom()
    ActionChoiceD()

#In the bathroom
def Bathroom():
    print "You are now in the bathroom."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the bathroom."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceBath():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Living room"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Basin"
            print "Mirror"
            print "Bath tub"
            ObjectChoiceBath()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            Bathroom()
    ActionChoiceBath()

#In the kitchen
def Kitchen():
    print "You are now in the kitchen."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the kitchen."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceK():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Dining room"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Refrigerator"
            print "Knife case"
            print "Floor"
            ObjectChoiceK()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            Kitchen()
    ActionChoiceK()

#In the balcony
def Balcony():
    print "You are now on the balcony."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is on the balcony."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceBal():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Living room"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Telescope"
            if FishingRodCheck is True:
                print "Fishing Rod"
            ObjectChoiceBal()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            Balcony()
    ActionChoiceBal()

#In the bedroom
def Bedroom():
    print "You are now in the bedroom."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the bedroom."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceBed():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Living room"
            print "Dining room"
            if AtticCheck is True:
                print "Attic"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Bed"
            print "Wardrobe"
            ObjectChoiceBed()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            Bedroom()
    ActionChoiceBed()

#In the study room
def StudyRoom():
    print "You are now in the study room."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the study room."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceS():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Dining room"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Drawer1"
            print "Drawer2"
            print "Drawer3"
            print "Computer"
            print "Teddy Bear"
            print "Book shelf"
            ObjectChoiceS()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            StudyRoom()
    ActionChoiceS()

#In the attic
def Attic():
    print "Hahaha"

"""Object Choice"""

#Object choice in the Study Room
def ObjectChoiceS():
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "drawer1"
        print "Hmmm...Seems like you've just found a shovel."
        ShovelCheck = True

    if ObjectChoose.lower() == "book shelf"
        print "Aha! The book shelf can be moved! Do you wish to move it? Type y or n"
        MoveChoice = raw_input()
        if MoveChoice == "y":
        print "Oh my god! There is a safe behind the book shelf. There seems to be four blank spaces and a vase"
        if MoveChoice == "n":
        print "Let's see what's on the shelf."
        print "Anthea and her cat"
        print "Beowulf"
        if BookCheck is True:
            print "Do you want to put your book onto the shelf? Type y or n"
            BookChoice = raw_input()
            if BookChoice.lower = "y"
                Ending1()
            else:
                print "I wish you could make a better choice."
                BookChoice = raw_input()
        print "Darwin's philosophy"
        print "Every object has its use... or not?"


    if ObjectChoose.lower() == "safe"
        if RobotCheck is False:
            print "Space one: looks like a robot (not found)"
        if CactusCheck is False:
            print "Space two: looks like a kind of plant (not found)"
        if RegretJuiceCheck is False:
            print "Space three: looks like a glass (not found)"
        if LitCandleCheck is False:
            print "Space four: looks like a candle (not found)"
        print "Space five: a vase with soil"
        if RobotCheck is True and CactusCheck is True and RegretJuiceCheck is True and LitCandleCheck is True:
            print "You have successfully found everything. The safe is now opened."
            SafeCheck = True
        if SafeCheck is True:
            print "Congratulations. You have found a book in the safe. The book is called Catholic Belief and is put into your bag."

#Object Choice in the Living Room
def ObjectChoiceL():

"""Object Choice"""

#BagCheck
def Bag():
    Bagchoose()
    if ShovelCheck is True:
        print "shovel"
    if BookCheck is True:
        print "Catholic Belief"
    if

#Use of object: Bag choose
def Bagchoose():
    Bagchoice = raw_input("Type in an object to examine it.")
    if Bagchoice.lower() == "shovel":
        print ""

#RoomChoice
def RoomChoice():
    RoomChoose = raw_input()
    if RoomChoose.lower() == "dining room":
        DiningRoom()
    elif RoomChoose.lower() == "bathroom":
        Bathroom()
    elif RoomChoose.lower() == "living room":
        LivingRoom()
    elif RoomChoose.lower() == "kitchen":
        Kitchen()
    elif RoomChoose.lower() == "balcony":
        Balcony()
    elif RoomChoose.lower() == "attic":
        Attic()
    elif RoomChoose.lower() == "bedroom":
        Bedroom()
    elif RoomChoose.lower() == "study room":
        StudyRoom()
    else:
        print "You are trying to go to a place that nobody knows that exists in here"
        print "You have known too much"
        print "Goodbye"
        BadEnd()




#NameChoice
def InputName():
    name1 = raw_input("Please enter your name:")
    print "Are you sure that you wanted to be called",
    print name1, "? Enter y or n."
    
    response = raw_input()
    
    if response.lower() == "y":
        global name
        name = name1
    else:
        InputName()

#Introduction to the game
def Introduction():
    print "Welcome to Escape From The House."
    InputName()
    print "Hi,"+name+"."+"Unfortunately, you are trapped here in a haunted crooked house."
    print "You and your friend Heny were trying to find out a dark secret in the house when someone attacked you from behind and you fainted."
    print "You need to leave the house ASAP before something happen to you."
    print "Now, try to escape the house safely."
    LivingRoom()

#A bad ending of the game
def BadEnd():
    print "Sorry, you have been killed by super natural force. The evil spirit is laughing with joy. Hahahahaha."

Introduction()