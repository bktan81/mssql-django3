
# Prepare the mssql directory
sudo rm -r mssql && mkdir mssql && sudo chmod 777 mssql

# Run docker compose
/usr/local/bin/docker-compose run --service-ports --rm mssql-server