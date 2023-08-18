dic={'valor':1, 'nota':2}

search=int(input())
for k,v in dic.items():
    if v == search:
        print("Si está")
        opt=int(input("nuevo"))
        dic[k]=opt

print(dic)