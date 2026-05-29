import urllib.request
import urllib.error
from time import sleep
import json
import os

CONNECT_URL=os.environ['CONNECT_URL']
PG_USER=os.environ['PG_USER']
PG_PASSWORD=os.environ['PG_PASSWORD']
PG_HOST=os.environ['PG_HOST']
PG_PORT=os.environ['PG_PORT']
PG_DBNAME=os.environ['PG_DBNAME']

connected = False
while not connected:
    try:
        with urllib.request.urlopen(CONNECT_URL) as response:
            response_code = response.code
        if response_code == 200:
            connected = True
        else:
            print(f"Not connected yet: {response_code}")
            sleep(5)
    except (ConnectionRefusedError, urllib.error.URLError) as e:
        print(f"Not connected yet: {e.reason}")
        sleep(5)

print("Connector is up! Registering json...")
try:
    content = {
      "name": "registry-connector",
      "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": PG_HOST,
        "database.port": PG_PORT,
        "database.user": PG_USER,
        "database.password": PG_PASSWORD,
        "database.dbname": PG_DBNAME,
        "topic.prefix": "registry",
        "slot.name": "registry_slot",
        "publication.autocreate.mode": "filtered"
      }
    }

    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        CONNECT_URL,
        headers=headers,
        data=json.dumps(content).encode('utf-8'),
        method='POST'
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(result)

    print("Finished registering connector!")
except urllib.error.HTTPError as e:
    if e.code == 409:
        print(
            "Connector is likely already running!"
        )
    else:
        raise e

