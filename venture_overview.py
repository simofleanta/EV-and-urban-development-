import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px

#open file
finance=pd.read_csv('Margin_Analysis.csv')
print(finance.columns)
df_v=DataFrame(finance.head(100))
print(df_v.head(10))

#extract year 2020
Year2020=df_v[df_v.Year==2020]

#extract 2019
Year2019=df_v[df_v.Year==2019]
Year2018=df_v[df_v.Year==2018]
Year2017=df_v[df_v.Year==2017]


#plotly pie
#df = px.data.tips()
#fig = px.pie(df_v, values='Total_gross_sales', names='Month', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='M')


#correlations
#plt.figure(figsize=(3,2))
#sns.heatmap(df_v.corr(), annot=True, cmap='Blues')
#plt.show()

#plot line gross margins

#plt.title('Gross margins')
#plt.plot(Year2019.Month, Year2019.Total_gross_sales, label='Total_gross_sales')
#plt.plot(Year2019.Month, Year2019.Sales_Margin, label='Sales_Margin')
#plt.legend()
#plt.show()

#scatter
#plt.scatter(df_v.Gross_Margin, df_v.Total_gross_sales, cmap='Blues', edgecolors='k', alpha=0.55)
#plt.show()

#boxplot with 2 vars
#sns.boxplot(x='Year',y='Sales_Gross', data=df_v)
#plt.show()

#pairplot = sns.pairplot(Year2019, vars=['Sales_Gross','Gross_Margin'])
#plt.show()


#scatter dashboard on sales gross and total sales in 4 years 
f,axes = plt.subplots(2,2, figsize=(15,13))
axes[0,0].scatter(Year2020.Sales_Gross, Year2020.Total_gross_sales, cmap='summer', edgecolors='k',\
     alpha=0.55)

axes[0,1].scatter(Year2019.Sales_Gross, Year2019.Total_gross_sales, cmap='viridis', edgecolors='k', \
    alpha=0.55)

axes[1,0].scatter(Year2018.Sales_Gross, Year2018.Total_gross_sales, cmap='ice', edgecolors='k', \
    alpha=0.55)

axes[1,1].scatter(Year2017.Sales_Gross, Year2017.Total_gross_sales, cmap='husl', edgecolors='k', \
    alpha=0.55)


plt.show()




























