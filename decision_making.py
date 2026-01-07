def classify_temperature(temp):
    if temp > 38:
        return "Fever detected"
    elif temp >= 36:
        return "Normal"
    else:
        return "Below normal"
print("Health:", classify_temperature(39))


def credit_risk(score):
    if score >= 700:
        return "Low risk"
    elif score >= 600:
        return "Medium risk"
    else:
        return "High risk"
    
print("Finance:", credit_risk(650))


def student_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Fail"

print("Education:", student_grade(82))

def bedtime(time):
    if time >= 21:
        return "Go to bed"
    elif time >= 19:
        return "Wind down"
    else:
        return "Play time"

print("Daily Life:", bedtime(20))

def classify_items(items, domain):
    for item in items:
        if domain == "Music":
            if item > 70:
                print(domain, item, "→ Energetic")
            else:
                print(domain, item, "→ Calm")

        elif domain == "Health":
            if item > 38:
                print(domain, item, "→ Fever detected")
            elif item >= 36:
                print(domain, item, "→ Normal")
            else:
                print(domain, item, "→ Below normal")

        elif domain == "Finance":
            if item >= 700:
                print(domain, item, "→ Low risk")
            elif item >= 600:
                print(domain, item, "→ Medium risk")
            else:
                print(domain, item, "→ High risk")

        elif domain == "Education":
            if item >= 90:
                print(domain, item, "→ A")
            elif item >= 75:
                print(domain, item, "→ B")
            elif item >= 60:
                print(domain, item, "→ C")
            else:
                print(domain, item, "→ Fail")

        elif domain == "Daily Life":
            if item >= 21:
                print(domain, item, "→ Go to bed")
            elif item >= 19:
                print(domain, item, "→ Wind down")
            else:
                print(domain, item, "→ Play time")
        else:
            print(domain, item, "→ No rule defined")

# Music
classify_items([60, 72, 75, 68], "Music")

# Health
classify_items([36.5, 37.2, 39.0, 35.8], "Health")

# Finance
classify_items([720, 650, 580, 690], "Finance")

# Education
classify_items([95, 82, 67, 55], "Education")

# Daily Life
classify_items([18, 20, 21, 17], "Daily Life")

classify_items([5, 12, 17], "Unknown Domain")

