import string
import requests
import random
CLIENT_ID    = '77xd01g5dju64h'
CLIENT_SECRET = 'MuonTK4T9Q7Wd1kY'
REDIRECT_URI = 'http://localhost:8000'

# Generate a random string to protect against cross-site request forgery
letters = string.ascii_lowercase
CSRF_TOKEN = ''.join(random.choice(letters) for i in range(24))


# Request authentication URL
auth_params = {'response_type': 'code',
               'client_id': CLIENT_ID,
               'redirect_uri': REDIRECT_URI,
               'state': CSRF_TOKEN,
               'scope': 'w_member_social'}

html = requests.get("https://www.linkedin.com/oauth/v2/authorization",
                    params = auth_params)

# Print the link to the approval page
print(html.url)
