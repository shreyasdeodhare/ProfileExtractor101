# Open the file containing proxies
with open('proxies.txt', 'r') as file:
    lines = file.readlines()

# Filter out only HTTP proxies and convert to single quotes
http_proxies = [f"'{line.strip()}'," for line in lines if line.startswith('http')]
if http_proxies:
    http_proxies[-1] = http_proxies[-1][:-1]

# Write HTTP proxies to the same file
with open('proxies.txt', 'w') as file:
    for proxy in http_proxies:
        file.write(proxy + '\n')
