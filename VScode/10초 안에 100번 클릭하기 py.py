print("엔터키를 누르세요:")
click = 0
import time
start_time = time.time()
while click < 100:
    blank = input()
    current_time = time.time()
    exeed_time = current_time - start_time
    if blank == '':
        click += 1
        print(f"엔터키를 {click}번 눌렀습니다.")
    elif exeed_time > 5:
        print("타임 오버")
        break
    else:
        click = 0
        print("초기화ㅋ")
    if exeed_time > 5:
        print("타임 오버")
        break
if click >= 100:
    print("성공!")
