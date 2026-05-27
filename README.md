# Learning App: Docker + Travis + Heroku

A hands-on learning project to practice containerization, CI/CD pipelines, and cloud deployment.

## Tech Stack

- **Docker** - Application containerization
- **Travis CI** - Continuous integration and testing
- **Heroku** - Cloud platform deployment

## Getting Started

heroku

### Prerequisites

- Docker
- Git
- Travis CI account
- Heroku account

### Local Development

```bash
# Build the Docker image
docker build -t cicd_docker_webapp .

# Run the container
docker run -p 8002:8002 cicd_docker_webapp
```

## CI/CD Pipeline

This project uses Travis CI to automatically test and deploy to Heroku on each push.

See `.travis.yml` for configuration details.

## Deployment

The app automatically deploys to Heroku when changes are pushed to the main branch.

## Learning Goals

- [ ] Dockerfile creation and optimization
- [ ] Travis CI configuration
- [ ] Heroku deployment automation
- [ ] Container orchestration basics
