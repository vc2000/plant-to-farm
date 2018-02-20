import xlrd
workbook = xlrd.open_workbook("Plant-Farm links.xlsx")
sheet = workbook.sheet_by_index(0)

data =[]
for rowx in range(sheet.nrows):
    cols = sheet.row_values(rowx)
    data.append(cols)


del data[0] # delete the first row


raw_plants = [] # store all the plant names
for i in data:
    del i[3] #delete the last item in each list
    raw_plants.append(i[0])

plants=[]
clean = list(set(raw_plants)) # remove duplicates
for plant in clean:
    plants.append(plant)

plants.sort()


lens=len(plants)
start = 0

farm_supply_to_plant= dict()

while start < lens:
    name = plants[start]
    dic= dict()
    start += 1
    for line in data:
        if name in line:
            dic.setdefault(line[0],[]).append(line[2])
    farm_supply_to_plant[name]=dic



count =1
for plants in farm_supply_to_plant:
    print(count)
    count +=1
    print(farm_supply_to_plant[plants])
