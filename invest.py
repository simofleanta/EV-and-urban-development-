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


investing=pd.read_csv('funding.csv')
print(investing.columns)
df=DataFrame(investing.head(5))
#print(df.head(5))

df_invest=df[['created_at','funded_at','raised_amount','raised_amount_usd','is_first_round','is_last_round','funding_round_type','participants']]
print(df_invest.head(4))





