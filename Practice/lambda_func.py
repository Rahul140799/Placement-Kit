from functools import reduce

nums = [10,3,2,4,5,5,8,6,9,8]

greater_than_two_even_numbers = list(filter(lambda a : a>2 and a%2 ==0,nums))
print(greater_than_two_even_numbers)

doubles = list(map(lambda a : a*2,greater_than_two_even_numbers))
print(doubles)

#Using Sorted method which returns an iterable list
x=sorted(doubles)
print("sorted_list is :",x)

#Using sort which return nothing,it changes the original doubles list
doubles.sort()
print("sort_list is:",doubles)

remove_duplicates = list(set(doubles))
print(remove_duplicates)

reduced = reduce(lambda a,b : a+b,remove_duplicates)
print(reduced)