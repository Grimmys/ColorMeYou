# manage cartridge sets
from src.entities.cartridge import Color


class CartridgeSet:
    def __init__(self, all_cartridges):
        self.egg_win = False
        self.all_cartridges = all_cartridges

    def check_win(self) -> bool:
        for cartridge in self.all_cartridges:
            if cartridge.color == Color.EGG and cartridge.collected:
                self.egg_win = True
        return all([cartridge.collected for cartridge in self.all_cartridges if cartridge.is_required])
