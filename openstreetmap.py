import folium
import pandas

df = pandas.read_csv("data/Volcanoes-USA.txt")


map_1 = folium.Map(location=[45.372,-121.697],zoom_start=4,tiles='Stamen Toner')

def marker_color(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1000,3000):
        col = 'orange'
    else:
        col ='red'
    return col



for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):

    folium.Marker([lat, lon],popup = name, icon = folium.Icon(color = marker_color(elev))).add_to(map_1)


map_1.save('test.html')
