import paramiko

# Set up SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("localhost", username="")

# Execute a command on the server
stdin, stdout, stderr = ssh_client.exec_command("ls")

# Receive output from the command
output = stdout.read().decode()
print(output)

# Close the SSH client
ssh_client.close()
