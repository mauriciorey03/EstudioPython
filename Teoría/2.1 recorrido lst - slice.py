s = "yo soy tu padre"

# recorrido de la cadena por su indice
for i in range(len(s)):
    print(s[i], end=", ")
    #y, o,  , s, o, y,  , t, u,  , p, a, d, r, e,

print()
# Recorrido de la cadena por sus elementos 
for elem in s:
    print(elem,end="")

num = "+34-91478248-76"
print()
print(num[2]) # 4
print(num[-2]) #7

#slice
print(num[1:3]) #34
print(num[5:]) #1478248-76
print(num[1:7:2]) #
print(num[::-1])
print(num[:5])