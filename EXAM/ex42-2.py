from ex42map import Map


class Engine(object):
    def __init__(self):
        self.quips = ['You died. You kinda suck at this.', 'Nice job, you died ...jackass.', "Such a loser.",
                      "I have a small puppy that's better at this."]

    def play(self):
        next_step = Map.central_corridor(self)

        while True:
            print("\n-------------")
            room = getattr(Map, next_step)
            next_step = room(self)


a_game = Engine()
a_game.play()
