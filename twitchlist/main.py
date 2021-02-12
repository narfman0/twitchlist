#!/usr/bin/env python3

from urllib.request import urlopen, Request
import json
import os

PERSISTED_QUERY_HASH = os.environ["PERSISTED_QUERY_HASH"]
CLIENT_ID = os.environ["CLIENT_ID"]
OAUTH_AUTHORIZATION = os.environ["OAUTH_AUTHORIZATION"]


class colors:
    RESET = "\033[0m"
    UNDERLINE = "\033[04m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    YELLOW = "\033[93m"
    PINK = "\033[95m"


def p(str):
    print(f"{colors.RESET}{str}")


def fetch():
    data = json.dumps(
        [
            {
                "operationName": "PersonalSections",
                "variables": {
                    "input": {"sectionInputs": ["FOLLOWED_SECTION"]},
                    "channelLogin": None,
                    "withChannelUser": False,
                },
                "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": PERSISTED_QUERY_HASH,
                    }
                },
            }
        ]
    ).encode("utf-8")

    return urlopen(
        Request(
            "https://gql.twitch.tv/gql",
            data=data,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Client-Id": CLIENT_ID,
                "Authorization": OAUTH_AUTHORIZATION,
            },
        )
    )


def main(items):
    for item in items:
        content = item.get("content", {}) or {}

        if content.get("type") != "live":
            continue

        title = item["user"]["broadcastSettings"]["title"].strip()
        if title.lower().startswith("rerun"):
            continue

        p(f"{colors.PURPLE}{item['user']['login']}{colors.RESET} - {title}")

        game = content.get("game", None)
        if game:
            p(
                f"Playing {colors.BLUE}{game['displayName']}{colors.RESET} for {colors.YELLOW}{content.get('viewersCount', 0)}{colors.RESET} viewers"
            )
        else:
            p(f"{colors.YELLOW}{content.get('viewersCount', 0)}{colors.RESET} viewers")

        print("")


if __name__ == "__main__":
    with fetch() as f:
        main(json.loads(f.read())[0]["data"]["personalSections"][0]["items"])
