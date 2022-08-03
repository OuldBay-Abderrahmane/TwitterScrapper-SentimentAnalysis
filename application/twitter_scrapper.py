import requests
import os
import json

bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def fetch_data(params):
    lang = 'en'
    query_params = {
        'query': f'({params.words}) {params.exacts} lang:en', 'max_results': '100', 'tweet.fields': 'author_id'}
    json_response = connect_to_endpoint(search_url, query_params)
    with open("application/scripts/tweets.json", "w") as outfile:
        json.dump(json_response, outfile, indent=4)


if __name__ == "__main__":
    json_response = fetch_data()
