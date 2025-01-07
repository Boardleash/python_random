#################
### RANDOM v1 ###
#################
#
# TITLE: random.py
# AUTHOR: Boardleash (Derek)
# DATE: Saturday, July 27 2024
#
# A script that uses random generation.
# Rather than stick to just numbers or letters though, it will randomly select a function.
# This iteration does not have many functions to choose from, but it is a starting point.
# Also, none of the functions within this script are malicious/have malicious intent.
# Tested on Python Versions 3.12.4 (Windows 11), 3.12.3 (Ubuntu 24.04 LTS Deskttop), and 3.9.19 (RHEL 9 and CentOS Stream 9).

##################
### WHADGYAGET ###
##################

# Define "whadgyaget" function.
def whadgyaget():
    import random
    a=['olaf', 'stubbe', 'sybil', 'yaga', 'krueger', 'dracula', 'dullahan', 'haunt', 'poltergeist', 'djinn']
    b=random.choice(a)
    c=''.join('{0:08b}'.format(ord(x), 'b') for x in b)
    print(f"\nHere's something..." + c + "\n")

###########
### ELM ###
###########

# Define "elm" function.
def elm():
    rd='\033[0;31m'
    brd='\033[1;31m'
    ird='\033[0;91m'
    noc='\033[0m'
    print("""....................................................................................................
.........................................."""+brd+"""%+"""+noc+"""........"""+brd+""":-"""+noc+"""..............................................
..........................................."""+brd+"""%@=:+@@@-"""+noc+"""."""+brd+""":@%"""+noc+"""............................................
................................."""+brd+"""-#"""+noc+""".."""+brd+"""::"""+noc+"""......"""+brd+""":#@@@@@#"""+noc+"""."""+brd+"""-@%"""+noc+"""...........................................
..............................."""+brd+"""*@-"""+noc+"""."""+brd+"""*#**-"""+noc+"""........"""+brd+"""%@@@#"""+noc+""".."""+brd+"""#@#"""+noc+"""..........................................
............................"""+brd+""":%@%"""+noc+""".."""+brd+"""+@@@+"""+noc+"""..........."""+brd+"""@@:"""+noc+""".."""+brd+"""-@@="""+noc+""".........................................
.........................."""+brd+"""-@@@*"""+noc+""".."""+brd+"""%@@:"""+noc+""".............."""+brd+"""-="""+noc+""".."""+brd+"""-@@%"""+noc+"""......."""+brd+"""::"""+noc+"""................................
........................"""+brd+""":@@@@="""+noc+""".."""+brd+"""@@%"""+noc+""".."""+brd+"""%+"""+noc+"""................-....."""+brd+"""+%+"""+noc+"""....................................
......................."""+brd+"""%@@@@#"""+noc+"""."""+brd+"""*@@@@@@="""+noc+""".................."""+brd+""":+%@="""+noc+""".......................................
....................."""+brd+""":@@@@@@@@@@@@@@@-"""+noc+"""..............."""+brd+"""+@@@@@@%"""+noc+""".......................................
....................."""+brd+"""+@@@@@@@@@@@@%@%-"""+noc+"""..........."""+brd+"""-##@@@@@@@@@:"""+noc+"""......................................
....................."""+brd+""":@@@@@@@@@@@@=#*"""+noc+"""........."""+brd+"""*@="""+noc+"""."""+brd+"""=@@@@@@@@@@%"""+noc+"""......................................
......................"""+brd+"""%@@@@@@@@@@*"""+noc+"""........"""+brd+""":#@%="""+noc+"""."""+brd+"""+@@@@@@@@@@@@@+"""+noc+""".....................................
......................"""+brd+"""+@@@@@@@@@%"""+noc+"""......"""+brd+"""-@@@@@#=#@@@@@@@@@@@@@@@"""+noc+""".....................................
......................."""+brd+"""@@@@@@@+"""+noc+"""......"""+brd+"""*@="""+noc+""".."""+brd+"""::"""+noc+""".."""+brd+"""-*%@@@@@@@@@@@@@@*"""+noc+"""....................................
......................."""+brd+"""@@@%#-"""+noc+"""....."""+brd+""":@#"""+noc+""".............."""+brd+"""*@@@@@@@@@@%@#:"""+noc+"""..................................
................................"""+brd+""":@+"""+noc+"""...................."""+brd+"""::::"""+noc+""".........................................
..............................."""+brd+"""#%"""+noc+"""..............................."""+brd+""":-==:"""+noc+"""...............................
.............."""+brd+""":=#%@@@@%:"""+noc+"""."""+brd+""":-"""+noc+""".."""+brd+"""=@@%%%%#+-:"""+noc+"""................"""+brd+"""=*%@@@+:"""+noc+"""....................................
........."""+brd+"""-#@@@@@@@@@%:"""+noc+"""...."""+brd+"""#+@@@@@@@@@@@@@@@@@*=:"""+noc+""".."""+brd+"""-*@@@@@%="""+noc+""".........................................
...."""+brd+"""-#@@@@@@@@@@@@+"""+noc+"""......."""+brd+"""%@@@@@@@@@@@@@@@@@@@@@@@@@@@#:"""+noc+"""............................................
"""+brd+""":#@@@@@@@@@@@@@@#*:"""+noc+"""....."""+brd+"""=@@@@@@@@@@@@@@@@@%%%*==---:---:"""+noc+"""............................................
"""+brd+"""@@@@@@@@@@@@@@@@"""+noc+"""....."""+brd+""":@@@@@@@@=:@@-"""+noc+"""............................"""+brd+""":=#%%#+=:"""+noc+"""............................
"""+brd+"""@@@@@@@@@@@@@@*"""+noc+"""......"""+brd+"""-+%@@#-"""+noc+"""...."""+brd+"""-%*="""+noc+""".................................."""+brd+""":-+*%@@@@@@@@@@@@%#**=-:"""+noc+"""......
"""+brd+"""@@@@@@@@@@@@@+"""+noc+"""......."""+brd+"""+*="""+noc+"""..."""+brd+"""-%.#%-@@"""+noc+"""........."""+brd+"""+@@@@@@@@@@@@@@@@@#*=:"""+noc+""".............."""+brd+"""-*@@@@@@@@@@@="""+noc+"""......
"""+brd+"""@@@@@@@@@@@@@@@@@@@:"""+noc+"""........."""+brd+"""=%-"""+noc+""".."""+brd+"""-@@*@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+-"""+noc+"""........"""+brd+"""-#@#-"""+noc+""".........
"""+brd+"""@@@@@@@@@@@@@@@@:#@:@="""+noc+"""..."""+brd+""":*@@*"""+noc+"""."""+brd+"""#@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%="""+noc+"""...............
"""+brd+"""@@@@@@@@@@@@@@@@@:++-=@**@%::#@@@@@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#="""+noc+""".."""+brd+""":=++:"""+noc+""".........
."""+brd+"""=@@@@@@@@@@@@@@%"""+noc+""".."""+brd+"""#"""+noc+""".."""+brd+"""#:++@@@@@@@@@@@:@@@@@@@:"""+noc+"""."""+brd+"""=@@@@@@@@@@@@@@@@*#@@@@@@@@@@@@*:"""+noc+"""............."""+brd+"""+="""+noc+""".....
....."""+brd+""":=@@@@@@@@@@"""+noc+"""...."""+brd+"""=@-"""+noc+"""."""+brd+"""*@@@@@@@@@@@@@@%=:*#%"""+noc+"""...."""+brd+"""+@@@@@@@@@@@@@@:@@@@@@#=:"""+noc+""".........................
........."""+brd+"""-"""+noc+"""."""+brd+""":+#%@@%"""+noc+"""."""+brd+"""*@@@:"""+noc+"""."""+brd+"""--@@@@@@@@@@#"""+noc+"""....."""+brd+"""-%"""+noc+"""."""+brd+""":="""+noc+"""......"""+brd+"""%@@@@@@@@@@:="""+noc+""".................................
................"""+brd+"""@:"""+noc+"""."""+brd+"""#@@="""+noc+"""..."""+brd+""":%@@@@%=:"""+noc+"""........"""+brd+"""=#="""+noc+""".."""+brd+"""-"""+noc+"""......"""+brd+"""*@@@@@@@@@:"""+noc+"""..................................
................"""+brd+"""*%"""+noc+"""."""+brd+"""%@%=:"""+noc+"""."""+brd+""":@#-"""+noc+"""..............."""+brd+"""*@@@:"""+noc+""".."""+brd+"""::"""+noc+"""...."""+brd+"""-%@@##+#"""+noc+"""...................................
................"""+brd+"""=%.@@@@@=*:"""+noc+"""."""+brd+"""%%:"""+noc+""".........."""+brd+"""=%@@@@@@#"""+noc+""".........."""+brd+""":"""+noc+"""."""+brd+"""--"""+noc+"""....................................
................"""+brd+"""+@@+%#:*="""+noc+""".."""+brd+"""%@@@%+++"""+noc+"""."""+brd+"""@*#@@@@@@@@@@@@@+"""+noc+""".."""+brd+"""-="""+noc+"""......."""+brd+""":"""+noc+"""...................................
................"""+brd+"""+=*#%#==*#*#@@#@@@@#:*#*+--::"""+noc+"""..."""+brd+"""+@@@@@@%%@%=:"""+noc+""".......................................
.................."""+brd+"""@@#%%@@@*--*@@%"""+noc+""".............."""+brd+""":@#+"""+noc+"""."""+brd+"""%@@@@@@%-"""+noc+""".......................................
.................."""+brd+"""#@@@@@@*+*@@@%*%:"""+noc+"""............."""+brd+"""--@"""+noc+""".."""+brd+"""+@@@@#=+-%+"""+noc+"""....................................
.................."""+brd+"""+@@@@@@@@@@@@@@@@%:"""+noc+"""."""+brd+""":-+-===+@@@@@+"""+noc+""".."""+brd+""":@@@@-"""+noc+"""...."""+brd+"""+#:"""+noc+""".................................
.................."""+brd+"""-@@@@@@@@@@@@#*%+@@@+#@@@@@@@*=#%"""+noc+"""....."""+brd+"""=@@%"""+noc+"""......"""+brd+""":%-"""+noc+"""...............................
..................."""+brd+"""@@@@@@@@@@@@=%%==="""+noc+"""."""+brd+"""=:*@@@@@@@@@@-"""+noc+"""......"""+brd+"""**"""+noc+"""........."""+brd+"""*+"""+noc+""".............................
..................."""+brd+"""%@@@@@@@@@@@@@@"""+noc+"""..."""+brd+""":*=*@@@@@@@@@@@@@@%"""+noc+"""..............."""+brd+"""=#"""+noc+"""...........................
..............."""+brd+""":=%@=@@@@@@@@@@%+-"""+noc+"""......"""+brd+""":@@@%@@@@@@@@@@@-"""+noc+"""................."""+brd+"""=#"""+noc+""".........................
..........."""+brd+"""+@@@@@@@-@@@@@@@*"""+noc+"""............"""+brd+"""**+@@@@@@@@@@@@@+"""+noc+""".................."""+brd+"""-%"""+noc+""".......................
....."""+brd+"""=*@@@@@@@@@@@@:@@@@*"""+noc+"""............."""+brd+"""::+:=-@@@@@@@%**#:"""+noc+"""."""+brd+"""*"""+noc+"""..................."""+brd+"""=*"""+noc+""".....................
."""+brd+"""-%@@@@@@@@@@@@@@@@:%*:"""+noc+"""............."""+brd+"""+@-=#-+:@@@@@@@@@@@+#:%"""+noc+"""...................."""+brd+"""#="""+noc+"""...................
.."""+brd+""":@@@@@@@@@@@@@@@%"""+noc+""".................."""+brd+""":::=+%@@@@@@@@@@@@%=*:#:"""+noc+"""..."""+brd+""":"""+noc+"""."""+brd+"""-"""+noc+"""............."""+brd+""":%-"""+noc+""".................
...."""+brd+"""::"""+noc+"""..."""+brd+""":@@@@@@@#"""+noc+"""...................."""+brd+"""-*=+@@@@@@@@@@@@@+%%##%="""+noc+""".."""+brd+"""-#@@@="""+noc+"""............."""+brd+""":"""+noc+"""................
"""+brd+"""#:"""+noc+"""............"""+brd+"""-%*"""+noc+"""................."""+brd+""":=:+="""+noc+"""."""+brd+""":@@@@++@#*#*%*#@#*=-"""+noc+"""."""+brd+"""=+"""+noc+""".....................................
"""+brd+"""@@#"""+noc+"""..............."""+brd+"""#*"""+noc+""".........."""+brd+""":*-+-@+:@+=@@@=:-:"""+noc+"""........"""+brd+""":"""+noc+"""....."""+brd+"""-*"""+noc+"""....."""+brd+"""::"""+noc+""".............................
"""+brd+"""@@@@="""+noc+"""........."""+brd+""":@@@@@*+"""+noc+"""."""+brd+"""=#***=::*@@@%*"""+noc+""".."""+brd+"""%@@@@@@#="""+noc+"""............."""+brd+"""=+*+"""+noc+"""...."""+brd+"""%@@@@@+"""+noc+"""........................
"""+brd+"""@@@@@@="""+noc+"""........"""+brd+"""+@@@@@@@@@#*++@@@@@@@%"""+noc+"""."""+brd+"""*@@@@@@@@@@@@@@@@%@@@@@@@@@-"""+noc+"""."""+brd+"""#@@@@@@@@@:"""+noc+"""......................
"""+brd+"""@@@@@@@@@%="""+noc+"""..."""+brd+"""#@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@-"""+noc+"""."""+brd+"""%@@@@@@@@@+"""+noc+""".....................
"""+brd+"""@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"""+noc+"""."""+brd+"""@@@*++*@-=*"""+noc+"""....................
"""+brd+"""@@@@@@@@@@@@+"""+noc+""".........."""+brd+""":+@@@@@@@@@@@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::@#"""+noc+"""........"""+brd+""":"""+noc+"""...................
"""+brd+"""::#@@@@@@@@-"""+noc+"""..............."""+brd+""":#@@@@@@@@@"""+noc+"""....."""+brd+"""-=+#%%@@@@@@@%*+:"""+noc+"""......."""+brd+"""-#"""+noc+"""."""+brd+"""=*"""+noc+"""........."""+brd+""":=="""+noc+"""................
"""+brd+""":"""+noc+"""..."""+brd+"""-@@@@@-"""+noc+"""..................."""+brd+"""=@@@@@@:"""+noc+""".............................."""+brd+"""-+"""+noc+"""........"""+brd+""":@@@@@@-"""+noc+"""..............
"""+brd+""":"""+noc+"""......"""+brd+"""=@:::"""+noc+""".."""+brd+""":"""+noc+"""."""+brd+""":"""+noc+"""."""+brd+""":"""+noc+"""............"""+brd+""":+@@@#-:"""+noc+""".............................."""+brd+"""*-"""+noc+""".."""+brd+""":"""+noc+""".."""+brd+""":"""+noc+"""."""+brd+"""=@@@@@@@%::"""+noc+"""...........
"""+brd+"""-"""+noc+"""......"""+brd+"""-#@@@@@@@@@@%=::::::"""+noc+"""....."""+brd+"""::#@@@@@@@@@%#*=-::"""+noc+"""."""+brd+""":::::::::"""+noc+"""."""+brd+""":::::::-#::::#@@%@@@@@@@@@=::"""+noc+"""."""+brd+""":"""+noc+""".......
"""+brd+"""-:::::#@@@@@@@@@@@@@@@@%=:::::::::+@@@@@@@@@@@@@@@@@@@@@@#*+=---::::::--=#@@@@@@@@@@@*:*@+:::::"""+noc+""".....
"""+brd+"""@#:::@@@@@@@@@@@@@@@@@@@@@#::::::-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:::=@:::::"""+noc+"""....
"""+brd+"""@@@#@@@@@@@@@@@@@@@@@@@@@@@@#::::%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+::-*+:::::-::"""+noc+"""....."""+brd+""":"""+noc+"""
"""+brd+"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:"""+noc+"""."""+brd+"""::"""+noc+"""...."""+brd+"""::"""+noc+"""........."""+brd+""":"""+noc+"""
"""+brd+"""%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:::-+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:.."""+brd+""":.."""+brd+""":::#@@@@%-...."""+brd+""":
"""+brd+"""%%=-+:"""+noc+""".."""+brd+"""-:+%@@@@@@@@@@@@@@@@@@@+::::::::::::"""+noc+"""..."""+brd+""":=*%@@@@@@@@@@@@@@@@@@@@%#*:"""+noc+"""........."""+brd+"""=@@@@@@@@@@%:"""+noc+""".."""+brd+""":"""+noc+"""
"""+brd+"""-"""+noc+""".........."""+brd+"""*:"""+noc+"""."""+brd+""":+%@@@@@@@@@@@@@@::::::::::::::::::::::::"""+noc+""".."""+brd+""":"""+noc+""".........................."""+brd+""":*@@@@@@@@@@%:::"""+noc+"""
"""+brd+"""-"""+noc+"""............."""+brd+"""=*"""+noc+""".."""+brd+"""-=%@@@@@@@@@+::::::::::::::::::::::"""+noc+"""............................"""+brd+""":::*%@@@@@@@@@@@@::"""+noc+"""
"""+brd+"""-"""+noc+"""..................."""+brd+"""-+=@@@@@@@@%*-:::::::::::::::::"""+noc+"""............................"""+brd+""":+@@@@@@@@@@@@@@=#@@-"""+noc+"""
""")
    print("                         ...when you sleep, do you dream...")
    print("                               hahahahahahahahahahaha\n")

