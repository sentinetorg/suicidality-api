# Suicidality-API

## START API SERVER LOCALLY

```shell

# Install all python dependencies.
yes | pip install fastapi==0.100.0
yes | pip install uvicorn==0.23.1
yes | pip install torch==2.0.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
yes | pip install transformers

python3 main.py

```

Access URL: `http://localhost:7777/?q=<text>token=<token>`

In the above link, the `<text>` should be replaced by the text you would like to predict for.
The `<token>` should be replaced from one of the active token from `storage/tokens.json` file.


## Setup to Server
To upload the application to server make sure to install `nginx` and configure to keep application running.

```shell
#sudo apt-get update
sudo apt-get install python3 python3-pip nginx -y

# Copy the Nginx configuration as default site
sudo cp installer/nginx.conf /etc/nginx/sites-available/default

# Restart Nginx
sudo systemctl restart nginx
```

### Process Manager

Here we'll be using pm2, but it is not mandatory. Any alternatives like `forever`, `supervisor`, etc. can be used.

To use pm2 you need to have `node.js` installed.

```shell
# Install PM2 process manager
npm install -g pm2

# Delete any previously running instance.
pm2 delete suicidality > /dev/null

# Start pm2 configured applications.
pm2 start ecosystem.json
```