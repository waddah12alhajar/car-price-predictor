#!/usr/bin/env python3
"""
Submit form and get ML prediction result
"""
import requests

# Submit form to get prediction
data = {
    'state-name': 'ca',
    'city-name': 'los angeles',
    'make-name': 'toyota',
    'model-name': 'camry',
    'purchase-year': '2018',
    'mileage': '35000'
}

session = requests.Session()

# Get the main page first (to get any session/cookies)
resp = session.get('http://127.0.0.1:5000/')
print(f"Home page status: {resp.status_code}")

# Submit the form
resp = session.post('http://127.0.0.1:5000/getprice', data=data, allow_redirects=True)
print(f"Prediction response status: {resp.status_code}")
print(f"Final URL: {resp.url}")

# Save the result page
with open('/tmp/prediction_result.html', 'w') as f:
    f.write(resp.text)

print("Saved result to /tmp/prediction_result.html")

# Check if we can find the predicted price in the response
if 'predicted' in resp.text.lower() or 'price' in resp.text.lower():
    # Extract price from HTML
    import re
    match = re.search(r'\$[\d,]+', resp.text)
    if match:
        print(f"\nPredicted Price Found: {match.group()}")
