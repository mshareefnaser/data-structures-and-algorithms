from queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):
        """Enqueue an animal to the animal shelter."""
        if animal.kind == 'dog':
            self.dog.enqueue(animal)
        elif animal.kind == 'cat':
            self.cat.enqueue(animal)
        else:
            return None

    def dequeue(self, pref):
        """Dequeue and return an animal from the animal shelter based on the preference.

        Raises:
            ValueError: If there are no animals of the preferred type available.
        """
        if pref == 'dog' and not self.dog.is_empty():
            return self.dog.dequeue()
        elif pref == 'cat' and not self.cat.is_empty():
            return self.cat.dequeue()
        else:
            raise ValueError("No animals available")


class Dog:
    def __init__(self):
        self.kind = 'dog'


class Cat:
    def __init__(self):
        self.kind = 'cat'
