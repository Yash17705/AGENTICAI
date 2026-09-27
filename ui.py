import asyncio

# Ensure an asyncio event loop exists in the Streamlit runner thread (required for agno under Python < 3.10)
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

import streamlit as st
from youtube_analyzer import build_youtube_agent

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent= get_agent()

st.text(" YouTube Video Analyzer")


video_url= st.text_input("Enter Youtube Video Link")
button= st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing Video....."):
        response= agent.run(f"Analyze this video: {video_url}")
    st.markdown("Analysis report of the Video:")
    st.markdown(response.content)
