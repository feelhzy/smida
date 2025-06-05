# Contributing to smida

Thank you for considering contributing to **smida**! We welcome issues and pull
requests that improve the project.

## How to Contribute

1. Fork this repository and create your feature branch from `main`.
2. Make your changes with clear and concise commits.
3. If the project contains tests, run them locally before submitting your PR.
4. Open a pull request describing your changes.
5. Participate in the review process and address any feedback.

Please ensure that all contributions comply with the [MIT license](LICENSE).

## Development Setup

The project can be developed locally using Docker. Ensure you have Docker
installed and running on your machine.

```bash
# Clone the repository
git clone https://github.com/your-username/smida.git
cd smida

# Build the Docker image
docker build -t smida .

# Start the application (adjust the port as needed)
docker run --rm -it -p 8000:8000 smida
```

### Running Tests

If test suites are available, they can be executed inside the container:

```bash
# Example: running tests
docker run --rm smida npm test
```

### Deployment

A CI/CD pipeline can be used to deploy the site automatically. A typical
workflow with GitHub Actions might include the following steps:

1. Build the Docker image on every push.
2. Run any tests to verify the build.
3. Push the image to a registry and deploy it to your hosting provider.

Feel free to adapt the pipeline to fit your hosting environment.
