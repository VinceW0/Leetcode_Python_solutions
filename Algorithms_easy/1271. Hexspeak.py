"""
1271. Hexspeak
Easy

A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

 

Example 1:

Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.
Example 2:

Input: num = "3"
Output: "ERROR"
 

Constraints:

1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.
"""
class Solution:
    def toHexspeak(self, num: str) -> str:
        s = hex(int(num)).upper()[2:].replace('0', 'O').replace('1', 'I')
        return 'ERROR' if any(c.isdigit() for c in s) else s

        
