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

global PillCheck
PillCheck = False

global Regret_pills
if PillCheck is True:
    Regret_pills = 10
else:
    Regret_pills = 0

global TableCheck
TableCheck = True

global GlassCheck
GlassCheck = False

global GlassFillCheck
GlassFillCheck = False

global SeedCheck
SeedCheck = False

global RobotCheck
RobotCheck = False

global CactusCheck
CactusCheck = False

global RegretJuiceCheck
RegretJuiceCheck = False

global LitCandleCheck
LitCandleCheck = False

global BookCheck
BookCheck = False

global Drawer3Check
Drawer3Check = False

global TelescopeCheck
TelescopeCheck = False

global DoorKeyCheck
DoorKeyCheck = False

global MagnetCheck
MagnetCheck = False

global KnifeCheck
KnifeCheck = False

global HammarCheck
HammarCheck = False

global TeddyBearCheck
TeddyBearCheck = True

global ThuleciteCheck
ThuleciteCheck = False

global SofaCheck
SofaCheck = True

global WireCheck
WireCheck = False

global ComputerCheck
ComputerCheck = True

global GearCheck
GearCheck = False

global RadioCheck
RadioCheck = False

global KnifeCaseCheck
KnifeCaseCheck = True

global LakeCheck
LakeCheck = False

global DiningTableCheck
DiningTableCheck = True

global CandleCheck
CandleCheck = False

global BathTubCheck
BathTubCheck = True

global MatchBoxCheck
MatchBoxCheck = False

global DroplightCheck
DroplightCheck = True

global PaperCheck
PaperCheck = False

global MetalCheck
MetalCheck = False

global KeyboardCheck
KeyboardCheck = False

"""globals"""

#In the living room
def LivingRoom():
    global TeammateCheck
    
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
    global TeammateCheck
    global DoorCheck
    
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
    global TeammateCheck
    
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
    global TeammateCheck
    
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
            ObjectChoiceK()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            Kitchen()
    ActionChoiceK()

#On the balcony
def Balcony():
    global TeammateCheck
    global FishingRodCheck
    global LakeCheck
    
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
            if LakeCheck is True:
                print "Lake"
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
    global TeammateCheck
    global AtticCheck
    
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
    global TeammateCheck
    global BookShelfCheck
    
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
    global TeammateCheck
    
    TeammateCheck = True
    print "You are now in the study room."
    if TeammateCheck is True:
        print "Type 'talk' or 't' to talk to Heny."
    print "Type 'move' or 'm' to check other parts of the room."
    print "Type 'examine' or 'e' to check what is in the study room."
    print "Type 'bag' or 'b' to check what is in the bag."

    def ActionChoiceA():
        ActionChoice = raw_input()
        if ActionChoice == "m" or ActionChoice == "move":
            print "Which room do you want to go to?"
            print "Bedroom"
            RoomChoice()
        elif ActionChoice == "e" or ActionChoice == "examine":
            print "Tape2"
            ObjectChoiceA()
        elif ActionChoice == "t" or ActionChoice == "talk":
            Heny()
        elif ActionChoice == "b" or ActionChoice == "bag":
            Bag()
        else:
            print "Invalid Comment. Please make a proper choice."
            Attic()
    ActionChoiceA()


"""Object Choice"""

