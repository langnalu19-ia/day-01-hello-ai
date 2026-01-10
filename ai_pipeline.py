# INPUT DATA (raw data)

# Music domain
song_tempos = [58, 72, 80, 65]

# Health domain
temperatures = [36.4, 39.1, 37.0, 35.6]

# Finance domain
credit_scores = [720, 610, 580, 690]

# Education domain
exam_grades = [90, 80, 70, 60, 50]

# daily life domain
bedtimes = [21, 18, 20, 16]

# PROCESSING FUNCTIONS

def analyze_music(tempo):
    if tempo > 70:
        return "Energetic"
    else:
        return "Calm"


def analyze_health(temp):
    if temp > 38:
        return "Fever detected"
    elif temp >= 36:
        return "Normal"
    else:
        return "Below normal"


def analyze_finance(score):
    if score >= 700:
        return "Low risk"
    elif score >= 600:
        return "Medium risk"
    else:
        return "High risk"

def analyze_education(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "Fail"
    
def analyze_daily_life(time):
    if time >= 21:
        return "Go to bed"
    elif time >= 19:
        return "Wind down"
    else:
        return "Play time"

# PIPELINE RUNNER

print("🎵 Music Analysis")
for tempo in song_tempos:
    result = analyze_music(tempo)
    print("Tempo:", tempo, "→", result)

print("\n🩺 Health Analysis")
for temp in temperatures:
    result = analyze_health(temp)
    print("Temperature:", temp, "→", result)

print("\n💰 Finance Analysis")
for score in credit_scores:
    result = analyze_finance(score)
    print("Credit Score:", score, "→", result)

print("\n🎓 Education Analysis")
for grade in exam_grades:
    result = analyze_education(grade)
    print("Grade:", grade, "→", result)

print("\n🛏️ Daily Life Analysis")
for bedtime in bedtimes:
    result = analyze_daily_life(bedtime)
    print("Bedtime:", bedtime, "→", result)

