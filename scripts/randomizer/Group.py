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
        return '[{0}]'.format(", ".join(self.names))