#Object Choice in the Study Room
def ObjectChoiceS():
    global Drawer1Check
    global Drawer2Check
    global Drawer3Check
    global ShovelCheck
    global PillCheck
    global TeddyBearCheck
    global KnifeCheck
    global ThuleciteCheck
    global HammarCheck
    global ComputerCheck
    global GearCheck
    global BookCheck
    global DoorKeyCheck
    global BookShelfCheck
    global RobotCheck
    global CactusBreak
    global LitCandleCheck
    global RegretJuiceCheck
    global SafeCheck
    global MoneyCheck
    
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

    if ObjectChoose.lower() == "drawer3":
        if Drawer3Check is True:
            print "I have gotton seven questions for you to answer. You may ignore these if you wish."
            print "Which element are arsonists most closely related to?"
            print "Which nation does Oscar Wilde belong to?"
            print "Which super hero was bitten by a spider?"
            print "Which game includes a war between birds and pigs?"
            print "Which country is famous for its people's attitude towards cows?"
            print "How many planets were there in the galaxy?"
            print "What color is chlorophyll unable to absorb?"
            StudyRoom()
        if Drawer3Check is False:
            print "Sorry, somebody else has just taken all the questions."
            StudyRoom()

    if ObjectChoose.lower() == "teddy bear":
        if TeddyBearCheck is True:
            print "This is a cute teddy bear."
            if KnifeCheck is True:
                print "The teddy bear is cut open."
                print "You have gotten thulecite"
                ThuleciteCheck = True
                TeddyBearCheck = False
                StudyRoom()
        if TeddyBearCheck is False:
            print "The teddy bear is broken"
            StudyRoom()

    if ObjectChoose.lower() == "computer":
        if ComputerCheck is True:
            print "This is a computer."
            if HammarCheck is True:
                print "Oh, you have a hammar. The computer is smashed."
                print "You have gotten gears."
                GearCheck = True
                HammarCheck = False
                ComputerCheck = False
                StudyRoom()
        if ComputerCheck is False:
            print "This is a broken computer with a hammar stucked in it."
            StudyRoom()

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
                    if DoorKeyCheck is True:
                        Ending1()
                    if DoorKeyCheck is False:
                        print "Sorry, you still lack something important."
                        StudyRoom()
                else:
                    print "I wish you could make a better choice."
                    BookChoice = raw_input()
            print "Darwin's philosophy"
            print "Every object has its use... or not?"
            StudyRoom()

    if ObjectChoose.lower() == "safe":
        BookShelfCheck = True
        print "If you have the right things in your bag, the spaces will be automatically filled."
        if RobotCheck is False:
            print "Space one: looks like a robot (not found)"
        if RobotCheck is True:
            print "Space one: Robot"
        if CactusCheck is False:
            print "Space two: looks like a kind of plant (not found)"
        if CactusCheck is True:
            print "Space two: Cactus"
        if RegretJuiceCheck is False:
            print "Space three: looks like a glass (not found)"
        if RegretJuiceCheck is True:
            print "Space three: Regret Juice"
        if LitCandleCheck is False:
            print "Space four: looks like a candle (not found)"
        if LitCandleCheck is True:
            print "Lit Candle"
        print "Space five: a vase with soil"
        if RobotCheck is True and CactusCheck is True and RegretJuiceCheck is True and LitCandleCheck is True:
            print "You have successfully found everything. The safe is now opened."
            SafeCheck = True
        if SafeCheck is True:
            print "Congratulations. You have found a book in the safe. The book is called Catholic Belief and is put into your bag."
            BookCheck = True
        StudyRoom()
    if ObjectChoose.lower() == "space five":
        if ShovelCheck is False:
            print "This is just a vase. Go and fetch other essential elements to open the safe."
        if ShovelCheck is True:
            print "Wow, something's in the vase, do you want to dig it out?"
            vasedig = raw_input("Type y or n")
            if vasedig == "y":
                print "Oh, the shovel is stuck in the vase."
                print "You have found a $100 bill."
                MoneyCheck = True
                ShovelCheck = False
            if vasedig == "n":
                StudyRoom()

