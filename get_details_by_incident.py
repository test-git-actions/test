import requests
from requests.auth import HTTPBasicAuth

# === Configuration ===
instance = 'dev206501'
username = 'admin'
password = 'ocz@Q=PN8Ih1'
incident_number = 'INC0010001'  # Replace with your actual incident number

# === API URL ===
url = f"https://{instance}.service-now.com/api/now/table/incident"

# === Fields you want to retrieve ===
fields = [
    'number',
    'requested_for',
    'state',
    'sys_created_on',
    'sys_created_by',
    'active',
    'approval',
    'severity',
    'category',
    'short_description',
    'u_custom_checkbox'
]

params = {
    'sysparm_query': f'number={incident_number}',
    'sysparm_fields': ','.join(fields),
    'sysparm_limit': 1
}

# === Make the API Call ===
response = requests.get(
    url,
    auth=HTTPBasicAuth(username, password),
    headers={"Accept": "application/json"},
    params=params
)

# === Handle Response ===
if response.status_code == 200:
    data = response.json()
    results = data.get('result', [])
    if results:
        record = results[0]
        print("Incident Details:")
        for key, value in record.items():
            print(f"{key}: {value}")
    else:
        print("No matching incident found.")
else:
    print(f"Failed to retrieve record. Status code: {response.status_code}")
    print(response.text)
