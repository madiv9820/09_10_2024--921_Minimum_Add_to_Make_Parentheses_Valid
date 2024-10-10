- ## Approach 1: Using Stack

    - ### Intuition
        - The problem requires us to make a string of parentheses valid by adding the minimum number of parentheses. A valid string has matched pairs of opening and closing parentheses. We can use a stack to track unmatched opening parentheses and count unmatched closing parentheses.

    - ### Approach
        1. Initialize a stack to keep track of unmatched opening parentheses.
        2. Iterate through each character in the string:
            - If it's an opening parenthesis `(`, push it onto the stack.
            - If it's a closing parenthesis `)`, check if there is an unmatched opening parenthesis in the stack:
                - If yes, pop it from the stack (a match is found).
                - If no, increment a counter for unmatched closing parentheses.
        3. The final result is the sum of the number of unmatched opening parentheses (size of the stack) and unmatched closing parentheses.

    - ### Code
        ```python3 []
        class Solution:
            def minAddToMakeValid(self, s: str) -> int:
                stack = []
                closing_Parameters_Count = 0
                
                for character in s:
                    if character == '(':
                        stack.append(character)
                    elif len(stack) > 0:
                        stack.pop()
                    else:
                        closing_Parameters_Count += 1
                
                return closing_Parameters_Count + len(stack)

        # Time Complexity: O(n), where n is the length of the input string s.
        # Space Complexity: O(n) in the worst case, where all characters are '('.
        ```

- ## Balance Counter Approach

    - ### Intuition
        - The balance counter approach simplifies the problem of making a string of parentheses valid. By using a counter to keep track of the difference between opening and closing parentheses, we can determine how many unmatched parentheses exist. The absolute value of the balance will tell us the total number of parentheses that need to be added to make the string valid.

    - ### Approach
        1. Initialize two counters: `open_count` to track unmatched opening parentheses and `close_count` for unmatched closing parentheses.
        2. Iterate through each character in the string:
            - If the character is an opening parenthesis `(`, increment `open_count`.
            - If the character is a closing parenthesis `)`:
                - If there is an unmatched opening parenthesis (i.e., `open_count > 0`), decrement `open_count`.
                - If not, increment `close_count` for the unmatched closing parenthesis.
        3. The total number of additions needed is the sum of `open_count` and `close_count`, representing unmatched parentheses.

    - ### Code
        ```python
        class Solution:
            def minAddToMakeValid(self, s: str) -> int:
                open_count = 0
                close_count = 0
                
                for character in s:
                    if character == '(':
                        open_count += 1
                    else:
                        if open_count > 0:
                            open_count -= 1
                        else:
                            close_count += 1
                
                return open_count + close_count

        # Time Complexity: O(n), where n is the length of the input string s.
        # Space Complexity: O(1), since we are using a fixed amount of space for the counters.
        ```