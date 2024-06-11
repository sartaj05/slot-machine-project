import random

class SlotMachine:
    def __init__(self):
        self.balance = 0
        self.lines = 0
        self.bet = 0
        self.reels = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def select_betting_lines(self, lines):
        self.lines = lines
        print(f"Selected {self.lines} betting lines")

    def place_bet(self, bet):
        if bet * self.lines > self.balance:
            print("Insufficient balance to place bet.")
        else:
            self.bet = bet
            print(f"Placed bet of ${self.bet} on {self.lines} lines")

    def spin_reels(self):
        if self.bet * self.lines > self.balance:
            print("Insufficient balance to spin the reels.")
            return

        self.balance -= self.bet * self.lines
        print(f"Spinning reels...")

        result = []
        for _ in range(self.lines):
            line_result = [random.choice(self.reels) for _ in range(3)]
            result.append(line_result)
            print(f"Line result: {' | '.join(line_result)}")

        self.check_winnings(result)

    def check_winnings(self, result):
        winnings = 0
        for line in result:
            if line[0] == line[1] == line[2]:
                winnings += self.bet * 10  # Example winning condition: all three symbols match
                print(f"Winning line! {' | '.join(line)} - Won ${self.bet * 10}")

        self.balance += winnings
        print(f"Total winnings: ${winnings}. Current balance: ${self.balance}")

    def play(self):
        while True:
            action = input("Choose action: (d)eposit, (s)elect lines, (b)et, (p)lay, (q)uit: ").strip().lower()
            if action == 'd':
                try:
                    amount = int(input("Enter deposit amount: ").strip())
                    self.deposit_money(amount)
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            elif action == 's':
                try:
                    lines = int(input("Enter number of lines to bet on (1-3): ").strip())
                    if 1 <= lines <= 3:
                        self.select_betting_lines(lines)
                    else:
                        print("Invalid number of lines. Please enter a number between 1 and 3.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif action == 'b':
                try:
                    bet = int(input("Enter bet amount per line: ").strip())
                    self.place_bet(bet)
                except ValueError:
                    print("Invalid bet amount. Please enter a valid number.")
            elif action == 'p':
                self.spin_reels()
            elif action == 'q':
                print(f"Exiting game. Final balance: ${self.balance}")
                break
            else:
                print("Invalid action. Please try again.")

# Run the game
game = SlotMachine()
game.play()
