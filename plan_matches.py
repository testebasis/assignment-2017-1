# import sys module to get access to the file
import sys
#import Counter from collections . This container used to keep track of how many times equivalent values are added.
from collections import Counter

#The list of command line arguments passed to a Python script. argv[1] is the script name.
input_file = sys.argv[1]

#init lists
#Lists with playersIds
list1 = []
list2 = []
#List with possible days to play
days_list = []
#List with results
results= []
#A players List
players_list = []
#Export Lists from players_list
home = []
away = []

#Find first common element from file list function.
def find_first_common_element(x, y):
    for w in x:
        if w in y:
            return w
    return None
    
#Show results function
def show_results(results):
    if __name__ == '__main__':
        for i in results:
            print i
            
#read files and move it on lines_list
with open(input_file, 'r') as i:
    lines_list = i.readlines()
#players_list init
for i in lines_list:
    for k in i:
        if k != ' ' and k != '\n':
            players_list.append(k)

days_of_tournament = Counter(players_list).values()
days_of_tournament = int(max(days_of_tournament)) + 2

#home-away players
home = players_list[::2]
away = players_list[1::2]

#distinct
players_list = sorted(list(set(players_list)))

#days_list
for i in range(0, len(players_list)):
    new = []
    for j in range(0, days_of_tournament):
        new.append(j)
    days_list.append(new + [i])
#put id for players for better implementation
for i in home:
    for j in players_list:
        if j == i:
            k = j
    id1 = players_list.index(k)
    list1.append(id1)

for i in away:
    for j in players_list:
        if j == i:
            k = j
    id1 = players_list.index(k)
    list2.append(id1)

#use zip for pararell read
for f, b in zip(list1, list2):
    day_var = find_first_common_element(days_list[f], days_list[b])
    results.append(((home[list1.index(f)], away[list2.index(b)]), day_var))
    for i in days_list:
        for j in i:
            if (days_list.index(i) == f or days_list.index(i) == b) and j == day_var:
                i.remove(j)

show_results(results)