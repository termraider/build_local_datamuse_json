import requests
import json
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def fetch(word):
    response = requests.get(f'https://api.datamuse.com/words?sp={word}')
    data = response.json()
    return (word, data[0] if data else [])

# Load words list from the file
with open('cmu/cmudict-stripped.yaml', 'r', encoding='ISO-8859-1') as f:
    words = [word.strip() for word in f.readlines()]

# Initialize empty dictionary to hold the data
data_dict = {}

# Start the Executor
with ThreadPoolExecutor() as executor:
    # Iterate over words and make requests
    for word, data in tqdm(executor.map(fetch, words), total=len(words), desc="processing words"):
        data_dict[word] = data

# Write the dictionary to a JSON file
with open('datamuse.json', 'w', encoding='ISO-8859-1') as json_file:
    json.dump(data_dict, json_file, indent=4)
