import jwt
import time

def create_apn_token(p8_key_path, team_id, key_id):
    with open(p8_key_path, 'r') as f:
        private_key = f.read()

    headers = {
        'alg': 'ES256',
        'kid': key_id
    }

    time_now = int(time.time())
    payload = {
        'iss': team_id,
        'iat': time_now
    }

    return jwt.encode(payload, private_key, algorithm='ES256', headers=headers)


p8_key_path = 'AuthKey_55P3T3ABQ8.p8'
team_id = '2HE7528K25'
key_id = '55P3T3ABQ8'

token = create_apn_token(p8_key_path, team_id, key_id)
print(token)
