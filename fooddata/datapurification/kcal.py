import pandas as pd

df = pd.read_csv("./FoodList.csv", encoding = 'utf-8')
eat = input('밥을 입력하세요 : ')
find_row = df.loc[df['식품명'] == eat ]

food_name = eat
weight = find_row.loc[:,'1회제공량(g)']
kcal = find_row.loc[:,'에너지(Kcal)']
carbohydrate = find_row.loc[:,'탄수화물(g)']
protein = find_row.loc[:,'단백질(g)']
fat = find_row.loc[:,'지방(g)']
sugar = find_row.loc[:,'총당류(g)']
sodium = find_row.loc[:,'나트륨(mg)']

print('음식 : {}'.format(eat) )
print('        1회제공량 : {}g'.format(int(weight)) )
print('        에너지 : {}kcal'.format(int(kcal)) )
print('        탄수화물 : {}(g)'.format(int(carbohydrate)) )
print('        단백질 : {}(g)'.format(int(protein)) )
print('        지방 : {}(g)'.format(int(fat)) )
print('        총당류 : {}(g)'.format(int(sugar)) )
print('        나트륨 : {}(mg)'.format(int(sodium)) )

