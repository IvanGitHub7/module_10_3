import random
from threading import Thread, Lock
import time


class Bank():
    
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        
    def deposit(self):
        for i in range(100):
            dep = random.randint(50, 500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
            
    def take(self):
        for i in range(100):
            with_ = random.randint(50, 500)
            print(f'Запрос на {with_}')
            if with_ <= self.balance:
                self.balance -= with_
                print(f'Снятие: {with_}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
        

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
          
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')