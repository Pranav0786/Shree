import sys

def main():
    """
    Main function to orchestrate the reading of input, processing, and printing of output.
    All logic is contained within this function to avoid global variables.
    """

    def sum_powers_recursive(numbers: list[int]) -> int:
        """
        Recursively calculates the sum of the fourth power of non-positive numbers in a list.
        This function replaces a for loop for summing values.
        
        :param numbers: A list of integers.
        :return: The calculated sum.
        """
        # Base case: if the list is empty, then the sum is 0.
        if not numbers:
            return 0
        
        head = numbers[0]
        tail = numbers[1:]
        
        # Recursively call the function on the rest of the list.
        sum_of_tail = sum_powers_recursive(tail)
        
        # If the current number is non-positive, add its fourth power to the sum.
        if head <= 0:
            return (head ** 4) + sum_of_tail
        else:
            # Otherwise, just return the sum from the rest of the list.
            return sum_of_tail

    def process_single_case(x_line: str, y_line: str) -> int:
        """
        Processes a single test case.
        
        :param x_line: The string line containing X.
        :param y_line: The string line containing the numbers Yn.
        :return: The calculated result as an integer.
        """
        try:
            expected_count = int(x_line.strip())
            
            # map() is a standard library function, not a loop structure.
            # It's used here to convert number strings to integers.
            numbers_str = y_line.strip().split()
            # Handle empty line of numbers
            if not numbers_str:
                numbers = []
            else:
                # Using map() for batch transformation, as per challenge constraints
                # (no loops or comprehensions).
                numbers = list(map(int, numbers_str))

            # Check if the actual number of integers matches the expected count X.
            if len(numbers) != expected_count:
                return -1
            
            return sum_powers_recursive(numbers)

        except (ValueError, IndexError):
            # Handles potential errors with malformed input.
            return -1

    def process_all_cases_recursive(lines: list[str]) -> list[int]:
        """
        Recursively processes all test cases from the input lines.
        This function replaces the main for loop over test cases.
        
        :param lines: A list of all remaining input lines.
        :return: A list of results for each test case.
        """
        # Base case: if there are no more lines to process, return an empty list.
        if not lines or len(lines) < 2:
            return []
            
        x_line = lines[0]
        y_line = lines[1]
        remaining_lines = lines[2:]
        
        result = process_single_case(x_line, y_line)
        
        # Prepend the current result to the results of the recursive call.
        return [result] + process_all_cases_recursive(remaining_lines)

    # 1. Read all input lines at once. This respects the "no output until all input is received" rule.
    all_lines = sys.stdin.readlines()
    
    # The first line is N, the number of test cases. We can ignore it in this recursive
    # model as we process lines in pairs until they are exhausted.
    test_case_lines = all_lines[1:]
    
    # 2. Process all test cases recursively.
    results = process_all_cases_recursive(test_case_lines)
    
    # 3. Format and print the final output string.
    # map(str, ...) converts all integer results to strings.
    # "\n".join(...) creates the final output string with newlines between results.
    if results:
        output_string = "\n".join(map(str, results))
        print(output_string)

if _name_ == "_main_":
    main()