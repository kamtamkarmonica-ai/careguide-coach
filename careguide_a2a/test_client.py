# careguide_a2a/test_client.py

import asyncio
import json
from urllib import request

A2A_ENDPOINT = "http://localhost:8081"  # same host/port as your server

async def main():
    url = A2A_ENDPOINT + "/_a2a/metadata"

    print(f"Calling A2A server at: {url}")
    resp = request.urlopen(url)
    data = resp.read().decode("utf-8")

    print("\nRaw response:")
    print(data)

    try:
        parsed = json.loads(data)
        print("\nPretty JSON:")
        print(json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        print("\n(Response was not JSON, but the server is reachable!)")

if __name__ == "__main__":
    asyncio.run(main())
