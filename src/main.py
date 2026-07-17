"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs

def run_profile(profile_name, user_prefs, songs):
    print(f"\n{'='*40}")
    print(f"🎧 Profile: {profile_name}")
    print(f"{'='*40}")
    recommendations = recommend_songs(user_prefs, songs, k=5)
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\n#{i} {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} / 4.00")
        print(f"   Why: {explanation}")
        print("-" * 40)

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Profile 1: CS Student studying Quant Engineering
    cs_student = {"genre": "jazz", "mood": "focused", "energy": 0.3}
    
    # Profile 2: Social Work Student building a persona
    social_work = {"genre": "lofi", "mood": "chill", "energy": 0.5}
    
    # Profile 3: Older person exploring this generation's music
    older_person = {"genre": "indie pop", "mood": "happy", "energy": 0.8}

    run_profile("CS Student (Quant Engineering)", cs_student, songs)
    run_profile("Social Work Student", social_work, songs)
    run_profile("Older Person exploring new music", older_person, songs)

if __name__ == "__main__":
    main()