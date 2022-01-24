# Siia lisame importid
import random
from Group import Group

class Randomizer:
    groups = []
    members = []
    fixed_groups = []

    def __init__(self, members):
        self.members = members

    def handleFixedGroups(self):
        for fixed_group in self.fixed_groups:
            if fixed_group not in self.groups:
                self.groups.append(fixed_group)
                for member in fixed_group:
                    self.members.remove(member)

    def randomize(self):
        if len(self.fixed_groups) > 0:
            self.handleFixedGroups()

        group = Group()

        original_length = len(self.members) # 6

        for member in range(0, original_length):
            length = len(self.members) # leiame sisendi listi pikkuse; esimene ring on len() = 6, siis len() = 5, jne

            # listi indekid algava 0st, aga listi pikkus algab 1st, kui on 5-elemendiline list, len()=5, indeksid on: 0,1,2,3,4
            random_index = random.randint(0, length - 1) # leiame random indeksi meie sisendist

            random_member = self.members[random_index] # same uue liikme nime kätte
            group.addMember(random_member) # lisame uue liikme(nime) gruppi

            # Eemaldame entity listist
            self.members.remove(random_member)
            # self.members.pop(random_index) # sama nagu ülemine rida

            if group.getGroupSize() >= group.length: # length = 1 -> 1 >= 2; length = 2 -> 2 >= 2
                self.groups.append(str(group))
                group = Group() # teeme ajutise grupi tühjas ning taaskasutame seda
                group.names = [] # teeme nimede listi tühjaks enne kui hakkame järgmise tsükli ringiga uut min-gruppi looma

    def run(self):
        self.randomize()

    def getGroups(self):
        print(self.groups)

    def setFixedGroups(self, fixed_group):
        self.fixed_groups.append(fixed_group)
