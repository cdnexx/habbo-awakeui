import pyautogui as pg
import time
from datetime import datetime

def move(position: tuple):
    pg.moveTo(position[0], position[1], 2)
    pg.click()

def get_time() -> str:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def time_sleep(t: int):
    for s in range(t):
        print(f"Nuevo ciclo en: {t-s} segundos...    ", end="\r")
        time.sleep(1)

def redifine_positions():
    print("-------- Definir posiciones --------")

    print("--------- Definir Asiento ----------")
    time_sleep(3)
    seat = (pg.position().x, pg.position().y)
    print(f"Posición definida en {seat}")

    print("------------ Posición 1 ------------")
    time_sleep(3)
    pos1 = (pg.position().x, pg.position().y)
    print(f"Posición definida en {pos1}")

    print("------------ Posición 2 ------------")
    time_sleep(3)
    pos2 = (pg.position().x, pg.position().y)
    print(f"Posición definida en {pos2}")

    print("------------ Posición 3 ------------")
    time_sleep(3)
    pos3 = (pg.position().x, pg.position().y)
    print(f"Posición definida en {pos3}")

seat = (1077, 1153)
pos1 = (896, 1155)
pos2 = (992, 1210)
pos3 = (1119, 1207)

inp = input("Redefinir posiciones? (y/n): ")
if inp.lower() == "y":
    redifine_positions()
else:
    print("Usando posiciones guardadas.")

cycle = 1
print("Iniciando en 5 segundos...")
time.sleep(5)
while True:
    print("------------ Posición 3 ------------")
    print(f"------------- Ciclo {cycle} -------------")
    print(f"Ciclo ejecutado a las {get_time()}")
    move(pos1)
    move(pos2)
    move(pos3)
    move(seat)
    time_sleep(15)
    cycle += 1
