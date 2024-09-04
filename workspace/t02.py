import paramiko

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the container
ssh.connect(hostname='localhost', port=2222, username='root', password='topsecret')

# Execute a command
stdin, stdout, stderr = ssh.exec_command('ls -l /')
print(stdout.read().decode())

# Close the connection
ssh.close()
