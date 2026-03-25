#1 Find the length of a string
s = "shashi"
print(len(s))

#2 Count the number of vowels in a string
s = "Shashi"
vowel = "aeiou"
count = 0
for ch in s:
    ch = ch.lower()
    if ch in vowel:
        count +=1

print("count of vowel = ", count)


#3 Count the number of consonants in a string
s = "shAShiVoWel"
s = s.lower()
countConsonant = 0
vowel = "aeiou"
for ch in s:
    if ch not in vowel:
        countConsonant += 1 

print("consonant -> ", countConsonant)

#4 Reverse a string
s = "abc"
rev_s = s[::-1]
print(rev_s)

#2nd
'''rev = "".join(reversed(s))
print(rev)'''

#3rd
'''text = "Python"
rev_text = ""

for ch in text:
    rev_text = ch + rev_text

print(rev_text)'''

#5 Check whether a string is a palindrome
text = "abca"
rev_text = text[::-1]
if text == rev_text:
    print("Pallindrome")
else:
    print("!not")

#6 Count how many times a character appears in a string
s = "ShashiSingh"
s = s.lower()
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1

print(freq)

#7 Remove spaces from a string
s = "   sds"
print(s)
print(s.strip())   # to remove whitespace from string

#8 Convert string to uppercase and lowercase
s = "shashI"
print("Lower -> ", s.lower())
print("Upper -> ", s.upper())

#9 Find the first non-repeating character
s = "shashi"

freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

#2nd
'''from collections import Counter
s = "swiss"
count = Counter(s)

for ch in s:
    if count[ch] == 1:
        print(ch)
        break'''


#10 Check if two strings are anagrams
'''if two words have have same frequency of characters call anagrams
ex-> silent, listen are anagrams '''
s1 = "silent"
s2 = "listen"

# method1 Get the frequency of both String and check if same TRUE(Anagrams)
from collections import Counter
print(Counter(s1) == Counter(s2))
# method2 Sort the both Strings and traverse via Loop and check
print(sorted(s1) == sorted(s2))
#method 3 Case-insensitive Anagram
s1 = "Listen"
s2 = "SiLeNt"
print(Counter(s1.lower()) == Counter(s2.lower()))