"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs
from tabulate import tabulate

def run_profile(profile_name, user_prefs, songs):
    print(f"\n{'='*60}")
    print(f"🎧 Profile: {profile_name}")
    print(f"{'='*60}")
    recommendations = recommend_songs(user_prefs, songs, k=5)
    
    table_data = []
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        table_data.append([
            f"#{i}",
            song['title'],
            song['artist'],
            f"{score:.2f}/4.00",
            explanation
        ])
    
    headers = ["Rank", "Title", "Artist", "Score", "Why"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    cs_student = {"genre": "jazz", "mood": "focused", "energy": 0.3}
    social_work = {"genre": "lofi", "mood": "chill", "energy": 0.5}
    older_person = {"genre": "indie pop", "mood": "happy", "energy": 0.8}

    run_profile("CS Student (Quant Engineering)", cs_student, songs)
    run_profile("Social Work Student", social_work, songs)
    run_profile("Older Person exploring new music", older_person, songs)

if __name__ == "__main__":
    main()