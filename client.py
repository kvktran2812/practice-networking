import socket

def tcp_client(host='127.0.0.1', port=65432):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to server
            s.connect((host, port))
            print(f"Connected to {host}:{port}")
            
            while True:
                # Get user input
                message = input("Enter message (or 'quit' to exit): ")
                if message.lower() == 'quit':
                    break
                
                # Send data
                s.sendall(message.encode('utf-8'))
                
                # Receive response
                data = s.recv(1024)
                print(f"Received: {data.decode('utf-8')}")
                
        except ConnectionRefusedError:
            print(f"Could not connect to {host}:{port}")
        except KeyboardInterrupt:
            print("\nClient shutting down...")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Change these to match your server
    tcp_client('127.0.0.1', 65432)