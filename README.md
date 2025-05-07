# 📊 YouTube Trending Video Analytics Dashboard

This project provides an interactive data dashboard to analyze trending YouTube videos using Python, Plotly, and Streamlit. It also integrates OpenAI GPT for Natural Language Query (NLQ).

## 🔧 Technologies Used
- Python 3.10+
- Pandas, NumPy
- Plotly for interactive visualizations
- Streamlit for dashboarding
- OpenAI GPT for NLQ (Optional)

## 📁 Dataset
Data used is from [Kaggle: Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new).

## 📈 Features
- Filter videos by category
- Interactive scatter plot for views vs. likes
- Metrics dashboard (total views, likes)
- Chat with your data using GPT-4

## 🚀 Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
```

To enable GPT responses, add your OpenAI key to `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your_api_key_here"
```

## 🧠 Sample Questions
- What is the average view count of trending videos?
- Which category has the most likes?
- Are longer titles more likely to trend?

## 📄 License
MIT License

---

✅ Developed by Anajni Kumar
