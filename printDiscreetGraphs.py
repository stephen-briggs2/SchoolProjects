class buildgraph:
    def __init__(self,vert):
        self.vert = vert
    def discreet(self):
        print (" ",end="") #formatting the upper row
        for i in range(self.vert):#printing the top row
            print ("     ",i+1, end=""), 
        print ("") #adding a new line
        for i in range(self.vert):
            print (i+1, end="") #prints the left labeling row
            for k in range(self.vert): #prints the entries in the row
                print ("     ", 0,end="") #formats the row
            print ("") #newline

    def cycle(self):
        print ("      ",end="") #formatting the upper row
        for row in range(vert): #Prints the top labeling row
            print (row+1, "    ",end="")
        print ("") #newline
        for row in range(vert-1): 
            print (row + 1,end="") #prints the left labeling column
            for column in range(vert):
                print ("     ",end="") #formats the row
                if (row+1 == column): #prints the entries in the row, determines if it is a 1 or 0 if the next column is equal to the row
                    print (1,end="") 
                else:
                    print (0,end="")
            print ("") #newline
        print (vert, "   ", 1, "    ",end="") #Prints and formats the last row
        for k in range(vert-1):
            print (0, "    ",end="") 
        print ("")
        

    def linear(self):
        print ("      ",end="")
        for row in range(vert): #Prints the top labeling row
            print (row+1, "    ",end="")
        print ("") #newline
        for row in range(vert): 
            print (row + 1,end="") #prints the left labeling column
            for column in range(vert):
                print ("     ",end="") #formatting the row
                if (row+1 == column): #prints the entries in the row, determines if it is a 1 or 0 if the next column is equal to the row
                    print (1,end="")
                else:
                    print (0,end="")
            print ("") #newline

    def complete(self):
        print (" ",end="") #formats the first row
        for row in range(vert):
            print ("     ", row+1,end="") #prints the top labeling row
        print ("")#newline
        for row in range(vert):
            print (row + 1,end="")#prints the left labeling column
            for column in range(vert):
                print ("     ", 1,end="") #adds the entries in the graph (all 1's)
            print ("")#newline

test = 0 #Flag for the while loop
while(test == 0): #Allows the user to use the program multiple times
    g = input("Enter the type of graph you want (D for discreet, C for cycle, L for linear, and K for complete): ") #Asks for the graph the user wants
    vert = 0 #Initializes a variable for the vertices

    #If statement to determine which graph the user wanted
    if (g == "D" or g == "d"):
        vert = int(input("How many vertices do you want? ")) #Prompt the user for the number of vertices in the graph
        graph = buildgraph(vert) #Call the class buildgraph to construct the graph
        graph.discreet() #perform the discreet function
    elif (g == "C" or g =="c"):
        while (vert < 2 or vert >= 11):
            vert = int(input("How many vertices do you want? (valid input is 2 < vertices < 11) "))#Prompt the user for the number of vertices in the graph
            graph = buildgraph(vert)#Call the class buildgraph to construct the graph
            graph.cycle() #perform the cycle function
    elif(g == "L" or g == "l"):
        while (vert < 1 or vert >= 11):
            vert = int(input("How many vertices do you want? (valid input is 2 < vertices < 11) "))#Prompt the user for the number of vertices in the graph
            graph = buildgraph(vert)#Call the class buildgraph to construct the graph
            graph.linear() #perform the linear function
    elif (g == "K" or g == "k"):
        vert = int(input("How many vertices do you want? "))#Prompt the user for the number of vertices in the graph
        graph = buildgraph(vert)#Call the class buildgraph to construct the graph
        graph.complete() #perform the complete function

    test = int(input("Continue? (0 = yes, 1 = no )")) #Ask if the user is done
                     
    



