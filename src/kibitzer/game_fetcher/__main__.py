import requests

def main() -> None:
    url = "https://api.chess.com/pub/player/arunraghunath/games/2026/04"
    response = requests.get(url, headers={"User-Agent": "kibitzer/0.0.1"}, timeout=30)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
