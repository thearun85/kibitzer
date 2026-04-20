import logging
import os
from datetime import datetime, timezone

import requests

from kibitzer.game_fetcher.parser import parse_game

logger = logging.getLogger(__name__)

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    
    username = os.environ["CHESS_COM_USERNAME"]
    now = datetime.now(tz=timezone.utc)
    url = f"https://api.chess.com/pub/player/{username}/games/{now.year}/{now.month:02d}"
    logger.info("Fetching games for %s from %s", username, url)
    
    response = requests.get(url, headers={"User-Agent": "kibitzer/0.0.1"}, timeout=30)
    response.raise_for_status()

    payload = response.json()
    events = [parse_game(raw) for raw in payload["games"]]
    logger.info("Parsed %d games", len(events))
    for event in events:
        logger.info("%s %s vs %s %s", event.played_at.date(), event.white, event.black, event.result)

if __name__ == '__main__':
    main()
