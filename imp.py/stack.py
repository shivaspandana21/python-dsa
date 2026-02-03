"""Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

def vaild(s):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}
    for char in s:
        if char in pairs:

            if len(stack)==0 or stack[-1]!=pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack)==0
s="()"
print(vaild(s))
#reverse polished notations
""def rpn(tockens):
    stack=[]
    for token in tockens:
        if token not in ['+','-','*','/']:
            stack.append(int(token))
        else:
            b=stack.top
            a=stack.top
            if token=='+':
                stack.append(a+b)
            elif toke"""