import random

MAX_LINES = 3
MIN_BET = 10
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "S": 2,
    "A": 3,
    "C": 5,
    "K": 18,
    "L": 20
}

symbol_value = {
    "S": 20,
    "A": 6,
    "C": 4,
    "K": 3,
    "L": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
    
        columns.append(column)

    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

        print("- - - - -")


def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("You must enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid numer of lines.")
        else:
            print("You must enter a number.")
    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet (per line)? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough money to deposit ${bet}, your balance is: ${balance}")
        else:
            break
        

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slot = get_spin(ROWS, COLS, symbol_count)
    print_slot(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)  
    return winnings - total_bet  


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
main()
