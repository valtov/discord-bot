import requests
import os

TOKEN = os.getenv('BATTLEMETRICS_TOKEN')

class DayZ:
    servers = {"la5540": "12350022"} 
    endpoint = "https://api.battlemetrics.com/servers/{}"

    def __init__(self, server='la5540'):
        self.server = server

    def get_player_count(self):
        r = requests.get(DayZ.endpoint.format(DayZ.servers[self.server]), headers={'Authorization': f'{TOKEN}'})
        if r.status_code == 200:
            response = r.json()
            return response['data']['attributes']['players']
        else:
            print(r.status_code, r.text)
            return -float('inf')

if __name__ == '__main__':
    dayz = DayZ()
    print(dayz.get_player_count())