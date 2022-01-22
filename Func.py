import random as r
import tkinter as tk
import gui as g
import string as s

def configIn(st):
    """Create int list from user input
    Input: string with int values(can contain white space)
    Output: int list
    """
    valid = False
    while not valid: #loop till valid input
        temp = input(st)
        if temp.isnumeric(): #check if string is numeric
            inputConfigst = list(temp.replace(' ','')) #removes white space and creates list of string from string
            newlist = [int(i) for i in inputConfigst] #converts string elem to int
            return newlist
        else:
            temp = input("Please Enter Valid Input: ")


def configOut(lst):
    """Creates string from int list
    Input: list of int
    Output: string of int
    """
    st = ''
    #appends each elem from list to string
    for i in lst:
        st += str(i) + ' '
    return st[0:-1] #return string except last white space
    

def cont():
    """Console output and input for after/between using program
    """
    cont = 'none'
    while cont == 'none': #correct input must be made to exit while loop
        cont = input("Enter [close] to Close or [cont] to Continue Using Program: ")

        if cont == 'close': #exit program
            print('EXITING PROGRAM')
            return False

        elif cont == 'cont': #continues program
            return True

        else: #invalid input
            print('Enter Valid Input')
            cont = 'none'


def movement(process, inputlist):
    """creates list with process instructions applied
    Input: both int list, process config and input config
    Output: updated list with instructions applied
    """
    input = inputlist.copy()
    pos = 0
    crane = 0

    for i in process: #iterates through entire process config

        if i == 1: #move left
            pos -= 1

        elif i == 2: #move right
            pos += 1

        elif i == 3 and crane == 0: #pick up box if it isnt already holding box
            if input[pos] > 0: #pick up if there are more than 0
                input[pos] -= 1
                crane += 1

        elif i == 4: #drop box 
            if input[pos] < 4: #drop if there is less than 4
                input[pos] += 1
                crane -= 1

        elif i == 0: #quit
            pos = 0

    return input


def lookPos(diff, loc):
    """returns index of nearest positive number relative to crane pos
    Input: diff: int list, loc: index of crane positiont
    output: index of found positive number
    """
    found = False
    look = 0

    while not found: #look until pos int found
        for i in range(2): #iterate twice for both +1 and -1 multiplier
            temp = loc + (-1)**i*(look) #calculate index of where to look at
            if temp >= 0 and temp <= len(diff)-1 and diff[temp] > 0: #if index is in range and elem at index is positive
                return temp
        look += 1 #increase look distance by 1


def lookNeg(diff, loc):
    """returns index of nearest negative number relative to crane pos
    Input: diff: int list, loc: index of crane positiont
    output: index of found negative number
    """
    found = False
    look = 0

    while not found: #look until pos int found
        for i in range(2): #iterate twice for both +1 and -1 multiplier
            temp = loc + (-1)**i*(look) #calculate index of where to look at
            if temp >= 0 and temp <= len(diff)-1 and diff[temp] < 0: #if index is in range and elem at index is negative
                return temp
        look += 1 #increase look distance by 1


def randlist(list):
    """creates a list of random ordered integers
    input: int list of input config
    output: list of random ordered int
    """
    ls = [] #empty list to return
    length = len(list) 

    while len(ls) != length: #loop till length is correct
        num = r.randint(0,length-1) #create random int between range
        if num not in ls: #stops from adding doubles
            ls.append(num)
    return ls

