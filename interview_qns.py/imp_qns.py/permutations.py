
from itertools import permutations

def generate_permutations(input_list):
    result = []
    for p in permutations(input_list):
        result.append(list(p))
    return result

# Driver code
numbers =[1,2,3,4]
output = generate_permutations(numbers)

print(output)
