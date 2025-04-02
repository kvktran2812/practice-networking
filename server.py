import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # Echo back
    finally:
        conn.close()

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)  # Echo back
        except KeyboardInterrupt:
            print("\nServer shutting down gracefully...")
        finally:
            print("Server closed")

if __name__ == "__main__":
    start_server()