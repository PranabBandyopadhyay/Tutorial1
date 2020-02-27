from EX35 import data
from bokeh.plotting import figure, show, output_file

output_file('C:\\Users\\Banerjea-PC\\OneDrive\\Documents\\Python_saved\\birthdays.html')

data = data()
x=[]
y=[]
x_catagories = ["January","February","March","April","May","June","July","August","September","October","November","December"]
for key in data.keys():
    x.append(key)
    y.append(data[key])

p = figure(x_range=x_catagories)
p.vbar(x=x, top=y, width=0.5)

show(p)