#Object Choice in the Living Room
def ObjectChoiceL():
    global TelevisionCheck
    global TableCheck
    global GlassCheck
    global SofaCheck
    global KnifeCheck
    global WireCheck
    
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

    elif ObjectChoose.lower() == "table":
        if TableCheck is True:
            print "You have collected a water glass"
            GlassCheck = True
            TableCheck = False
            LivingRoom()
        if TableCheck is False:
            print "There's nothing on the table"
            LivingRoom()
    elif ObjectChoose.lower() == "sofa":
        if SofaCheck is True:
            print "There is a wire behind the sofa."
            if KnifeCheck is True:
                print "Oh, you have a knife."
                KnifeCut = raw_input("Do you want to cut the wire? Type y or n: ")
                if KnifeCut == "y":
                    print "The house goes into complete darkness."
                    WireCheck = True
                    SofaCheck = False
                    LivingRoom()
                if KnifeCut == "n":
                    print "Maybe come back later"
                    LivingRoom()
        if SofaCheck is False:
            print "There is nothing here."
            LivingRoom()





#Object Choice in the Kitchen
def ObjectChoiceK():
    global KnifeCaseCheck
    global KnifeCheck
    global HammarCheck
    global RefrigeratorCheck
    global LitCandleCheck
    
    ObjectChoose = raw_input()
    if ObjectChoose.lower == "knife case":
        if KnifeCaseCheck is True:
            print "You have received a knife."
            print "You have received a hammar."
            KnifeCheck = True
            HammarCheck = True
            KnifeCaseCheck = False
            Kitchen()
        if KnifeCaseCheck is False:
            print "You have already taken away everything from this knife case."
            Kitchen()
    if ObjectChoose.lower == "refrigerator":
        if RefrigeratorCheck is True:
            print "You have found a magnet."
            if LitCandleCheck is True:
                print "Sorry, the fire on your candle has died out."
                LitCandleCheck = False
                Kitchen()
        if RefrigeratorCheck is False:
            print "There's nothing else in the refrigerator."
            if LitCandleCheck is True:
                print "Sorry, the fire on your candle has died out."
                LitCandleCheck = False
                Kitchen()

#Object Choice in the Dining Room
def ObjectChoiceD():
    global DroplightCheck
    global RadioCheck
    global DiningTableCheck
    global CandleCheck
    
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "droplight":
        if DroplightCheck is True:
            print "Wow, there is a radio in the droplight."
            RadioCheck = True
            DiningRoom()
        if DroplightCheck is False:
            print "This is a droplight."
            DiningRoom()
    if ObjectChoose.lower() == "dining table":
        if DiningTableCheck is True:
            print "There is a candle on the table."
            CandleCheck = True
            DiningTableCheck = False
            DiningRoom()
        if DiningTableCheck is False:
            print "There's nothing on the table."
            DiningRoom()


#Object Choice in the Bathroom
def ObjectChoiceBath():
    global GlassCheck
    global GlassFillCheck
    global AtticCheck
    global BathTubCheck
    global MatchBoxCheck
    
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "basin":
        if GlassCheck is True:
            GlassFill = raw_input("Do you want to fill your glass? Type y or n")
            if GlassFill == "y":
                print "Your glass is filled."
                GlassFillCheck = True
                Bathroom()
            else:
                print "Maybe you can come later."
                Bathroom()
        if GlassCheck is False:
            print "You should come back later."
            Bathroom()
    if ObjectChoose.lower() == "mirror":
        MirrorQuestion = raw_input("Hahahahaha! I am a really smart guy since I will never admit that I am stupid. Now, I am most proud of myself because for all my accounts, I use the same password that is most difficult to guess because it does not contain a single number. Now, make a try. If you succeed, I will give you a big surprise. Password: ")
        if MirrorQuestion == "password":
            print "Congratulations!"
            AtticCheck = True
            Attic()
    if ObjectChoose.lower() == "bath tub":
        if BathTubCheck is True:
            print "You have found a match box in the bath tub."
            MatchBoxCheck = True
            Bathroom()
        if BathTubCheck is False:
            print "You have found another match box in the bath tub."
            MatchBoxCheck = True
            Bathroom()

#Object Choice in the Bedroom
def ObjectChoiceBed():
    global TelephoneCheck
    global MoneyCheck
    
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
    if ObjectChoose.lower() == "bed":
        print "You have taken a nap."
        Bedroom()
    if ObjectChoose.lower() == "wardrobe":
        print "Sorry, your teammate is not in here and this wardrobe is not movable."
        Bedroom()


