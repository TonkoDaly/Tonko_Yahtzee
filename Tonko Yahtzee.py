import tkinter as tk
import random
from collections import Counter

r = tk.Tk()
r.geometry('900x900')
r.title("Tonko's Yahtzee")
c = tk.Canvas(r, width=900, height=900)
c.pack()

turncounter=0
multiple1=0
multiple2=0
multiple3=0
multiple4=0
multiple5=0
multiple6=0
threeok=0
fourok=0
fullhouse=0
smallstraight=0
largestraight=0
fiveok=0
chance=0

def roll_dice():

    # Global variables
    global rolls
    global die1
    global die2
    global die3
    global die4
    global die5
    global multiple1
    global multiple2
    global multiple3
    global multiple4
    global multiple5
    global multiple6
    global threeok
    global fourok
    global fullhouse
    global smallstraight
    global largestraight
    global fiveok
    global chance

    # Unlock dice
    lock1button.configure(state='normal')
    lock2button.configure(state='normal')
    lock3button.configure(state='normal')
    lock4button.configure(state='normal')
    lock5button.configure(state='normal')

    # Set dice
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}

    # Check if dice are unlocked and roll
    if lock1button['text'] == 'Unlocked':
        die1 = random.choice(dice)
    if lock2button['text'] == 'Unlocked':
        die2 = random.choice(dice)
    if lock3button['text'] == 'Unlocked':
        die3 = random.choice(dice)
    if lock4button['text'] == 'Unlocked':
        die4 = random.choice(dice)
    if lock5button['text'] == 'Unlocked':
        die5 = random.choice(dice)

    # Set dice as pictures
    ldice.configure(text=f'{die1} {die2} {die3} {die4} {die5}')
    c.create_window(450, 250, window=ldice)

    # Track rerolls and lock if 0
    rolls-= 1
    if rolls == 1:
        label1['text'] = "You have " + str(rolls) + " reroll remaining"
    else:
        label1['text'] = "You have " + str(rolls) + " rerolls remaining"
    if rolls == 0:
        lock1button.configure(state='disabled')
        lock2button.configure(state='disabled')
        lock3button.configure(state='disabled')
        lock4button.configure(state='disabled')
        lock5button.configure(state='disabled')
        rollbutton.configure(state='disabled')

    # Run scores
    dice = d[die1], d[die2], d[die3], d[die4], d[die5]
    counterdice = Counter(dice)
    countdice = counterdice[1], counterdice[2], counterdice[3], counterdice[4], counterdice[5], counterdice[6]

    # Top half calcs
    multiple1 = dice.count(1) * 1
    multiple2 = dice.count(2) * 2
    multiple3 = dice.count(3) * 3
    multiple4 = dice.count(4) * 4
    multiple5 = dice.count(5) * 5
    multiple6 = dice.count(6) * 6

    # Three of a kind calc
    if all(i < 3 for i in countdice):
        threeok = 0
    else:
        threeok = sum(dice)

    # Four of a kind calc
    if all(i < 4 for i in countdice):
        fourok = 0
    else:
        fourok = sum(dice)

    # Full house calc
    if countdice.count(3) == 1 and countdice.count(2) == 1:
        fullhouse = 25
    else:
        fullhouse = 0

    # Small straight calc
    if dice.count(1) > 0 and dice.count(2) > 0 and dice.count(3) > 0 and dice.count(4) > 0:
        smallstraight = 30
    elif dice.count(2) > 0 and dice.count(3) > 0 and dice.count(4) > 0 and dice.count(5) > 0:
        smallstraight = 30
    elif dice.count(3) > 0 and dice.count(4) > 0 and dice.count(5) > 0 and dice.count(6) > 0:
        smallstraight = 30
    else:
        smallstraight = 0

    # Large straight calc
    if dice.count(1) > 0 and dice.count(2) > 0 and dice.count(3) > 0 and dice.count(4) > 0 and dice.count(5) > 0:
        largestraight = 40
    elif dice.count(2) > 0 and dice.count(3) > 0 and dice.count(4) > 0 and dice.count(5) > 0 and dice.count(6) > 0:
        largestraight = 40
    else:
        largestraight = 0

    # Yahtzee calc
    if all(i < 5 for i in countdice):
        fiveok = 0
    else:
        fiveok = 50

    # Chance calc
    chance = sum(dice)

    # Make score display
    if selectAbutton.winfo_exists():
        labelA3.configure(text=multiple1)
        selectAbutton.configure(state='normal')
    if selectBbutton.winfo_exists():
        labelB3.configure(text=multiple2)
        selectBbutton.configure(state='normal')
    if selectCbutton.winfo_exists():
        labelC3.configure(text=multiple3)
        selectCbutton.configure(state='normal')
    if selectDbutton.winfo_exists():
        labelD3.configure(text=multiple4)
        selectDbutton.configure(state='normal')
    if selectEbutton.winfo_exists():
        labelE3.configure(text=multiple5)
        selectEbutton.configure(state='normal')
    if selectFbutton.winfo_exists():
        labelF3.configure(text=multiple6)
        selectFbutton.configure(state='normal')
    if selectGbutton.winfo_exists():
        labelG3.configure(text=threeok)
        selectGbutton.configure(state='normal')
    if selectHbutton.winfo_exists():
        labelH3.configure(text=fourok)
        selectHbutton.configure(state='normal')
    if selectIbutton.winfo_exists():
        labelI3.configure(text=fullhouse)
        selectIbutton.configure(state='normal')
    if selectJbutton.winfo_exists():
        labelJ3.configure(text=smallstraight)
        selectJbutton.configure(state='normal')
    if selectKbutton.winfo_exists():
        labelK3.configure(text=largestraight)
        selectKbutton.configure(state='normal')
    if selectLbutton.winfo_exists():
        labelL3.configure(text=fiveok)
        selectLbutton.configure(state='normal')
    if selectMbutton.winfo_exists():
        labelM3.configure(text=chance)
        selectMbutton.configure(state='normal')

