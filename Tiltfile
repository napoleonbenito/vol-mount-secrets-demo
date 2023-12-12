# Set up Docker image build and Kubernetes deployment
k8s_yaml('k8s.yaml')
docker_build('python-secret-app', '.')
k8s_resource('python-secret-app', port_forwards='8080:8080')