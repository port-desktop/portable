import tomllib;
import csv;

import os

walk_dirs = ['portable']

def walk(dir_name, writer):
    for root, _, files in os.walk(dir_name):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'rb') as data:
                info = tomllib.load(data)
                writer.writerow([info["manifest"]["type"], info['manifest']['platform'], info['manifest']['uid'], info['manifest']['name'], info['manifest']['arch']])


if __name__ == "__main__":

    with open('public/index.csv', 'w+') as index:
        writer = csv.writer(index, quoting=csv.QUOTE_MINIMAL)
        for dir in walk_dirs:
            csv.writer.writerow(['type', 'platform', 'uid', 'name', 'architecture'])
            walk(dir, writer)