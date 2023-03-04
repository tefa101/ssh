import paramiko

# Set up SSH server
ssh_server = paramiko.Transport(("0.0.0.0", 22))
ssh_server.add_server_key(paramiko.RSAKey.generate(2048))
ssh_server.start_server()

# Accept incoming connection
ssh_channel = ssh_server.accept(20)
if ssh_channel is None:
    print("No incoming connection.")
else:
    print("Incoming connection accepted.")

    # Authenticate the client
    ssh_channel.auth_none(username="")
    if not ssh_channel.is_authenticated():
        print("Authentication failed.")
        ssh_channel.close()
    else:
        print("Authentication successful.")

        # Execute a command on the server
        ssh_channel.exec_command("ls")

        # Receive output from the command
        output = ssh_channel.recv(1024)
        print(output)

        # Close the channel
        ssh_channel.close()

# Close the SSH server
ssh_server.close()
