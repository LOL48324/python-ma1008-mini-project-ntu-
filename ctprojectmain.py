import turtle
from rndv2 import*
import rndv2
from translation import*
import translation
##importing my other two files for ease for debugging and translation 
# Function to draw a line from point (x1, y1) to (x2, y2)
def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Function to evaluate the cubic Bezier curve at parameter t
def bezier(t, P0, P1, P2, P3):
    x = (1 - t)**3 * P0[0] + 3 * (1 - t)**2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1 - t)**3 * P0[1] + 3 * (1 - t)**2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]
    return x, y

# Function to draw a cubic Bezier curve
def draw_cubic_bezier_curve(P0, P1, P2, P3):
    turtle.penup()
    turtle.goto(P0)
    turtle.pendown()

    # Draw the cubic Bezier curve
    t = 0
    while t <= 1:
        x, y = bezier(t, P0, P1, P2, P3)
        turtle.goto(x, y)
        t += 0.01  # Increment t for the next point

# Function to display coordinates on the turtle graphics window
def display_coordinates(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"({x}, {y})", align="left", font=("Arial", 12, "normal"))

# Function to get user input for a new line
def get_user_input(coordinates):
    global x2, y2
    while True:
        try:
            xn, yn = eval(turtle.textinput("User Input", "Enter the next coordinate (x, y): "))
            break
        except NameError:
            turtle.penup()# exception handlering for wrong user input that are not int
            turtle.goto(-150, 200)  # Adjust the y-coordinate as needed
            turtle.write("please input integer only!", align="center", font=("Arial", 12, "normal"))
            turtle.hideturtle()  # Hide the turtle cursor
    draw_line(x2, y2, xn, yn)
    x2, y2 = xn, yn
    coordinates.append((xn, yn, "line"))
    display_coordinates(xn, yn)

# Function to get user input for a new cubic Bezier curve
def get_user_input_cubic(coordinates):
    global P0, P1, P2, P3, x2, y2
    P0 = (x2, y2)
    display_coordinates(x2,y2)
    P1 = eval(turtle.textinput("User Input", "Enter P1 coordinate (x, y): "))
    P2 = eval(turtle.textinput("User Input", "Enter P2 coordinate (x, y): "))
    P3 = eval(turtle.textinput("User Input", "Enter P3 coordinate (x, y): "))
    x2, y2 = P3[0], P3[1]
    coordinates.extend([(P1[0], P1[1], "curve"), (P2[0], P2[1], "curve"), (P3[0], P3[1], "curve")])
    draw_cubic_bezier_curve(P0, P1, P2, P3)

# Function to draw X and Y axes with labels
def draw_axes():
    turtle.penup()
    turtle.goto(-400, 0)
    turtle.pendown()
    turtle.forward(800)  # X-axis
    turtle.write("X", align="left")

    turtle.penup()
    turtle.goto(0, -400)
    turtle.pendown()
    turtle.setheading(90)  # Turn turtle to face north (up)
    turtle.forward(800)  # Y-axis
    turtle.write("Y", align="left")

# Function to save coordinates to a data file 
def savecoor(list_name, initial_coordinates, coordinates):
    while True:
        filename = turtle.textinput("output file?", "Enter output filename: ")
        try:
            with open(filename, "a") as outfile:
                print(f"XY coordinates for {list_name}\n", file=outfile)## naming my file for user to read the data file easily 
                print(f"  first   {initial_coordinates[0]}           {initial_coordinates[1]}                line", file=outfile)
                for coord in coordinates:
                    print(f"     {coord[0]}             {coord[1]}             {coord[2]}", file=outfile)
                print(f"     {initial_coordinates[0]}           {initial_coordinates[1]}                line", file=outfile)
                print(f" last", file=outfile)
            turtle.penup()
            turtle.goto(-150, 200)  # Adjust the y-coordinate as needed
            turtle.write("Saved successfully!", align="center", font=("Arial", 12, "normal"))
            turtle.hideturtle()  # to Hide the turtle cursor so that the user is not distracted
            break
        except OSError:
            print("Error saving coordinates. Try again.")

# Function to load coordinates from a file and draw the figure
def loadcoor(filename):
    try:
        with open(filename, "r") as infile:
            lines = infile.readlines()
            initial_coordinates = eval(lines[2].split(":")[1].strip())
            coordinates = []
            turtle.penup()
            turtle.goto(initial_coordinates)
            turtle.pendown()
            for line in lines[3:]:
                data = line.split()
                x, y, draw_type = int(data[0]), int(data[1]), data[2]
                if draw_type == "line":
                    draw_line(initial_coordinates[0], initial_coordinates[1], x, y)
                elif draw_type == "curve":
                    draw_cubic_bezier_curve(initial_coordinates, (x, y), (x, y), (x, y))
                initial_coordinates = (x, y)
            turtle.hideturtle()
    except FileNotFoundError:
        print(f"Error reading the file: {filename}")


