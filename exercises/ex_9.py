'''
#1st
circle_data = list(map(int, input().split()))
print(2*circle_data[0]*circle_data[2]+2*circle_data[1])

#2nd
import math as number_math
user_input = int(input())
while user_input > 2:
    user_input = number_math.sqrt(user_input)
    print('{:.3f}'.format(user_input))

#3rd
frozen_treats = int(input())
possible_divisors = []
for divisor_candidate in range(2, frozen_treats+1):
    if frozen_treats % divisor_candidate == 0:
        possible_divisors.append(divisor_candidate)
print(possible_divisors[0])

#4th
number_sequence = []
while 0 not in number_sequence:
    number_sequence.append(int(input()))
counter = 0
for value in number_sequence:
    if value%4 == 0:
        counter +=1
print(counter)

#5th
number_range = range(100000, 1000000)
special_numbers = []
for index in range(0, len(number_range)-3):
    first_num = list(str(number_range[index]))
    second_num = list(str(number_range[index+1]))
    third_num = list(str(number_range[index+2]))
    fourth_num = list(str(number_range[index+3]))
    if first_num[1] == first_num[5] and first_num[2] == first_num[4]:
        if second_num[1] == second_num[5] and second_num[2] == second_num[4]:
            if third_num[1] == third_num[4] and third_num[2] == third_num[3]:
                if fourth_num[0] == fourth_num[5] and fourth_num[1] == fourth_num[4] and fourth_num[2]==fourth_num[3]:
                    special_numbers.append(number_range[index])
print(special_numbers)

#6th
result_numbers = []
for two_digit in range(10, 100):
    if (str(two_digit) in str(two_digit**2)) and (two_digit**2<1000) and ((two_digit**2)%100 == two_digit):
        result_numbers.append(two_digit**2)
print(result_numbers)

#7th
import tqdm
possible_combinations = []
for first_operand in tqdm.tqdm(range(1000, 10000)):
    first_digits = list(str(first_operand))
    for second_operand in range(1000, 10000):
        second_digits = list(str(second_operand))
        sum_digits = list(str(first_operand+second_operand))
        if sum_digits[3] == second_digits[3] == first_digits[1] and sum_digits[2] == first_digits[2] and sum_digits[1] == second_digits[1] and sum_digits[0] == second_digits[0] and (sum_digits[4] not in second_digits and first_digits)\
                and (second_digits[2] not in first_digits and sum_digits) and (first_digits[0] and first_digits[3] not in second_digits and sum_digits):
            possible_combinations.append([first_operand, second_operand, first_operand+second_operand])
print(possible_combinations)

#8th
import math as calculation
input_value = int(input())
square_pairs = 0
for first_value in range(input_value+1):
    for second_value in range(input_value+1):
        if first_value**2 + second_value**2 == input_value:
            square_pairs+=1
print(square_pairs//2)

#9th
import math as computation
user_number = int(input())
print(computation.factorial(user_number+2)/((user_number+2)/2))
'''

#10th
import math as math_ops
factorial_input = int(input())

def get_inverse_fact(n):
    current_k = 1
    running_fact = 1

    while running_fact < n:
        current_k += 1
        running_fact *= current_k

    return current_k if running_fact == n else None

inverse_result = get_inverse_fact(factorial_input)-1
number_list = []
current_fact = get_inverse_fact(factorial_input)
for position in range(inverse_result):
    number_list.append(current_fact)
    current_fact -=1
extra_terms = 0

while inverse_result > 2:
    number_list[0] += number_list[inverse_result]
    number_list[inverse_result] = 0
    inverse_result -= 1
    extra_terms +=1

print(get_inverse_fact(factorial_input)+extra_terms)