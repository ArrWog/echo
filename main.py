import socket
import threading


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Получено: {data.decode('utf-8')}")
            response = data.upper()
            client_socket.send(response)
    except Exception as e:
        print(f"Ошибка при обработке клиента: {e}")
    finally:
        client_socket.close()


def echo_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 7777))
        server_socket.listen(5)
        print("Сервер слушает на порту 7777...")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Принято соединение от {addr}")

            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except Exception as e:
        print(f"Ошибка при запуске сервера: {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    echo_server()