# Locks for the 5 dice
def lock1():
    if lock1button['text'] == 'Unlocked':
        lock1button.configure(text= "Locked", background= "red")
    elif lock1button['text'] == 'Locked':
        lock1button.configure(text="Unlocked", background="green")
def lock2():
    if lock2button['text'] == 'Unlocked':
        lock2button.configure(text= "Locked", background= "red")
    elif lock2button['text'] == 'Locked':
        lock2button.configure(text="Unlocked", background="green")
def lock3():
    if lock3button['text'] == 'Unlocked':
        lock3button.configure(text= "Locked", background= "red")
    elif lock3button['text'] == 'Locked':
        lock3button.configure(text="Unlocked", background="green")
def lock4():
    if lock4button['text'] == 'Unlocked':
        lock4button.configure(text= "Locked", background= "red")
    elif lock4button['text'] == 'Locked':
        lock4button.configure(text="Unlocked", background="green")
def lock5():
    if lock5button['text'] == 'Unlocked':
        lock5button.configure(text= "Locked", background= "red")
    elif lock5button['text'] == 'Locked':
        lock5button.configure(text="Unlocked", background="green")

# Select scores
def selectA():
    selectAbutton.destroy()
    if labelA3["text"] > 0:
        labelA3.configure(foreground="green")
    else:
        labelA3.configure(foreground="brown")
    newturn()
def selectB():
    selectBbutton.destroy()
    if labelB3["text"] > 0:
        labelB3.configure(foreground="green")
    else:
        labelB3.configure(foreground="brown")
    newturn()
def selectC():
    selectCbutton.destroy()
    if labelC3["text"] > 0:
        labelC3.configure(foreground="green")
    else:
        labelC3.configure(foreground="brown")
    newturn()
def selectD():
    selectDbutton.destroy()
    if labelD3["text"] > 0:
        labelD3.configure(foreground="green")
    else:
        labelD3.configure(foreground="brown")
    newturn()
def selectE():
    selectEbutton.destroy()
    if labelE3["text"] > 0:
        labelE3.configure(foreground="green")
    else:
        labelE3.configure(foreground="brown")
    newturn()
def selectF():
    selectFbutton.destroy()
    if labelF3["text"] > 0:
        labelF3.configure(foreground="green")
    else:
        labelF3.configure(foreground="brown")
    newturn()
def selectG():
    selectGbutton.destroy()
    if labelG3["text"] > 0:
        labelG3.configure(foreground="green")
    else:
        labelG3.configure(foreground="brown")
    newturn()
def selectH():
    selectHbutton.destroy()
    if labelH3["text"] > 0:
        labelH3.configure(foreground="green")
    else:
        labelH3.configure(foreground="brown")
    newturn()
def selectI():
    selectIbutton.destroy()
    if labelI3["text"] > 0:
        labelI3.configure(foreground="green")
    else:
        labelI3.configure(foreground="brown")
    newturn()
def selectJ():
    selectJbutton.destroy()
    if labelJ3["text"] > 0:
        labelJ3.configure(foreground="green")
    else:
        labelJ3.configure(foreground="brown")
    newturn()
def selectK():
    selectKbutton.destroy()
    if labelK3["text"] > 0:
        labelK3.configure(foreground="green")
    else:
        labelK3.configure(foreground="brown")
    newturn()
