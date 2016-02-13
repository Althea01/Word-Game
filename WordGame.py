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

global BookShelfCheck
BookShelfCheck = False

global MoneyCheck
MoneyCheck = False

global Drawer1Check
Drawer1Check = True

global Drawer2Check
Drawer2Check = True

global TelevisionCheck
TelevisionCheck = False

global Regret_pills
Regret_pills = 10

global TableCheck
TableCheck = True

global GlassCheck
GlassCheck = False


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
            print "Telephone"
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
            if BookShelfCheck is True:
                print "Space one"
                print "Space two"
                print "Space three"
                print "Space four"
                print "Space five"
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

#Object Choice in the Study Room
def ObjectChoiceS():
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "drawer1":
        if Drawer1Check is True:
            print "Hmmm...Seems like you've just found a shovel."
            ShovelCheck = True
            Drawer1Check = False
            StudyRoom()
        if Drawer1Check is False:
            print "You have already checked this drawer."

    if ObjectChoose.lower() == "drawer2":
        if Drawer2Check is True:
            PassWord = raw_input("Please type in the first four numbers of pi")
            if PassWord == "3141":
                print "You have found a bottle that contains ten regret pills."
                PillCheck = True
                Drawer2Check = False
                Regret_pills = 10
            else:
                print "Try again next time."
                StudyRoom()
        if Drawer2Check is False:
            print "You have already checked this drawer."

    if ObjectChoose.lower() == "book shelf":
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
                if BookChoice.lower == "y":
                    Ending1()
                else:
                    print "I wish you could make a better choice."
                    BookChoice = raw_input()
            print "Darwin's philosophy"
            print "Every object has its use... or not?"
            StudyRoom()

    if ObjectChoose.lower() == "safe":
        BookShelfCheck = True
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
        StudyRoom()
    if ObjectChoose.lower() == "space five":
        if ShovelCheck is False:
            print "This is just a vase. Go and fetch other essential elements to open the safe."
        if ShovelCheck is True:
            print "Wow, something's in the vase, do you want to dig it out?"
            vasedig = raw_input("Type y or n")
            if vasedig == "y":
                print "You have found a $100 bill."
                MoneyCheck = True
                ShovelCheck = False
            if vasedig == "n":
                StudyRoom()

#Object Choice in the Living Room
def ObjectChoiceL():
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "television":
        if TelevisionCheck is False:
            print "Do you want to breathe fresher air?"
            print "Do you want to have better eye sight?"
            print "Buy our magic cactus seed to plant your own cactus."
            print "The cactus is on a 50% discount and only costs $100."
            print "Hold the $100 dollar bill in your hand and call 19971115."
            print "Have a nice day."
            TelevisionCheck = True
            LivingRoom()
        elif TelevisionCheck is True:
            print "There's really nothing interesting."
            LivingRoom()

    if ObjectChoose.lower() == "table":
        if TableCheck is False:
            print "You have collected a water glass"
            GlassCheck = True


#Object Choice in the Kitchen
def ObjectChoiceK():

#Object Choice in the Dining Room
def ObjectChoiceD():

#Object Choice in the Bathroom
def ObjectChoiceBath():

#Object Choice in the Bedroom
def ObjectChoiceBed():
    ObjectChoose == raw_input()
    if ObjectChoose.lower() == "telephone":
        if TelephoneCheck is False:
            TelephoneNumber = raw_input("Which number do you want to dial?")
            if TelephoneNumber == "19971115":
                print "This is cactus seed selling hotline. Do you want to buy seed?"
                BuyChoice = raw_input("Type 1 for yes and 2 for no")
                if BuyChoice == "1":
                    if MoneyCheck is True:
                        print "You have received a cactus seed"
                        MoneyCheck = False
                    if MoneyCheck is False:
                        print "You do not have enough money to buy a cactus seed"
                        Bedroom()
                if BuyChoice == "2":
                    Bedroom()
                else:
                    print "Choose another valid number"
                    BuyChoice = raw_input("Type 1 for yes and 2 for no")
            else:
                print "Sorry, the number seems to be wrong."
                Bedroom()
        elif TelephoneCheck is True:
            print "..."
            Bedroom()


#Object Choice in the Balcony
def ObjectChoiceBal():

"""Object Choice"""

#BagCheck
def Bag():
    Bagchoose()
    if ShovelCheck is True:
        print "shovel"
    if BookCheck is True:
        print "Catholic Belief"
    if MoneyCheck is True:
        print "$100 Bill"

#Use of object: Bag choose
def Bagchoose():
    Bagchoice = raw_input("Type in an object to examine it.")
    if Bagchoice.lower() == "shovel":
        print "Seems like it could be used to dig something...as a shovel."
    if Bagchoice.lower() == "catholic belief"
        print "I would say that it is obvious where this book should be placed in."


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

#Ending one by leaving from Book Shelf
def Ending1():
    if TeammateCheck is True:
        print "Now, it is time for you to make a final choice."
        print "Only one of you can leave from this door."
        print "You have once claimed that you would do anything for your friend Heny, even if it will cost your life. If selfish you choose to die, then your best friend Heny can live."
        print "Make your choice, will you give your door key to your friend Heny?"
        endingchoice2 = raw_input("Type y or n")
        if endingchoice2 == "y"
            print "Heny leaves the house through the door."
            print "A black shadow appears in front of you and reaches out its hands..."
            print " "
            print "Congratulations, you have woken from a nightmare. You have managed to save 'love'(Heny) from 'hatred'(supernatural power)'s hands."
            print "Whole Story Line"
            print "Your friend has betrayed you and were begging for your forgiveness. You were entangled to decide whether you should forgive him. With this feeling of anxiety, you fell into a nightmare. If it proves that you are selfish, then your hatred towards your friend will devour your loving nature and you shall never be able to escape that nightmare. Luckily, you did not let your resentment develop and choose to instead forgive your friend."
        if endingchoice2 == "n"
            print "With a cry of despair, Heny is pulled away by two hands that seems to appear from nowhere."
            print "You opened the door and stepped out..."
            print " "
            BadEnd()
            print "Your friend has betrayed you and were begging for your forgiveness. You were entangled to decide whether you should forgive him. With this feeling of anxiety, you fell into a nightmare. If it proves that you are selfish, then your hatred towards your friend will devour your loving nature and you shall never be able to escape that nightmare. Unfortunately, you have chosen to let your resentment develop and not forgive your best friend."
    if TeammateCheck is False:
        print "The book shelf moves to the right and a door appears."
        endingchoice1 = raw_input("Do you wish to leave the house from here? Type y or n")
        if endingchoice1 == "y":
            BadEnd()
        if endingchoice1 == "n":
            print "Maybe you can come back later when you find something more precious"

Introduction()