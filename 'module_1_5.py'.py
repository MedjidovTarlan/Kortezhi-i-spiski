mutable_list=["Лебедь", "Рак", "Щука"]
print(mutable_list)
mutable_list.append("Чук")
print(mutable_list)

immutable_var = tuple["лебедь", "Рак", "Щука", 1999, True]
print(immutable_var)
immutable_var = ["Лебедь"]="Рак"
print(immutable_var)
# Ошибка возникла из-за того,  что кортеж не поддерживает обращение по элементам






