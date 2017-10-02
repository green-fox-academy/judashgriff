

class Entity:
    def __init__(self):
        pass

    def move(self, x, y):
        for i in range(20):
            time.sleep(0.0001)
            self.canvas.update()
            self.canvas.move(self.hero, x * 72 / 20, y * 72 / 20)

    def on_key_press(self, e):
        if ( e.keysym == 'Up' ):
            self.move(0, -1)
        elif( e.keysym == 'Down' ):
            self.move(0, 1)
        elif ( e.keysym == 'Left' ):
            self.move(-1, 0)
        elif( e.keysym == 'Right' ):
            self.move(1, 0)





class Hero(Entity):
    def __init__(self):
        super().__init__(self)

    def draw_hero(self, x, y, size):
        self.h = PhotoImage(file='hero-down.png')
        self.hero = self.canvas.create_image(x, y, image = self.h)

    def hero_shape(self, direction):
        if direction == 'Down':
            self.h = PhotoImage(file='hero-down.png')
        elif direction ==  'Up':
            self.h = PhotoImage(file='hero-up.png')
        elif direction ==  'Right':        
            self.h = PhotoImage(file='hero-right.png')
        elif direction ==  'Left':
            self.h = PhotoImage(file='hero-left.png')
        
    
class Monster(Entity):
    pass