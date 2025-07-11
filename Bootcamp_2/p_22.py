
# pertemuan 22

import requests
respon = requests.get(url='http://api.open-notify.org/iss-now.json')
print(respon)
# 1xx = artinya hold on     2xx = success       3xx = pergi lu      4xx = masalah ada di pengguna    5xx = masalah ada di server
print(respon.status_code) #buat cek klo API ada yg error

data = respon.json()
# print(data)
lat = data['iss_position']['latitude']
long = data['iss_position']['longitude']
position = (lat, long)
print(f'POSISI data ISS:\t{position}')


my_lat = -1.909870
my_long = 116.194321
my_format = 0
my_timzone = 'Asia/Hong_Kong'
# day = 


parameters = {
    'lat':my_lat,
    'lng':my_long,
    'tzid':my_timzone
    
}
respon = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
respon.raise_for_status()
data = respon.json()

zone = data['tzid']
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']


print(f'Sunset at {sunset} in gatau {sunrise}')
print(data)

