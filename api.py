import requests

def main():
    print("Search")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks",
            {"q": artist}
        )
    except requests.HTTPError:
        print("Net Problem")

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

main()