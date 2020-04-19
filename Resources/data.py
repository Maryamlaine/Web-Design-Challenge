import pandas as pd 
import numpy as np

a = pd.read_csv('Resources/cities.csv')
a.to_html("table.html")
html_file = a.to_html() 
