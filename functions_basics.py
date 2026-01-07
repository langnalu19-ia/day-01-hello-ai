
def greet(name):
    print("Hello", name, "- welcome to your AI journey!")

greet("Bernard")
greet("Future AI Expert")
greet("ChatGPT Student")

def classify_tempo(tempo):
    if tempo > 70:
        return "energetic"
    else:
        return "calm"

result = classify_tempo(75)
print("The song is", result)

result = classify_tempo(60)
print("The song is", result)