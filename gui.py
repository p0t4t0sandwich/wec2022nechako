import tkinter as tk

def gui_create(name, window, boxes):
    """Create a GUI to represent the boxes
    Input: name: string denoting the name of the GUI window
           window: A tkinter object to contain the GUI
           boxes: A List of integers that represent the boxes
    Output: None, modifies the tkinter object
    """
    # Initialize the window
    window.rowconfigure(boxes, minsize=2)
    window.columnconfigure(boxes, minsize=2)
    window.title(name)

    # Create the scale of the boxes, dependant on the total number of columns
    scale = 7/len(boxes)

    # Nested lists to create the array of boxes
    for i in range(5):
        for j in range(len(boxes)):

            # Default values
            boxc = "grey"
            temp = boxes[j]

            # A color override if there is a box at i, j
            if temp + i - 4 > 0:
                boxc="orange"
            
            # Initializing and adding each box to the array
            frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text="", bg=boxc, fg="black", width=int(18*scale), height=int(5*scale))
            label.pack()

def gui_init(window):
    """Initiate the GUI that represents the boxes
    Input: A tkinter object containing the GUI
    Output: Presents the GUI to the user
    """
    # Initiates the GUI
    window.mainloop()