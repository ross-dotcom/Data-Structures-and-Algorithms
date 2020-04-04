
class Dog:
    
    # Class Attribute
    species = 'mammal'
    
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        return '{} is {} years old.'.format(self.name, self.age)
    
# Child class inherits from Dog class
class Pitbull(Dog):
    
    def run(self, speed):
        return '{} runs {}.'.format(self.name, speed)
        
def get_biggest_number(*args):
    return max(args)


if __name__ == '__main__':
    
    # Instantiate the Dog object
    roxy = Dog("Roxy", 10)
    zoey = Dog("Zoey", 5)
    lucy = Dog("Lucy", 2)
    
    neeko = Pitbull('Neeko', 8)
    
    print(roxy.description())
    print(zoey.description())
    print(lucy.description())
    print('The oldest dog is {} years old.'.format(get_biggest_number(roxy.age, zoey.age, lucy.age)))
    
    print(neeko.description())
    print(neeko.run('slowly'))
    
    print(isinstance(neeko, Dog))