def Drawnewlif():
    global x2,y2
    while True:
    # Get user input for the initial point
        while True:
            try:
                x1, y1 = eval(turtle.textinput("User Input", "Enter the initial coordinate (x, y): "))
                break
            except NameError:
                turtle.penup()
                turtle.goto(-150, 200)  # Adjust the y-coordinate as needed
                turtle.write("please input int only!", align="center", font=("Arial", 12, "normal"))
                turtle.hideturtle()  # Optional: Hide the turtle cursor

        # Set initial values
        initial_coordinates = (x1, y1)
        coordinates = []

        # Draw the initial point
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.dot(5)  # Draw a dot to represent the initial point
        display_coordinates(x1, y1)

        # Set initial values for the next points
        x2, y2 = x1, y1

        # Get user input for subsequent lines or curves
        decision = "L"
        while decision != "X":
            while True:
                try:
                    decision = turtle.textinput("User Input", "Enter L to draw line, \nC to draw cubic Bezier \
curve, \nB to go back to the first coordinate to form a polygon, or X to exit: ")
                    break
                except:
                    turtle.penup()
                    turtle.goto(-150, 200)  # Adjust the y-coordinate as needed
                    turtle.write("please input L/C/B or X  only!", align="center", font=("Arial", 12, "normal"))
                    turtle.hideturtle()  # Optional: Hide the turtle cursor                    
            if decision == "B":
                draw_line(x2, y2, x1, y1)
                display_coordinates(x1, y1)
                save = turtle.textinput("User Input", "Press S to save the coordinates,\nPress E to exit")
                if save == "S":
                    list_name = turtle.textinput("User Input", "Enter a name for the figure:")
                    savecoor(list_name, initial_coordinates, coordinates)
                break
            if decision == "L":
                get_user_input(coordinates)
            if decision == "C":
                get_user_input_cubic(coordinates)

        # Ask if the user wants to draw another figure
        another_figure = turtle.textinput("User Input", "Do you want to draw another figure? (Y/N)").upper()
        if another_figure != "Y":
            break


original_point = (-60, -100, 1)        # Replace px and py with the coordinates of your point
translation_vector = (-30, 50)  

#translation.translate_and_draw(original_point, translation_vector)
user_name = turtle.textinput("User", "What is your name?")
window = turtle.Screen()
window.title(f"Draw polygon with {user_name}")
choose = "L"
# Set up the turtle window
turtle.speed(5)
transfigurepoints=[]
translist=[]
# Draw X and Y axes with labels
draw_axes()
while True:
    choose = turtle.textinput("Dear User", "Do you want to load(L) a data file, draw(D) a new file, or Exit(E)?")
    
    if choose == "L":# when the user chose to Load a file 
        filename = turtle.textinput("Dear user", "Which file do you want to load?")
        rndv2.loadcoor2(filename)# call my file rndv2 to load my coordinates from the file
        transop = turtle.textinput("Dear user", "do you want to perform translation on this file(Y/N)?")
        if transop=="Y":#if the user chose to translate the file 
            turtle.clear()
            rndv2.draw_axes()
            transfigurepoints=rndv2.loadcoor2(filename,transfigurepoints)#load the file from rndv2 first 
            transv = eval(turtle.textinput("User Input", "Enter translation vector(x, y): "))
            turtle.clear()
            print(transfigurepoints)
            translist.append(translation.translate_and_draw(transfigurepoints,transv))# call on the translation that i created 
            print(translist)
            flattened_lists = [item[0] for sublist in translist for item in sublist]
            flattened_lists = [list(item) for item in flattened_lists]# to flattend my list for the use of the code ,this method is taken from chatgpt.
            ###flattened_lists = flattened_lists[1:]
            print("flattened_lists",flattened_lists)
            flattened_list=[]

            for element in flattened_lists:
                rndv2.drawf(element,"red")#send the fatten list back the function rndv2 to draw a new figure with red lines 
                
            
            
            
    elif choose == "D":#if the user entered D , the program will start to draw new figure instead
        Drawnewlif()
    elif choose == "E":#if the user entered E , the program will start break out of loop exit the program
        break



# Keep the window open
turtle.done()
