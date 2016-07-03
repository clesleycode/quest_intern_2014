import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys

names = [] # names ommited for privacy reasons 

random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]


births = [random.randint(low=0,high=1000) for i in range(1000)]
births[:10]


BabyDataSet = zip(random_names,births)
BabyDataSet[:10]

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df.to_csv('births1880.txt',index=False,header=False)

df = pd.read_csv('births1880.txt', names = ['Names', 'Births'])

name = df.groupby('Names')

df = name.sum()
print df
sorted_df = df.sort(['Births'], ascending = False)
print sorted_df

sorted_df.plot(kind = 'line')
plt.show()



