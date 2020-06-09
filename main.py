import turtle
import random


class TurtleRace:
    """
    Opens window and initiates a turtle race between multiple players.
    """

    def __init__(self):
        self.screen = turtle.getscreen()
        self.screen_width = self.screen.window_width()
        self.screen_height = self.screen.window_height()
        self.screen_top = self.screen_height / 2
        self.screen.title('Turtle Race Game')

        self.colors = ['red', 'green', 'blue', 'teal', 'yellow', 'orange', 'purple', 'grey', 'chartreuse', 'pink']
        self.players = []
        self.pen_size = 5
        # Number of players much not exceed number of colors
        self.num_of_players = 10

        self.turtle_spacing = self.screen_height / (self.num_of_players + 1)
        self.locations = []
        self.winner = ''

    # main function to call helper functions.
    def run(self):
        """
        Main function that runs the TurtleRace class
        """

        self.screen.clear()
        self.player()
        self.get_location()
        self.start()
        while not self.win():
            self.update()
        turtle.ht()     # Hides auto created turtle
        turtle.write(self.winner, False, 'center', font=('Arial', 24, 'normal'))
        print('Press space bar to play again.')
        self.screen.listen()
        self.screen.onkey(TurtleRace().run, 'space')
        return

    # Creates each new turtle and appends to list of players
    def player(self):
        """
        Creates each new turtle
        :return: List of players
        """

        i = 0
        for player in range(self.num_of_players):
            player = turtle.Turtle()
            player.shape('turtle')
            player.color(self.colors[i])
            player.pensize(self.pen_size)
            self.players.append(player)
            i += 1
        return self.players

    def get_location(self):
        """
        Gets location for newly created turtle to move to.
        Makes turtles space evenly down window regardless of
        number of players.
        :return: Location for specific turtle
        """
        for player in range(self.num_of_players):
            ylocation = self.screen_top - self.turtle_spacing * (player + 1)
            location = [-300, int(ylocation)]
            self.locations.append(location)
        return self.locations

    def start(self):
        """
        Moves turtle to starting position.
        :return:
        """
        i = 0
        for player in self.players:
            player.pu()
            player.goto(self.locations[i])
            player.pd()
            i += 1

    # Moves turtles across screen
    def update(self):
        """
        Updates turtle position each frame.
        :return: New location of each turtle
        """
        for player in self.players:
            player.fd(random.randrange(20))

    # Check for a turtle to reach the finish and returns that turtles color.
    def win(self):
        """
        Checks location of each turtle for a winner.
        :return: True, if a turtle has crossed the finish line.
        """
        for player in self.players:
            if player.xcor() > 290:
                self.winner = f'{player.color()[0].title()} wins!!!'
                return True


if __name__ == '__main__':
    TurtleRace().run()
    turtle.mainloop()
