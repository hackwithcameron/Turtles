from collections import deque
import turtle
import random


class TurtleRace:

    def __init__(self):
        self.screen = turtle.getscreen()
        self.screen_width = self.screen.window_width()
        self.screen_height = self.screen.window_height()
        self.players = []
        self.pen_size = 5
        self.num_of_players = 6
        self.turtle_spacing = self.screen_height / (self.num_of_players + 1)
        self.screen_top = self.screen_height / 2
        self.locations = deque()
        self.winner = ''

        self.colors = deque(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'grey'])

    def run(self):
        self.player()
        self.get_location()
        self.start()
        while not self.win():
            self.update()
        turtle.write(self.winner, False, 'center', font=('Arial', 24, 'normal'))

    def start(self):
        for player in self.players:
            player.pu()
            player.goto(self.locations.popleft())
            player.pd()

    def player(self):
        for player in range(self.num_of_players):
            player = turtle.Turtle()
            player.shape('turtle')
            player.color(self.colors.popleft())
            player.pensize(self.pen_size)
            self.players.append(player)
        return self.players

    def get_location(self):
        for player in range(self.num_of_players):
            ylocation = self.screen_top - self.turtle_spacing * (player + 1)
            location = [-300, int(ylocation)]
            self.locations.append(location)
        return self.locations

    def update(self):
        for player in self.players:
            player.fd(random.randrange(20))

    def win(self):
        for player in self.players:
            if player.xcor() > 290:
                self.winner = f'{player.color()[0].title()} wins!!!'
                return True


def run():
    turtle.reset()
    return TurtleRace().run()


if __name__ == '__main__':
    run()
    print('Press space bar to play again.')
    turtle.listen()
    turtle.onkey(run, 'space')
    turtle.mainloop()
