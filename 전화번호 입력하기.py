import time
import random
import threading
import tkinter as tk

cell_phon = 0

# 색깔 정의
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'
RESET = '\033[0m'


def logout():
    input("종료하려면 엔터를 누르세요...")
    print("종료")
    exit()

def select_phone_number_method():  # 방식 선택
    print(f'{"전화번호 선택 방법들":=^100}')
    print(f"{RED}순차적 전화번호(1){RESET}, {GREEN}랜덤형 전화번호(2){RESET}, "
            f"{YELLOW}타이밍형 전화번호(3){RESET}, {BLUE}가챠형 전화번호(4){RESET}, "
            f"{MAGENTA}2진법형 전화번호(5){RESET}, {BRIGHT_CYAN}아날로그형 전화번호(6){RESET}")
    method = input("어떤 방법으로 전화번호를 입력할까요? ").strip().lower()
    time.sleep(0.2)
    return method

method = select_phone_number_method()

if method == "1":    # 순차적 전화번호
    print(f"{CYAN}010 - 0000 - 0000{RESET}")
    while True:
        number = input("너의 전화번호를 입력하시오.(0만 입력 가능): ").lower()
        if number == "0":
            cell_phon += 1
            formatted_cellphon = f"{int(cell_phon):08d}"
            print(f"{CYAN}010 - {formatted_cellphon[:4]} - {formatted_cellphon[4:]}{RESET}")        
        elif number == "멈춰":
            print(f"{CYAN}{'010 - 0000 - 0000은 너의 전화번호야':=^100}{RESET}")
            time.sleep(1)
            break

elif method == "2":  # 랜덤형 전화번호
    part1 = "0000"
    part2 = "0000"
    print(f"{CYAN}010 - {part1} - {part2}{RESET}")
    while True:
        random_number = input("자신의 전화번호가 나올 때까지 0을 입력하시오.: ").strip()
        if random_number == "0":
            part1 = f"{random.randint(0, 9999):04d}"
            part2 = f"{random.randint(0, 9999):04d}"
            print(f"{CYAN}010 - {part1} - {part2}{RESET}")
        elif random_number == "멈춰":
            print(f"{CYAN}010 - {part1} - {part2}은 너의 전화번호야{RESET}")
            time.sleep(1)
            break

elif method == "3":  # 타이밍형 전화번호
    running = True
    watch_time = 0

    def display_time():
        global watch_time
        while running:
            print(f"{CYAN}{watch_time:0.2f}{RESET}", end='\r') 
            watch_time += 0.01
            time.sleep(0.001)

    def get_input():
        global running
        global watch_time
        while True:
            answer = input("             '0'을 입력해 종료").strip()
            if answer == "0":
                running = False
                formatted_time = f"{int(watch_time):08d}"
                print(f"{CYAN}010 - {formatted_time[:4]} - {formatted_time[4:]}{RESET}")
                break

    display_thread = threading.Thread(target=display_time)
    display_thread.start()

    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    input_thread.join()
    display_thread.join()

elif method == "4":  # 가챠형 전화번호
    part = [0] * 8
    running = True
    each_number = 0
    input_count = 0

    def display_time():
        global each_number
        while running:
            global each_number
            if each_number >= 10:
                each_number = 0
            print(f"{CYAN}{each_number:01}{RESET}", end='\r')
            each_number += 1
            time.sleep(0.01)

    def get_input():
        global running
        global each_number
        global input_count
        while input_count < 8:
            answer = input("    '0'을 입력해 입력: ").strip()
            if answer == "0":
                current_number = each_number
                part[input_count] = current_number
                formatted_part = ''.join(map(lambda x: f"{x:01}", part))
                print(f"{CYAN}010 - {formatted_part[:4]} - {formatted_part[4:]}{RESET}")
                input_count += 1
                each_number = 0
        formatted_part = ''.join(map(lambda x: f"{x:01}", part))
        print(f"{CYAN}010 - {formatted_part[:4]} - {formatted_part[4:]}은 너의 전화번호야{RESET}")
        running = False

    display_thread = threading.Thread(target=display_time)
    display_thread.start()

    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    input_thread.join()
    display_thread.join()

elif method == "5":  # 2진법형 전화번호
    def binary_to_decimal(binary_str):
        decimal_value = int(binary_str, 2)
        return decimal_value
    
    cell_phon = input("전화번호를 2진법으로 바꿔서 입력하시오: ").strip()
    cell_phon = binary_to_decimal(cell_phon)
    cell_phon = str(cell_phon)

    if len(cell_phon) > 8:
        cell_phon = cell_phon[-8:]
    cell_phon = cell_phon.zfill(8)
    print(f"{CYAN}010 - {cell_phon[:4]} - {cell_phon[4:]}은 너의 전화번호야{RESET}")

elif method == "6":  # 아날로그형 전화번호
    def button_click():
        cell_phon = scale.get()
        cell_phon = str(cell_phon).rjust(8, '0')
        cell_phon = f"010-{cell_phon[:4]}-{cell_phon[4:]}"
        label.config(text=f"너의 전화번호: {cell_phon}")
        print(f"{CYAN}{cell_phon}이 너의 전화번호야{RESET}")
        root.destroy()

    root = tk.Tk()
    root.title("아날로그형 전화번호 입력하기")

    intro_label = tk.Label(root, text="도윤도윤 전화번호", font=("Arial", 12))
    intro_label.pack()

    scale = tk.Scale(root, from_=0, to=99999999, orient='horizontal', length=100)
    scale.pack()

    button = tk.Button(root, text="선택", command = button_click)
    button.pack()

    label = tk.Label(root, text="너의 전화번호: 010-0000-0000")
    label.pack()

    root.mainloop()

logout()
