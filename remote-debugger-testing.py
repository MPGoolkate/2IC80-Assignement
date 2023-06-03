import json
import requests

# Set up the remote debugging URL
url = 'http://localhost:9222/json'

# Get the list of available tabs
response = requests.get(url)
tabs = json.loads(response.content)

# Find the tab with the Google.com URL
google_tab = None
for tab in tabs:
    if tab['url'] == 'https://www.google.com/':
        google_tab = tab
        break

# Send the alert command to the tab
if google_tab:
    print(google_tab)
    alert_url = f"http://localhost:9222/devtools/page/{google_tab['id']}/" \
                f"Runtime.evaluate"
    alert_payload = {
        "expression": "console.log('Hello, world!')",
        "userGesture": True,
        "returnByValue": True
    }
    r = requests.post(alert_url, json=alert_payload)
    print(r)
else:
    print("Google.com tab not found")