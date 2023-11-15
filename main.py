MAX_LINES = 3
MIN_BET = 10
MAX_BET = 100


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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough money to deposit ${bet}, your balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


main()