#Object Choice in the Balcony
def ObjectChoiceBal():
    global TelescopeCheck
    global LakeCheck
    global FishingRodCheck
    global MagnetCheck
    global DoorKeyCheck
    
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "telescope":
        if TelescopeCheck is False:
            print "Through the telescope, you see an old man fishing."
            print "He suddenly raises his head and stares at your direction."
            print "He puts on a weird smile and jumps into the lake with his fishing rod."
            TelescopeCheck = True
            LakeCheck = True
        if TelescopeCheck is True:
            FishingRodCheck = True
            print "A dead body floats on the surface of the lake."
    if ObjectChoose.lower() == "fishing rod":
        FishingRodUse = raw_input("Do you want to use the fishing rod? Type y or n: ")
        if FishingRodUse == "y":
            if MagnetCheck is True:
                print "You have gotten a door key."
                DoorKeyCheck = True
            else:
                print "You have gotten absolutely nothing."
        if FishingRodUse == "n":
            Balcony()

#Object Choice in the Attic
def ObjectChoiceA():
    global RadioCheck
    
    ObjectChoose = raw_input()
    if ObjectChoose.lower() == "tape2":
        if RadioCheck is True:
            RadioUse = raw_input("Do you want to put tape2 into the radio?")
            if RadioUse == "y":
                print "Congratulations, you have successfully saved your teammate Heny. From now on, you can talk to him and get a whole lot of information."
                Attic()
            if RadioUse == "n":
                print "I think you should listen to the tape."
                Attic()
        if RadioCheck is False:
            print "You can't listen to tape2 just with this single tape, right?"
            Attic()



"""Object Choice"""

#BagCheck
def Bag():
    global ShovelCheck
    global BookCheck
    global MoneyCheck
    global GlassCheck
    global GlassFillCheck
    global SeedCheck
    global CactusCheck
    global RobotCheck
    global RegretJuiceCheck
    global LitCandleCheck
    global DoorKeyCheck
    global MagnetCheck
    global KnifeCheck
    global HammarCheck
    global ThuleciteCheck
    global WireCheck
    global GearCheck
    global RadioCheck
    global CandleCheck
    global MatchBoxCheck
    global PaperCheck
    global MetalCheck
    global KeyboardCheck
    
    
    print "tape1"
    if ShovelCheck is True:
        print "shovel"
    if BookCheck is True:
        print "Catholic Belief"
    if MoneyCheck is True:
        print "$100 Bill"
    if GlassCheck is True:
        print "a glass"
    if GlassFillCheck is True:
        print "a glass of water"
    print "Regret Pill * " + str(Regret_pills)
    if SeedCheck is True:
        print "cactus seed"
    if CactusCheck is True:
        print "cactus"
    if RobotCheck is True:
        print "robot"
    if RegretJuiceCheck is True:
        print "regret juice"
    if LitCandleCheck is True:
        print "a lit candle"
    if DoorKeyCheck is True:
        print "key"
    if MagnetCheck is True:
        print "magnet"
    if KnifeCheck is True:
        print "knife"
    if HammarCheck is True:
        print "hammar"
    if ThuleciteCheck is True:
        print "thulecite"
    if WireCheck is True:
        print "wire"
    if GearCheck is True:
        print "gear"
    if RadioCheck is True:
        print "radio"
    if CandleCheck is True:
        print "candle"
    if MatchBoxCheck is True:
        print "a box of match"
    if PaperCheck is True:
        print "paper"
    if MetalCheck is True:
        print "metal"
    if KeyboardCheck is True:
        print "keyboard"

    Bagchoose()
    LivingRoom()