def selectL():
    selectLbutton.destroy()
    if labelL3["text"] > 0:
        labelL3.configure(foreground="green")
    else:
        labelL3.configure(foreground="brown")
    newturn()
def selectM():
    selectMbutton.destroy()
    if labelM3["text"] > 0:
        labelM3.configure(foreground="green")
    else:
        labelM3.configure(foreground="brown")
    newturn()

# Start game
def start():
    global turncounter

    turncounter = 14

    newturn()
    button1.configure(text='Restart game', command=restart)


# Restart game
def restart():
    global turncounter
    global selectAbutton
    global selectBbutton
    global selectCbutton
    global selectDbutton
    global selectEbutton
    global selectFbutton
    global selectGbutton
    global selectHbutton
    global selectIbutton
    global selectJbutton
    global selectKbutton
    global selectLbutton
    global selectMbutton

    ldice.configure(text="")
    totaltext.configure(text="")

    turncounter = 14

    labelA3.configure(foreground="black")
    labelB3.configure(foreground="black")
    labelC3.configure(foreground="black")
    labelD3.configure(foreground="black")
    labelE3.configure(foreground="black")
    labelF3.configure(foreground="black")
    labelG3.configure(foreground="black")
    labelH3.configure(foreground="black")
    labelI3.configure(foreground="black")
    labelJ3.configure(foreground="black")
    labelK3.configure(foreground="black")
    labelL3.configure(foreground="black")
    labelM3.configure(foreground="black")
    labelO3.configure(foreground="black")

    selectAbutton.destroy()
    selectBbutton.destroy()
    selectCbutton.destroy()
    selectDbutton.destroy()
    selectEbutton.destroy()
    selectFbutton.destroy()
    selectGbutton.destroy()
    selectHbutton.destroy()
    selectIbutton.destroy()
    selectJbutton.destroy()
    selectKbutton.destroy()
    selectLbutton.destroy()
    selectMbutton.destroy()

    selectAbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectA)
    c.create_window(400, 425, window=selectAbutton)

    selectBbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectB)
    c.create_window(400, 475, window=selectBbutton)

    selectCbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectC)
    c.create_window(400, 525, window=selectCbutton)

    selectDbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectD)
    c.create_window(400, 575, window=selectDbutton)

    selectEbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectE)
    c.create_window(400, 625, window=selectEbutton)

    selectFbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectF)
    c.create_window(400, 675, window=selectFbutton)

    selectGbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectG)
    c.create_window(800, 400, window=selectGbutton)

    selectHbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectH)
    c.create_window(800, 450, window=selectHbutton)

    selectIbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectI)
    c.create_window(800, 500, window=selectIbutton)

    selectJbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectJ)
    c.create_window(800, 550, window=selectJbutton)

    selectKbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectK)
    c.create_window(800, 600, window=selectKbutton)

    selectLbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectL)
    c.create_window(800, 650, window=selectLbutton)

    selectMbutton = tk.Button(r, text='Select', font=('Helvetica', 13, "bold"), state="disabled", background="white",
                              foreground='black', height=1, width=8, command=selectM)
    c.create_window(800, 700, window=selectMbutton)

    newturn()

