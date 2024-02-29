
# Using CSV

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    day = []
    temp = []
    condition = []
    for row in data:
        if row[0] == "day":
            pass
        else:
            day.append(row[0])
            temp.append(row[1])
            condition.append(row[2])
            
# Using Pandas 

import pandas as pd 

data = pd.read_csv("weather_data.csv")

# Normal form to calculate mean
data_temp = data["temp"].to_list()
mean = sum(data_temp) / len(data_temp)

# Pandas form to calculate mean
mean = data["temp"].mean()

# Calculate max temp
max_temp = data["temp"].max()

# Get Data in columns
colum = data["condition"]
colum = data.condition

# Get Data in row (Monday)
row = data[data.day == "Monday"]

# Get Data in row (Max temp)
row = data[data.temp == data.temp.max()]

# Get Monday Temp in Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp 
monday_temp_F = (monday_temp * 9/5) + 32

# Create a dataframe from scratch 
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "score" : [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")




