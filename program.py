import random

print("Hello World")

def game():
    print("바위가위보 게임을 시작합니다.")
    print("가위바위보 중 하나를 입력하세요")
    user = input()
    computer = random.randint(0, 2)
    print(user, computer)

if __name__ == "__main__":
    game()









