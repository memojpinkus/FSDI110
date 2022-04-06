from itertools import count


def younger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    solution = ages[0]

    for age in ages:
        if age < solution:
            solution = age
    print(solution)

def statistics():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]

    c = 0

    sum = 0

    for number in data:
        c += 1 #c = c + 1
        sum += number #sum = sum + number

    print(c)
    print(len(data))
    print(sum)

def print_some_nums():
    #print the multiples of 10 that exist between 10 and 100

    for num in range(1, 11):
        print(num*10)

    for num in range(10,110,10):
        print(num)



print("Tests test test")
younger_person()
statistics()
print_some_nums()