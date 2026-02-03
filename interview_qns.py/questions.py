"""INTERVIEW QUESTIONS ON STRINGS:
      1.Indexing and Slicing
      2.String Imutability
      3.Loop traversal
      4.Lexico comparision
      5.Substring Problems
      6. Duplicates detection
      7. Anagram checking
      8.Character Frequency
      9.Palindrome Checking
      10. Removing character at specific place
       11. String reverse logic
       12.Fixed Window length and Variable window length
       13. Word ordered Problem
       14.Parsing Number From String
       15.Longest and Smallest Substring Problem
       16.Validation Rules(Regex)
       17.Tokenization
       18.Basic Sorting and Custom Sorting
     19.Unique Code and Encoding
     20.Group Anagram"""


"""You are given a string S. Using only string indexing and slicing 
(do not use built-in functions like reverse(), split(), etc.), perform the following operations:

1. Print the first character of the string.
2. Print the last character of the string.
3. Print the string excluding the first and last characters.
4. Print the characters at even indexes.
5. Print the characters at odd indexes.
6. Reverse the given string.
7. Print the first half of the string.
8. Print the second half of the string.
9. Print the string in reverse order excluding the first character.
10. Safely extract characters from index 2 to 10 (even if length is smaller).

n = input("Enter the string: ")
print(n[0])
print(n[-1])
print(n[1:11])
print(n[::2])
print(n[1::2])
print(n[::-1])
print(n[0:6])
print(n[7:13])
print(n[:0:-1])"""
"""2.Traverse a string and perform multiple operations
Problem

Write a program to:
1. Traverse a string using loop
2. Print each character with its index
3. Print even index characters
4. Print odd index characters
5. Reverse the string using loop
6. using while loop
n=input()
#Print each character with its index
for i in range(len(n)):
    print(i,"->",n[i])
#Print even index characters
for i in range(len(n)):
    if i%2==0:
        print(n[i],end=" ")
#Print odd index characters
for i in range(len(n)):
    if i%2!=0:
        print(n[i],end=" ")
#Reverse the string using loop
s=input()
rev=""
for char in s:
    rev=char+rev
print(rev)
#using while loop
n=input()
i=0
while i<len(n):
    print(n[i],end="")
    i+=1"""

#string mutablity
"""you are given a string s,you need to change the character at index 0 to 'j'
Testcases 1: input :"code",output:"jode" 2.input:"A" output:"j" """
#as strings are immutable
#we can do by using slicing
s=input()
s='j'+s[1:]
print(s)

    



