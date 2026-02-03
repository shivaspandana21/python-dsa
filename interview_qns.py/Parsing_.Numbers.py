#14. Parsing Numbers from String
#Q1: Extract numbers
def extract_numbers(s):
    nums, temp = [], ""
    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            if temp:
                nums.append(int(temp))
                temp = ""
    if temp:
        nums.append(int(temp))
    return nums

#Q2: Sum numbers
def sum_numbers(s):
    return sum(extract_numbers(s))