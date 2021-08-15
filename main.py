import pandas as pd
import plotly.express as px

df = pd.read_csv("main.csv")

GRE_Score = df["GRE Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()


m=0.01
c=-2.5
y=[]

for x in GRE_Score:
    y_value=m*x + c
    y.append(y_value)

    fig=px.scatter(x=GRE_Score,y=Chances_of_admit)
    fig.update_layout(shapes=[dict(type='line', y0 = min(y),y1=max(y),x0=min(GRE_Score), x1=max(GRE_Score))])

fig.show()

x=600
y=m*x +c
print(f"Chances of atmitation witth its GRE score {x} is {y}")

import numpy as np 
GRE_Score=np.array(GRE_Score)
Chances_of_admit=np.array(Chances_of_admit)
#the slope and intercept using pre built function
m,c=np.polyfit(GRE_Score, Chances_of_admit,1)

y=[]
for x in GRE_Score:
    y_value=m*x + c
    y.append(y_value)

    fig=px.scatter(x=GRE_Score,y=Chances_of_admit)
    fig.update_layout(shapes=[dict(type='line', y0 = min(y),y1=max(y),x0=min(GRE_Score), x1=max(GRE_Score))])