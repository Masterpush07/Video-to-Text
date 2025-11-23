
import streamlit as st
import requests

API_URL = "https://<YOUR_RENDER_BACKEND_URL>/analyze"

st.title("🎥 YouTube → Text (Gemini)")

video_url = st.text_input("Enter YouTube Video URL")

if st.button("Analyze Video"):
    if not video_url:
        st.error("Please enter a video URL")
    else:
        with st.spinner("Processing..."):
            response = requests.post(API_URL, json={"video_url": video_url})

        if response.status_code != 200:
            st.error("Backend error ❌")
        else:
            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader("Transcript")
                st.write(data["transcript"])

                st.subheader("Summary")
                st.write(data["summary"])

                st.subheader("Sentiment")
                st.write(data["sentiment"])

                st.subheader("Key Points")
                st.write(data["key_points"])

                st.subheader("Suggestions")
                st.write(data["suggestions"])

                st.subheader("Overall Score")
                st.metric(label="Communication Score", value=data["overall_score"])
