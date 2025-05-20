def generate_series(a):
    if a == 1 or a == 2:
        return "1"  # For a = 1 or 2, return "1"
    else:
        # Create a list of the first 'a' odd numbers
        odd_numbers = []
        for i in range(1, a + 1):
            odd_numbers.append(2 * i - 1)  # Calculate the odd number
        return ", ".join(map(str, odd_numbers))  # Join the numbers into a string
# Example usage:
for i in range(1, 8):  # Test for inputs from 1 to 7
    print(f"input a = {i}, then output : {generate_series(i)}")
