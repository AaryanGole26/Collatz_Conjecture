import matplotlib.pyplot as plt
import random

def random_color(exclude_colors):
    while True:
        r = lambda: random.randint(0, 255)
        color = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())
        if color not in exclude_colors and color != ['#000000','white','grey']: 
            return color

def plot_collatz_sequence(sequence, label, color):
    plt.plot(sequence, marker='o', linestyle='-', label=f'Starting Number {label}', color=color)
    
    for i, value in enumerate(sequence):
        plt.text(i, value, str(value), color='white', fontsize=9, ha='right')

'''
The Collatz Conjecture is a mathematical hypothesis proposed by Lothar Collatz in 1937. It suggests that for any positive integer n, 
if you apply the following rules repeatedly, you will eventually reach the number 1:
1. If n is even, divide it by 2.
2. If n is odd, multiply it by 3 and add 1.
'''
def get_collatz_sequence(num):
    sequence = []
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = 3 * num + 1
    sequence.append(1)
    return sequence

def collatz_conjecture():
    print("The Collatz Conjecture")
    
    # Collect sequences from user input
    collatz_sequences = []
    used_colors = []  
    
    while True:
        num = int(input("Enter a natural number: "))
        if num <= 0:
            print("Enter a natural number, i.e. from 1 to +∞")
        else:
            # Get the Collatz sequence for this number
            sequence = get_collatz_sequence(num)
            collatz_sequences.append((sequence, num))
            
            another = input("Do you want to enter another number? (yes/no): ").strip().lower()
            if another != 'yes':
                break
    
    # Plot all the sequences in one graph
    plt.figure(figsize=(10, 5))
    plt.gca().set_facecolor('black')
    plt.gca().tick_params(colors='white')
    plt.gca().spines['bottom'].set_color('white')
    plt.gca().spines['left'].set_color('white')
    
    # Set label colors directly
    plt.xlabel('Step', color='white')
    plt.ylabel('Value', color='white')
    plt.title('The Collatz Conjecture', color='white') 
    
    for sequence, label in collatz_sequences:
        color = random_color(used_colors)
        used_colors.append(color)
        plot_collatz_sequence(sequence, label, color)

    plt.grid(True, color='gray') 
    plt.legend()
    plt.show()

collatz_conjecture()
