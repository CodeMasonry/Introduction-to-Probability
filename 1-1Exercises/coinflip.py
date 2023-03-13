import random

class Coin:
    def __init__(self):
        self.num_of_tosses = 0
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
                print("Heads proportoin minus 0.5: ", proportion) #problem 1.1
                ratio = self.head_count - (self.num_of_tosses / 2) #problem 1.2
                print("Heads ratio minus the number of tosses cut in half: ", ratio) #problem 1.2
                print("Head count: " + str(self.head_count) + " Division: " + str(self.num_of_tosses / 2) + " Heads ratio minus the number of tosses cut in half: " + str(self.head_count)) #problem 1.2

    def coinflip_variant_two(self, num_of_flips):
        proportion_count = 0
        while self.num_of_tosses < num_of_flips:
            choice = random.choice(self.coin_sides)
            if choice == 'h':
                self.head_count += 1
            else:
                self.tail_count += 1
            self.num_of_tosses += 1
            proportion = (self.head_count / self.num_of_tosses)#problem 1.1
            print("Heads proportion: ", proportion) #problem 2.1
            if proportion > 0.4 and proportion < 0.6:
                proportion_count += 1
        print("Proportion count: " + str(proportion_count))
        if (proportion_count / num_of_flips) >= (95/100):
                print(proportion_count / num_of_flips)
        else:
            print("Failed")
                
class Die:
    def __init__(self):
        self.dice_sides = [1,2,3,4,5,6]
        self.face_value = 0
    

class DiceGame:
    def __init__(self, num_of_dice) -> None:
        self.dice_list = [Die()] * num_of_dice
        self.sum_of_faces = self.sum_faces()

    def sum_faces(self):
        sum = 0
        for die in self.dice_list:
            sum += die.dice_sides[0]
        return sum
    
    def roll_dice_and_sum(self) -> int:
        sum = 0
        for die in self.dice_list:
            sum += random.choice(die.dice_sides)
        return sum

    def play_dice_games(self, num_of_games):
        nine_count = 0
        ten_count = 0
        for i in range(0,num_of_games):
            if self.roll_dice_and_sum() == 9:
                nine_count += 1
            if self.roll_dice_and_sum() == 10:
                ten_count += 1
        print("Nine Count: ", nine_count, "Ten Count: ", ten_count)


def main():
    #Coin Problems
    flip_one = Coin()
    flip_two = Coin()

    flip_one.coinflip_variant_one(10000) #problem 1 
    flip_two.coinflip_variant_two(100) #problem 2

    #Dice Problems
    dice_game = DiceGame(3)
    dice_game.play_dice_games(10000000) #problem 3


main()