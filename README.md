# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

Fast/slow (tempo), happy/sad/angry/nostalgic (mood), jazz/gospel/r&b/hiphop/country/afrobeat (genre)

You can include a simple diagram or bullet list if helpful.

This project simulates a music recommender that uses content based filtering to suggest songs based on a user's favorite genre, mood and energy level. 

I grouped the systems feature into two categories, User Behavior Data and Songg Attribute Data 

Bucket 1: User Behavior Data
(what the user DOES)

Skip, like, dislike, replay, share, download, report, add to playlist, interested/not interested, double rewind

Bucket 2: Song Attribute Data
(what describes the SONG itself)


Features each Song uses:

Mood — focuses on the user's emotion
Energy — different temperaments come into play based on how the user feels
Genre — personal preference of the user

What UserProfile stores:

Favorite genres: afrobeats, r&b, hip-hop, indie pop, pop, soul
Favorite moods: happy, chill
Target energy: 0.65

How Recommender scores songs:

Compares each song's attributes against the user's taste profile
Songs that match mood get the most points
Songs that match energy level get second most points
Genre match gives bonus points
Songs are ranked highest to lowest score

Real world recommendation systems like Spotify use both collaborative filtering (based on what similar users listened to) and content based filtering (based on song attributes). My version focuses on content based filtering only, prioritizing Genre match (+2.0 points), Mood match (+1.0 point) and Energy similarity (max 1.0 points, more points the closer to the user's target).

user_profile = {
    "favorite_genre": ["afrobeats", "r&b", "hip-hop", "indie pop", "pop", "soul"],
    "favorite_mood": ["happy", "chill"],
    "target_energy": 0.65
}

Final Algorithm Recipe 
Genre match = +2.0 points
Mood match = +1.0 point
Energy similarity = 1 - |user_energy - song_energy| (max 1.0 points)

Input → Process → Output

User wants: happy, afrobeats, energy 0.65
     ↓
Loop through all 15 songs in CSV
     ↓
Score each song:
  - Genre match? +2.0
  - Mood match? +1.0  
  - Energy close? up to +1.0
     ↓
Sort all songs highest to lowest score
     ↓
Return top 3 recommendations

This system might be biased because my catalog doesn't have enough afrobeats, r&b, hip-hop and soul songs to match my favorite genres. This means genre matching becomes less useful and recommendations end up relying mostly on mood and energy instead
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

🎵 Top Music Recommendations

========================================

#1 Sunrise City by Neon Echo
   Score: 3.98 / 4.00
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)
----------------------------------------

#2 Gym Hero by Max Pulse
   Score: 2.87 / 4.00
   Why: genre match (+2.0), energy similarity (+0.87)
----------------------------------------

#3 Electric Love by BØRNS
   Score: 1.98 / 4.00
   Why: mood match (+1.0), energy similarity (+0.98)
----------------------------------------

#4 Rooftop Lights by Indigo Parade
   Score: 1.96 / 4.00
   Why: mood match (+1.0), energy similarity (+0.96)
----------------------------------------

#5 Put Your Records On by Corinne Bailey Rae
   Score: 1.75 / 4.00
   Why: mood match (+1.0), energy similarity (+0.75)
----------------------------------------

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

### Three User Profiles Tested:

**Profile 1: CS Student (Quant Engineering)**
genre=jazz, mood=focused, energy=0.3

#1 Coffee Shop Stories by Slow Stereo
   Score: 2.93 / 4.00
   Why: genre match (+2.0), energy similarity (+0.93)
#2 Focus Flow by LoRoom
   Score: 1.90 / 4.00
   Why: mood match (+1.0), energy similarity (+0.90)
#3 Spacewalk Thoughts by Orbit Bloom
   Score: 0.98 / 4.00
   Why: energy similarity (+0.98)

**Profile 2: Social Work Student**
genre=lofi, mood=chill, energy=0.5

#1 Midnight Coding by LoRoom
   Score: 3.92 / 4.00
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.92)
#2 Library Rain by Paper Lanterns
   Score: 3.85 / 4.00
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.85)
#3 Focus Flow by LoRoom
   Score: 2.90 / 4.00
   Why: genre match (+2.0), energy similarity (+0.90)

**Profile 3: Older Person exploring new music**
genre=indie pop, mood=happy, energy=0.8

#1 Electric Love by BØRNS
   Score: 3.98 / 4.00
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)
#2 Rooftop Lights by Indigo Parade
   Score: 3.96 / 4.00
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.96)
#3 Sunrise City by Neon Echo
   Score: 1.98 / 4.00
   Why: mood match (+1.0), energy similarity (+0.98)
## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

## Limitations and Risks

- This system only works on a small catalog of 15 songs which limits variety
- It does not understand lyrics, language or cultural context
- Genre matching is less useful because my catalog lacks enough afrobeats, r&b and soul songs
- The system might over-recommend happy songs since mood is weighted heavily
- Energy similarity alone can surface songs that feel completely wrong in other ways

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



