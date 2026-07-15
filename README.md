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

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



