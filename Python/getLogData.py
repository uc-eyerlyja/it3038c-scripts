import os

filename = "/var/log/secure"

with open(filename) as f:
    lines = set(f.read().splitlines())
    for line in lines:
        if "eyerlyja" in line:
            print(line)