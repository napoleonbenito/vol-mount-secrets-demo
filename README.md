# Documentation: Python Kubernetes Application with Volume-Mounted Secrets and AWS Secrets Manager Integration

## Overview

This project demonstrates the use of volume-mounted secrets in Kubernetes with a Python application and explores an extension for integrating AWS Secrets Manager. This approach enhances the application's capability to manage sensitive data securely and flexibly, catering to different operational needs.

## Project Structure

- `app.py`: Python application that reads secrets from a Kubernetes volume mount.
- `Dockerfile`: Instructions for building the Docker image for the application.
- `k8s.yaml`: Kubernetes deployment manifest including secret volume mount configuration.
- `Tiltfile`: Configuration for Tilt to automate deployment and updates.
- `requirements.txt`: Required Python packages for the application.

## Key Concepts

### 1. Kubernetes Volume-Mounted Secrets

- **Secure Management**: Kubernetes secrets provide a secure way to handle sensitive data like passwords and API keys.
- **Simplicity and Consistency**: Mounting secrets as volumes simplifies the application's access to sensitive data and ensures consistency across different environments.

### 2. Extending with AWS Secrets Manager

- **Robust Security**: AWS Secrets Manager offers advanced features like secret rotation, fine-grained access control, and auditing capabilities.
- **Scalability**: Ideal for applications with complex secret management needs or those requiring dynamic secret updates.
- **Flexibility**: Allows applications to access secrets stored in AWS, useful in hybrid or multi-cloud environments.

## Setting Up the Environment

### Local Development Setup

1. **Create and Activate Virtual Environment**:
   - `python -m venv venv`
   - Activate the environment:
     - macOS/Linux: `source venv/bin/activate`
     - Windows: `venv\Scripts\activate`
   
2. **Install Dependencies**:
   - `pip install -r requirements.txt`

### Using Tilt for Development

- Run `tilt up` in your project directory to build and deploy the application.

## Accessing the Application

- The application will be accessible at `http://localhost:8080`, displaying the secret read from the mounted volume.

## Extending the Project with AWS Secrets Manager

To further enhance the project, consider integrating AWS Secrets Manager. This extension is ideal for scenarios requiring more complex secret management strategies.

### Steps for Integration

1. **Update Dependencies**:
   - Include `boto3` (AWS SDK for Python) in `requirements.txt`.

2. **Modify the Application**:
   - Update `app.py` to add logic for fetching secrets from AWS Secrets Manager.

3. **AWS Configuration**:
   - Ensure AWS credentials are set up for local development and in the Kubernetes environment.
   - Consider using IAM roles for service accounts in Kubernetes for secure access.

4. **Update Tiltfile**:
   - No changes needed in the Tiltfile. Tilt will continue to manage the build and deployment process.

## Conclusion

This project provides a foundational approach to managing secrets in a Kubernetes environment and proposes a potential extension with AWS Secrets Manager. The integration with AWS enhances the application's capabilities for handling secrets, making it suitable for diverse operational requirements and larger, more complex environments.