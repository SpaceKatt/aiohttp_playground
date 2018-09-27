# Playground for aiohttp Testing

```bash
curl -I 127.0.0.1:8080/

curl 127.0.0.1:8080/

curl 127.0.0.1:8080/play; echo

curl --header "Content-Type: application/json" \
     --request PUT \
     --data '{"state":"Hello, World"}' \
     127.0.0.1:8080/name/bob

curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"state":"Hello, World"}' \
     127.0.0.1:8080/name/bob
```
