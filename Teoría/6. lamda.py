todos={
    "1": {
        
    "Grado":1,
    "Nota": 5,},
"2":{
    "Grado": 2,
    "Nota": 3,
    },
"3":{
    "Grado": 3,
    "Nota": 5,
    },
"4":{
    "Grado": 3,
    "Nota": 3,
    },
"5":{
    "Grado": 2,
    "Nota": 1,
    },
"6":{
    "Grado": 2,
    "Nota": 3,
    },
"7":{
    "Grado": 2,
    "Nota": 5,
    }
}

todos_by_grade = {}
for key,todo in todos.items():
    try:
        todos_by_grade[todo["Grado"]]+=todo["Nota"]
    except KeyError:
        todos_by_grade[todo["Grado"]]=todo["Nota"]
print(todos_by_grade)
#Devuelve la suma del total de notas de cada grado

top_users = sorted(todos_by_grade.items(),
key=lambda x: x[1], reverse=True)
#sorted(valores,key=lambda x: f(x), reverse=)
print(top_users)
[x**2 for x in range(4)]

#[f(x) for x in iterable()]

print(top_users[2][1])
