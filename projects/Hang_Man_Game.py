import random

HANGMANPICS = [
    """
========
  +---+
      |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
words = [
    # Nature
    "apple",
    "mountain",
    "river",
    "forest",
    "desert",
    "ocean",
    "sand",
    "stone",
    "breeze",
    "storm",
    "thunder",
    "horizon",
    "sunrise",
    "meadow",
    "valley",
    "field",
    "lake",
    "canyon",
    "tide",
    "sky",
    "cloud",
    "rain",
    "snow",
    "fog",
    "hail",
    "lightning",
    "rainbow",
    "waterfall",
    "volcano",
    "glacier",
    "flower",
    "tree",
    "bush",
    "leaf",
    "branch",
    "seed",
    "vine",
    "moss",
    "bark",
    "petal",
    # Animals
    "lion",
    "tiger",
    "bear",
    "eagle",
    "dolphin",
    "whale",
    "shark",
    "zebra",
    "giraffe",
    "elephant",
    "panther",
    "cheetah",
    "leopard",
    "parrot",
    "crow",
    "hawk",
    "owl",
    "penguin",
    "otter",
    "wolf",
    "fox",
    "rabbit",
    "squirrel",
    "deer",
    "moose",
    "beaver",
    "lynx",
    "alligator",
    "falcon",
    "rhino",
    "buffalo",
    "hedgehog",
    "porcupine",
    "bat",
    "stingray",
    "octopus",
    "seal",
    "turtle",
    "sparrow",
    "finch",
    # Objects
    "lamp",
    "sofa",
    "table",
    "chair",
    "book",
    "pen",
    "pencil",
    "notebook",
    "backpack",
    "clock",
    "mirror",
    "bottle",
    "cup",
    "mug",
    "spoon",
    "fork",
    "plate",
    "bowl",
    "desk",
    "computer",
    "phone",
    "camera",
    "battery",
    "window",
    "door",
    "curtain",
    "fan",
    "heater",
    "keyboard",
    "monitor",
    "television",
    "radio",
    "pillow",
    "blanket",
    "bed",
    "dresser",
    "wardrobe",
    "basket",
    "shelf",
    "drawer",
    # Emotions
    "joy",
    "sadness",
    "anger",
    "fear",
    "love",
    "hope",
    "happiness",
    "melancholy",
    "regret",
    "excitement",
    "disgust",
    "envy",
    "pride",
    "shame",
    "remorse",
    "gratitude",
    "compassion",
    "sorrow",
    "guilt",
    "peace",
    "contentment",
    "euphoria",
    "loneliness",
    "jealousy",
    "curiosity",
    "amusement",
    "frustration",
    "disappointment",
    "relief",
    "anticipation",
    "confidence",
    "embarrassment",
    "boredom",
    "awe",
    "admiration",
    "tension",
    "pity",
    "sympathy",
    "affection",
    "passion",
    # Actions
    "run",
    "jump",
    "swim",
    "climb",
    "throw",
    "catch",
    "walk",
    "crawl",
    "sit",
    "stand",
    "bend",
    "stretch",
    "dance",
    "sing",
    "read",
    "write",
    "draw",
    "paint",
    "cook",
    "bake",
    "drive",
    "fly",
    "ride",
    "dig",
    "lift",
    "drop",
    "push",
    "pull",
    "carry",
    "drag",
    "open",
    "close",
    "throw",
    "catch",
    "twist",
    "spin",
    "shake",
    "stir",
    "build",
    "break",
    # Concepts
    "freedom",
    "justice",
    "truth",
    "honesty",
    "courage",
    "faith",
    "love",
    "hope",
    "integrity",
    "wisdom",
    "loyalty",
    "friendship",
    "patience",
    "determination",
    "discipline",
    "strength",
    "intelligence",
    "creativity",
    "ambition",
    "pride",
    "respect",
    "compassion",
    "equality",
    "responsibility",
    "curiosity",
    "imagination",
    "potential",
    "growth",
    "independence",
    "knowledge",
    "understanding",
    "empathy",
    "harmony",
    "balance",
    "adaptability",
    "resourcefulness",
    "insight",
    "perseverance",
    "humility",
    "resilience",
    # Places
    "city",
    "village",
    "town",
    "forest",
    "desert",
    "ocean",
    "mountain",
    "island",
    "beach",
    "valley",
    "canyon",
    "river",
    "lake",
    "swamp",
    "jungle",
    "rainforest",
    "savanna",
    "prairie",
    "tundra",
    "cave",
    "temple",
    "church",
    "mosque",
    "library",
    "museum",
    "zoo",
    "school",
    "college",
    "university",
    "garden",
    "park",
    "playground",
    "market",
    "hospital",
    "restaurant",
    "cafe",
    "hotel",
    "bakery",
    "grocery",
    "station",
    # Vehicles
    "car",
    "truck",
    "bus",
    "train",
    "bicycle",
    "motorcycle",
    "airplane",
    "helicopter",
    "boat",
    "ship",
    "canoe",
    "kayak",
    "submarine",
    "scooter",
    "skateboard",
    "rollerblades",
    "jet",
    "glider",
    "balloon",
    "raft",
    "yacht",
    "ferry",
    "spaceship",
    "hovercraft",
    "ambulance",
    "firetruck",
    "police car",
    "tractor",
    "bulldozer",
    "snowmobile",
    "crane",
    "forklift",
    "skates",
    "snowboard",
    "surfboard",
    "windsurfer",
    "sailboat",
    "rowboat",
    "cart",
    "limousine",
    # Occupations
    "doctor",
    "nurse",
    "teacher",
    "lawyer",
    "engineer",
    "scientist",
    "chef",
    "farmer",
    "mechanic",
    "pilot",
    "police officer",
    "firefighter",
    "soldier",
    "writer",
    "artist",
    "musician",
    "actor",
    "architect",
    "builder",
    "plumber",
    "carpenter",
    "electrician",
    "pharmacist",
    "dentist",
    "psychologist",
    "counselor",
    "veterinarian",
    "chemist",
    "astronaut",
    "athlete",
    "coach",
    "scientist",
    "analyst",
    "consultant",
    "receptionist",
    "manager",
    "accountant",
    "salesperson",
    "entrepreneur",
    "tailor",
    # Additional random words to reach 1000
    "champion",
    "vacation",
    "treasure",
    "galaxy",
    "festival",
    "holiday",
    "ceremony",
    "concert",
    "parade",
    "carnival",
    "fireworks",
    "destination",
    "celebration",
    "adventure",
    "exploration",
    "expedition",
    "journey",
    "voyage",
    "quest",
    "mission",
    "invention",
    "discovery",
    "breakthrough",
    "legend",
    "myth",
    "miracle",
    "mystery",
    "puzzle",
    "riddle",
    "enigma",
    "alchemy",
    "astronomy",
    "chemistry",
    "physics",
    "biology",
    "geology",
    "meteorology",
    "philosophy",
    "psychology",
    "sociology",
]
random_word = random.choice(words)
lives = 6
display = ["_ "] * len(random_word)
print("".join(display))
print(HANGMANPICS[0])
guessed_letters = []
while not random_word == "".join(display) and lives > 0:
    guessed = input("Please guess a letter: ").lower()
    print("\n")
    if len(guessed) != 1 or not guessed.isalpha():
        print("Please enter a single letter.")
        continue
    if guessed in guessed_letters:
        print("You already guessed this letter.Try again.")
        print(f"You have {lives} lives left")
        continue
    guessed_letters.append(guessed)

    if guessed not in random_word:
        print("\n" + HANGMANPICS[0] + "\n")
        HANGMANPICS.remove(HANGMANPICS[0])
        lives -= 1
    else:
        for position in range(len(random_word)):
            if guessed == random_word[position]:
                display[position] = guessed

    print("".join(display))
    print(f"You have {lives} lives left\n")
if lives == 0:
    print(
        """
  *******
  You lose!
  *******

  """
    )
    print(HANGMANPICS[-1])
else:
    print(
        """
  *******
  You Win
  *******

  """
    )
print(f"the word was {random_word}")
