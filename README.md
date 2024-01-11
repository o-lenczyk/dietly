## scrap.py
- scrap menu from dietly.pl
- push it to DB

## UI
### Build:
- `docker build -t dietly:0.3 . `
### Run:
- `docker run --detach --publish 8080:8080  --volume $(pwd)/keys/client-key.pem:/keys/client-key.pem --name dietly-ui dietly:0.4`