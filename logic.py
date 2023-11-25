import phonenumbers
import shutil
import folium
from phonenumbers.geocoder import description_for_number
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import os 

def location(pno):
    theNumber = phonenumbers.parse(pno)
    yourLocation = description_for_number(theNumber, "en")
    print(yourLocation)


#Other details


    service_provider = phonenumbers.parse(pno)
    c_name=carrier.name_for_number(service_provider, "en")
    print(c_name)


    geocoder = OpenCageGeocode("3b764c9c087a4b7d8c80f78aafb14732")
    query =str(yourLocation)
    results = geocoder.geocode(query)
#print(results)

    lat = results[0]['geometry']['lat']

    long = results[0]['geometry']['lng']

    print(lat, long)


    myMap = folium.Map(location =[lat, long], zoom_start= 0)

    folium.Marker([lat , long], popup=  yourLocation).add_to(myMap)

    myMap.save("myLoc.html")

    org=r'E:\\flask project\\myLoc.html'
    target=r'E:\\flask project\\templates\\myloc.html'
    shutil.copyfile(org,target)
    
    """
    inipath='myLoc.html'
    path=os.path.abspath('myLoc.html')
    newloc='E:\flask project\templates\\'+inipath
    shutil.copy(inipath,newloc)
    """
    print(c_name)
    return yourLocation,c_name