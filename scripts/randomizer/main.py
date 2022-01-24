from logic import Randomizer

members = ['Hardy', 'Mihail', 'Heigo', 'Henri', 'Timo', 'Hannes'] # meie sisend; sisendi indeksid: [0, 1, 2, 3, 4, 5]


randomizer = Randomizer(members) # loob loogikafailist, kus asub klass Randomizer uue objekti
randomizer.setFixedGroups(['Hardy', 'Heigo'])
randomizer.run() # käivitab randomizer "mootori"
randomizer.getGroups() # kuvab välja grupid
