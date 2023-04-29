import json
from urllib.request import urlopen
from urllib.parse import quote

def search(q: str) -> list:
	with urlopen(f"https://tlepeopledir.mit.edu/q/{quote(q)}?_format=json") as res:
		return json.load(res).get("result", [])
