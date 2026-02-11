HISTORY_FILE = "history.txt"


# ---------------------------
# Show previous calculations
# ---------------------------
def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()

    if len(lines) == 0:
        print("no history")
    else:
        # Print latest calculations first
        for line in reversed(lines):
            print(line.strip())

    file.close()


# ---------------------------
# Clear the history file
# ---------------------------
def clear_history():
    file = open(HISTORY_FILE, 'w')  # Opening in 'w' mode clears the file
    file.close()
    print("history clear")


# ---------------------------
# Save a calculation to file
# ---------------------------
def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()


# ---------------------------
# Perform the calculation
# Expected input: number operator number
# Example: 2 + 3
# ---------------------------
def calculator(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("invalid input")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "/":
        if num2 == 0:
            print("cant be devided")
            return
        result = num1 / num2

    elif op == "%":
        result = num1 % num2

    elif op == "*":
        result = num1 * num2

    else:
        print("invalid input")
        return

    # Convert result to int if it is a whole number
    if int(result) == result:
        result = int(result)

    print("result", result)
    save_to_history(user_input, result)


# ---------------------------
# Main program loop
# ---------------------------
def main():
    print("Simple calculator (type: history, clear, exit)")

    while True:
        user_input = input("Enter your operation: ")

        if user_input == "exit":
            print("good bye")
            break

        elif user_input == "history":
            show_history()

        elif user_input == "clear":
            clear_history()

        else:
            calculator(user_input)


# Start the program
main()
