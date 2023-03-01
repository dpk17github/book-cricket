from functools import reduce
import time
import random


# function for playing game of book cricket 
def BookCricket(turn,team,t=0):
        batting_team = team
        dict_run = {'1':1,'2':2,'3':'out','4':4,'5':0,'6':6,'7':1,'8':4,'9':0,'10':6}
        your_process = []
        team_process = 0
        team_run = 0
        score_card ={}
        hc, c = 0, 0
        while len(score_card) != 3:
            if turn == 'Y':
                your_turn = input('Press Enter to Play')
            else:
                time.sleep(1)
            you_got = random.randint(1,501)
                
            y_got = you_got
            while you_got>10:
                list = [i for i in str(you_got)]
                z = map(int,list)
                x = reduce(lambda x,y: x+y,z)
                you_got = x
            if dict_run[str(you_got)] == 'out':
                if ( (len(score_card)+1) - (len(score_card)) ) == 1:
                    print(f"Playing.....{batting_team['player'][f'p{len(score_card)+1}']}")
                    print(f"Book page no.->{y_got} -->{you_got} ---> OUT <---  ---> OUT <--- ---> OUT <--- ---> OUT <---{batting_team['player'][f'p{len(score_card)+1}']}")
                    score_card.update({f"player{len(score_card)+1}":your_process})
                    try:
                        team_process = team_process + reduce(lambda x,y:x+y,your_process)
                    except:
                        team_process = team_process + 0
                    your_process = []
                    hc, c = 0, 0
                    
            else:
                if ( (len(score_card)+1) - (len(score_card)) ) == 1:
                    print(f"Playing.....{batting_team['player'][f'p{len(score_card)+1}']}")
                time.sleep(1)
                print(f"Book page no.-> {y_got} --> {you_got} ------------------------------------->> {dict_run[str(you_got)]} Run <<-----")
                your_process.append(dict_run[str(you_got)])
                current_run = reduce(lambda x,y:x+y,your_process)
                print(f"*****SCORE*****SCORE*****SCORE***** {batting_team['player'][f'p{len(score_card)+1}']} RUN = {current_run} ({len(your_process)}) ball *****SCORE*****SCORE*****SCORE*****\n")

                if hc == 0:
                    if current_run >= 50:
                        print(f"{batting_team['player'][f'p{len(score_card)+1}']} *** HALF CENTURY ******** 50 ********** 50 ******** HALF CENTURY ***\n")
                        time.sleep(7)
                        hc = 1
                if c == 0:
                    if current_run >= 100:
                        print(f"{batting_team['player'][f'p{len(score_card)+1}']} $$$$$$$$$$$$$$ CENTURY ******** 100 ****$$$**** 100 ******** CENTURY $$$$$$$$$$$$$$$$\n")
                        time.sleep(7)
                        c = 1
                team_run = team_process + current_run
                
            print(f"{batting_team['teamname']} Score: {team_run}/{len(score_card)}\n")
            if t != 0:
                print(f"{batting_team['teamname']}'s Target = {t} \t{batting_team['teamname']} {max(0,t-team_run)} More Run to WIN\n")
                if team_run >= t:
                    score_card.update({f"player{len(score_card)+1}":your_process})
                    return {'sc':score_card,'tr':team_run, 'won':'yes','bt':batting_team}

            if len(score_card) == 3:
                return {'sc':score_card,'tr':team_run,'won':'no','bt':batting_team}

# function for toss 
def Toss(y_team,o_team):
    print(f"LET'S PLAY {y_team['teamname']} v/s {o_team['teamname']} MATCH")
    time.sleep(2)
    print(f"Both the captains took the field for the toss")
    time.sleep(4)
    print(f"{y_team['teamname']}'s Captain {y_team['player']['p1']} and {o_team['teamname']}'s Captain {o_team['player']['p1']} Are Ready For Toss")
    time.sleep(4)
    print("What Your Call ???  Press T For Tail or Press H For Head")
    choice = input().upper()
    while choice != 'T' and choice !='H':
        choice = input('Please Press only T or H \n').upper()
    coin =['T','H']
    coin_flic = random.choice(coin) 
    if choice == coin_flic:
        toss = 'won'
    else:
        toss = 'loss'
    return toss

