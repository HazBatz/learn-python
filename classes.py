class Thing:
    pass

class Animate(Thing):
    pass

class Animal(Animate):
    pass

class Mammal(Animal):
    pass

class Giraffe(Mammal):
    pass

class Animal(Animate):
    def breathe (self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammal(Animal):
    def feed_young_with_milk(self):
        pass

class Giraffe(Mammal):
    def eat_leaves_from_trees(self):
        pass

reginald=Giraffe()
reginald=Giraffe()
reginald.move()
reginald.eat_leaves_from_trees()

harriet = Giraffe()
harriet.move()

class Animal(Animate):
    def breathe(self):
        pass
    print('breathing')
    def move(self):
        pass
    print('moving')
    def eat_food(self):
        pass
    print('eating food')
class Mammal(Animal):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffe(Mammal):
    def eat_leaves_from_trees(self):
        print('eating leaves')

reginald=Giraffe()
harriet=Giraffe()
reginald.move()
harriet.eat_leaves_from_trees()







