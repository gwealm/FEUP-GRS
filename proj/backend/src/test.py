from engine.docker.compose.handler import DockerComposeManifestHandler
from engine.docker.compose import DockerCompose
from engine.models.network import IPAddress

handler = DockerComposeManifestHandler()
compose = DockerCompose()

manifest_template = handler.load("../templates/docker-compose.yml")

manifest = manifest_template.compile({
    "orgname": "test_org",
    "subnet": "172.20.0.0/16",
    "router_ip": "172.20.0.3",
    "proxy_ip": "172.20.0.4",
    "client_1_ip": "172.20.0.2",
})

if compose.is_available():
    print("docker compose is available")
    
    print(compose.provision(manifest))
    print("docker compose project provisioned")
    # compose.tear_down(manifest)
    # print("docker compose project torn down")
