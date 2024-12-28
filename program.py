print("Hello World")

def game():
    user = input("가위바위보 중 하나를 입력하세요")
    computer = random.randint(0, 2)
    print(user, computer)

game()