# funtion for select both team 
def Team_pick():
    IND = {'teamname':'India','player':{'p1':'Rohit','p2':'KL Rahul','p3':'V Kohli'}}
    AUS = {'teamname':'Australia','player':{'p1':'Warner','p2':'G Maxwell','p3':'S Smith'}}
    END = {'teamname':'England','player':{'p1':'Buttler','p2':'Roy','p3':'M Ali'}}
    PAK = {'teamname':'Pakistan','player':{'p1':'B Azam','p2':'Rizwan','p3':'Fakhar'}}
    SL = {'teamname':'Sri Lanka ','player':{'p1':'D Silva','p2':'D Chandimal','p3':'Rajapaksha'}}

    teams = {'1':'IND','2':'AUS','3':'END','4':'PAK','5':'SL'}
    teamList = {'1':IND,'2':AUS,'3':END,'4':PAK,'5':SL}
    print('Please select Your Team')
    for k,v in teams.items():
        print(f"Press {k} For {v}")
    select_yteam = input()
    while select_yteam not in teams.keys():
        select_yteam = input('Wronge key!! Press Valid Key\n')
    y_team = teamList[select_yteam] 

    print('Please select Your Opponents Team')
    for k,v in teams.items():
        if k == select_yteam:
            continue
        print(f"Press {k} For {v}")
    select_oteam = input()
    t = True
    while t:
        while select_oteam not in teams.keys():
            select_oteam = input('Wronge key!! Press Valid Key\n')
        while select_oteam == select_yteam:
            select_oteam = input('Opponets team cant be same! Pleaase choose different team\n')
        if select_oteam in teams.keys() and select_oteam != select_yteam:
            t = False
    o_team = teamList[select_oteam]
    return {'y_team':y_team,'o_team':o_team} 


# function for play the BookCricket game 
def PlayBCric(toss,yt,ot):
    y_team = yt
    o_team = ot
    if toss == 'won':
        want = input(f"Your Team {y_team['teamname']} Won The toss.. So What you want first !! Press B for Bat or L for Bowl\n").upper()
        while want != 'B' and want !='L':
            want = input('Wronge key Press !! Press only B for bat or L for bowl\n' ).upper()
    else:
        cch = ['B','L']
        want = random.choice(cch)
        if want == 'B':
            print(f"{o_team['teamname']} Won The toss and Elect to Bat first\n")
        else:
            print(f"{o_team['teamname']} Won The toss and Elect to Bowl first\n")

    if (toss == 'won' and want == 'B') or (toss != 'won' and want == 'L'):
        p = BookCricket('Y',y_team)
        print(f"target is {p['tr']+1}\n")
        print('innings break! 2nd innings will be start soon.. Please wait\n')
        time.sleep(10)
        c = BookCricket('N',o_team,p['tr']+1)
        return {'p':p,'c':c}
    else:
        c = BookCricket('N',o_team)
        print(f"target is {c['tr']+1}\n")
        print('innings break! 2nd innings will be start soon.. Please Ready to bat\n')
        time.sleep(10)
        p = BookCricket('Y',y_team,c['tr']+1)
        return {'p':p,'c':c,'toss':toss}


# function for man of match (mom) in book cricket
def Mom(dic,winteam):
    sc = dic
    wt = winteam
    try:
        p1 = reduce(lambda x,y:x+y,sc['player1'])
    except:
        p1 = 0
    try:
        p2 = reduce(lambda x,y:x+y,sc['player2'])
    except:
        p2 = 0
    try:
        p3 = reduce(lambda x,y:x+y,sc['player3'])
    except:
        p3 = 0
    if p1 > p2:
        if p1 > p3:
            return f"Man of The Match {wt['player']['p1']} {p1}({len(sc['player1'])}) Run"
        else:
            return f"Man of The Match {wt['player']['p3']} {p3}({len(sc['player3'])}) Run "
    elif p2 > p3:
        return f"Man of The Match {wt['player']['p2']} {p2}({len(sc['player2'])}) Run"
    else:
        return f"Man of The Match {wt['player']['p3']} {p3}({len(sc['player3'])}) Run"


# function for results the BookCricket
def Resulet(play):
    if play['p']['won'] == 'yes':
        print(f"Congratulations Your Team {play['p']['bt']['teamname']} WON BY {4 - len(play['p']['sc'])} wicket")
        print(Mom(play['p']['sc'],play['p']['bt']))

    elif play['c']['won'] == 'yes':
        print(f"{play['c']['bt']['teamname']} Won BY {4 - len(play['c']['sc'])} wicket")
        print(Mom(play['c']['sc'],play['c']['bt']))

    elif play['p']['tr'] > play['c']['tr']:
        print(f"Congratulations Your Team {play['p']['bt']['teamname']} WON BY {play['p']['tr']-play['c']['tr']} RUN")
        print(Mom(play['p']['sc'],play['p']['bt']))

    elif play['p']['tr'] == play['c']['tr']:
        print('match tie!')
    else:
        print(f"{play['c']['bt']['teamname']} Won BY {play['c']['tr']-play['p']['tr']} RUN")
        print(Mom(play['c']['sc'],play['c']['bt']))