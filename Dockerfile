FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /app

# Install any needed system packages (optional)
# RUN apk add --no-cache some-system-dependencies

# Copy your project files
COPY . .

# Expose the port your app listens on
EXPOSE 5000

# Set the entry point to run your mock server
CMD ["uv", "run", "server_with_sockets.py"]
