import requests
from requests.auth import HTTPBasicAuth

# === Configuration ===
instance = 'dev206501'
username = 'admin'
password = 'ocz@Q=PN8Ih1'
sys_id = 'a80c6b9ec34362107656b61ed40131ca'

# === Table to query (Request Item / RITM) ===
table = 'sc_req_item'  # Can change to 'incident', 'sc_request', etc.

# === API URL ===
url = f"https://{instance}.service-now.com/api/now/table/{table}/{sys_id}"

# === Make the API Call ===
response = requests.get(
    url,
    auth=HTTPBasicAuth(username, password),
    headers={"Accept": "application/json"}
)

# === Handle Response ===
if response.status_code == 200:
    data = response.json()
    record = data.get('result', {})
    print(f"Details for sys_id {sys_id}:")
    for key, value in record.items():
        print(f"{key}: {value}")
else:
    print(f"Failed to retrieve record. Status code: {response.status_code}")
    print(response.text)
