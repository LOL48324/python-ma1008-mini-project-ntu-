import turtle

# Function to draw a line from point (x1, y1) to (x2, y2)
def draw_line(x1, y1, x2, y2,color="black"):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


# Function to evaluate the cubic Bezier curve at parameter taken and improved from Bezier curve from Dr Lee yong Tsui 
def bezier(t, P0, P1, P2, P3):
    x = (1 - t)**3 * P0[0] + 3 * (1 - t)**2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1 - t)**3 * P0[1] + 3 * (1 - t)**2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]
    return x, y
# Function to draw the X and Y axis of the graph 
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


# Function to draw a cubic Bezier curve segment
def draw_cubic_bezier_curve_segment(P0, P1, P2, P3,color="black"):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(P0)
    turtle.pendown()

    # Draw the cubic Bezier curve segment
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
def drawf(elements,color="black"):
    global x2, y2,control_points
    ic1, ic2 = int(elements[0]), int(elements[1])
    if len(elements) >= 3:
        x, y = int(elements[0]), int(elements[1])
        coord_type = elements[2]
    if coord_type == "line":
        draw_line(x2, y2, x, y,color)
        display_coordinates(x, y)
        x2 = x
        y2 = y
    elif coord_type == "curve":
        # Store the control points for the curve
        control_points.append((x, y))
        display_coordinates(x, y)

        # Draw the cubic Bezier curve segment if control points are available
        if len(control_points) == 3:
            P0 = x2, y2
            P1 = control_points[0]
            P2 = control_points[1]
            P3 = control_points[2]
            x2,y2=P3
            draw_cubic_bezier_curve_segment(P0, P1, P2, P3,color)

# Function to load coordinates from a txt file and draw the figure
def loadcoor2(filename,transfigurepoints=[]):
    global x2, y2,control_points
    try:
        with open(filename, "r") as infile:
            lines = infile.readlines()

            # Print the content of lines in shell to help identify the issue
            print("Lines from file:", lines)

            # Initialize coord_type outside the loop first 
            coord_type = None

            # Initialize control_points outside the loop
            control_points = []

            # Initialize x2 and y2
            x2, y2 = 0, 0
            ic1, ic2 = 0, 0
            # Iterate over lines to find coordinate lines
            for line in lines:
                if line.startswith("XY coordinates"):
                 ###   draw_line(x2, y2, ic1, ic2)
                   continue  # Skip headers so that the program wont create a line with XY coorinates only
                # Assume coordinate line
                elements = line.split()
                ##To specify and identify the first and the last lines
                if "first"in elements:
                    x2,y2=int(elements[1]), int(elements[2])
                    transfigurepoints.append([elements[0],elements[1],elements[2],elements[3]])
                elif "last"in elements:
          ###          draw_line(x2, y2, ic1, ic2)
                    x2, y2 = ic1, ic2
                    control_points = []
                    continue
                #continue if the elements is empty 
                elif elements == []:
                    continue
                else:
                    #append elements for translation later if necessary 
                    drawf(elements)
                    transfigurepoints.append(elements,)
                
    
           ## turtle.done()
    #exception handlering mechanism 
    except (OSError, ValueError, SyntaxError) as e:
        print(f"Error reading the file: {e}")
    return transfigurepoints

