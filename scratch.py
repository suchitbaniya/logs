import re
import json

log_line = "Nov 28 06:26:46 server-01 dhcpd: DHCPDISCOVER from cc:d3:e2:9d:f9:19 via 10.50.0.1"

regex_pattern = r"(\w{3} \d{2} \d{2}:\d{2}:\d{2}) (\S+) (\w+): (.*)"

match = re.match(regex_pattern, log_line)

if match:
    timestamp = match.group(1)
    server = match.group(2)
    services = match.group(3)
    message = match.group(4)

    log_data = {
        "timestamp": timestamp,
        "server": server,
        "services": services,
        "message": message
    }

    json_output = json.dumps(log_data)
    print(json_output)
else:
    print("No match found.")