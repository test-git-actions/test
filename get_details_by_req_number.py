import requests
from requests.auth import HTTPBasicAuth

# === Configuration ===
instance = 'dev206501'
username = 'admin'
password = 'ocz@Q=PN8Ih1'
base_url = f"https://{instance}.service-now.com"

auth = HTTPBasicAuth(username, password)
headers = {"Accept": "application/json"}


def get_request_sys_id(request_number):
    """Fetch the sys_id of a given Request (REQ) number."""
    url = f"{base_url}/api/now/table/sc_request"
    params = {
        'sysparm_query': f'number={request_number}',
        'sysparm_fields': 'sys_id',
        'sysparm_limit': 1
    }

    response = requests.get(url, auth=auth, headers=headers, params=params)

    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch REQ. Status: {response.status_code}")
        print(response.text)
        return None

    results = response.json().get('result', [])
    return results[0]['sys_id'] if results else None


def get_ritms_by_request_sys_id(req_sys_id):
    """Fetch all RITMs (Requested Items) related to a given Request sys_id."""
    url = f"{base_url}/api/now/table/sc_req_item"
    params = {
        'sysparm_query': f'request={req_sys_id}',
        'sysparm_fields': 'number,short_description,state,stage,requested_for,cat_item',
        'sysparm_limit': 100
    }

    response = requests.get(url, auth=auth, headers=headers, params=params)

    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch RITMs. Status: {response.status_code}")
        print(response.text)
        return []

    return response.json().get('result', [])


def display_ritms(ritms, request_number):
    """Prints out all RITMs neatly."""
    if not ritms:
        print(f"No RITMs found under request: {request_number}")
        return

    print(f"\nRITMs under {request_number}:")
    for ritm in ritms:
        print("-------------------------")
        for key, value in ritm.items():
            print(f"{key}: {value}")


def main():
    request_number = 'REQ0010004'  # You can parameterize this
    req_sys_id = get_request_sys_id(request_number)
    if not req_sys_id:
        print(f"No REQ found with number: {request_number}")
        return

    ritms = get_ritms_by_request_sys_id(req_sys_id)
    display_ritms(ritms, request_number)


if __name__ == "__main__":
    main()
