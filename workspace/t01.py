import paramiko

# Define the server connection details
hostname = 'ec2-13-239-2-162.ap-southeast-2.compute.amazonaws.com'
port = 22  # Default SSH port is 22
username = 'ec2-user'
pem_file_path = '/Users/vinod/Desktop/trainings/aws-ec2-instance.pem'

commands = """
cd vin-contact-service
ls -l
cd ..
cd vinbasket
ls -l
nohup npm start &
"""

# Create an SSH client object
with paramiko.SSHClient() as ssh:

    # Load host keys and automatically add untrusted hosts (like "ssh-keyscan")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server using the .pem file
    ssh.connect(hostname, port=port, username=username, key_filename=pem_file_path)

    # Execute a command (e.g., 'ls -l' to list directory contents)
    stdin, stdout, stderr = ssh.exec_command(commands)

    # Read and print the output of the command
    output = stdout.read().decode('utf-8')
    print("Command output:")
    print(output)

    # Check for any errors
    error = stderr.read().decode('utf-8')
    if error:
        print("Error:")
        print(error)