# New turn
def newturn():
    global rolls
    global multiple1
    global multiple2
    global multiple3
    global multiple4
    global multiple5
    global multiple6
    global threeok
    global fourok
    global fullhouse
    global smallstraight
    global largestraight
    global fiveok
    global chance
    global columnscore
    global topscore
    global botscore
    global total
    global turncounter

    turncounter -= 1

    if turncounter > 0:
        rolls= 3
        lock1button.configure(text='Unlocked', background='green')
        lock2button.configure(text='Unlocked', background='green')
        lock3button.configure(text='Unlocked', background='green')
        lock4button.configure(text='Unlocked', background='green')
        lock5button.configure(text='Unlocked', background='green')
        rollbutton.configure(state='normal')
        label1['text'] = "You have " + str(rolls) + " rolls remaining"
        ldice['text'] = ''

        if selectAbutton.winfo_exists():
            labelA3.configure(text=0)
            selectAbutton.configure(state='disabled')
        if selectBbutton.winfo_exists():
            labelB3.configure(text=0)
            selectBbutton.configure(state='disabled')
        if selectCbutton.winfo_exists():
            labelC3.configure(text=0)
            selectCbutton.configure(state='disabled')
        if selectDbutton.winfo_exists():
            labelD3.configure(text=0)
            selectDbutton.configure(state='disabled')
        if selectEbutton.winfo_exists():
            labelE3.configure(text=0)
            selectEbutton.configure(state='disabled')
        if selectFbutton.winfo_exists():
            labelF3.configure(text=0)
            selectFbutton.configure(state='disabled')
        if selectGbutton.winfo_exists():
            labelG3.configure(text=0)
            selectGbutton.configure(state='disabled')
        if selectHbutton.winfo_exists():
            labelH3.configure(text=0)
            selectHbutton.configure(state='disabled')
        if selectIbutton.winfo_exists():
            labelI3.configure(text=0)
            selectIbutton.configure(state='disabled')
        if selectJbutton.winfo_exists():
            labelJ3.configure(text=0)
            selectJbutton.configure(state='disabled')
        if selectKbutton.winfo_exists():
            labelK3.configure(text=0)
            selectKbutton.configure(state='disabled')
        if selectLbutton.winfo_exists():
            labelL3.configure(text=0)
            selectLbutton.configure(state='disabled')
        if selectMbutton.winfo_exists():
            labelM3.configure(text=0)
            selectMbutton.configure(state='disabled')

        columnscore = labelA3["text"] + labelB3["text"] + labelC3["text"] + labelD3["text"] + labelE3["text"] + labelF3["text"]
        labelO2.configure(text="35 points if column score 63 or more (Currently {})".format(columnscore))

        if columnscore >= 63:
            labelO3.configure(text="35", foreground="green")
        topscore = labelA3["text"] + labelB3["text"] + labelC3["text"] + labelD3["text"] + labelE3["text"] + labelF3["text"] + int(labelO3["text"])
        botscore = labelG3["text"] + labelH3["text"] + labelI3["text"] + labelJ3["text"] + labelK3["text"] + labelL3["text"] + labelM3["text"]
        labelP3.configure(text=topscore)
        labelQ3.configure(text=botscore)
        total = topscore + botscore
    else:
        ldice.configure(text="")
        totaltext['text'] = "Final score - {}".format(total)
        lock1button.configure(state='disabled')
        lock2button.configure(state='disabled')
        lock3button.configure(state='disabled')
        lock4button.configure(state='disabled')
        lock5button.configure(state='disabled')
        rollbutton.configure(state='disabled')
        label1['text'] = ""


# Display dice and top buttons
totaltext = tk.Label(r, text='', font=('Helvetica', 80), fg='black')
c.create_window(450, 225, window=totaltext)
ldice = tk.Label(r, text='', font=('Times', 120),fg='green')
button1 = tk.Button(r, text='Start game', font=('Helvetica', 15,"bold"),background="blue",foreground='white',height=1, width=15, command=start)
c.create_window(150, 50, window=button1)
rollbutton = tk.Button(r, text='Roll the dice', font=('Helvetica', 20,"bold"),state="disabled",background="brown",foreground='yellow',height=1, width=15, command=roll_dice)
c.create_window(450, 50, window=rollbutton)

# Display locks
lock1button = tk.Button(r, text='Unlocked', font=('Helvetica', 13,"bold"),state="disabled",background="green",foreground='yellow',height=1, width=8, command=lock1)
c.create_window(130, 325, window=lock1button)
lock2button = tk.Button(r, text='Unlocked', font=('Helvetica', 13,"bold"),state="disabled",background="green",foreground='yellow',height=1, width=8, command=lock2)
c.create_window(290, 325, window=lock2button)
lock3button = tk.Button(r, text='Unlocked', font=('Helvetica', 13,"bold"),state="disabled",background="green",foreground='yellow',height=1, width=8, command=lock3)
c.create_window(450, 325, window=lock3button)
lock4button = tk.Button(r, text='Unlocked', font=('Helvetica', 13,"bold"),state="disabled",background="green",foreground='yellow',height=1, width=8, command=lock4)
c.create_window(611, 325, window=lock4button)
lock5button = tk.Button(r, text='Unlocked', font=('Helvetica', 13,"bold"),state="disabled",background="green",foreground='yellow',height=1, width=8, command=lock5)
c.create_window(773, 325, window=lock5button)

# Display text
label1 = tk.Label(r, text='', font=('Helvetica',20,'bold'),fg='brown')
c.create_window(450, 120, window=label1)

# Scoreboard
# Aces
labelA1 = tk.Label(r, text='Aces', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 425, window=labelA1)
labelA2 = tk.Label(r, text='\u2680', font=('Helvetica',30,'bold'),fg='black')
c.create_window(225, 425, window=labelA2)
labelA3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 425, window=labelA3)
selectAbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectA)
c.create_window(400, 425, window=selectAbutton)

