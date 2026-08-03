item = input("qual e o nome do produto ")
esto = int(input("qual é a quantidade "))
max = int(input(f"máximo do estoque desse produto {item} "))

mini = (max*20)/100

print("===============relatori do estoque===============")
if esto >= max :
    print("não e nessário")
elif esto <= mini :
    print(f"qualtidade do produto {item} e nessária")
print("================================================")
print(item)
print(esto)
print(max)
print(mini)
print("=================================================")
