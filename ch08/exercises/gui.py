class Player:
    def move(self, direction):
        if direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1

class Brick:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.is_broken = False


class Goomba:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.is_dead = False

  def die(self):
    self.is_dead = True