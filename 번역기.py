from googletrans import Translator, LANGUAGES

def translate_text(text, src_lang='auto', dest_lang='en'):
    # Translator 객체 생성
    translator = Translator()
    
    # 번역 수행
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    
    return translated.text

def list_languages():
    # 지원하는 언어 목록 출력
    print("지원하는 언어 목록:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

def main():
    # 언어 목록 출력
    list_languages()
    
    # 사용자 입력
    text = input("번역할 텍스트를 입력하세요: ")
    src_lang = input("원본 언어 코드를 입력하세요 (예: 'en' for English, 'ko' for Korean, 'auto' for 자동 감지): ")
    dest_lang = input("목표 언어 코드를 입력하세요 (예: 'en' for English, 'ko' for Korean): ")
    
    # 번역 수행
    translated_text = translate_text(text, src_lang, dest_lang)
    
    # 번역 결과 출력
    print(f"번역 결과: {translated_text}")

if __name__ == "__main__":
    main()
