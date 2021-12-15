#o clasa este un template, o specificatie a unei bucati de funcitonalitate, unde avem datele si cum transformam datele

class Animal:
    def __init__(self, name='Unknown', age=None): #name si age se completeaza automat daca nu exista alte valori
        self.name = name
        self.animal_age = age
    def change_name(self, new_name): #metoda
        self.name = new_name 


class NewAnimal(Animal): #Animal = parinte de sus
    def __init__(self, name=None, age=None):
        super().__init__(name, age)

    def change_age(self, new_age):
        self.animal_age = new_age


a0 = Animal()
a1 = Animal("p", 10)

print(f"a0 = name {a0.name}; a0 age = {a0.animal_age}")
print(f"a0 = name {a1.name}; a0 age = {a1.animal_age}")

a0.name = "new name"
print(f"a0 = name {a0.name}; a0 age = {a0.animal_age}")
print(f"a0 = name {a1.name}; a0 age = {a1.animal_age}")

a1.change_name("changed name")
print(f"a1 = name {a1.name}; a0 age = {a1.animal_age}")

a2 = NewAnimal()
print(f"a2 name= {a2.name}: a2 age  = {a2.animal.age}")
a2.change_name("a2 new name")
a2.change_age(20)
print(f"a2 name = {a2.name}: a2 age = {a2.animal.age}" )