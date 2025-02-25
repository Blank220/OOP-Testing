import random
import pygame
import sys

# Pygame initialization
pygame.init()

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
WIDTH = 800
HEIGHT = 600
FONT = pygame.font.SysFont('comicsans', 30)

# Slot machine symbols and values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Load images for the symbols
symbol_images = {
    "A": pygame.image.load('A.png'),
    "B": pygame.image.load('B.png'),
    "C": pygame.image.load('C.png'),
    "D": pygame.image.load('D.png')
}

# Initialize Pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine Game")

# Function to check winnings
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

# Function to get the spin result (columns)
def get_slot_machine_spin(rows, cols, symbols):
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

# Function to render text to the screen
def draw_text(text, x, y, color=(255, 255, 255)):
    label = FONT.render(text, 1, color)
    WIN.blit(label, (x, y))

# Function to display the slot machine visuals (symbols)
def draw_slot_machine(columns):
    cell_width = WIDTH // COLS
    cell_height = HEIGHT // (ROWS + 2)

    for col in range(COLS):
        for row in range(ROWS):
            symbol = columns[col][row]
            x = col * cell_width
            y = row * cell_height + 100  # Offset to leave space for the balance and instructions
            symbol_image = symbol_images[symbol]  # Get the image corresponding to the symbol
            symbol_image = pygame.transform.scale(symbol_image, (cell_width, cell_height))  # Resize image
            WIN.blit(symbol_image, (x, y))  # Draw the image on the screen

# Function to deposit amount
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Function to get number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Function to get bet per line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

# Function to run the spin and calculate the result
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

# Main function to run the game
def main():
    balance = deposit()

    run_game = True
    while run_game:
        WIN.fill((0, 0, 0))  # Fill the screen with black background
        draw_text(f"Current balance: ${balance}", 10, 10)

        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            run_game = False
            break

        balance += spin(balance)

        # Draw the slot machine visuals
        columns = get_slot_machine_spin(ROWS, COLS, symbol_count)
        draw_slot_machine(columns)

        pygame.display.update()

    print(f"You left with ${balance}")
    pygame.quit()

# Run the game
if _name_ == "_main_":
    main()
