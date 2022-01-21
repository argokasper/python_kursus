import random

class Group:
    names = []
    length = 2

    def addMember(self, memberName):
        if self.length > len(self.names):
            self.names.append(memberName)
        else:
            print('Ei saa üle ' + str(self.length) + ' liikme lisada')

    def getGroupSize(self):
        return len(self.names)

    def __str__(self):
        # return '[{0}]'.format(",".join(self.names))
        return 'test'









entities = ['Hardy', 'Mihail', 'Heigo', 'Henri', 'Timo', 'Hannes'] # meie sisend; sisendi indeksid: [0, 1, 2, 3, 4, 5]
group_size = 2 #

groups = []

group = Group()

enitites_original_length = len(entities)

for entity in range(0, enitites_original_length):

    entities_length= len(entities) # leiame sisendi listi pikkuse

    # listi indekid algava 0st, aga listi pikkus algab 1st, kui on 5-elemendiline list, len()=5, indeksid on: 0,1,2,3,4
    random_entity_index = random.randint(0, entities_length - 1) # leiame random indeksi meie sisendist

    random_entity = entities[random_entity_index] # same uue liikme nime kätte
    group.addMember(random_entity) # lisame uue liikme gruppi

    # Eemaldame entity listist
    entities.remove(random_entity)

    if group.getGroupSize() >= group_size: # length = 1 -> 1 >= 2; length = 2 -> 2 >= 2
        groups.append(group)
        group = Group() # teeme ajutise grupi tühjas ning taaskasutame seda
        group.names = []

for group in groups:
    print(group.names)


