import pyttsx3
import folium
import geocoder
import webbrowser

# ---------- Engine Creation --------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#-----------------------------------------


def myMap() :
    myip = geocoder.ip('me')
    myLocation = myip.latlng

    m = folium.Map(location=[18.443098903366863, 73.83184699883172], zoom_start=15)

    folium.Marker([18.443098903366863, 73.83184699883172],
                  popup="<h6>You are here !!</h6>",
                  tooltip="TSSM's BSCOER",
                  icon=folium.Icon(icon='pencil', icon_color='red', color='black')).add_to(m)

    folium.CircleMarker(
        location=(18.443098903366863, 73.83184699883172),
        radius=50,
        popup='You are somewhere here',
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

    m.save('map.html')
    webbrowser.open_new('map.html')