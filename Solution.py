class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters for open and close parentheses
        open_count = 0
        close_count = 0
        
        # Iterate over each character in the input string
        for character in s:
            if character == '(':
                open_count += 1  # Increment for an open parenthesis
            else:
                if open_count > 0:
                    open_count -= 1  # Match with an open parenthesis
                else:
                    close_count += 1  # Increment for unmatched closing parenthesis
        
        # The total number of additions needed is the sum of unmatched open and close parentheses
        return open_count + close_count

# Time Complexity: O(n), where n is the length of the input string s.
# Each character is processed once.

# Space Complexity: O(1), since we are using a fixed amount of space
# for the open_count and close_count variables, regardless of the input size.
