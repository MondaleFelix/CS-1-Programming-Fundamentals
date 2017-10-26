
class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        with open(self.file_name, 'w') as file:
            log = '{}\t{}\t{}\t{}\t{}\n'.format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)
            file.write(log)


    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        interaction = open(self.file_name, 'a')
        # Change code below to format function
        # interaction.write("ID: %s is matched with ID: %s\n" % (person._id, random_person._id))
        if did_infect is True:
            interaction.write('{person1} infects {person2}\n'.format(person1=person1._id, person2=person2._id))
        elif person2_vacc is True:
            interaction.write('{person1} did not infect {person2} because {person2} was vaccinated\n'.format(person1=person1._id,
                                                                                                     person2=person2._id))
        elif person2_sick is True:
             interaction.write('{person1} did not infect {person2} because {person2} was sick\n'.format(person1=person1._id,
                                                                                                     person2=person2._id))



    def log_infection_survival(self, person, did_die_from_infection):
        with open(self.file_name, 'a') as file:
            if did_die_from_infection is True:
                log = '{} died from infection\n'.format(person._id)
                file.write(log)
                return
            else:
                log = '{} survived infection\n'.format(person._id)
                file.write(log)



    def log_time_step(self, time_step_number):
        with open(self.file_name, 'a') as file:
            log = 'Time step {num} ended, beginning {num_plus}...\n"'.format(num=time_step_number,
                                                                            num_plus=time_step_number+1)
            file.write(log)

