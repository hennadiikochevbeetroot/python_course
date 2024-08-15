import abc


class Bird(abc.ABC):

    @property
    @abc.abstractmethod
    def name(self):
        """Bird name"""

    @abc.abstractmethod
    def fly_describe(self) -> str:
        """Describes how bird flies"""


class Pigeon(Bird):
    name = 'Pigeon'

    def fly_describe(self) -> str:
        return 'Swings wings fast'


class Hawk(Bird):
    name = 'Hawk'

    def fly_describe(self) -> str:
        return 'Swings wings gracefully'


class Kiwi(Bird):
    # name = 'Kiwi'

    @property
    def name(self):
        return 'Kiwi'

    def fly_describe(self) -> str:
        return 'Cannot fly :('


kiwi = Kiwi()
hawk = Hawk()
pigeon = Pigeon()


birds = [kiwi, hawk, pigeon]
# birds[0].name = 'New name'
# kiwi.name = 'New name'

# If we have a common interface to all the objects
# (Meaning we can call same methods/ get same properties)
# We may use it in a loop, which would be a nice example of polymorphism
for bird in birds:
    print(bird.name)
    print(bird.fly_describe())
