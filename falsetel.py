import socket
import threading
import logging

address = "0.0.0.0"
port = 23

logging.basicConfig(
        filename="FalseTel.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
)

def client(client_socket, client_address):

    try:
        logging.info(f"Recived connection from {client_address}")

        client_socket.sendall(b"Backups Server Admin Console\n")
        client_socket.sendall(b"Login: ")
        
        username = client_socket.recv(1024).strip().decode("utf-8")
        logging.info(f"Recived username: {username} from address: {client_address}")

        client_socket.sendall(b"Password: ")
        password = client_socket.recv(1024).strip().decode("utf-8")
        logging.info(f"Recived password: {password} from address: {client_address}")

        if username == "admin" and password == "admin":
            client_socket.sendall(b"admin$> ")

            while 1:
                command = client_socket.recv(1024).strip().decode("utf-8")
                if not command:
                    break
                logging.info(f"Recived command {command} from address {client_address}")
                client_socket.sendall(b"admin$> ")
        else:
            client_socket.sendall(b"Invalid username or password\n")
    
    except Exception as error:
        logging.info(f"Recived error: {error} from address {client_address}")

    finally:
        client_socket.close()

def run_service():
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind((address, port))
    service.listen(3)
    print("[+] Service is up")
    
    try:
        while 1:
            client_socket, client_address = service.accept()
            client_handler = threading.Thread(target=client, args=(client_socket, client_address))
            client_handler.start()
    except KeyboardInterrupt:
        logging.info("Recived KeyboardInterrupt by user")
        print("[!] Service Stoped")
    finally:
        service.close()

if __name__ == "__main__":
    print("[*] Trying to run Service...") 
    run_service()
