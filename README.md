# Sample of API created in FastAPI as exercise to create full CI/CD flow

- The code is simple. It creates a quick API using Faker library and FastAPI with Python to simulate a real API

## Configuration

- No special configuration is needed other than execute the PY file
- Except when it is mounted as a docker container. Which files are provided
- This specific project uses Poll SCM each 5 minutes: H/5 * * * *

## Execute

1. Enable VENV
2. Go to root of the project
3. Directly execute "python api.py" command

## Jenkins and CI/CD implications
- Since we are using Docker, both APP and TESTING parts must belong to the same network. This was ensured using:
```
echo "Ensuring external Docker network '${PROJECT_NAME}' exists..."
docker network inspect "$PROJECT_NAME" >/dev/null 2>&1 || \
    docker network create --driver bridge "$PROJECT_NAME"
```
- Jenkins credentials were used to address environment variables:
```
skeleton_api_host
skeleton_api_port
```
- Due to project being inside a VPN, the HOST will be the IP address of the VPN