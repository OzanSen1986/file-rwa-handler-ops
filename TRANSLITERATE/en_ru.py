from googletrans import Translator

def smart_translate(text: str, target_lang = 'en'):
    translator = Translator()
    # detect the language first:
    detected = translator.detect(text)
    print(f"Detected language: {detected.lang} (confidence: {detected.confidence})")

    # translate if not already in target language
    if detected.lang != target_lang:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    else:
        return text

def main() -> None:

    texts = ["Bent u wettelijk bevoegd om in Nederland te werken?",
             "Hoeveel jaren bent u werkzaam als Data Scientist?"]    
    for text in texts:
        result = smart_translate(text)
        print(f'Original: {text}')
        print(f'Translated: {result}\n') 

if __name__ == '__main__':
    main()


