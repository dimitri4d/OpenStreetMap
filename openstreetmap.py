import folium
import pandas

df = pandas.read_csv("data/Volcanoes-USA.txt")

avgLAT = df['LAT'].mean()
avgLON = df['LON'].mean()


map_1 = folium.Map(location=[avgLAT, avgLON],zoom_start=4,tiles='Stamen Toner')


def marker_color(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1000,3000):
        col = 'orange'
    else:
        col ='red'
    return col


volcano_fg = folium.FeatureGroup(name="Volcano Locations")


for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):

    folium.Marker([lat, lon],popup = name, icon = folium.Icon(color = marker_color(elev))).add_to(volcano_fg)

volcano_fg.add_to(map_1)

map_1.add_child(folium.LayerControl())

map_1.save('test1.html')