# Twos
labelB1 = tk.Label(r, text='Twos', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 475, window=labelB1)
labelB2 = tk.Label(r, text='\u2681', font=('Helvetica',30,'bold'),fg='black')
c.create_window(225, 475, window=labelB2)
labelB3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 475, window=labelB3)
selectBbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectB)
c.create_window(400, 475, window=selectBbutton)

# Threes
labelC1 = tk.Label(r, text='Threes', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 525, window=labelC1)
labelC2 = tk.Label(r, text='\u2682', font=('Helvetica',30,'bold'),fg='black')
c.create_window(225, 525, window=labelC2)
labelC3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 525, window=labelC3)
selectCbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectC)
c.create_window(400, 525, window=selectCbutton)

# Fours
labelD1 = tk.Label(r, text='Fours', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 575, window=labelD1)
labelD2 = tk.Label(r, text='\u2683', font=('Helvetica',30,'bold'),fg='black')
c.create_window(225, 575, window=labelD2)
labelD3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 575, window=labelD3)
selectDbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectD)
c.create_window(400, 575, window=selectDbutton)

# Fives
labelE1 = tk.Label(r, text='Fives', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 625, window=labelE1)
labelE2 = tk.Label(r, text='\u2684', font=('Helvetica',30,'bold'),fg='black')
c.create_window(225, 625, window=labelE2)
labelE3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 625, window=labelE3)
selectEbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectE)
c.create_window(400, 625, window=selectEbutton)

# Sixes
labelF1 = tk.Label(r, text='Sixes', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 675, window=labelF1)
labelF2 = tk.Label(r, text='\u2685', font=('Helvetica',30,'bold'),fg='black')
c.create_window(225, 675, window=labelF2)
labelF3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 675, window=labelF3)
selectFbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectF)
c.create_window(400, 675, window=selectFbutton)

# Three of a Kind
labelG1 = tk.Label(r, text='Three of a Kind', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 400, window=labelG1)
labelG3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 400, window=labelG3)
selectGbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectG)
c.create_window(800, 400, window=selectGbutton)

# Four of a Kind
labelH1 = tk.Label(r, text='Four of a Kind', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 450, window=labelH1)
labelH3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 450, window=labelH3)
selectHbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectH)
c.create_window(800, 450, window=selectHbutton)

# Full House
labelI1 = tk.Label(r, text='Full House', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 500, window=labelI1)
labelI3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 500, window=labelI3)
selectIbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectI)
c.create_window(800, 500, window=selectIbutton)

# Small Straight
labelJ1 = tk.Label(r, text='Small Straight', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 550, window=labelJ1)
labelJ3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 550, window=labelJ3)
selectJbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectJ)
c.create_window(800, 550, window=selectJbutton)

# Large Straight
labelK1 = tk.Label(r, text='Large Straight', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 600, window=labelK1)
labelK3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 600, window=labelK3)
selectKbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectK)
c.create_window(800, 600, window=selectKbutton)

# Yahtzee
labelL1 = tk.Label(r, text='Yahtzee', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 650, window=labelL1)
labelL3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 650, window=labelL3)
selectLbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectL)
c.create_window(800, 650, window=selectLbutton)

# Chance
labelM1 = tk.Label(r, text='Chance', font=('Helvetica',20,'bold'),fg='black')
c.create_window(600, 700, window=labelM1)
labelM3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 700, window=labelM3)
selectMbutton = tk.Button(r, text='Select', font=('Helvetica', 13,"bold"),state="disabled",background="white",foreground='black',height=1, width=8, command=selectM)
c.create_window(800, 700, window=selectMbutton)

# Top bonus
labelO1 = tk.Label(r, text='Bonus', font=('Helvetica',20,'bold'),fg='black')
c.create_window(100, 775, window=labelO1)
labelO2 = tk.Label(r, text='35 points if column score is 63 or more (Currently 0)', font=('Helvetica',10,'bold'),fg='black', wraplength=130)
c.create_window(225, 775, window=labelO2)
labelO3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 775, window=labelO3)

# Top score
labelP1 = tk.Label(r, text='Total of left column', font=('Helvetica',20,'bold'),fg='black', wraplength=200)
c.create_window(100, 850, window=labelP1)
labelP3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(325, 850, window=labelP3)

# Bottom score
labelQ1 = tk.Label(r, text='Total of right column', font=('Helvetica',20,'bold'),fg='black', wraplength=200)
c.create_window(600, 850, window=labelQ1)
labelQ3 = tk.Label(r, text='0', font=('Helvetica',20,'bold'),fg='black')
c.create_window(725, 850, window=labelQ3)

# call the mainloop of Tk
r.mainloop()