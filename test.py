# SBERT Test File

from sentence_transformers import SentenceTransformer, util

# 1. Load a pre-trained model
# 'all-MiniLM-L6-v2' is a great balance of speed and accuracy
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define your texts
source_material = "The Feynman Technique involves explaining a concept in simple terms to identify gaps in your understanding."
user_transcript = "I'm explaining this topic simply so I can see what parts I don't actually know yet."

# 3. Compute embeddings
embedding1 = model.encode(source_material, convert_to_tensor=True)
embedding2 = model.encode(user_transcript, convert_to_tensor=True)

# 4. Calculate cosine similarity
cosine_score = util.cos_sim(embedding1, embedding2)

print(f"Similarity Score: {cosine_score.item():.4f}")