# main.py

import streamlit as st
from components.login_page import login_page
from components.signup_page import signup_page
from PIL import Image

# st.set_page_config(layout="wide")


def main():
    st.set_page_config(page_title="Job Recommendation System")
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    if not st.session_state['logged_in']:      
        st.title("Job Recommendation System")
        st.title("Login/Signup")
        tab1, tab2 = st.tabs(["Login", "Signup"])
        
        with tab1:
            login_page()
            
        with tab2:
            signup_page()
    else:
        st.sidebar.title('Menu')

        if st.sidebar.button('Logout'):
            st.session_state['logged_in'] = False
            del st.session_state['access_token']
            st.rerun()

if __name__ == "__main__":
    main()
