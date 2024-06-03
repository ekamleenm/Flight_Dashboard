import streamlit as st

st.sidebar.title('Flight Analytics')
user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Flights')
elif user_option == 'Analytics':
    st.title("Analytics")
else:
    st.title('About the App')
