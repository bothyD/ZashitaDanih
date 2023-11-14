from other.prime import get_prime, is_prime
from other.gen_evlkid import generateC_D
import socket
import pickle
import random
import math


def RSA():
    q = get_prime(1 << 1023, (1 << 1024) - 1)
    while True:  # Генерируем p
        p = get_prime(1 << 1023, (1 << 1024) - 1)
        if p !=q:
            break
    N = p * q
    fu = (p-1)*(q-1)
    d, c = generateC_D(fu)
    return c, d, N

def main():
    C, D, N = RSA()
    # # Создаем сокет
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # # Привязываем сокет к хосту и порту
    # host = '127.0.0.1'
    # port = 12345
    # server_socket.bind((host, port))
    # # Прослушиваем входящие соединения
    # server_socket.listen()
    # print(f"Сервер слушает на {host}:{port}")
    # while True:
    #     # Принимаем соединение
    #     client_socket, client_address = server_socket.accept()
    #     print(f"Установлено соединение с {client_address}")
    #     # Отправляем ответ клиенту
    #     response = "Привет, прими участие в анонимном голосовании!\n Выбери соответствующий номер:\n1 - Да, 2 - Нет, 3 - Воздержался"
    #     client_socket.send(response.encode('utf-8'))

    #     # Принимаем данные от клиента
    #     data = client_socket.recv(1024)
    #     print(f"Получены данные от клиента, ожитайте...")
    #     data = pickle.loads(data)


    #     # Закрываем соединение с клиентом
    #     client_socket.close()

if __name__ =="__main__":
    main()    
