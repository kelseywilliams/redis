import redis
pwd="LFBzws/2gd++y8H6VGSzfHXt+nM1USm9NvpnQbOckzk="
with open("./log", "a") as f:
    f.write("I am here!\n")
try:
    r = redis.Redis(host="redis", port="6379", username="worker", password=pwd, db="0")
    r.ping()
    with open("./log", "a") as f:
        f.write("Success!\n")
        f.write(f"{r}\n")
        r.set("foo", "Holy SHIT WE FUCKING DID IT ")
        f.write(f"{r.get('foo')}\n")
        f.write(f"{r.close()}")
except Exception as e:
    with open("./log", "a") as f:
        f.write(f"{e}\n")