#Use of object: Bag choose
def Bagchoose():

    global FishingRodCheck
    global ShovelCheck
    global SafeCheck
    global BookShelfCheck
    global MoneyCheck
    global Drawer1Check
    global Drawer2Check
    global TelevisionCheck
    global PillCheck
    global Regret_pills
    global TableCheck
    global GlassCheck
    global GlassFillCheck
    global SeedCheck
    global RobotCheck
    global CactusCheck
    global RegretJuiceCheck
    global LitCandleCheck
    global BookCheck
    global Drawer3Check
    global TelescopeCheck
    global DoorKeyCheck
    global MagnetCheck
    global KnifeCheck
    global HammarCheck
    global TeddyBearCheck
    global ThuleciteCheck
    global SofaCheck
    global WireCheck
    global ComputerCheck
    global GearCheck
    global RadioCheck
    global KnifeCaseCheck
    global LakeCheck
    global DiningTableCheck
    global CandleCheck
    global BathTubCheck
    global MatchBoxCheck
    global DroplightCheck
    global PaperCheck
    global MetalCheck
    global KeyboardCheck
    
    Bagchoice = raw_input("Type in an object to examine it: ")
    if Bagchoice.lower() == "tape1":
        if RadioCheck is True:
            print "Yes. It is I who attracted you to here."
            print "You do not need to know who I am."
            print "You have always been a selfish guy who pretends to be generous."
            print "However, you have a best friend whose name is Heny and you have claimed that you would do anything for him."
            print "He is now trapped in this house. You may choose to save him or not."
            print " "
            LivingRoom()
        if RadioCheck is False:
            print "You can't listen just with a tape, right?"
            LivingRoom()
    if Bagchoice.lower() == "shovel":
        print "Seems like it could be used to dig something...as a shovel."
        LivingRoom()
    if Bagchoice.lower() == "catholic belief":
        print "I would say that it is obvious where this book should be placed in."
        if LitCandleCheck is True and BookCheck is True:
            PaperCreate = raw_input("Do you want to lit your book? Type y or n: ")
            if PaperCreate == "y":
                print "You have gotten a piece of paper."
                PaperCheck = True
                LitCandleCheck = False
                CandleCheck = True
                BookCheck = False
        LivingRoom()
    if Bagchoice.lower() == "$100 bill":
        print "Of course, money should be used to buy things."
        LivingRoom()
    if Bagchoice.lower() == "a glass":
        print "This is collected from the table."
        LivingRoom()
    if Bagchoice.lower() == "a glass of water":
        print "I think you can do more than just drink it."
        if Regret_pills >= 1:
            RegretJuiceChoose = raw_input("Do you want to create regret juice? Type y or n: ")
            if RegretJuiceChoose == "y":
                print "One pill is used."
                RegretJuiceCheck = True
                Regret_pills -= 1
                GlassFillCheck = False
                LivingRoom()
            if RegretJuiceChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
    if Bagchoice.lower() == "regret pill":
        print "These pills can help you regret."
        Break = raw_input("Which object do you want to change back?")
        if Break.lower() == "cancel":
            LivingRoom()
        if Break.lower() == "cactus":
            print "cactus is changed."
            CactusCheck = False
            SeedCheck = True
            Regret_pills -= 1
            LivingRoom()
        if Break.lower() == "robot":
            print "robot is changed"
            RobotCheck = False
            ThuleciteCheck = True
            WireCheck = True
            GearCheck = True
            MagnetCheck = True
            Regret_pills -= 1
            LivingRoom()
        if Break.lower() == "a lit candle":
            print "a lit candle is changed"
            LitCandleCheck = False
            CandleCheck = True
            Regret_pills -= 1
            LivingRoom()
        if Break.lower() == "regret juice":
            print "regret juice is changed"
            RegretJuiceCheck = False
            GlassFillCheck = True
            LivingRoom()
        if Break.lower() == "paper":
            print "paper is changed"
            PaperCheck = False
            BookCheck = True
            Regret_pills -= 1
            LivingRoom()
        if Break.lower() == "metal":
            print "metal is changed"
            MetalCheck = False
            DoorKeyCheck = True
            Regret_pills -= 1
            LivingRoom()
        if Break.lower() == "keyboard":
            print "keyboard is changed"
            KeyboardCheck = False
            WireCheck = True
            GearCheck = True
            Regret_pills -= 1
            LivingRoom()
        else:
            print "This cannot be changed. Sorry."
            LivingRoom()
    if Bagchoice.lower() == "cactus seed":
        print "This seed is bought from an advertisement and has great use."
        if GlassFillCheck is True and if SeedCheck is True:
            SeedChoose = raw_input("You have a glass of water in your bag, do you want to water the seed? Type y or n")
            if SeedChoose == "y":
                print "The seed turns into a cactus."
                CactusCheck = True
                SeedCheck = False
                GlassFillCheck = False
                GlassCheck = True
                LivingRoom()
            if SeedChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
    if Bagchoice.lower() == "cactus":
        print "I would say this is just a cactus."
        LivingRoom()
    if Bagchoice.lower() == "robot":
        print "A robot can be used to do what...? I don't know."
        LivingRoom()
    if Bagchoice.lower() == "regret juice":
        print "At least it does not have as much effect as when it is still pills."
        LivingRoom()
    if Bagchoice.lower() == "a lit candle":
        print "I guess this is just a candle on fire."
        LivingRoom()
    if Bagchoice.lower() == "key":
        print "This key can be used to open a lock."
        if LitCandleCheck is True and DoorKeyCheck is True:
            MetalCreate = raw_input("Do you want to melt down your key? Type y or n: ")
            if MetalCreate == "y":
                print "You have gotten a piece of metal."
                MetalCheck = True
                LitCandleCheck = False
                CandleCheck = True
                DoorKeyCheck = False
        LivingRoom()
    if Bagchoice.lower() == "magnet":
        print "This magnet can be used to attract metals."
        if ThuleciteCheck is True and GearCheck is True and MagnetCheck is True and WireCheck is True:
            RobotChoose = raw_input("You have thulecite, gear and wire in your bag, do you want to combine them? Type y or n: ")
            if RobotChoose == "y":
                print "A robot is created."
                RobotCheck = True
                ThuleciteCheck = False
                GearCheck = False
                WireCheck = False
                LivingRoom()
            if RobotChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
        LivingRoom()
    if Bagchoice.lower() == "knife":
        print "I think its usage is more like that of a pair of scissors."
        LivingRoom()
    if Bagchoice.lower() == "hammar":
        print "A hammar is usually used to smash things"
        LivingRoom()
    if Bagchoice.lower() == "thulecite":
        print "I would recommend you use a dictionary."
        if ThuleciteCheck is True and GearCheck is True and MagnetCheck is True and WireCheck is True:
            RobotChoose = raw_input("You have wire, gear and magnet in your bag, do you want to combine them? Type y or n: ")
            if RobotChoose == "y":
                print "A robot is created."
                RobotCheck = True
                ThuleciteCheck = False
                GearCheck = False
                WireCheck = False
                LivingRoom()
            if RobotChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
    if Bagchoice.lower() == "wire":
        print "A wire provides electricity."
        if ThuleciteCheck is True and GearCheck is True and MagnetCheck is True and WireCheck is True:
            RobotChoose = raw_input("You have thulecite, gear and magnet in your bag, do you want to combine them? Type y or n: ")
            if RobotChoose == "y":
                print "A robot is created."
                RobotCheck = True
                ThuleciteCheck = False
                GearCheck = False
                WireCheck = False
                LivingRoom()
            if RobotChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
        if ThuleciteCheck is False and GearCheck is True and MagnetCheck is False and WireCheck is True or ThuleciteCheck is True and GearCheck is True and MagnetCheck is False and WireCheck is True or ThuleciteCheck is False and GearCheck is True and MagnetCheck is True and WireCheck is True:
            KeyboardChoose = raw_input("Do you want to create a keyboard with gear and wire? Type y or n: ")
            if KeyboardChoose == "y":
                print "A keyboard is created."
                KeyboardCheck = True
                GearCheck = False
                WireCheck = False
                LivingRoom()
            if KeyboardChoose == "n":
                print "Okay, maybe later."
                LivingRoom()

    if Bagchoice.lower() == "gear":
        print "Can be created by smashing any machine."
        if ThuleciteCheck is True and GearCheck is True and MagnetCheck is True and WireCheck is True:
            RobotChoose = raw_input("You have thulecite, wire and magnet in your bag, do you want to combine them? Type y or n: ")
            if RobotChoose == "y":
                print "A robot is created."
                RobotCheck = True
                ThuleciteCheck = False
                GearCheck = False
                WireCheck = False
                LivingRoom()
            if RobotChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
    if Bagchoice.lower() == "radio":
        print "Radios are used to play tapes."
        LivingRoom()
    if Bagchoice.lower() == "candle":
        print "The candle is gotten from the dining table."
        if CandleCheck is True and MatchBoxCheck is True:
            LitCandleChoose = raw_input("You have match box in your bag, do you want to light the candle? Type y or n: ")
            if LitCandleChoose == "y":
                print "A lit candle is created."
                LitCandleCheck = True
                MatchBoxCheck = False
                CandleCheck = False
                LivingRoom()
            if LitCandleChoose == "n":
                print "Okay, maybe later."
                LivingRoom()
    if Bagchoice.lower() == "a box of match":
        print "Matches are to light things."
        LivingRoom()
    if Bagchoice.lower() == "paper":
        print "A part of the book."
        LivingRoom()
    if Bagchoice.lower() == "metal":
        print "The door key is melt down."
        LivingRoom()
    if Bagchoice.lower() == "keyboard":
        print "If connected to computer, can be used to type things out."
        LivingRoom()
    else:
        print "Please examine something that is in your bag by typing in the correct name."
        Bagchoose()

