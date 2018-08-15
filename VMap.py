import folium
import pandas
map=folium.Map(location=[38.58,-99.09],zoom_start=5, tiles=("Mapbox Bright"))
volcano=pandas.read_csv("Volcanoes_USA.txt")
lat=list(volcano["LAT"])
lon=list(volcano["LON"])
elevation=list(volcano["ELEV"])
name=list(volcano["NAME"])

def pcolor(el):
    if el < 1000:
        return 'green'
    elif 1000<= el <3000:
        return 'orange'
    else:
        return 'red'
fgv= folium.FeatureGroup(name="Volcanoes")

for lat,lon,el,na in zip(lat,lon,elevation,name):
    fgv.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup("Name: "+str(na)+"  Elevation: "+str(el)+" m",parse_html=True),icon=folium.Icon(color=pcolor(el))))


fgp= folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' if 20000000 <= x['properties']['POP2005'] < 40000000 else 'yellow'}))


map.add_child(fgv)
map.add_child(fgp)


map.add_child(folium.LayerControl())


map.save("Map1.html")
