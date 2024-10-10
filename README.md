# 921. Minimum Add to Make Parentheses Valid

__Type:__ Medium <br>
__Topics:__ String, Stack, Greedy <br>
__Companies:__ Meta, Amazon, Google, Bloomberg, Apple, TikTok, Microsoft, Walmart Labs, Nvidia, Adobe <br>
__Leetcode Link:__ [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)
<hr>

A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(()))"` or a closing parenthesis to be `"())))"`.

Return _the minimum number of moves required to make_ `s` _valid_.
<hr>

### Examples

__Example 1:__ <br>
__Input:__ s = "())" <br>
__Output:__ 1

__Example 2:__ <br>
__Input:__ s = "(((" <br>
__Output:__ 3 <br>
<hr>

### Constraints:

- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`.