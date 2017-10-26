import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.initial_infected = initial_infected
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        self.logger = Logger('log.txt')
        self.logger.write_metadata(self.population_size, self.vacc_percentage, self.virus_name, self.mortality_rate, self.basic_repro_num)

        self.newly_infected = []
        self._create_population(self.initial_infected)

    def _create_population(self, initial_infected):
        infected_count = 0
        vacc_count = 0
        regular_count = 0
        person_id = 1
        print('before:', self.population)
        while len(self.population) != self.population_size:
            if infected_count !=  initial_infected:
                self.population.append(Person(person_id, False, True, self.mortality_rate))
                person_id += 1
                infected_count += 1

            else:
                random_number = random.randint(0,1)
                if random_number < self.vacc_percentage:
                    self.population.append(Person(person_id, True, False, self.mortality_rate))
                    person_id += 1
                    vacc_count += 1
                else:
                    self.population.append(Person(person_id, False, False, self.mortality_rate))
                    person_id += 1
                    regular_count += 1

        print('after:', len(self.population))
        print(vacc_count, regular_count)
        return self.population

    def _simulation_should_continue(self):
        vacc_count = 0
        alive_count = 0
        infect_count = 0
        if len(self.population) == 0:
            return False
        for person in self.population:
            if person.is_alive is True and person.is_vaccinated is True:
                vacc_count += 1
                alive_count += 1
            elif person.infected is True:
                infect_count += 1

        if vacc_count >= len(self.population):
            return False
        # elif alive_count >= len(self.population):
        elif alive_count == 0:
            return False
        elif infect_count == 0:
            return False
        else:
            return True

    def did_die(self):
        for person in self.population:
            person.did_survive_infection()
            # person.did_survive_infection()
            if person.is_alive is True:
                if person.did_survive_infection() is True:
                    self.logger.log_infection_survival(person, True)
                else:
                    self.logger.log_infection_survival(person, False)
            else:
                self.logger.log_infection_survival(person, False)



    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        print(should_continue)
        index = 0
        while should_continue == True:
            # if index > 20:
            #     break
            self.time_step()
            self.logger.log_time_step(time_step_counter)
            self.did_die()
            should_continue = self._simulation_should_continue()
            # index += 1
            time_step_counter += 1
        print('loop count:', index)
        print('The simulation has ended after ' + str(time_step_counter) + ' turns.')

    def time_step(self):
        interaction_counter = 0
        infected_list = []
        for select_person in self.population:
            random_person = random.choice(self.population)
            if select_person.infected is True and random_person.is_alive is True:
                self.interaction(select_person, random_person)


    def interaction(self, sick_person, random_person):
        if random_person.is_vaccinated is True:
            self.logger.log_interaction(sick_person, random_person, False, True, False)
        elif random_person.infected is True:
            self.logger.log_interaction(sick_person, random_person, False, False, True)
        else:
            rand_num = random.random()
            if rand_num < self.basic_repro_num:
                self.newly_infected.append(random_person)
                random_person.infected = True
                self.logger.log_interaction(sick_person, random_person, True)
                self._infect_newly_infected()
            else:
                pass


    def _infect_newly_infected(self):
        for person in self.newly_infected:
            if person._id == self.newly_infected[0]:
                pass

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    # print('this is params:',params)
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    # print('pop:', pop_size, 'vacc:', vacc_percentage, 'virus:', virus_name, 'morta:', mortality_rate, 'basic:', basic_repro_num, 'infected:', initial_infected)
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
