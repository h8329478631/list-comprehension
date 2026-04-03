'''
10 List Comprehension Tasks
1) Square Numbers

👉 Create a list of squares from 1 to 10

# Expected: [1, 4, 9, ..., 100]
'''

# square_list = [i**2 for i in range(1,11)]

# print(square_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


'''
2) Even Numbers

👉 Create a list of even numbers from 1 to 20

# Expected: [2, 4, 6, ..., 20]

'''

# even_list = [i for i in range(1,21) if i%2==0]

# print(even_list) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
3) Odd Numbers

👉 Create a list of odd numbers from 1 to 15

# Expected: [1, 3, 5, ..., 15]

'''
# odd_num = [i for i in range(1,16) if i%2!=0]

# print(odd_num)  # [1, 3, 5, 7, 9, 11, 13, 15]

'''

4) Multiply List Elements

👉 Given list [1,2,3,4], create new list with each element multiplied by 5

# Expected: [5, 10, 15, 20]

'''

# orignal_list = [1,2,3,4,5]

# multi_by_5list = [ i*5 for i in orignal_list]

# print(multi_by_5list)  # [5, 10, 15, 20, 25]

'''

5) Convert to Uppercase

👉 Convert all names to uppercase

names = ["rahul", "pavan", "raj"]
# Expected: ["RAHUL", "PAVAN", "RAJ"]

'''
# names = ["rahul", "pavan", "raj"]

# upper_case_names = [name.upper() for name in names]

# print(upper_case_names)  # ['RAHUL', 'PAVAN', 'RAJ']

'''

6) Filter Positive Numbers

👉 From list [2, -3, 4, -1, 0], keep only positive numbers

# Expected: [2, 4]

'''

# mix_list = [2, -3, 4, -1, 0]

# pos_num = [i for i in mix_list if i>0]

# print(pos_num)  # [2, 4]

'''

7) Length of Each Word

👉 Find length of each word

words = ["apple", "banana", "kiwi"]
# Expected: [5, 6, 4]

'''
# words = ["apple", "banana", "kiwi"]

# len_of_each_word = [len(i) for i in words]

# print(len_of_each_word)  # [5, 6, 4]



'''
8) Flatten Nested List

👉 Convert nested list into single list

l = [[1,2], [3,4], [5,6]]
# Expected: [1,2,3,4,5,6]

'''

# l = [[1,2], [3,4], [5,6]]

# single_list = [x for i in l for x in i]

# print(single_list)  # [1, 2, 3, 4, 5, 6]

'''

9) Numbers Divisible by 3

👉 From 1 to 30, get numbers divisible by 3

# Expected: [3, 6, 9, ..., 30]

'''

# div_by_3 = [i for i in range(1,31) if i%3==0]

# print(div_by_3) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

'''
10) Conditional Expression

👉 Replace even numbers with "Even" and odd with "Odd"
nums = [1,2,3,4,5]
# Expected: ["Odd", "Even", "Odd", "Even", "Odd"]

'''

# nums = [1,2,3,4,5]

# odd_even = ["Even" if i%2==0 else "Odd" for i in nums]

# print(odd_even)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']