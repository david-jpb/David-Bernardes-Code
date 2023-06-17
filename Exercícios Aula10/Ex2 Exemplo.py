import random

# Function to simulate dice rolls and calculate frequencies
def simulate_dice_rolls(num_rolls):
    frequencies = [0] * 6  # Initialize a list to hold the frequencies of each number (1 to 6)
    for _ in range(num_rolls):
        roll = random.randint(1, 6)  # Simulate a dice roll by generating a random number between 1 and 6 (inclusive)
        frequencies[roll - 1] += 1  # Increment the frequency count for the rolled number by accessing the corresponding index in the list

    return frequencies

# Function to display the frequencies of dice rolls
def display_frequencies(frequencies):
    print("Frequency of dice rolls:")
    for i, frequency in enumerate(frequencies):
        number = i + 1
        print(f"Number {number}: {frequency} times")

# Main code
num_rolls = 1000000  # Specify the number of dice rolls to simulate
roll_frequencies = simulate_dice_rolls(num_rolls)  # Call the simulate_dice_rolls function to get the frequencies
display_frequencies(roll_frequencies)  # Call the display_frequencies function to print the frequencies
