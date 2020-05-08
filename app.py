import folium
import pandas as pd

corona_map = folium.Map(location=[14.4974,-14.4524], zoom_start=2)
confirmed_statistics = pd.read_csv('Blog_corona.csv')
for index, row in confirmed_statistics.iterrows():
    _, country, latitude, longitude, confirmed = row
    popup_text = country + '\n' + str(confirmed) + ' cases'
    folium.CircleMarker(location=[latitude, longitude], radius=10, popup=popup_text,color='#3186cc',fill=True,fill_color='#3186cc').add_to(corona_map)
corona_map.save('index.html')    