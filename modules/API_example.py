import urllib.request
import json

api_key = "b0a0c97469a37bc09af75bf42fccb0d5"

base_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}"
params = "&query=star+wars&year=2013"

def get_data_from_URL(base_url, options):
    """
    (str, str) -> NoneType
    Takes url and takes and writes into a file data from this url.
    """
    rqst = base_url + options

    with urllib.request.urlopen(rqst) as response:
        data = json.load(response)
        with open('modules/data.json', 'w') as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    get_data_from_URL(base_url, params)