__author__ = 'BenYang'

print "--------------"
print "|Hello, world|"
print "--------------"

"""globals"""
global name

global physicscheck
physicscheck = False

global scorechange
scorechange = False

global diary1check
diary1check = False

global studentusername

global physicsscore
physicsscore = "32.25"

global newmessage1
newmessage1 = False


"""globals"""

def diary():
    print "Welcome to your diary."
    if scorechange is True:
        print "** You have entered a new diary entry **"
    print "Type n to create new entries."
    print "Type c to check past entries."
    print "Type e to exit"

    def pastentries():
        print "Type the date to check the entry."
        print "Type e to exit"
        print ""
        print "1.21"
#1.21
        if scorechange is True:
            print "1.27"

        global pastentrieschoice
        pastentrieschoice = raw_input()
        if pastentrieschoice == "1.21":
            print "Woo...physics is really hard. If I do not do well."
            print "possibly I'll just hack into the system to change my score."
            print "Mr.Ao, the admin of TSIMS does not seem like a very smart person."
            global diary1check
            diary1check = True
            pastentries()
#1.27
        elif pastentrieschoice == "1.27" and scorechange is True:
            print "32.25...what kind of score is that...so weird..."
            print "doesn't matter now"
            print "And lyra's message...I think she's trying to say something else"
            pastentries()

        elif pastentrieschoice == "e":
            mainmenu()

        else:
            print "Invalid command."
            pastentries()


    def diarychoice():
        diarychoose = raw_input()
        if diarychoose == "c":
            pastentries()
        elif diarychoose == "n":
            print name+":Hmm...there is really nothing to say."
            print ""
            diary()
        elif diarychoose == "e":
            mainmenu()
        else:
            print "Invalid command."
            print ""
            diary()
    diarychoice()


def inputname():
    name1 = raw_input("Please enter your name:")
    print "Are you sure you wanted to be called",
    print name1, "? Enter y or n."

    response = raw_input()

    if response.lower() == "y":
        global name
        name = name1
        print "Hi, "+name1+"."
        mainmenu()
    else:
        inputname()

def student():
    print "TSIMS Database Login"
    global studentusername
    studentusername = raw_input("Student Number:")
    studentpassword = raw_input("Password:")
    print "Welcome, "+name
    print "Physcis grade has been released. Press Enter to check your grades."
    raw_input()
    print "Your score is 32.25/100. "
    print "Press Enter to exit"
    raw_input()
    global physicscheck
    physicscheck = True
    mainmenu()

def teacherui(teachername):
    print "Welcome, "+teachername
    print ""
    global newmessage1
    if newmessage1 is True:
        print "*** NEW MESSAGE! ***"
    print "Type i_student number (e.g i_20138226) to see student info."
    print "Type t to see notes"
    print "Type m to see messages"
    print "Type e to exit"

    def tuiexit(teachername):
        print "Type e to return"
        raw_input()
        teacherui(teachername)

    tuic = raw_input()

    global studentusername
    if tuic == "i_"+str(studentusername):
        print name+"'s grade report"
        print "Chinese A SL 78"
        print "Math HL 68"
        print "English B SL 76"
        print "Physics HL "+physicsscore
        print "Chemistry SL 74"
        print "Economics HL 64"
        print ""

        def changescore():
            print "Type subject to make adjustments."
            print "Type e to exit"
            subject = raw_input()
            if subject.lower() == "physics":
                global physicsscore
                physicsscore = raw_input("Type a new score:")
                global scorechange
                scorechange = True
                global newmessage1
                newmessage1 = True
                tuiexit("mrao")
            elif subject == "e":
                teacherui("mrao")
            else:
                print "Invalid command."
                tuiexit("mrao")

        changescore()
    if tuic == "e":
        mainmenu()
    if tuic == "t":
        if teachername == "mrao":
            print "No notes written"
            tuiexit("mrao")
    if tuic == "m":
        print ""
        print "Type number before sender to view message"
        print ""

        if teachername == "mrao":
            global scorechange
            if scorechange is False:
                print "1 Lyra"
                mraom = raw_input()
                if mraom == "1":
                    print ""
                    print "Lyra:"
                    print ""
                    print "Physics is not that hard...really"
                    print "A is easy to get."
                    print "Some students just aren't paying attention"
                    print "Simple problems like these..."
                    print "What on earth are they thinking..."
                    print "Oh...maybe you are the wrong person to complain to."
                    print "Really...I'm just so upset."
                    print "Doing what I told them to do isn't that hard..."
                    print ""
                    print "If you have time, I can buy you a beer."
                    print "Sure you do have time...I know it."
                    print ""
                    print "Still not making up your mind?"
                    print "Come on."
                    print "Or I'll tell you what's happened"
                    print "Ready for a hint?"
                    print "Everything has a start."
                    print ""
                    print ""
                    print "Press Enter to exit"
                    raw_input()
                    teacherui("mrao")
                else:
                    print "Invalid command."
                    tuiexit("mrao")
            elif scorechange is True:
                print "1 Hector"
                print "2 Lyra"
                mraom = raw_input()
                if mraom == "1":
                    print ""
                    print "Hector:"
                    print ""
                    print "You haven't come to school for three days, what happened?"
                    print "Anyway, finally Lyra's gone."
                    print "Hope she did not tell anyone her password."
                    print "Thanks a lot for helping me."
                    print ""
                    print "Oh..if Lyra send you something, just get rid of it."
                    print ""

                    newmessage1 = False
                    tuiexit("mrao")

                elif mraom == "2":
                    print ""
                    print "Lyra:"
                    print ""
                    print "Physics is not that hard...really"
                    print "A is easy to get."
                    print "Some students just aren't paying attention"
                    print "Simple problems like these..."
                    print "What on earth are they thinking..."
                    print "Oh...is this a game?"
                    print "Really?"
                    print "Don't you play with me"
                    print ""
                    print ""
                    print "If I find out your secret,"
                    print "Somebody will disclose it"
                    print ""
                    print ""
                    print "Still not giving up?"
                    print "Come here."
                    print "Or get out"
                    print "Ready for a hint? You are chosen."
                    print "E"
                    print ""

                    tuiexit("mrao")
                else:
                    print "Invalid command."
            else:
                print "20130930"

        elif teachername == "lyra":
            print "1 Lyra"
            lyram = raw_input()
            if lyram == "1":
                "The truth"

    elif teachername == "lyra":
        print "Welcome to level two (which is not constructed yet)"

def teacher():
    print "TSIMS Database Login"
    teacherusername = raw_input("Username:")
    teacherpassword = raw_input("Password:")

    if teacherusername == "admin" and teacherpassword == "admin":
        print "Login success"
        teacherui("mrao")
    elif teacherusername.lower() == "lyra" and teacherpassword == "32.25":
        print "Welcome, Lyra"
        teacherui("lyra")
    else:
        print "Invalid combination"
        print "Type e to exit"
        print "Type t to try again"
        invalidcombinationchoice = raw_input()
        if invalidcombinationchoice == "e":
            mainmenu()
        else:
            teacher()


def mainmenu():
    print "Welcome to your Personal Electronic System."
    print "Type d to open your diary."
    print "Type t to open TSIMS Database (Student)."

    if physicscheck is True and diary1check is True:
        print "Type h to open TSIMS Database (Teacher)."

    global mainmenuchoice
    mainmenuchoice = raw_input()
    if mainmenuchoice == "t":
        student()
    elif mainmenuchoice == "d":
        diary()
    elif mainmenuchoice == "h" and physicscheck is True:
        teacher()
    else:
        print "Invalid command."
        mainmenu()

inputname()
