# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
VibeFinder 1.0

---

## 2. Intended Use
VibeFinder 1.0 is designed to suggest songs based on a user's favorite genre, mood and energy level. It is built for classroom exploration to demonstrate how content based filtering works. It assumes the user has clear preferences for genre, mood and energy and that those preferences can be matched against song attributes in a small catalog.

---

## 3. How the Model Works
VibeFinder scores every song in the catalog against a user's taste profile. If a song matches the user's favorite genre it gets 2 points. If it matches the user's preferred mood it gets 1 point. The closer the song's energy is to the user's target energy the more points it gets up to 1 point. Songs are then ranked from highest to lowest score and the top 5 are returned. Think of it like a judge at a talent show giving points for each category and crowning the highest scorer.

---

## 4. Data
The catalog contains 15 songs across genres including pop, lofi, rock, jazz, ambient, synthwave, indie pop, folk, soul, afrobeats and r&b. I started with 10 starter songs and added 5 of my own including Electric Love, Call Your Mom, Put Your Records On, Idan by Korra Obidi and Which One by Drake. The dataset is small and lacks diversity in afrobeats, r&b and hip-hop which affects genre matching for users who prefer those genres.

---

## 5. Strengths
The system works well for users who like pop, lofi and indie pop since those genres are well represented in the catalog. The CS Student profile correctly surfaced jazz and focused songs. The Older Person profile correctly recommended upbeat indie pop songs. The scoring logic is simple and transparent — every recommendation comes with a clear explanation of why it was chosen.

---

## 6. Limitations and Bias
The catalog only has 15 songs which severely limits variety. Genre matching is less useful for afrobeats, r&b and soul listeners because those genres are underrepresented. The system might over-recommend happy songs since mood is weighted and several songs share that mood. Energy similarity alone can surface songs that feel wrong in other ways — for example a high energy jazz song might score well for a pop lover just because of energy. The system does not consider lyrics, language, cultural context or listening history.

---

## 7. Evaluation
I tested three user profiles: a CS Student studying Quant Engineering who wanted jazz and focused low energy music, a Social Work Student who wanted lofi chill mid energy music, and an Older Person exploring new music who wanted happy high energy indie pop. The CS Student correctly got Coffee Shop Stories as the top result. The Social Work Student got Midnight Coding and Library Rain which both made sense. The Older Person got Electric Love and Rooftop Lights which felt right. The results matched my intuition for all three profiles.

The CS Student profile recommended jazz and focused low energy songs 
which made sense for someone studying. The Social Work Student got 
lofi chill songs which matched the calm focused mood needed for 
building a persona. The Older Person got upbeat indie pop which felt 
right for someone exploring new music. 

Comparing CS Student vs Older Person — the CS Student got low energy 
calm songs while the Older Person got high energy happy songs. This 
makes sense because energy and mood preferences were completely 
opposite between the two profiles showing the system correctly 
differentiates between very different listener types.

---

## 8. Future Work
I would expand the catalog to at least 100 songs with better genre diversity especially afrobeats, r&b and hip-hop. I would add collaborative filtering so the system can learn from what similar users listen to. I would also add a diversity penalty so the same artist doesn't appear multiple times in the top results. Finally I would add tempo and danceability to the scoring logic for more nuanced recommendations.

---

## 9. Personal Reflection
Building this recommender taught me that recommendation systems are not magic — they are just math applied to data. The biggest surprise was how much the quality of the dataset matters. My system struggled to recommend afrobeats songs not because the algorithm was wrong but because the data was not there. This changed the way I think about apps like Spotify — the reason they work so well is not just clever algorithms but massive diverse datasets built over years. Using Claude as my AI assistant helped me move faster but I had to verify every suggestion and make all the design decisions myself.