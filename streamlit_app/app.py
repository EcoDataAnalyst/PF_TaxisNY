import streamlit as st
from app_add_inputs import add_input

def main():
    st.set_page_config(layout="wide")  # Ensure the app uses the full width

    # Main Layout
    st.markdown("<h1 style='text-align: center;'>Simulador de CO2</h1>", unsafe_allow_html=True)  # H1 Title centered
    #st.write("Simulador de CO2")

    # Row with Two Columns
    col1, col2 = st.columns([0.2, 0.8])  # Create columns with 20%/80% split
    # col1, col2 = st.columns([1, 4])

    with col1:
        # Content for the first (narrower) column goes here
        st.write("This is the 20% column. You can add content, widgets, etc.")

        add_input()

    with col2:
        # Content for the second (wider) column goes here
        st.write("This is the 80% column. Use this for main content or visualizations.")
        # Fill with image placeholder with full width and height
        st.image("https://picsum.photos/800/600", width=800, height=600)

if __name__ == "__main__":
    main()