# SBERT-test

Siamese BERT model testing and exploration for SimplySaid.

Tips for SimplySaid:

- Segment the Transcript: Break the Whisper output into individual sentences or logical chunks. Compare each chunk against the target concepts to see which ones were hit. (Length of segmentation to be decided).

- Setting a Threshold: A similarity score of 0.7 to 0.8 for correct explanation with different words.

- Handling Technical Jargon: Looking for domain-specific models have to be done because standardized models have a hard time dealing with specialized fields.
