# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """(Rat,str,int,int)-> NoneType
        Precondition: len(symbol) = 1
        Precondition: row >= 0
        precondition: col >= 0

        A Rat with a symbol, row, col and num_sprouts_eaten
        symbol: the 1-character symbol for the rat
        row: the row where the rat is located
        col: the column where the rat is located
        num_sprouts_eaten: number of sprouts eaten by the rat

        >>>rat = Rat('P',1,4)
        >>>rat.symbol
        'P'
        etc.
        """
        assert len(symbol) == 1, \
            'symbol is not 1-character'

        self.symbol = symbols
        self.set_location(row,col)
        self.num_sprouts_eaten = 0 


    def set_location(self,row,col):
        """(Rat, int, int)-> NoneType
        Sets the rat's row and col variables for a Rat's instance

        >>>rat=Rat('A',1,4)
        >>>rat.set_location(6,7)
        >>>rat.row
        6
        >>>rat.col
        5
        """
        assert row >= 0, \
            'row is negative'
        assert col >= 0, \
            'col is negative'
        
        self.row = row
        self.col = col

    def eat_sprout(self):
        """(Rat)->NoneType
        Increments rat's variable num_sprouts_eaten
        >>>rat = Rat('P'2,5)
        >>>rat.eat_sprout()
        >>>rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1
    
    def __str__(self):
        """(Rat)->str
        Return a string representation of a Rat
        >>>rat = Rat('D',5,1)
        >>>rat.eat_sprout()
        >>>rat.eat_sprout()
        >>>print(rat)
        D at (5,1) ate 2 sprouts.
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """
    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType
        Precondition: rows of the maze > 2
	    Precondition: cols of the maze > 2
	    Precondition: maze have the same number of columns in all rows
	    Precondition: rat_1 is the inside maze and not on the wall and not on the sprout
	    Precondition: rat_2 is the inside maze and not on the wall and not on the sprout

         A 2D maze with two rats and a number of sprouts.
        maze: the contents of the maze.
        rat_1: the first rat in the maze.
        rat_2: the second rat in the maze.
        num_sprouts_left: the number of uneaten sprouts in this maze.

        >>>maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#']], \
                        Rat('J', 1, 1), \
                        Rat('P', 1, 4))

        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol

        num_sprouts_left = 0

        for row in maze:
            num_sprouts_left = num_sprouts_left + row.count(SPROUT)
        self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        """(Maze, int,int)-> bool
        Precondition: 0 <= row < len(maze)
	    Precondition: 0 <= col < len(maze[0])
        Return True if and only if there is a wall at the given row and column of the maze.
        """

        return self.get_character(row, col) == WALL

    def get_character(self,row,col):
        """(Maze,int,int)->str
        Precondition: 0 <= row < len(maze)
        Precondition: 0 <= col < len(maze[0])
        Returns the character ar the give row and column location
        """

        assert 0 <= row < len(self.maze), \
           'row not in the maze.'
        assert 0 <= col < len(self.maze[0]), \
           'col not in the maze.'

        return self.maze[row][col]

    def move(self_rat_vertical, horizontal):
         """ (Maze, Rat, int, int) -> bool
	    Precondition: vertical == UP or vertical == NO_CHANGE or vertical == DOWN
	    Precondition: horizontal == LEFT or horizontal == NO_CHANGE or horizontal == RIGHT
        Move the rat in the given direction, unless there is a wall in the way.
        Also, check for a Brussels sprout at that location and, if present:
            have the rat eat the Brussels sprout,
           make that location a HALL, and
           decrease the value that num_sprouts_left refers to by one.
        Return True if and only if there wasn't a wall in the way.
        >>>LEFT = -1
        >>>RIGHT = 1
        >>>NO_CHANGE = 0
        >>>UP = -1
        >>>DOWN = 1
        >>>rat_1 = Rat('J', 1, 1)
        >>>rat_2 = Rat('P', 1, 4)
        >>>maze = Maze([ ['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#'] ], \
                        rat_1, \
                        rat_2)
       
        """
        assert vertical == UP or \
            vertical == NO_CHANGE or \
            vertical == DOWN, \
            'vertical direction wrong.'

        assert horizontal == UP or \
            horizontal == NO_CHANGE or \
            horizontal == DOWN, \
            'horizontal direction wrong.'
      
        new_row = rat.row + vertical
        new_col = rat.col + horizontal

        if self.is_wall(new_row, new_col):
            return False

        if self.get_character(new_row, new_col) == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left = self.num_sprouts_left - 1

        self.maze[rat.row][rat.col] = HALL

        rat.set_location(new_row, new_col)
        
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        return True

    def __str__(self):
        """ (Maze) -> str
        Return a string representation of this Maze.
        >>>maze = Maze([ ['#', '#', '#', '#', '#', '#', '#'], \
                          ['#', '.', '.', '.', '.', '.', '#'], \
                          ['#', '.', '#', '#', '#', '.', '#'], \
                          ['#', '.', '.', '@', '#', '.', '#'], \
                          ['#', '@', '#', '.', '@', '.', '#'], \
                          ['#', '#', '#', '#', '#', '#', '#']], \
                         Rat('J', 1, 1), \
                         Rat('P', 1, 4))
        >>>print(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        result = ''
        for row in self.maze:
            for char in row:
                result = result + char
            result = result + '\n'
        return result + "{0}\n{1}".format(self.rat_1, self.rat_2)