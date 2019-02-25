#Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.

#Test it to make sure it works.

number = []
for num in range(1, 100):
    number.append(num)
    
def list(list_num):
    odd = 0
    for num in list_num:
        if num % 2 != 0:
            odd += num
    return odd



odd = list(number)
print(odd)
