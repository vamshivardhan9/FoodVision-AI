import json
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True,

)

with open("nutrition.json", "r") as f:
    data = json.load(f)

r.set("nutrition", json.dumps(data))

print("Entire JSON stored successfully")