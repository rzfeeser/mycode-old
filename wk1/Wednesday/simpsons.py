challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[-1]}")



trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

print(f"My {trial[2].get('goggles')}! The {trial[2].get('eyes')} do {trial[-1]}")



nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]



print(f"My {nightmare[0].get('user').get('name').get('first')}! The {nightmare[0].get('kumquat')} do {nightmare[0].get('d')}")
