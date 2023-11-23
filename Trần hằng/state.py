
class State():
  def _Init_(self, game):
    self.game = game
    self.prev_stat = None
  def update(self, delta_time, actions):
       pass
  def render(solf, surface):
       pass
  def enter_state(self):
    if len(self.game.state_stack>1):
        self.prev_state - self.game.state_stack[-1]
    self.game.state_stack.append(self)
  def exit_state(self):
       self.game.state_stack.pop()
