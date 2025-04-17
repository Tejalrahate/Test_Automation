# Test_Automation
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# # Initialize pre-trained model
# model = SentenceTransformer('all-MiniLM-L6-v2')


def clean_expected_output(expected_answer):
    cleaned = re.sub(r'(?i)Sources?:.*', '', expected_answer, flags=re.DOTALL)
    return cleaned.strip()

class SimilarityComparitor:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to compute similarity score
    def compute_similarity(self, expected_answer, answer):
        if isinstance(answer, float) and np.isnan(answer):
            return 0

        if isinstance(expected_answer, float) and np.isnan(expected_answer):
            return 0

        if answer.strip().lower() == 'failed error':
            return 0

        actual_output = str(answer) if answer is not None else ""
        # expected_output = str(expected_output) if expected_output is not None else ""
        expected_output = clean_expected_output(str(expected_answer)) if expected_answer is not None else ""
        print("expected_output:", expected_answer)
        embeddings1 = self.model.encode([expected_answer])
        embeddings2 = self.model.encode([answer])

        # Calculate the cosine similarity between the embeddings
        similarity_score = cosine_similarity(embeddings1, embeddings2)[0][0]

        return [similarity_score*100]


# # Read the Excel file into a pandas DataFrame
# df = pd.read_excel('test.xlsx')  # Replace with your Excel file path
#
# df['similarity'] = df.apply(lambda row: compute_similarity(row['Expected Result'], row['Answer']), axis=1)
#
# # Convert similarity to percentage
# df['similarity_percentage'] = df['similarity'] * 100
# df.drop(columns=['similarity'], inplace=True)
#
# # Save the updated DataFrame to a new Excel file
# df.to_excel('output_with_similarity.xlsx', index=False)
#
# print("Similarity scores have been calculated and saved to 'output_with_similarity.xlsx'.")
