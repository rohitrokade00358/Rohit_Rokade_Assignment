def count_multiples(numbers):
    # Initialize a dictionary to hold counts for multiples of 1 to 9
    counts = {i: 0 for i in range(1, 10)}
    
    # Iterate through each number in the input list
    for number in numbers:
        for i in range(1, 10):
            if number % i == 0:  # Check if 'number' is a multiple of 'i'
                counts[i] += 1  # Increment the count for this multiple
                
    return counts
# Example usage:
input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(input_numbers)
print(output)
