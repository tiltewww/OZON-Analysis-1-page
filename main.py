%matplotlib notebook
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
import requests

df = pd.read_csv('result.csv')


def graph(x):
    low_price = []
    high_price = []
    medium_price = []
    for i in range(len(df['Price'])):
        if df['Price'][i] < 1000:
            low_price.append(df['Price'][i])
        elif 1000 < df['Price'][i] < 3000:
            medium_price.append(df['Price'][i])
        elif df['Price'][i] > 3000:
            high_price.append(df['Price'][i])
    all_price = len(low_price) + len(high_price) + len(medium_price)
    lowPercent = (len(low_price) / all_price) * 100
    mediumPercent = (len(medium_price) / all_price) * 100
    highPercent = (len(high_price) / all_price) * 100
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.pie(
        [lowPercent, mediumPercent, highPercent],
        labels=['Low Price', 'Medium Price', 'High Price']
    )
    fig.savefig('graph.jpg')
    img.value = open('graph.jpg', 'rb').read()


def on_button_max(b):
    low_price = []
    high_price = []
    medium_price = []
    for i in range(len(df['Price'])):
        if df['Price'][i] < 1000:
            low_price.append(df['Price'][i])
        elif 1000 < df['Price'][i] < 3000:
            medium_price.append(df['Price'][i])
        elif df['Price'][i] > 3000:
            high_price.append(df['Price'][i])
    all_price = len(low_price) + len(high_price) + len(medium_price)
    MaxPrice = df['Price'].max()
    print(f"Maximum Price: {MaxPrice}")


def on_button_avg(b):
    low_price = []
    high_price = []
    medium_price = []
    for i in range(len(df['Price'])):
        if df['Price'][i] < 1000:
            low_price.append(df['Price'][i])
        elif 1000 < df['Price'][i] < 3000:
            medium_price.append(df['Price'][i])
        elif df['Price'][i] > 3000:
            high_price.append(df['Price'][i])
    all_price = len(low_price) + len(high_price) + len(medium_price)
    AvgPrice = round(
        (sum(low_price) + sum(high_price) + sum(medium_price)) / (len(low_price) + len(medium_price) + len(high_price)),
        1)
    print(f"Average Price: {AvgPrice}")


def on_button_min(b):
    low_price = []
    high_price = []
    medium_price = []
    for i in range(len(df['Price'])):
        if df['Price'][i] < 1000:
            low_price.append(df['Price'][i])
        elif 1000 < df['Price'][i] < 3000:
            medium_price.append(df['Price'][i])
        elif df['Price'][i] > 3000:
            high_price.append(df['Price'][i])
    all_price = len(low_price) + len(high_price) + len(medium_price)
    MinPrice = df['Price'].min()
    print(f"Minimum Price: {MinPrice}")


image = widgets.Image(
    value=requests.get(
        'https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-vikipediya-logotip-na-prozrachnom-fone-40.png').content,
    width=170
)
right = widgets.VBox([
    widgets.HTML('<b>Select Option</b>'),
    widgets.RadioButtons(options=['Price'], value='Price'),
])
left = widgets.VBox([
    widgets.HTML('<b>Show Graphic</b>'),
])

btnAvg = widgets.Button(
    description='Average',
    ButtonStyle='white'
)
btnMax = widgets.Button(
    description='Maximum',
    ButtonStyle='white'
)
btnMin = widgets.Button(
    description='Minimum',
    ButtonStyle='white'
)
btnShow = widgets.Button(
    description='Show',
    ButtonStyle='white'
)

btnShow.on_click(graph)
btnMax.on_click(on_button_max)
btnAvg.on_click(on_button_avg)
btnMin.on_click(on_button_min)

img = widgets.Image()
row1 = widgets.HBox([image])
row2 = widgets.HBox([left, btnShow, right])
row3 = widgets.HBox([btnAvg, btnMax, btnMin])
row4 = widgets.HBox([img])

column = widgets.VBox([row1, row2, row3, row4])
display(column)
