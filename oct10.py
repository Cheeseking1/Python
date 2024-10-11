
class dog:
    def __init__ (self, name, breed, age, bark):
        self.name = name
        self.breed = breed
        self.age = age
        self.bark = bark
    def describe(self):
        return f"This is my dog. His name is {self.name}. His breed is {self.breed} He is {self.age} years old."
    def barking(self):
        return f"Dog goes {self.bark} {self.bark} {self.bark}"
def main():
    doglist = []
    while True: 
        name = input("Welcome\nWhat is your dog's name?\n")
        breed = input("What is your dog's breed?\n")
        age = int(input("what is your dog's age?\n"))
        extra = input("WHO DO YOU THINK YOU ARE?\n")
        inputdog = dog(name, breed, age, extra)
        print(inputdog.describe())
        print(inputdog.barking())
        doglist.append(inputdog.describe())
        print(doglist)
        con = input("Would you like to enter another dog? (yes or no)\n")
        if con == "yes":
            continue
        else:
            break
main()