import math, turtle

def distance(p, q):
        # Return the distance between points p and q.
        distance = math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
        return distance
                
def tourLength(tour):
        # Return the total length of a tour.
        totalDistance = 0
        tour.append(tour[0])
        for i in range (len(tour)-1):
                totalDistance = distance(tour[i],tour[i+1]) + totalDistance
            
        return totalDistance
        
def readCities(filename):
        #'''Read a list of city coordinates from a file.
        #   The first line in the file contains the width and height 
        #   of the coordinate system on which the cities are plotted.
        #   The function returns the list of cities and the width and height
        #   in a 3-element tuple.'''

        inputFile = open(filename, 'r')   # open file named filename for reading
        
        line = inputFile.readline()       # put the first line into a string
        values = line.split()             # split the line into a list of "words"
        width = int(values[0])            # first "word" is the width of the cities
        height = int(values[1])           # second "word" is the height of the cities
        
        cities = []                       # init the list of city coordinates
        for line in inputFile:            # process rest of the lines one at a time
                values = line.split()          # split line into "words" (x and y values)
                cities.append([float(values[0]), float(values[1])])   # append (x,y)
                
        return (cities, width, height)    # return 3 values packaged in a tuple

def drawTour(tour, width, height):
        # Draw a tour expressed as a list of (x,y) coordinates.
        screen = turtle.Screen()
        screen.setworldcoordinates(0,0,width,height)
        t = turtle.Turtle()
        t.tracer(100)
        t.up()
        t.goto(tour[0][0],tour[0][1])
        t.down()
        for i in range (len(tour)):
                t.goto(tour[i][0],tour[i][1])
                t.dot()
        screen.exitonclick()


def tspNN(filename):
        # Nearest neighbor TSP heuristic
        (cities, width, height) = readCities(filename)
        # NN heuristic goes here
        tour = []     # the new tour
        tour.append(cities[0])    # first city in the tour
        for i in range (1,len(cities)):
                # find out the optimal position for each city
                dis = distance(tour[0],cities[i])   # distance btw the first city and the current city
                position = 1   
                for j in range (len(tour)):
                        # calculate the distance between the currenct city and every city in the existing tour
                        d = distance(tour[j],cities[i])
                        if d < dis:
                                # update the position if the distance is currently the least
                                position = j+1
                                dis = d
                tour.insert(position,cities[i])# insert the current city at the optimal position
        
        drawTour(tour, width, height)   # draw the tour
        return tourLength(tour)


def tspSI(filename):   
        # Smallest increase TSP heuristic
        # much slower than tspSI because it deals with lists
        (cities, width, height) = readCities(filename)
        # SI heuristic goes here
        tour = []
        
        tour.append(cities[0])
        
        for i in range (1,len(cities)):
                distance = tourLength(tour+[cities[i]])
                position = -1
                for j in range (len(tour)+1):
                        Try = tour[:]
                        Try.insert(j,cities[i])
                        d = tourLength(Try)
                        if distance > d :
                                # update the position if necessary
                                position = j
                                distance = d
                if position == -1:
                    tour.append(cities[i])
                else:
                   tour.insert(position,cities[i])
        drawTour(tour,width,height)
        return tourLength(tour)

def main():
        print tspNN('tsp10.txt')
        
       
        print tspSI('tsp10.txt')
        
        
main()
