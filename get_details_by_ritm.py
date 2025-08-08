import requests
from requests.auth import HTTPBasicAuth

# === Configuration ===
instance = 'dev206501'  # Your instance name
username = 'admin'
password = 'ocz@Q=PN8Ih1'
ritm_number = 'RITM0010003'  # Replace with your RITM number

# === API URL ===
url = f"https://{instance}.service-now.com/api/now/table/sc_req_item"

# === Fields you want to retrieve ===
fields = [
    'number',
    'short_description',
    'requested_for',
    'state',
    'stage',
    'sys_created_on',
    'cat_item',
    'u_custom_checkbox'  # Optional custom field
]

params = {
    'sysparm_query': f'number={ritm_number}',
    # 'sysparm_fields': ','.join(fields),
    # 'sysparm_limit': 1
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
    print(data)
    results = data.get('result', [])
    if results:
        record = results[0]
        print("RITM Details:")
        for key, value in record.items():
            print(f"{key}: {value}")
    else:
        print("No matching RITM found.")
else:
    print(f"Failed to retrieve record. Status code: {response.status_code}")
    print(response.text)
