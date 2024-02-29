import pandas as pd 

data = pd.read_csv("Squirrel_Data.csv")

colors = ["Cinnamon", "Gray", "Black"]

data_dic = {
    "Fur Color": colors,
    "Count": []
}

for color in colors:
    num = len(data[data["Primary Fur Color"] == color])
    data_dic["Count"].append(num)

data = pd.DataFrame(data_dic)
data.to_csv("data_dic.csv")




