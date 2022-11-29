from main import *

os.system("cls")
player = make_hero(name="Вася Питонов", hp_now=100, inventory=[" изношенный меч", "поношенный шит", "изношенная кольчуга"])
start_fight(player)
input("Продолжить - ENTER")
os.system("cls")
show_hero(player)
