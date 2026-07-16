"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n🎵 Top Music Recommendations\n")
    print("=" * 40)
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\n#{i} {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} / 4.00")
        print(f"   Why: {explanation}")
        print("-" * 40)

if __name__ == "__main__":
    main()