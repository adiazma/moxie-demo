from projects.base_project import BaseProject
from requests import Request
import json

class PokemonScraper(BaseProject):

    BASE_URL: str = 'pokeapi.co'

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def run(self, **kwargs) -> dict:
        
        # GET POKEMON LIST
        search_by_pokemon = True
        pokemon = kwargs.get('queryStringParameters')
        if pokemon is None:
            search_by_pokemon = False
        elif pokemon.get('name') is None:
            search_by_pokemon = False
        elif len(pokemon.get('name')) <= 3:
            search_by_pokemon = False

        if search_by_pokemon:
            pokemon = pokemon['name']
            print('Searching for pokemon: {0}'.format(pokemon))
            url = f'https://{self.BASE_URL}/api/v2/pokemon?limit=100000'
            request = Request('GET', url=url)
            req = self._session.prepare_request(request)
            res = self._session.send(req, verify=False).json().get('results', [])
            res = list(filter(lambda x: pokemon.lower() in x['name'].lower(), res))
        else:
            url = f'https://{self.BASE_URL}/api/v2/pokemon?limit=10'
            request = Request('GET', url=url)
            req = self._session.prepare_request(request)
            res = self._session.send(req, verify=False).json().get('results', [])

        # GET POKEMON DATA
        total = []
        for item in res:

            # GET DETAILS
            request = Request('GET', url=item['url'])
            req = self._session.prepare_request(request)
            data = self._session.send(req, verify=False).json()

            # GET ENCOUNTERS
            request = Request('GET', url='{0}encounters'.format(item['url']))
            req = self._session.prepare_request(request)
            encounters = self._session.send(req, verify=False).json()

            # SET DATA
            total.append({
                'id': data.get('id'),
                'name': data.get('name'),
                'height': data.get('height'),
                'weight': data.get('weight'),
                'abilities': [a.get('ability', {}).get('name') for a in data.get('abilities', [])],
                'Location_area_encounters': [a.get('location_area', {}).get('name') for a in encounters],
            })

        print('Result: {0}'.format(total))
        return {
            'statusCode': 200,
            'body': json.dumps({'result': total})
        }