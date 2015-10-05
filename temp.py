# SEEd
# Project 3


import turtle
def setworldcoordinates(self, llx, lly, urx, ury):
        """Set up a user defined coordinate-system.

        Arguments:
        llx -- a number, x-coordinate of lower left corner of canvas
        lly -- a number, y-coordinate of lower left corner of canvas
        urx -- a number, x-coordinate of upper right corner of canvas
        ury -- a number, y-coordinate of upper right corner of canvas

        Set up user coodinat-system and switch to mode 'world' if necessary.
        This performs a screen.reset. If mode 'world' is already active,
        all drawings are redrawn according to the new coordinates.

        But ATTENTION: in user-defined coordinatesystems angles may appear
        distorted. (see Screen.mode())

        Example (for a TurtleScreen instance named screen):
        >>> screen.setworldcoordinates(-10,-0.5,50,1.5)
        >>> for _ in range(36):
        ...     left(10)
        ...     forward(0.5)
        """
        if self.mode() != "world":
            self.mode("world")
        xspan = float(urx - llx)
        yspan = float(ury - lly)
        wx, wy = self._window_size()
#       self.screensize(wx-20, wy-20)
        oldxscale, oldyscale = self.xscale, self.yscale
        self.xscale = self.canvwidth / xspan
        self.yscale = self.canvheight / yspan
        srx1 = llx * self.xscale
        sry1 = -ury * self.yscale
        srx2 = self.canvwidth + srx1
        sry2 = self.canvheight + sry1
        self._setscrollregion(srx1, sry1, srx2, sry2)
        self._rescale(self.xscale/oldxscale, self.yscale/oldyscale)
        self.update()


def gcFreq(dna,window,t):
    # Plot GC frequency over a sliding window.
    t.up()
    t.goto(0,5)   # turtle go to starting point
    t.down()
    t.color('red')      # set color to be red before drawing
    t.goto(len(dna)*5,5)   # draw the straight line first
    t.up()  # lift up tail and goback
    t.goto(0,5)
    t.color('blue')     # set to blue before drawing the GC content
    StrWin = [] 
    for i in range (window):
        # set the starting point
        # convert the dna string to a list so that the window is mutable 
        StrWin.append(dna[i])
    numC = StrWin.count('C')
    numG = StrWin.count('G')
    total = numC + numG
    t.goto(0,float(total)/window+5)
    t.down()
    for i in range (len(dna)-window+1): # continue with rest of the graph
        numC = StrWin.count('C')
        numG = StrWin.count('G')
        total = numC + numG
        t.goto(i,float(total)/window+5)
        StrWin.pop(0)
        StrWin.insert(-1,dna[i+19])
    

def orf(dna,rf,t):
    # Opening Reading Frame
    #'''Find all ORFs in reading frame rf = 0, 1, 2 (forward only), 
    # not including ORFs contained in other ORFs.'''
    t.goto(0,1+rf)
    t.down()
    t.color('red')
    inORF = 0
    for i in range (rf,len(dna)-3,3):
        if inORF == 0 and dna[i:i+3] == 'AGT':
            t.color('blue')
            inORF = 1
        t.goto((i+3),1+rf)
        if i>=2 and inORF == 1:
            end = dna[i:i+3]
            if end == 'TAA' or end == 'TAG' or end == 'TGA':
                t.color('red')
                inORF = 0
    t.goto((len(dna)-1)*10,1+rf)
    t.up()

def viewer(dna):
	'''Display ORFs and GC content for dna.'''
   
	dna = dna.upper()      # make everything upper case, just in case
   
	t = turtle.Turtle()
	turtle.setup(1440, 240)                  # make a long, thin window
	turtle.screensize(len(dna) * 6, 200)     # make the canvas big enough to hold the sequence
	# scale coordinate system so one character fits at each point
	setworldcoordinates(turtle.getscreen(), 0, 0, len(dna), 6)
	turtle.hideturtle()
	t.speed(0)
	t.tracer(100)
	t.hideturtle()
   
	# Draw the sequence across the bottom of the window.
	t.up()
	for i in range(len(dna)):
		t.goto(i, 0)
		t.write(dna[i],font=("Helvetica",8,"normal"))
      
	# Draw bars for ORFs in forward reading frames 0, 1, 2.
	# Draw the bar for reading frame i at y = i + 1.
	t.width(5)              # width of the pen for each bar
	for i in range(3):
		orf(dna, i, t)
      
	t.width(1)              # reset the pen width
	gcFreq(dna, 20, t)      # plot GC content over windows of size 20
      
	turtle.exitonclick()
   

def main():    
    inputFile = open('Eco536-500.txt','r')  # open a file for reading
    dna = inputFile.read()      # read entire file as a string into dna
    viewer(dna)         # call the viewer function with dna


main()
