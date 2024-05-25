import streamlit as st


def add_input():

    # Initialize session state variables
    if 'inputs' not in st.session_state:
        st.session_state['inputs'] = []

    def add_input():
        st.session_state.inputs.append({'dropdown': '', 'text_input': ''})



    # Button to add new input fields
    if st.button("Agregar Vehiculo"):
        add_input()

    # Display the dynamically added input fields
    for i, input_pair in enumerate(st.session_state.inputs):
        st.session_state.inputs[i]['dropdown'] = st.selectbox(f"Modelo del Vehiculo {i+1}", ["Option 1", "Option 2", "Option 3"], key=f"dropdown_{i}")
        st.session_state.inputs[i]['text_input'] = st.text_input(f"Ingrese la cantidad del modelo {i+1}", key=f"text_input_{i}")

    st.write("Inputs:", st.session_state.inputs)
