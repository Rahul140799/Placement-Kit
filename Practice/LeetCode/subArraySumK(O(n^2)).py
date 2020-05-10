index = 0 1 2

value = 1 1 1

i -> 0,3   => 0,1,2
j -> i+1,3 => 1,2

Formula : sum(i,j) = sum(0,j) - sum(0,i)
          [ sum of all from i to j-1 ]

sum(0,1) = sum(0,1) - sum(0,0) = 1 - 1 = 0 
sum(0,2) = sum(0,2) - sum(0,0) = 2 - 1 = 1
sum(0,3) = sum(0,3) - sum(0,0) = 3 - 1 = 2 *

sum(1,2) = sum(0,2) - sum(0,1) = 2 - 1 = 1
sum(1,3) = sum(0,3) - sum(0,1) = 3 - 1 = 2 *

sum(2,3) = sum(0,3) - sum(0,2) = 3 - 2 = 1

