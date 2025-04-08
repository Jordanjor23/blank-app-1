import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import plotly.io as pio
import plotly.subplots as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl import Workbook


#read the csv file
starbucks=pd.read_csv('/workspaces/blank-app-1/Copy_of_cleaned_starbucks.csv')
print(starbucks.head(30))

# Display the first 30 rows of the DataFrame
starbucks_preview =pd.DataFrame(starbucks.head(30))
print(starbucks_preview)












