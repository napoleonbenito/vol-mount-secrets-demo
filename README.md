# Using Volume-Mounted Secrets in a Python Kubernetes Application

## Overview

This project demonstrates the use of volume-mounted secrets in a Kubernetes environment, utilizing a simple Python application. By leveraging Kubernetes secrets, we ensure secure management of sensitive data, making it accessible to the application in a safe and controlled manner.

## Project Structure

- `app.py`: Python application that reads a secret from a mounted volume and serves it over HTTP.
- `Dockerfile`: Defines the Docker image for the Python application.
- `k8s.yaml`: Kubernetes manifest for deploying the application, including secret mounting.
- `Tiltfile`: Configures Tilt for streamlined development and deployment workflow.
- `requirements.txt`: Lists Python dependencies for the application.

## Key Concepts

### 1. Security and Confidentiality

Kubernetes secrets are used to store sensitive data like API keys and passwords, ensuring that such information is not exposed in source code or Docker images.

### 2. Environment Abstraction

Mounting secrets as volumes allows the application to abstract the source of sensitive data. This enables the same codebase to run seamlessly across various environments (development, staging, production) without any code changes.

### 3. Centralized Management

Kubernetes provides a centralized approach to managing secrets. This setup allows updates and rotations of secrets without necessitating changes in the application or its deployment configuration.

### 4. Reduced Risk of Exposure

Volume-mounted secrets are not exposed to the container's environment variables, lowering the risk of accidental exposure through logs or debugging processes.

### 5. Ease of Use

The application reads secrets as if they were regular files, which simplifies implementation and negates the need for specialized secret management libraries.

## Setting Up the Environment

### Local Development Setup

1. **Create a Virtual Environment**:
   - Navigate to the project directory.
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```cmd
       venv\Scripts\activate
       ```

2. **Install Dependencies**:
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

### Using Tilt for Development

- Run `tilt up` in the terminal within the project directory.
- Tilt will build the Docker image and deploy the application, watching for code changes.

## Accessing the Application

- The application is accessible at `http://localhost:8080` where it displays the secret read from the mounted volume.

## Conclusion

This project showcases the use of volume-mounted secrets in Kubernetes for a Python application, emphasizing the importance of security best practices. It provides a flexible and developer-friendly approach to managing confidential data while demonstrating the benefits of a containerized development workflow with Tilt.