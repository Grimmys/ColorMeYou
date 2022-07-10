# manage cartridge sets

from typing import List
from src.entities.cartridge import cartridge_set

class CartridgeSet:
    def __init__(self, cartridges_set: List):
        self.collected = []
        self.egg_win = False
        self.no_egg_win = False
    
    def update_collected(self):
        for cartridge in cartridge_set:
            if cartridge.state == False:
                self.collected.append(cartridge)
    
    def check_win(self):
        if len(self.collected) == 3:
            for cartridge in cartridge_set:
                if cartridge.color == 3:
                    self.egg_win = True
            self.no_egg_win = True
        

