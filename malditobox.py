class MalditoBox(object):
    items = [""]*5
    prices = [0]*5
    elements = 0

    def __init__(self):
        pass

    def _price(self):
        return sum(self.prices)

    def _add_item(self, malditoitem):
        if self.elements <5  and (self._price() + malditoitem[1]):
            self.items[self.elements]=malditoitem[0]
            self.prices[self.elements] = malditoitem[1]
            self.elements = self.elements + 1

    def print(self):
        return self.items.copy()

    def clear(self):
        self.items = [""] * 5
        self.prices = [0] * 5
        self.elements = 0


class MalditoItems(object):
    items=[["AlaspuertasdeLoyang",45],
    ["Agra", 65],
    ["Airetierraymar",15],
    ["AmunReEljuegodecartas",20],
    ["Bees",18],
    ["BlackAngel",70],
    ["Bosk",35],
    ["BrassBirminghan",60],
    ["BrassLancashire",60],
    ["Cairn",30],
    ["CarpeDiem",43],
    ["CartaventuraLhasa",10],
    ["CartaventuraVinland",10],
    ["Cazamosquitos",22],
    ["CenaenParis",45],
    ["Charterstone",70],
    ["CloudCity",27],
    ["CodexNaturalis",15],
    ["Coinx",15],
    ["ColoniasCosmicas",45],
    ["ColonosdelimperioRollwrite",25],
    ["ConejosSaltarines",20],
    ["CrystalPalace",55],
    ["Cubirds",15],
    ["CuriousCargo",35],
    ["Cuzco",55],
    ["Dalielzorro",20],
    ["DawnoftheZeds",75],
    ["DetectivesParanormales",45],
    ["ElForodeTrajano",50],
    ["ElGranBosque",22],
    ["EljardindeAlicia",20],
    ["Enelanodeldragon",43],
    ["Endeavor",25],
    ["EntredoscastillosdelreylocoLudwig",45],
    ["EntredoscastillosdelreylocoLudwigSecretosyveladasconelbase",65],
    ["ErizosArodar",25],
    ["Exploradoresdelmundoperdido",25],
    ["Feudum",80],
    ["Fuji",28],
    ["Furnace",27],
    ["Gentes",45],
    ["GorintoExpansiones",40],
    ["Herbaceas",20],
    ["Herrlof",12],
    ["Isladelosgatos",50],
    ["Laisladelbotin",20],
    ["LaStanza",60],
    ["LibrojuegoViajeporlastierrasocres",18],
    ["Lincoln",40],
    ["Livingforest",40],
    ["Llamaland",35],
    ["LoscienTorii",40],
    ["LunaEdicionDeluxe",100],
    ["MaestrosdelRenacimiento",36],
    ["Mafiozoo",45],
    ["Merv",50],
    ["MipequenoScythe",50],
    ["MipequenoScytheCastillosenelaireconelbase",70],
    ["MonolithArena",40],
    ["NorthAmericanRailways",27],
    ["NotreDame",45],
    ["Paperdungeons",25],
    ["PatchworkExpres",18],
    ["Pendulum",55],
    ["Pipeline",55],
    ["PixelTactics",20],
    ["Prehistorias",25],
    ["Pretaporter",55],
    ["Primercontacto",25],
    ["Queenz",32],
    ["ReinosRodados",20],
    ["Riftforce",20],
    ["Secretosentreamigos",12],
    ["SmartphoneInc",55],
    ["SmartphoneIncActualizacion1soloconelbase",70],
    ["SpaceBase",40],
    ["Tak",40],
    ["Tawantinsuyu",55],
    ["Tekhenu",55],
    ["TerraformingMars",50],
    ["TierrasBajas",50],
    ["Tikal",55],
    ["Tortuga2199",50],
    ["Tortuga2199Labahiadelosnaufragiosconelbase",65],
    ["Trek12",25],
    ["USTelegraph",40],
    ["Viticulture",60],
    ["Wingspan",55],
    ["YellowYangtze",45]]

    length = 0

    def __init__(self):
        self.length = len(self.items)

combinations = []
combinationprices =[]
malditoitems = MalditoItems()

