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

#pening a file
git=pd.read_csv('GitHub_data.csv')
print(git.columns)
df=DataFrame(git.head(20))
print(df.head(20))

#making sense of data 
c=df.dtypes
c_missing=df.isnull().sum()
print(c_missing)
x=c.describe()
#print(x)
x_describe=df.describe()
print(x_describe)
x_shape=df.shape
print(x_shape)

#just in case need to encode numerical 
#encoder=LabelEncoder()
#numerical=df['date']=encoder.fit_transform(df['date'])

xdf=df[['topic','projects','contributers','name','user','star','fork','issue','License','commits']].copy()
#print(xdf)








