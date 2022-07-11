# manage cartridge sets

from src.entities.cartridge import all_cartridges


class CartridgeSet:
    def __init__(self, all_cartridges):
        self.collected = []
        self.egg_win = False
        self.no_egg_win = False
        self.all_cartridges = all_cartridges

    def update_collected(self):
        for cartridge in all_cartridges:
            if cartridge.state == False and not cartridge.added:
                self.collected.append(cartridge)
                cartridge.added = True

    def check_win(self):
        if len(self.collected) >= 3:
            for cartridge in all_cartridges:
                if cartridge.color == 3:
                    self.egg_win = True
            self.no_egg_win = True
