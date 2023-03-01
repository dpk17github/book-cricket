import time
import random
from BCric import *
from functools import reduce


     


print("*********************************** WELCOME TO BOOK CRICKET *************************************\n")
time.sleep(3)
team = Team_pick()
toss = Toss(team['y_team'],team['o_team'])
play = PlayBCric(toss,team['y_team'],team['o_team'])
result = Resulet(play)
print("\n*********************************** MATCH OVER *************************************")

# print(f"-------------------------------------------------------------------------")
# print(f"|                           MATCH SUMMARY                               |")
# print(f"------------------------------------------------------------------------|")
# print(f"|                                                                       |")
# print(f"|                                                                       |")
# print(f"|                                                                       |")
# print(f"-------------------------------------------------------------------------")










