
class Entity:
    def __init__(self, x, y, model):
        self.position_x = x
        self.position_y = y
        self.model = model

    def move(self, direction):
        if direction == "Up":
            self.position_y -= 1
        elif direction == "Down":
            self.position_y += 1
        elif direction == "Left":
            self.position_x -= 1
        elif direction == "Right":
            self.position_x += 1


class Hero(Entity):
    def __init__(self):
        super().__init__(self)
        self.draw_hero(self.zero_point+self.hud, self.zero_point, 72)

    def draw_hero(self, x, y, size):
        self.h = PhotoImage(file='hero-down.png')
        self.hero = self.canvas.create_image(x, y, image = self.h)

    def hero_shape(self, direction):
        if direction == 'Down':
            self.h = PhotoImage(file='hero-down.png')
            return self.h
        elif direction ==  'Up':
            self.h = PhotoImage(file='hero-up.png')
            return self.h
        elif direction ==  'Right':        
            self.h = PhotoImage(file='hero-right.png')
            return self.h
        elif direction ==  'Left':
            self.h = PhotoImage(file='hero-left.png')
            return self.h
        
    def on_key_press(self, e):
        self.coords = self.canvas.coords(self.hero)
        self.facing = self.hero_shape(e.keysym)
        if ( e.keysym == 'Up' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(0, -1)
        elif( e.keysym == 'Down' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(0, 1)
        elif ( e.keysym == 'Left' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(-1, 0)
        elif( e.keysym == 'Right' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(1, 0)

        
    
class Monster(Entity):
    pass