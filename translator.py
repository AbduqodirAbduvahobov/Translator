from googletrans import Translator

translater = Translator()
language = input("Enter a language: ")
text = input("Enter a text which you want translate: ")
translate = translater.translate(text, dest = language)

print("Result:", translate.text)

