import abc


class Bird(abc.ABC):

    @abc.abstractmethod
    def fly_describe(self) -> str:
        """Describes how bird flies"""


class Pigeon(Bird):
    def fly_describe(self) -> str:
        return 'Swings wings fast'


class Hawk(Bird):
    def fly_describe(self) -> str:
        return 'Swings wings gracefully'


class Kiwi(Bird):
    def fly_describe(self) -> str:
        return 'Cannot fly :('


kiwi = Kiwi()
hawk = Hawk()
pigeon = Pigeon()

birds = [kiwi, hawk, pigeon]

# If we have a common interface to all the objects
# (Meaning we can call same methods/ get same properties)
# We may use it in a loop, which would be a nice example of polymorphism
for bird in birds:
    print(bird.fly_describe())
