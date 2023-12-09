class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        # Initialize a Virus object with the given name, reproduction rate, and mortality rate.
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

if __name__ == "__main__":
    # Create a Virus object with name "HIV", reproduction rate 0.8, and mortality rate 0.3
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    # Create a Virus object with name "COVID-19", reproduction rate 0.5, and mortality rate 0.1
    virus2 = Virus("COVID-19", 0.5, 0.1)
    assert virus2.name == "COVID-19"
    assert virus2.repro_rate == 0.5
    assert virus2.mortality_rate == 0.1

    # Create a Virus object with name "Influenza", reproduction rate 0.6, and mortality rate 0.15
    virus3 = Virus("Influenza", 0.6, 0.15)
    assert virus3.name == "Influenza"
    assert virus3.repro_rate == 0.6
    assert virus3.mortality_rate == 0.15
