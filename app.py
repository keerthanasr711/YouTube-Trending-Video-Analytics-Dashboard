import os
import pandas as pd
import streamlit as st
import plotly.express as px
import kagglehub
from openai import OpenAI

# Download dataset using kagglehub
path = kagglehub.dataset_download("datasnaek/youtube-new")
data_file = os.path.join(path, "USvideos.csv")

# Category mapping (from categoryId to human-readable category name)
category_mapping = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    19: "Travel & Events",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "How-to & Style",
    27: "Education",
    28: "Science & Technology",
    29: "Nonprofits & Activism"
}

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(data_file)
    # Map categoryId to category_name
    df['category_name'] = df['categoryId'].map(category_mapping)
    return df

df = load_data()

# Streamlit UI
st.title("📊 YouTube Trending Video Analytics")
st.markdown("Explore trends and statistics of YouTube trending videos in the US.")

# Sidebar filters
category = st.sidebar.selectbox("Select Category", df['category_name'].unique())
filtered_df = df[df['category_name'] == category]

# Plot: Views vs Likes
st.subheader("Views vs Likes")
fig = px.scatter(filtered_df, x='views', y='likes', size='comment_count',
                 hover_data=['title'], color='channel_title')
st.plotly_chart(fig)

# Natural Language Query (GPT)
st.subheader("🔍 Ask a question about the data")
prompt = st.text_input("Ask me anything about the YouTube data (e.g., 'Which video had the most views?')")

if prompt:
    try:
        # OpenAI client with API key from Streamlit secrets
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Change the model name if needed
                messages=[
                    {"role": "system", "content": "You are a helpful data analyst with access to YouTube trending data."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.write("**GPT Response:**")
            st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error accessing OpenAI: {e}")
