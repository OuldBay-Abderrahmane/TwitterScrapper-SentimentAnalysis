import requests
import os
import json

bearer_token = os.environ.get("BEARER_TOKEN")


search_url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {
    'query': 'Omicron lang:en', 'tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    return json_response


if __name__ == "__main__":
    json_response = main()
    with open("tweets.json", "w") as outfile:
        json.dump(json_response, outfile)
