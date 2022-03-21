import csv 
import plotly.express as px
with open("data.csv")as f:
    df=csv.DictReader(f)
    figure=px.scatter(df,x="Marks",y="Days")
    figure.show()

