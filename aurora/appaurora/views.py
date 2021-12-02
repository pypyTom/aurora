import json
import urllib.request
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['search']
    
        if city == '':
            return redirect('index')
        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city.replace(" ","%20")}&appid=1b79ea7b1251b76ccda830b41a81d6bd').read()
       
        #zmienna otwiera adres api po q zmiena przekazuje wpisana nazwe miasta 
        json_data = json.loads(res)
        #zmienna zawiera dane z api w formacie json
        datas = {
            "country_code" : str(json_data['sys']['country']),
            "cordinate": str(json_data['coord']['lon'])+ ''+ 
            str(json_data['coord']['lat']),
            "temp": str(int(json_data['main']['temp']-273)) + 'C',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),

        }
    else:
        city = ''
        datas = {}
    

        
    return render(request,'index.html', {'city':city, 'datas':datas});