import requests


def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["value"]
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch Chuck Norris joke: {e}"

if __name__ == "__main__":
        joke = get_random_chuck_norris_joke()
        print(joke)
