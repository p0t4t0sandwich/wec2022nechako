
import Func as f
import random as r
import tkinter as tk
import gui as g

play = True

while play:
    # user input to choose which setting they would like to use
    setting = input('Enter Option Number:\n1. Enter Input Config and Process Config; Recieve Output Config\n2. Enter Input Config and Output Config; Recieve Process Config\n3. Enter Input Config; Recieve Random Config\nEnter [close] to close program\n>> ')



    #setting 1: Enter Input Config and Process Config; Recieve Output Config
    if setting == '1':

        inputConfig = f.configIn('Enter Input Config: ') #converts input config to int list
        procConfig = f.configIn('Enter Process Config: ') #converts process config into int list

        output = f.movement(procConfig, inputConfig) #executes process instructions

        #output stuff
        print('OUTPUT: Output Config: ' + f.configOut(output))

        inputtk = tk.Tk()
        g.gui_create('Input Config',inputtk,inputConfig) #box gui for input
        outputtk = tk.Tk()
        g.gui_create('Output Config',outputtk,output) #box guy for output

        g.gui_init(inputtk)
        g.gui_init(outputtk)




    #setting 2: Enter Input Config and Output Config; Recieve Process Config
    elif setting == '2':

        inputConfig = f.configIn('Enter Input Config: ') #converts input config to int list
        outputConfig  = f.configIn('Enter Output Config: ') #converts output config to list

        #creates a new list called diff which contains the difference in number of boxes between input and output
        diff = []
        for i in range(len(inputConfig)): #for look to iterate through each list, calc difference and append to diff
            diff.append(inputConfig[i] - outputConfig[i])
            
        procConfig = [] #empty list for process config
        loc = 0 #location of crane

        #while loop for process of creating instructions(process config)
        while diff.count(0) < len(diff): #condition says that difference between num of boxes in input and output must all be 0

            look = f.lookPos(diff,loc) #find position of closest positive value

            #append movement towards next positive number
            move = loc - look #calc relative position of crane position to next loc
            if move > 0: #if next loc is left of crane pos
                for i in range(move):
                    procConfig.append(1)

            if move < 0: #if next loc is right of crane pos
                for i in range(abs(move)):
                    procConfig.append(2)
            
            #pick up box process: append instruction, update location, and change diff list
            procConfig.append(3)
            loc = look
            diff[loc] -= 1

            look = f.lookNeg(diff,loc) #find position of closest negative value

            #append movement to next negative number
            move = loc - look #calc relative position of crane position to next loc
            if move > 0: #if next loc is left of crane pos
                for i in range(move):
                    procConfig.append(1)

            if move < 0: #if next loc is right of crane pos
                for i in range(abs(move)):
                    procConfig.append(2)

            #drop box process: append instruction, update location, and change diff list
            procConfig.append(4)
            loc = look
            diff[loc] += 1

        #output stuff
        procConfig.append(0)
        print('OUTPUT: Process Config: ' + f.configOut(procConfig))




    #setting 3: Enter Input Config; Recieve Random Config
    elif setting == '3':

        inputConfig = f.configIn('Enter Input Config: ') #convert input config to int list
        randConfig = [] #new list for random configurated list
        ls = f.randlist(inputConfig) #holds list of random values

        #appends elems from input config list to new list in random order generated in ls by using elems in ls as index
        for i in ls: 
            randConfig.append(inputConfig[i])
        
        #output stuff
        print('OUTPUT: Output Config: ' + f.configOut(randConfig))

        inputtk = tk.Tk()
        g.gui_create('Input Config',inputtk,inputConfig) #box gui for input
        outputtk = tk.Tk()
        g.gui_create('Output Config',outputtk,randConfig) #box guy for output

        g.gui_init(inputtk)
        g.gui_init(outputtk)
        



    elif setting == 'close':
        print('EXITING PROGRAM')
        play = False



    
    #incase of false input
    else:
        print('Enter Valid Input')




    if play == True:
        play = f.cont() #sets play to true or false based on user input