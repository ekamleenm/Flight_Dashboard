import streamlit as st

from connection_DBeaver import DB

st.sidebar.title('Flight Analytics')
user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

db = DB()

if user_option == 'Check Flights':
    st.title('Flights')
    col1, col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source', sorted(city))
    with col2:
        Destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        table = db.fetch_all_flights(source, Destination)
        st.dataframe(table)

elif user_option == 'Analytics':
    st.title("Analytics")
    
else:
    st.title('About the App')
