import json
import requests


def send_apn_notification(device_token, payload, apn_key_path, team_id, key_id, topic,authToken):
    url = 'https://api.sandbox.push.apple.com/device/' + device_token

    headers = {
        'content-type': 'application/json',
        'authorization': 'bearer ' + authToken,
        'apns-topic': topic,
        'apns-push-type': 'alert'
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    if r.status_code != 200:
        print(f'Error sending notification to {device_token}: {r.text}')
    else:
        print(f'Notification sent to {device_token}')


deviceToken = 'cd4e0575907e4e219b89800d1e86d9b1fe9ab126f5ab20c1d41ad1fdb71cbf9c'
payload  = {
    "aps": { 
        "alert": {
            "title": "Hello",
            "body": "World"
        },
        "sound": "default"
    }
}

apn_key_path = '/AuthKey_55P3T3ABQ8.p8'
authToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjU1UDNUM0FCUTgifQ.eyJpc3MiOiIySEU3NTI4SzI1IiwiaWF0IjoxNjgwNDM1ODExfQ.XTUSeL8xi2liSX9GUloydIOt_kTLEPlHgVW9or8XMxDrVOJp9wF00pMW-MqL1wn4WDRBg6j76U5TRUrE_6NnFg'
send_apn_notification(deviceToken,payload, apn_key_path, '2HE7528K25', '55P3T3ABQ8', 'com.munozcreates.ambulane', authToken)
