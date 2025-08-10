import streamlit as st
from team_selector import team_chain

st.set_page_config(page_title="Cricket Team Selector",page_icon="🏏")
st.title("Cricket Team Selector 🏏")
st.markdown("""
    Select the format, country, pitch conditions, and strategy to get the best cricket team selection.
""")
with st.form("team_selection_form"):
    format = st.selectbox("Select Format",["Test","ODI","T20"])
    country = st.selectbox("Select Country",["India","Australia","England","South Africa","Pakistan","New Zealand"])
    pitch = st.selectbox("Select Pitch Conditions",["Dry","Green","Flat","Turning","Bouncy"])
    strategy = st.selectbox("Enter Team Strategy",["Aggressive","Defensive","Balanced"])

    submit_button = st.form_submit_button("Generate Team")

if submit_button:
    with st.spinner("Generating team..."):
        result = team_chain.run(format=format,country=country,pitch=pitch,strategy=strategy)
        st.success("Team generated successfully!")
        st.markdown(f"### Selected Team for {country} in {format} format")
        st.text_area("🏆 Selected Team",result,height=400)

        