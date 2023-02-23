import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Get the referral source from the request headers
    referrer = request.headers.get('Referer')

    # Get the user's IP address
    ip_address = request.remote_addr

    # Get the user agent from the request headers
    user_agent = request.headers.get('User-Agent')

    # Get the user's geographic location
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    location_data = response.json()

    # Check that the necessary keys are present in the response
    if all(key in location_data for key in ['city', 'region', 'country_name']):
        location = f"{location_data['city']}, {location_data['region']}, {location_data['country_name']}"
    else:
        location = "Unknown"

    # Log the tracking information to a file or database
    with open('tracking.log', 'a') as f:
        f.write(f'Referrer: {referrer}\n')
        f.write(f'IP Address: {ip_address}\n')
        f.write(f'Location: {location}\n')
        f.write(f'User Agent: {user_agent}\n')
        f.write('\n')

    # Return the page content
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()

