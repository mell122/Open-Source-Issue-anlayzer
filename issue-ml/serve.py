import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read CSV file into a DataFrame
df = pd.read_csv("../output/github_issues.csv")

# Combine the title and body columns into a single text column
df['text'] = df['title'] +  df['body']

# Vectorize the text data using the Bag-of-Words model
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(df['text'])

# Load the trained classifier
clf = MultinomialNB()
clf.load_model('classifier.pkl')

# Predict the category of new issues
new_issues = [
    "I'm having trouble installing my software",
    "My software is not working as expected",
    "I have a suggestion for improvement"
]
new_issue_vectors = vectorizer.transform(new_issues)
new_issue_predictions = clf.predict(new_issue_vectors)

# Print the predictions
for issue, prediction in zip(new_issues, new_issue_predictions):
    print(f"Issue: {issue}")
    print(f"Prediction: {prediction}")
    print()
