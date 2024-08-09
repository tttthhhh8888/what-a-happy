import random
import time
import base64


player = input("1p, 2p?: ").lower()
if player == "1p":
    def choose_word():
        words = ['python', 'hangman', 'minchan', 'doyun', 'fuckyou', 'apple', 'banana']
        words.extend(['cherry', 'date', 'elephant', 'flame', 'grape', 'house', 'ice'])
        words.extend(['juice', 'kite', 'lemon', 'monkey', 'nut', 'orange', 'pearl', 'queen'])
        words.extend(['rose', 'snake', 'tree', 'umbrella', 'violin', 'wolf', 'xylophone'])
        words.extend(['yacht', 'zebra', 'apricot', 'butterfly', 'candle', 'dragon', 'engine'])
        words.extend(['feather', 'giraffe', 'horizon', 'island', 'jungle', 'key', 'lamp'])
        words.extend(['moon', 'notebook', 'octopus', 'pencil', 'quilt', 'rainbow'])
        words.extend(['star', 'train', 'unicorn', 'vacuum', 'window', 'chamber'])
        words.extend(['airplane', 'balloon', 'cactus', 'dolphin', 'eagle', 'falcon', 'glove'])
        words.extend(['hat', 'iceberg', 'jacket', 'koala', 'lemonade', 'mountain', 'nest'])
        words.extend(['opera', 'penguin', 'quasar', 'rocket', 'sunflower', 'telescope'])
        words.extend(['vulture', 'whale', 'yak', 'zeppelin', 'acorn', 'beetle'])
        words.extend(['cat', 'dog', 'fish', 'frog', 'goat', 'hill'])
        words.extend(['jug', 'kite', 'lamp', 'mouse', 'owl', 'pig'])
        words.extend(['quilt', 'ring', 'sock', 'unit', 'van', 'wind'])
        words.extend(['box', 'cow', 'duck', 'ear', 'fork', 'grill'])
        words.extend(['jam', 'key', 'leaf', 'man', 'nose', 'oak'])
        words.extend(['toy', 'ufo', 'vase'])
        words.extend(['xray', 'yarn', 'zoo', 'ant', 'ball', 'car'])
        words.extend(['egg', 'fish', 'goose', 'jar'])
        words.extend(['rat', 'sock', 'umbrella', 'web'])
        words.extend(['zebra', 'bike', 'fan'])
        words.extend(['brimstone', 'viper', 'cypher', 'sova', 'sage', 'phoenix'])
        words.extend(['jett', 'raze', 'breach', 'killjoy', 'skye', 'astra'])
        words.extend(['yoru', 'kayo', 'neon', 'chamber', 'harbor', 'deadlock'])
        words.extend(['omen'])
        words.extend(['bulldog', 'guardian', 'phantom', 'vandal', 'spectre', 'bucky'])
        words.extend(['judge', 'stinger', 'classic', 'sheriff', 'ares', 'odin'])
        words.extend(['marshal', 'operator'])
        return random.choice(words)

    word = choose_word()
elif player == "2p":
    word = input("어떤 단어로 할까요?: ").lower()

else :
    print("1p, 2p를 입력해주세요.")

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          -|-  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          -|-  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          -|-  |
          / |  |
               |
        --------
        """
    ]
    attempts = 6 - attempts
    return stages[attempts]

def hangman():
    guessed_letters = set()
    attempts = 6
    list = []

    print("게임을 시작하지")

    while attempts > 0:
        print("\n남은 기회:", attempts)
        print("사용한 단어들: ", ', '.join(guessed_letters))
        print(display_hangman(attempts))
        print("단어:", display_word(word, guessed_letters))
        hint_decode = "cHJpbnQoIu2MmOydtOumuCDsnY7tlbwiKQ=="
        eval(compile(base64.b64decode(hint_decode).decode(), '<string>', 'exec'))
        guess = input("단어 한개 말해보세요: ").lower()

        if guess == "힌트":
            hint = word[random.randint(0, len(word) - 1)]

            print(hint_decode)
            print("\n힌트: ", hint)


        else:
            if guess == "봐줘":
                attempts = attempts * 2
                print("기회 곱하기 2")

            else:
                if len(guess) != 1 or not guess.isalpha():
                    print("알파벳만 입력할 수 있어요")
                    continue

                if guess in guessed_letters:
                    print("아까 이미 적었어요")
                    continue

                guessed_letters.add(guess)

                if guess in word:
                    print("정답!")
                else:
                    print("땡!")
                    attempts -= 1

            if all(letter in guessed_letters for letter in word):
                print("\n단어를 맞췄습니다:", word)
                time.sleep(2)
    else:
        print('\n응아니야 정답은 "', word, '"이야')

hangman()