const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/run-curl', (req, res) => {
  exec(`curl -v --header "apns-topic: $TOPIC" --header "apns-push-type: alert" --header "authorization: bearer $AUTHENTICATION_TOKEN" --data '{"aps":{"alert":{"title":"Merge Left","body":"Emergency vehicle behind you"}}}' --http2 https://${APNS_HOST_NAME}/3/device/${DEVICE_TOKEN}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error running curl command: ${error}`);
      res.status(500).send('Internal server error');
      return;
    }

    console.log(`Curl command output: ${stdout}`);
    res.send(`Curl command output: ${stdout}`);
  });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
