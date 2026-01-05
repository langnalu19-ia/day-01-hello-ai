songs = ["Praise", "Worship", "Adoration", "Thanksgiving", "Joy"]
for song in songs:
    print(song)

for i in range(5):
    print("Training step:", i)

song_info = {
    "title": "Joy in the Middle of Trouble",
    "tempo": 72,
    "mood": "hopeful",
    "duration": 4.5
}

for key, value in song_info.items():
    print(key, ":", value)
   
songs = [
    {"title": "Praise", "tempo": 68},
    {"title": "Worship", "tempo": 72},
    {"title": "Adoration", "tempo": 60},
    {"title": "Thanksgiving", "tempo": 75}
]

for song in songs:
    if song["tempo"] > 70:
        print(song["title"], "→ energetic")
    else:
        print(song["title"], "→ calm")
count = 0

while count < 5:
    print("Current count is:", count)
    count += 1