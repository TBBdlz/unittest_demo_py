from game.player import Player

if __name__ == "__main__":
    lena = Player("lena", "lena@gmail.com", "mage")
    lena._set_email("lena_chan@gmail.com")
    print(lena)
