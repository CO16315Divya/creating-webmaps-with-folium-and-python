import folium
import pandas
import json
data=pandas.read_csv("data_file.csv")
lat=list(data["lat"])
lon=list(data["lng"])
population=list(data["pop"])

def provide_color(populations):
    if populations < 1000:
        return 'green'

    elif 1000<=populations<=100000 :
        return 'orange'

    else:
      return 'red'



map=folium.Map(location=[30.72,99.6], zoom_start=3 , tiles='Mapbox Bright')

fg= folium.FeatureGroup(name="My Map")
for lt,ln,popu in zip(lat,lon,population):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=5, popup=str(popu)+"ppa",
    fill_color=provide_color(popu), color='grey',fill=True, fill_opacity= 0.7))

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'orange' if 1000000 <=x['properties']['POP2005']<= 20000000 else 'red'}))

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("map1.html")
