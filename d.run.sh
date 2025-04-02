# Automatically stop and delete old container to create and run the new one
docker rm -f skeleton_api_app 2>/dev/null || true && \
docker run -d --name skeleton_api_app --restart unless-stopped --network skeleton_api --env-file .env -p 10200:10200 skeleton_api_app
