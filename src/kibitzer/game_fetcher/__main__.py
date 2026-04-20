import os
from datetime import datetime, timezone

import requests

def main() -> None:
    username = os.environ["CHESS_COM_USERNAME"]
    now = datetime.now(tz=timezone.utc)
    url = f"https://api.chess.com/pub/player/{username}/games/{now.year}/{now.month:02d}"
    response = requests.get(url, headers={"User-Agent": "kibitzer/0.0.1"}, timeout=30)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
