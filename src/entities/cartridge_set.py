# manage cartridge sets

from typing import List
from src.entities.cartridge import cartridge_set

class CartridgeSet:
    def __init__(self, cartridges_set: List):
        self.collected = []
    
    def update_collected(self):
        for cartridge in cartridge_set:
            if cartridge.state == False:
                self.collected.append(cartridge)
