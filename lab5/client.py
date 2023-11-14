from other.gost import makeCertif
import socket
import pickle

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))



# Получаем ответ от сервера
response = client_socket.recv(1024)
massege = response.decode('utf-8')
print(f"Получен ответ от сервера: {massege}")

# Отправляем данные серверу
while True:
    massage = input()
    try:
        massege = int(massage)
        if massege == 1 or massege == 2 or massege == 3:
            break
        print("error input!")
    except:
        print("error input!")
publicData = makeCertif(massage)
serialized_data = pickle.dumps(publicData)
client_socket.send(serialized_data)


# Закрываем соединение с сервером
client_socket.close()