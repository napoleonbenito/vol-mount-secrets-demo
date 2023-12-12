# Set up Docker image build and Kubernetes deployment
k8s_yaml('k8s.yaml')
docker_build('go-secret-app', '.')
k8s_resource('go-secret-app', port_forwards='8080:8080')