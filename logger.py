class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        with open(self.file_name, 'w') as file:
            file.write(f"Population Size: {pop_size}\tVaccination Percentage: {vacc_percentage}\tVirus Name: {virus_name}\tMortality Rate: {mortality_rate}\tBasic Reproduction Number: {basic_repro_num}\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step_number}: Interactions - {number_of_interactions}, New Infections - {number_of_new_infections}\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        did_die_from_infection = number_of_new_fatalities > 0
        survival_rate = 1 - (number_of_new_fatalities / population_count) if population_count > 0 else 0
    
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step_number}: Population - {population_count}, New Fatalities - {number_of_new_fatalities}, Did Die From Infection - {did_die_from_infection}, Survival Rate - {survival_rate}\n")


if __name__ == "__main__":
    log_file = "simulation_log.txt"
    logger = Logger(log_file)
    logger.write_metadata(100000, 0.9, "Ebola", 0.7, 0.25)
    logger.log_interactions(1, 50, 10)
    logger.log_infection_survival(2, 90000, 100)
