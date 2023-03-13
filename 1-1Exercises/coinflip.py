import random

class Coin:
    def __init__(self):
        self.num_of_tosses = 1
        self.coin_sides = ['h', 't']
        self.head_count = 0
        self.tail_count = 0

    def coinflip_variant_one(self, num_of_flips):
        while self.num_of_tosses < num_of_flips:
            choice = random.choice(self.coin_sides)
            if choice == 'h':
                self.head_count += 1
            else:
                self.tail_count += 1
            self.num_of_tosses += 1
            if self.num_of_tosses % 100 == 0:
                proportion = (self.head_count / self.num_of_tosses) - 0.5 #problem 1.1
                print("Heads proportoin minus 0.5: {}", proportion) #problem 1.1
                ratio = self.head_count - (self.num_of_tosses / 2) #problem 1.2
                print("Heads ratio minus the number of tosses cut in half: ", ratio) #problem 1.2
                print("Head count: " + str(self.head_count) + " Division: " + str(self.num_of_tosses / 2) + " Heads ratio minus the number of tosses cut in half: " + str(self.head_count)) #problem 1.2

            


def main():
    flip_one = Coin()
    flip_one.coinflip_variant_one(100000000)
    #coinflip_variant_two()

main()