import folium

mymap = folium.Map
mymap = folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')
mymap.save('test.html')
