import random

#creating list of random numbers
random_list = random.sample(range(0, 1000), 100)


#sorting numbers
for i in range(len(random_list)):
    for k in range(i + 1, len(random_list)):

        if random_list[i] > random_list[k]:
            random_list[i], random_list[k] = random_list[k], random_list[i]

print(random_list)

#avg for even numbers
even_numbers = [j for j in random_list if j % 2 == 0]
even_avg = sum(even_numbers)/len(even_numbers)
print('Even average:', format(even_avg,'.2f'))

#avg for odd numbers
odd_numbers = [j for j in random_list if j % 2 != 0]
odd_avg = sum(odd_numbers)/len(odd_numbers)
print('Odd average:', format(odd_avg,'.2f'))