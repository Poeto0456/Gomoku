from state import State

class Title(State):
    def _init_(self, game):
        State._Init_(self, game)

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, display):
            display.fill((255,255,255))
            self.game.draw_text(display,"Game States Demo", (0,0,0), self.game.GANE_W/2, self.game.GAME_H/2)
