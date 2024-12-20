# sum_values.py
def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        # Read values from the input file
        with open(input_file, "r") as f:
            numbers = [float(line.strip()) for line in f if line.strip()]

        # Calculate the sum
        total = sum(numbers)

        # Save the result in the output file
        with open(output_file, "w") as f:
            f.write(f"Sum of values: {total}\n")

        print(f"Sum has been calculated and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
    except ValueError:
        print("Error: Ensure all lines in the input file are valid numbers.")

if __name__ == "__main__":
    main()
