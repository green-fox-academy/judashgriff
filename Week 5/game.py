# from entity import Entity
from map import Map
from view import View
from entity import Entity


class Game:
    def __init__(self):
        # self.game_status()
        my_map = Map()
        self.my_view = View(my_map.map1)
        unit_id = self.my_view.draw_game_object(my_map.creatures[0].position_x, 
                                                my_map.creatures[0].position_y, 
                                                my_map.creatures[0].model)
        # self.my_entity = Entity()
        self.is_going = True
        self.my_view.start()

    # def game_status(self):
    #     if self.is_going == False:
    #         pass 
    #         # Game Over

game = Game()

