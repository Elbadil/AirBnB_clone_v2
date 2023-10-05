#!/usr/bin/env bash
# Bash script that sets up my web servers fo the deployment of web_static

# Update and install nginx if it's not already installed
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# Create data web static folders if not already created
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create Html File inside the test folder
echo "<html>
  <head>
  </head>
  <body>
    Hello to Web Static
  </body>
</html>" >> /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu's user and group
sudo chown -R ubuntu:ubuntu /data/

# Add to the nginx config hbnb_static so it can serve /data/web_static/current/
sudo sed -i "30i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart to apply changes
sudo service nginx restart