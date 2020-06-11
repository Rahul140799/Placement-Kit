def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while(m < n):
            n -= (n & -n)
        return n

Brilliant Logic :
1) Flip the LSB of b.
2) And check if the new number is in range(a < number < b) or not
   -> if the number greater than 'a' again flip lsb
   -> if it is not then that's the answer


Example 1 :
x = 10, y = 20
y = 10100
Flip LSB of y New Number = 10000 i.e. 16
16 is in range so Again flip : 00000 i.e. 0 and 0 is not in range so 0 is the answer.

Example 2 :
x = 17, y = 19
y = 10011
Flip LSB of y so New Number = 10010 i.e. 18
18 is in range so Again flip : 10000 i.e. 16 and 16 is 'a' so Stop , answer is 16.
