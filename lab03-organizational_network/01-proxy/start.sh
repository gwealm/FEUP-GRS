docker compose up -d --build

docker exec proxy ip r d default via 10.0.1.1
docker exec proxy ip r a default via 10.0.1.254

docker exec -it client /bin/bash