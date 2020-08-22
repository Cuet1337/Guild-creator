import requests

token = 'NzQ2NjEwNzI3Nzg3Mjk4ODc2.X0C1ig.YRgFbHMIWWYMHC8OXPnrLEvPwEQ'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
guild = {
    'channels': None, # Default channels
    'icon': None, # Guild logo/icon
    'name': "cuet1337", # Guild name 
    'region': "europe" #Region
}

p = requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)

if p.status_code == 201:
  print('1 Guild created.')

elif p.status_code == 401:
  print('Token invalid.')
  
elif "You are being rate limited." in p.text:
  print('You are beign rate limited, please try again later.')
