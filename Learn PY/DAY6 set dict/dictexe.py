#1 Dictionary kya hoti hai?

#2 Key–value pair kya hota hai?

#3 Dictionary ordered hoti hai ya nahi? (Python 3.7+)

#4 Ek dictionary create karo student ke marks ke saath
dict = {
    "aman": 81,
    "rohan": 85,
    "sanu": 90,
    "vishal": 75
}

#5 Dictionary me new key-value add karo
dict["nihal"]= 96
print(dict)

#6 Dictionary se value access karo key ke through
print(dict["nihal"])
print(dict.get("vishal"))

#7 Dictionary ke sabhi keys aur values print karo
for key,value in dict.items():
    print(key, value)

for key in dict:
    print(key,dict[key])  

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

#8 Check karo key exist karti hai ya nahi
if "vishal" in dict.keys():
    print("yes")



#9 Dictionary me highest value wali key find karo
dict = {
    "aman": 81,
    "rohan": 85,
    "sanu": 90,
    "vishal": 75
}
max_key = max(dict, key=dict.get)
min_key = min(dict, key=dict.get)
print("max Value key-> ", max_key)
print("min Value key-> ", min_key)

# Key + Value dono
print(max(dict.items(), key=lambda x: x[1]))



#10 Dictionary ko loop me traverse karo
for key,value in dict.items():
    print(key , "-> ", value)

#11 Ek string me har character ki frequency count karo
s = "shashi"
freq={}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1
print(freq)    

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1    
# print[freq]

#12 Do dictionaries merge karo
d1 = {
    1: "aman",
    2: "sohan"
}

d2 = {
    "name": "Shashi",
    "caste": "Rajput"
}

#1 print(d1 | d2) # by using union

#2 d1.update(d2)
# print(d1)

#3 d3 = {**d1, **d2}
# print(d3)



#13 Dictionary ko value ke basis par sort karo
d1 = {"aman": 86, "don": 34, "mohan": 67}
sorted_d1 = sorted(d1.items(), key=lambda x:x[1])
print(sorted_d1)

#14 Duplicate values remove karo dictionary se


#15 Dictionary invert karo (value → key)