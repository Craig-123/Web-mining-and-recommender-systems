import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to preprocess text
def preprocess_text(text):
    return text

# Function to cluster text data
def cluster_text(text_data, num_clusters):
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(text_data)
    km = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100)
    km.fit(features)
    return km, vectorizer

# Function to visualize clusters using word clouds
def visualize_clusters(km, vectorizer, num_clusters, documents, titles, links):
    centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()

    for i in range(num_clusters):
        st.markdown(f"## Cluster {i+1}")
        term_frequencies = km.cluster_centers_[i]
        sorted_terms = centroids[i]
        frequencies = {terms[ind]: term_frequencies[ind] for ind in sorted_terms}
        wordcloud = WordCloud(background_color="white", max_words=50).generate_from_frequencies(frequencies)
        st.image(wordcloud.to_array(), caption=f'Word Cloud for Cluster {i+1}', width=500)
        
        # Display Titles and URLs of news articles in the cluster
        st.markdown("### Titles and URLs of News Articles:")
        cluster_indices = documents[km.labels_ == i].index
        for idx in cluster_indices:
            st.write(f"**Title:** {titles[idx]}")
            st.write(f"**Link:** {links[idx]}")
            st.markdown("---")

def main():
    st.title("News Articles Clustering App")
    st.subheader("Developed by Craig T chipendo (R204740C), HDSC")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Settings")

    # Load CSV file
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        # Read CSV data
        all_data = pd.read_csv(uploaded_file)
        documents = all_data['Content'].astype(str)
        titles = all_data['Title']
        links = all_data['Link']

        # Preprocess text
        preprocessed_documents = documents.apply(preprocess_text)

        # Cluster settings
        num_clusters = st.sidebar.slider("Number of Clusters", min_value=2, max_value=10, value=4)

        # Cluster text
        st.sidebar.markdown("---")
        st.sidebar.subheader("Clustering Results")
        km, vectorizer = cluster_text(preprocessed_documents, num_clusters)

        # Visualize clusters using word clouds and display Titles and URLs
        visualize_clusters(km, vectorizer, num_clusters, documents, titles, links)

if __name__ == "__main__":
    main()
