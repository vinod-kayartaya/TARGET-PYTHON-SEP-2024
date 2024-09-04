# Use Alpine Linux as the base image
FROM alpine:latest

# Install OpenSSH
RUN apk add --no-cache openssh

# Set root password
RUN echo 'root:topsecret' | chpasswd

# Generate SSH host keys
RUN ssh-keygen -A

# Create the .ssh directory and set the correct permissions
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh

# Ensure SSH is available by exposing the port
EXPOSE 22

# Start SSHD when the container launches
CMD ["/usr/sbin/sshd", "-D"]
