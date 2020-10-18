#Andrew Eppinger
#CS 325 Fall 2020


output = ''                         #Var to store the sorted lines at to be output to results.txt
content_list = []                   #Var to store the each line of the shopping.txt file
input = []           #Var to store the numbers from each line after they're converted to ints
text_file = open('shopping.txt', 'r')

for line in text_file:              #Iterates through each line of the text file, storing each line in a list
    line = line.split(' ')
    content_list.append(line)

for line in content_list:           #Iterates through the list of lines, converts each number from a str to an int
    for i in range(len(line)):
        line[i] = int(line[i])

for list in content_list:
    for num in list:
        input.append(num)

number_of_test_cases = input[0]     #The following code breaks up the input text into a list of test cases.
input = input[1:]
test_cases = []
family_size_list = []
while number_of_test_cases > 0:
    T = []
    number_of_items = input[0]*2
    T.append(input[0])
    input = input[1:]
    while number_of_items > 0:
        T.append(input[0])
        input = input[1:]
        number_of_items -= 1
    family_members = input[0]
    family_size_list.append(input[0])
    T.append(family_members)
    input = input[1:]
    while family_members > 0:
        T.append(input[0])
        input = input[1:]
        family_members -= 1
    number_of_test_cases-=1
    test_cases.append(T)

def shopping(W, wt, val, n):
    '''
    This function finds the highest possible value of items that can be taken one time each
    given a list of weights and corresponding values, as well as a maximum weight capacity.
    '''

    K = [[0 for x in range(W + 1)] for x in range(n + 1)] #Creates a table K to store all max values

    for i in range(n + 1): #Iterates through all given values
        for w in range(W + 1):  #Iterates through all weights up to the target weight + 1
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]+ K[i - 1][w - wt[i - 1]], K[i - 1][w]) #Stores the highest value only
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]


total_list = []
for case in test_cases:     #The following code takes the values from the list of test cases and runs them
                            #through the shopping function
    price_list = []
    weight_list = []
    number_of_items = case[0]
    case = case[1:]
    while number_of_items > 0:
        W = []
        price_list.append(case[0])
        weight_list.append(case[1])
        case = case[2:]
        number_of_items -= 1
    family_size = case[0]
    case = case[1:]
    price_list_length = len(price_list)
    total = 0

    while family_size > 0:
        total = total + shopping(case[0],weight_list,price_list,price_list_length)
        family_size -= 1
        case = case[1:]
    total_list.append(total)

fam_length = len(family_size_list)
output = ''
counter = 1

while  fam_length > 0:
    fam_counter = 1
    output = output + 'Test Case ' + str(counter) +'\n' + 'Total Price ' + str(total_list[0]) + '\n'
    output = output + 'Member Items ' + '\n'
    fam_size = family_size_list[0]
    family_size_list = family_size_list[1:]
    while fam_size > 0:
        output = output + str(fam_counter) + ': ' + 'Unknown'  + '\n'
        fam_size -= 1
        fam_counter += 1
    output = output + '\n'
    total_list = total_list[1:]
    fam_length -= 1
    counter += 1

shopping_out = open('results.txt','w')
shopping_out.write(output)
shopping_out.close()
text_file.close()










