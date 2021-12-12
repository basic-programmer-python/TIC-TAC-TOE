def create(box,pos,char):
    if pos==1:
        return (box[:2]+char+box[3:-1])
    elif pos==2:
        return (box[:6]+char+box[7:-1])
    elif pos==3:
        return (box[:10]+char+box[11:-1])
    elif pos==4:
        return (box[:26]+char+box[27:-1])
    elif pos==5:
        return (box[:30]+char+box[31:-1])
    elif pos==6:
        return (box[:34]+char+box[35:-1])
    elif pos==7:
        return (box[:50]+char+box[51:-1])
    elif pos==8:
        return (box[:54]+char+box[55:-1])
    elif pos==9:
        return (box[:58]+char+box[59:-1])
    else:
        return box;


def win(arr):
    if((arr.count(1)==arr.count(2)==arr.count(3)==1) or (arr.count(4)==arr.count(5)==arr.count(6)==1) or (arr.count(7)==arr.count(8)==arr.count(9)==1)or (arr.count(1)==arr.count(4)==arr.count(7)==1) or (arr.count(2)==arr.count(5)==arr.count(8)==1) or (arr.count(3)==arr.count(6)==arr.count(9)==1) or (arr.count(1)==arr.count(5)==arr.count(9)==1) or (arr.count(3)==arr.count(5)==arr.count(7)==1)):
        return True
    else:
        False

def full(arr):
    if(len(arr)==9):
        return True
    else:
        False

#initialize
print("Hey Buddy ")
print("Player one Uses X and two uses O")
name1=input("Enter name of player 1 ")
play1=[]
name2=input("Enter name of player 2 ")
play2=[]

play3=[]


#box
box=""
grid="""
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
"""
box="""
   |   |   
---+---+---
   |   |   
---+---+---
   |   |   
"""

#driver 
print("Instructions")
print("These are the set of valid input Vs position to apply Your Character")
print(grid)
grid=box
for i in range(9):
    while(1):
        one=int(input("Enter the Input from player"+name1))
        if(play3.count(one)==0):
            if(grid==create(box,one,"X")):
                print("Tried to rob player "+name2+" = Punishment => Miss a turn")
            else:
                play3.append(one)
                play1.append(one)
                grid=box=create(box,one,"X")
        else:
            print("Tried To misplace = Punishment => Miss a turn")
        print(box)

        if(win(play1)):
            print("Hey Luckey Boy "+name1+" You Emerged to victory")
            exit(0)
        if(full(play3)):
            print("Unforunately Both are competitive")
            exit(0)
        
        two=int(input("Enter the Input from player"+name2))
        if(play3.count(two)==0):
            if(grid==create(box,two,"X")):
                print("Tried to rob player "+name1+" = Punishment => Miss a turn")
            else:
                play3.append(two)
                play2.append(two)
                grid=box=create(box,two,"O")
        else:
            print("Tried To misplace = Punishment => Miss a turn")
        print(box)
        
        if(win(play2)):
            print("Hey Luckey Boy "+name2+" You Emerged to victory")
            exit(0)
        if(full(play3)):
            print("Unforunately Both are competitive")
            exit(0)
