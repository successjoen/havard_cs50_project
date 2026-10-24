#input emotion
emotion = input("")

text = emotion.strip().replace(":)", "🙂").replace(":(", "🙁")

print(text)