first_iter = 0
second_iter = 0
third_iter = 0
fourth_iter = 0
fifth_iter = 0
candidate = MalditoBox()
candidateprice = []
for first_iter in range(0,malditoitems.length):
    for second_iter in range(first_iter + 1, malditoitems.length):
        for third_iter in range(second_iter + 1, malditoitems.length):
            for fourth_iter in range(third_iter + 1 , malditoitems.length):
                for fifth_iter in range(fourth_iter + 1 , malditoitems.length):

                    candidate._add_item(malditoitems.items[first_iter])
                    candidate._add_item(malditoitems.items[second_iter])
                    candidate._add_item(malditoitems.items[third_iter])
                    candidate._add_item(malditoitems.items[fourth_iter])
                    candidate._add_item(malditoitems.items[fifth_iter])

                    candidateprice = [malditoitems.items[first_iter][1], malditoitems.items[second_iter][1],
                                      malditoitems.items[third_iter][1], malditoitems.items[fourth_iter][1],
                                      malditoitems.items[fifth_iter][1]]

                    if candidate.elements == 5 and candidate._price() > 150 and candidate._price() < 170:
                        combinations.append(candidate.print())
                        combinationprices.append(candidateprice)
                    candidate.clear()
                    candidateprice = []

print ("Number of combinations")
print (len(combinations))

probabilities = []

for first_iter in range(0,malditoitems.length):
    count = 0
    game = malditoitems.items[first_iter][0]
    price = malditoitems.items[first_iter][1]
    for i in range(0,len(combinations)):
        if game in combinations[i]:
            count = count + 1
    probabilities.append([game,count, price])


print ("Game / Combinations / Price")
for first_iter in range(0,len(probabilities)):
    print(probabilities[first_iter])

LISTPRICES=[10,12,15,18,20,22,25,27,28,30,32,35,36,40,43,45,50,55,60,65,70,75,80,100]

firstpricesprob = []
for i in LISTPRICES:
    count = 0
    for j in combinationprices:
        if i == j[0]:
            count = count + 1
    firstpricesprob.append([i, count])

print ("Price 1st column/ Combinations")
for first_iter in range(0,len(firstpricesprob)):
    print(firstpricesprob[first_iter])

secondpricesprob = []
for i in LISTPRICES:
    count = 0
    for j in combinationprices:
        if i == j[1]:
            count = count + 1
    secondpricesprob.append([i, count])

print ("Price 2nd column/ Combinations")
for first_iter in range(0,len(secondpricesprob)):
    print(secondpricesprob[first_iter])

thirdpricesprob = []
for i in LISTPRICES:
    count = 0
    for j in combinationprices:
        if i == j[2]:
            count = count + 1
    thirdpricesprob.append([i, count])

print ("Price 3rd column/ Combinations")
for first_iter in range(0,len(thirdpricesprob)):
    print(thirdpricesprob[first_iter])

fourthpricesprob = []
for i in LISTPRICES:
    count = 0
    for j in combinationprices:
        if i == j[3]:
            count = count + 1
    fourthpricesprob.append([i, count])

print ("Price 4th column/ Combinations")
for first_iter in range(0,len(fourthpricesprob)):
    print(fourthpricesprob[first_iter])

fifthpricesprob = []
for i in LISTPRICES:
    count = 0
    for j in combinationprices:
        if i == j[4]:
            count = count + 1
    fifthpricesprob.append([i, count])

print ("Price 5th column/ Combinations")
for first_iter in range(0,len(fifthpricesprob)):
    print(fifthpricesprob[first_iter])

probabilidadescondicionadas=[]

first_line = ['',]
for i in range(0, malditoitems.length):
    first_line.append(malditoitems.items[i][0])
probabilidadescondicionadas.append(first_line)

for i in range(0, malditoitems.length):
    probabilidadescondicionadas.append([malditoitems.items[i][0],])

for j in range(1, malditoitems.length + 1):
    pivote = probabilidadescondicionadas[j][0]
    ocurrencies = 100000000000000
    for k in probabilities:
        if pivote == k[0]:
            ocurrencies = k[1]
            print(ocurrencies)
    for first_iter in range(1, malditoitems.length + 1):
        if i < j:
            probabilidadescondicionadas[j].append(probabilidadescondicionadas[i][j])
        count = 0
        game = probabilidadescondicionadas[0][first_iter]
        for i in range(0, len(combinations)):
            if game in combinations[i] and pivote in combinations[i]:
                count = count + 1
        probabilidadescondicionadas[j].append(count*100/ocurrencies)
    print (j)


print ("Probabilidades condicionadas")
for j in range(0, len(probabilidadescondicionadas)):
    print (probabilidadescondicionadas[j])
