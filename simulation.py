import random

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # Create a logger object
        self.logger = Logger("simulation_logs.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()  # Create the population

    def _create_population(self):
        people = []
        for _ in range(self.pop_size):
            person = Person(is_vaccinated=(random.random() < self.vacc_percentage), infected=False)
            people.append(person)

        for _ in range(self.initial_infected):
            index = random.randint(0, self.pop_size - 1)
            people[index].infected = True

        return people

    def _simulation_should_continue(self):
        # Check if there are any infected people who are not vaccinated
        return any(person.infected and not person.is_vaccinated for person in self.population)

    def run(self):
        # Write metadata to the logger
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name,
                                   self.virus.mortality_rate, self.virus.repro_rate)
        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step()
            should_continue = self._simulation_should_continue()

        living_count = sum(not person.infected for person in self.population)
        dead_count = self.pop_size - living_count
        vaccinated_count = sum(person.is_vaccinated for person in self.population)
        # Log infection survival
        self.logger.log_infection_survival(time_step_counter, living_count, dead_count)
        # Write metadata to the logger
        self.logger.write_metadata(living_count + dead_count, vaccinated_count, self.virus.name,
                                   self.virus.mortality_rate, self.virus.repro_rate)
        # Log time step
        self.logger.log_time_step(time_step_counter)

    def time_step(self):
        for person in self.population:
            if person.infected:
                for _ in range(100):
                    random_index = random.randint(0, self.pop_size - 1)
                    random_person = self.population[random_index]
                    self.interaction(person, random_person)

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated or random_person.infected:
            return
        elif random.random() < self.virus.repro_rate:
            self.population[self.population.index(random_person)].infected = True
            # Log interactions
            self.logger.log_interactions(time_step_counter, 1, 1)

    def _infect_newly_infected(self):
        for person in self.population:
            if person.infected and not person.is_vaccinated:
                for _ in range(100):
                    random_index = random.randint(0, self.pop_size - 1)
                    random_person = self.population[random_index]
                    if random_person.is_vaccinated and not random_person.infected:
                        if random.random() < self.virus.repro_rate:
                            random_person.infected = True
                            # Log interactions
                            self.logger.log_interactions(time_step_counter, 1, 1)
                            break
