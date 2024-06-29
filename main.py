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
    if df['Price'][i] < 1000: low_price.append(df['Price'][i])
    elif 1000 < df['Price'][i] < 3000: medium_price.append(df['Price'][i])
    elif df['Price'][i] > 3000: high_price.append(df['Price'][i])
  all_price = len(low_price) + len(high_price) + len(medium_price)
  lowPercent = (len(low_price)/all_price)*100
  mediumPercent = (len(medium_price)/all_price)*100
  highPercent = (len(high_price)/all_price)*100
  fig = plt.figure()
  ax = fig.add_subplot()
  ax.pie(
      [lowPercent, mediumPercent, highPercent],
      labels = ['Low Price', 'Medium Price', 'High Price']
    )
  fig.savefig('graph.jpg')
  img.value = open('graph.jpg', 'rb').read()

def rateGraph(b):
  five_rate = []
  good_rate = []
  low_rate = []
  for i in range(len(df['Rate'])):
    if df['Rate'][i] == 5.0: five_rate.append(df['Rate'][i])
    elif 4.5 <= df['Rate'][i] < 5.0: good_rate.append(df['Rate'][i])
    elif df['Rate'][i] > 4.5: low_rate.append(df['Rate'][i])
  fig = plt.figure()
  ax = fig.add_subplot()
  ax.pie(
      [len(low_rate), len(good_rate), len(five_rate)],
      labels = ['Bad Rating', 'Good Rating', 'Best Rating']
  )
  fig.savefig('rateGraph.jpg')
  img.value = open('rateGraph.jpg', 'rb').read()

def reviewGraph(b):
  alotReview = []
  mediumReview = []
  alittlebitReview = []
  for i in range(len(df['Review'])):
    if df['Review'][i] > 10000: alotReview.append(df['Review'][i])
    elif 2000 < df['Review'][i] < 10000: mediumReview.append(df['Review'][i])
    elif df['Review'][i] < 2000: alittlebitReview.append(df['Review'][i])
  fig = plt.figure()
  ax = fig.add_subplot()
  ax.pie(
      [round(len(alittlebitReview)), round(len(mediumReview)), round(len(alotReview))],
      labels = ['Few reviews', 'Average Reviews', 'A lot of Reviews']
  )
  fig.savefig('reviewGraph.jpg')
  img.value = open('reviewGraph.jpg', 'rb').read()

def on_button_max(b):
  low_price = []
  high_price = []
  medium_price = []
  for i in range(len(df['Price'])):
    if df['Price'][i] < 1000: low_price.append(df['Price'][i])
    elif 1000 < df['Price'][i] < 3000: medium_price.append(df['Price'][i])
    elif df['Price'][i] > 3000: high_price.append(df['Price'][i])
  all_price = len(low_price) + len(high_price) + len(medium_price)
  MaxPrice = df['Price'].max()
  MinPrice = df['Price'].min()
  AvgPrice = round((sum(low_price) + sum(high_price) + sum(medium_price)) / (len(low_price) + len(medium_price) + len(high_price)), 1)
  print(f"Maximum Price: {MaxPrice}")

def on_button_avg(b):
  low_price = []
  high_price = []
  medium_price = []
  for i in range(len(df['Price'])):
    if df['Price'][i] < 1000: low_price.append(df['Price'][i])
    elif 1000 < df['Price'][i] < 3000: medium_price.append(df['Price'][i])
    elif df['Price'][i] > 3000: high_price.append(df['Price'][i])
  all_price = len(low_price) + len(high_price) + len(medium_price)
  MaxPrice = df['Price'].max()
  MinPrice = df['Price'].min()
  AvgPrice = round((sum(low_price) + sum(high_price) + sum(medium_price)) / (len(low_price) + len(medium_price) + len(high_price)), 1)
  print(f"Average Price: {AvgPrice}")

def on_button_min(b):
  low_price = []
  high_price = []
  medium_price = []
  for i in range(len(df['Price'])):
    if df['Price'][i] < 1000: low_price.append(df['Price'][i])
    elif 1000 < df['Price'][i] < 3000: medium_price.append(df['Price'][i])
    elif df['Price'][i] > 3000: high_price.append(df['Price'][i])
  all_price = len(low_price) + len(high_price) + len(medium_price)
  MaxPrice = df['Price'].max()
  MinPrice = df['Price'].min()
  AvgPrice = round((sum(low_price) + sum(high_price) + sum(medium_price)) / (len(low_price) + len(medium_price) + len(high_price)), 1)
  print(f"Minimum Price: {MinPrice}")

def changeRadioBtns(change):
  if change.new == 'Price': btnShow.on_click(graph)
  elif change.new == 'Rating': btnShow.on_click(rateGraph)
  elif change.new == 'Reviews': btnShow.on_click(reviewGraph)

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

image = widgets.Image(
    value = requests.get('https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-vikipediya-logotip-na-prozrachnom-fone-40.png').content,
    width = 170
)
right = widgets.VBox([
    widgets.HTML('<b>Select Option</b>'),
])
radio_buttons = widgets.RadioButtons(options=['Price', 'Rating', 'Reviews'], value='Price')
left = widgets.VBox([
    widgets.HTML('<b>Show Graphic</b>')
])
btnShow.on_click(graph)

radio_buttons.observe(changeRadioBtns, names='value')
btnMax.on_click(on_button_max)
btnAvg.on_click(on_button_avg)
btnMin.on_click(on_button_min)
img = widgets.Image()
row1 = widgets.HBox([image])
row2 = widgets.HBox([left, btnShow, right, radio_buttons])
row3 = widgets.HBox([btnAvg, btnMax, btnMin])
row4 = widgets.HBox([img])
column=widgets.VBox([row1, row2, row3, row4])
display(column)