#Advice from Heny
def Heny()
    print "Hahaha"


#RoomChoice
def RoomChoice():
    global LakeCheck
    
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
    elif RoomChoose.lower() == "lake":
        print "Are you sure that you want to leave the house by jumping into the lake?"
        LakeChoose = raw_input("Type y or n")
        if LakeChoose == "y":
            print "As you try to swim away from the house, you feel grabbed by two hands."
            print "Without knowing what has happened, you drowned into the lake."
        if LakeChoose == "n":
            LakeCheck = False
            Balcony()
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
    print "Remember, you can type 'cancel' to return to the Living Room at specific times."
    LivingRoom()

#A bad ending of the game
def BadEnd():
    print "Sorry, you have been killed by super natural force. The evil spirit is laughing with joy. Hahahahaha."

#Ending one by leaving from Book Shelf
def Ending1():
    global TeammateCheck
    
    if TeammateCheck is True:
        print "Now, it is time for you to make a final choice."
        print "Only one of you can leave from this door."
        print "You have once claimed that you would do anything for your friend Heny, even if it will cost your life. If selfish you choose to die, then your best friend Heny can live."
        print "Make your choice, will you give your door key to your friend Heny?"
        endingchoice2 = raw_input("Type y or n")
        if endingchoice2 == "y":
            print "Heny leaves the house through the door."
            print "A black shadow appears in front of you and reaches out its hands..."
            print " "
            print "Congratulations, you have woken from a nightmare. You have managed to save 'love'(Heny) from 'hatred'(supernatural power)'s hands."
            print "Whole Story Line"
            print "Your friend has betrayed you and were begging for your forgiveness. You were entangled to decide whether you should forgive him. With this feeling of anxiety, you fell into a nightmare. If it proves that you are selfish, then your hatred towards your friend will devour your loving nature and you shall never be able to escape that nightmare. Luckily, you did not let your resentment develop and choose to instead forgive your friend."
        if endingchoice2 == "n":
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