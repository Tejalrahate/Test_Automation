import java.util.*;

public class SimilaritySearch {

    // Method to calculate term frequency (TF)
    public static Map<String, Integer> getTermFrequency(String text) {
        Map<String, Integer> frequencyMap = new HashMap<>();
        for (String word : text.toLowerCase().split("\\s+")) {
            frequencyMap.put(word, frequencyMap.getOrDefault(word, 0) + 1);
        }
        return frequencyMap;
    }

    // Method to calculate cosine similarity
    public static double cosineSimilarity(Map<String, Integer> vec1, Map<String, Integer> vec2) {
        Set<String> allWords = new HashSet<>();
        allWords.addAll(vec1.keySet());
        allWords.addAll(vec2.keySet());

        double dotProduct = 0.0;
        double normVec1 = 0.0;
        double normVec2 = 0.0;

        for (String word : allWords) {
            int val1 = vec1.getOrDefault(word, 0);
            int val2 = vec2.getOrDefault(word, 0);

            dotProduct += val1 * val2;
            normVec1 += val1 * val1;
            normVec2 += val2 * val2;
        }

        return (normVec1 == 0 || normVec2 == 0) ? 0.0 : dotProduct / (Math.sqrt(normVec1) * Math.sqrt(normVec2));
    }

    public static void main(String[] args) {
        String doc1 = "AI can assist in software development and testing";
        String doc2 = "Software testing and AI can work together";
        String doc3 = "Nature and wildlife photography is amazing";

        Map<String, Integer> tf1 = getTermFrequency(doc1);
        Map<String, Integer> tf2 = getTermFrequency(doc2);
        Map<String, Integer> tf3 = getTermFrequency(doc3);

        double similarity1 = cosineSimilarity(tf1, tf2);
        double similarity2 = cosineSimilarity(tf1, tf3);

        System.out.println("Similarity between doc1 and doc2: " + similarity1);
        System.out.println("Similarity between doc1 and doc3: " + similarity2);
    }
}
