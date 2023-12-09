import random

class Person(object):
    def __init__(self, _id, is_vaccinated, infection=None):
        # Initialize attributes of a person
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    def did_survive_infection(self):
        if self.infection:
            # Generate a random number between 0 and 1
            random_number = random.random()
            if random_number < self.infection.mortality_rate:
                # Person did not survive the infection
                self.is_alive = False
                self.is_vaccinated = False
                return False
            else:
                # Person survived the infection
                self.is_vaccinated = True
                self.infection = None
                return True
        return None

if __name__ == "__main__":
    # Test cases
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    virus = Virus("Ebola", 0.6, 0.4)

    person1 = Person(4, True)
    assert person1.did_survive_infection() is None
    assert person1.is_alive is True
    assert person1.is_vaccinated is True
    assert person1.infection is None

    person2 = Person(5, False, virus)
    assert person2.did_survive_infection() is False
    assert person2.is_alive is False
    assert person2.is_vaccinated is False
    assert person2.infection is None

    person3 = Person(6, False, virus)
    person3.infection = virus
    assert person3.did_survive_infection() is True
    assert person3.is_alive is True
    assert person3.is_vaccinated is True
    assert person3.infection is None

    people = []
    for i in range(1, 100):
        person = Person(i, False, virus)
        people.append(person)

    did_survive = 0
    did_not_survive = 0

    for person in people:
        if person.did_survive_infection():
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive}, Did not survive: {did_not_survive}")
