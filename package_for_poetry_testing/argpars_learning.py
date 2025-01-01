import argparse

# Create a parser
parser = argparse.ArgumentParser(description="A simple program that greets the user.")

# Add arguments
parser.add_argument('--name', type=str, required=True, help="Your Name")
parser.add_argument('--age', type=int, required=True, help="Your age")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}! You are {args.age} years old.")



