class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize a stack to keep track of open parentheses
        stack = []
        # This variable counts how many closing parentheses are needed
        closing_Parameters_Count = 0
        
        # Iterate over each character in the input string
        for character in s:
            # If the character is an open parenthesis, push it onto the stack
            if character == '(':
                stack.append(character)
            # If the character is a closing parenthesis
            elif len(stack) > 0:
                # Pop from the stack if there's a matching open parenthesis
                stack.pop()
            else:
                # If there's no matching open parenthesis, increment the counter
                closing_Parameters_Count += 1

        # Return the total number of parentheses needed:
        # closing_Parameters_Count (for unmatched closing parentheses)
        # plus the length of the stack (for unmatched opening parentheses)
        return closing_Parameters_Count + len(stack)            

# Time Complexity: O(n), where n is the length of the input string s.
# Each character is processed once.

# Space Complexity: O(n) in the worst case, where all characters are '('
# and need to be stored in the stack.