##############
### RECIPE ###
##############

# Define "recipe" function.
def recipe():
    import platform
    import subprocess
    import time
    import webbrowser
    param=''
    if platform.system().lower() == 'windows':
        param='-n'
    else:
        param='-c'
    testping=subprocess.run(['ping', param, '1', '8.8.8.8'], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if testping.returncode == 1:
        print("   ....oh, it seems like I can't reach the Internet.  I was hoping to fetch you a recipe, but am unable to....\n")
    else:
        print("Hey!  How about this?\n")
        time.sleep(2)
        webbrowser.open('https://www.allrecipes.com/recipe/10740/pumpkin-chocolate-chip-cookies-iii/')

################
### DATEINFO ###
################

# Define "dateinfo" function.
def dateinfo():
    parityone=0
    while parityone == 0:
        day=input("Please enter the numerical day that you were born (1-31): ")
        month=input("Please enter the numerical month at you were born (1-12): ")
        year=input("Please enter the year that you were born (1920-2024): ")
        if (int(day) in range(1,32)) and (int(month) in range(1,13)) and (int(year) in range(1920,2025)):
            total=int(day)+int(month)+int(year)
            subtraction=int(year)-int(month)-int(day)
            multiplication=int(day)*int(month)*int(year)
            division=int(year)/int(month)/int(day)
            print("\nThe sum of your birth date is: "+str(total))
            print("The difference of your birth date is: "+str(subtraction))
            print("The product of your birth date is: "+str(multiplication))
            print("The quotient of your birth date is: "+str(division)+"\n")
            parityone=1
        else:
            print("\nIt appears that you made an entry that is either not within the specified range or is not a number.  Please try again.\n")

#####################
### MAIN FUNCTION ###
#####################

# Define the "primary condition" function that will use an if/else statement with the user response as the condition.
def primary_condition():
    import random
    import time
    response=input("Yes or No?: ")
    # If one of the below forms of "yes" is provided, then pause for 3 seconds and run the random function.
    if response == 'Yes' or response == 'yes' or response == 'Y' or response == 'y':
        print(f"\nAh, gutsy!  Give me a few seconds to find and perform a function!\n")
        time.sleep(3)
        func_list=[whadgyaget, elm, recipe, dateinfo]
        a=random.choice(func_list)()
    # If one of the below forms of "no" is provided, exit the script without performing the random function.
    elif response == 'No' or response == 'no' or response == 'N' or response == 'n':
        print(f"\nNo sweat!  I would be a little nervous too!  No further actions will occur.  Take care!\n")
    # If an invalid response if provided, let the user know and re-run the "primary condition" function.
    else:
        print(f"\nThat's not a valid answer!  Please respond with 'Yes', 'yes', 'Y', 'y' OR 'No', 'no', 'N', 'n'\n")
        primary_condition()

# Run the script.
print(f"\nGreetings!  This script will randomly perform a function!  All you need to do is type 'yes' or 'no'.\n")
primary_condition()
