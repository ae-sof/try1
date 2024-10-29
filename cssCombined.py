import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="UTP ParcelHub", page_icon=":package:", layout="centered")

# Initialize session states
if 'page' not in st.session_state:
    st.session_state.page = 'splash_screen'

# Define a placeholder for content
placeholder = st.empty()

# Define page-specific CSS and content
if st.session_state.page == 'splash_screen':
    # Page-specific CSS for splash screen
    st.markdown("""
        <style>
        .stApp { background-color: #F1F0EC; }
        .centered-content {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            text-align: center;
        }
        h1 { text-align: center; color: #344EAD; }
        p { text-align: center; color: #000000; }
        </style>
    """, unsafe_allow_html=True)
    
    # Splash screen content
    with placeholder.container():
        st.markdown("""
            <div class="centered-content">
                <h1>UTP<br>ParcelHub</h1>
                <p>By students for students</p>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(3)  # Display splash screen for 3 seconds
        placeholder.empty()
        st.session_state.page = 'feature_offering'  # Transition to the feature offering page

    
if st.session_state.page == 'feature_offering':
    placeholder.empty()
    
    # Page-specific CSS for feature offering
    st.markdown("""
        <style>
        .stApp { background-color: #F1F0EC; }
        h2 { text-align: center; color: #1c53d6; }
        p { text-align: center; color: #000000; }
        .stButton button {
            color: white; background-color: #344EAD;
            border-radius: 8px; padding: 5px 60px; font-size: 18px;
            border: 1px solid transparent;
            margin: auto; display: block;
        }
        .stButton button:hover {
            background-color: #223372; border: 1px solid white; color: white;
        }
        </style>
    """, unsafe_allow_html=True)
    
    placeholder.empty()
    # Feature offering content
    with placeholder.container():
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
                
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image("https://raw.githubusercontent.com/username/repository/branch/path/to/savetime2 again.png", width=200, height=200)
            
        # Title with new color
        st.markdown('<h2>Save Time and Energy!</h2>', unsafe_allow_html=True)

        # Description text
        st.markdown('<p>Get your parcels delivered in a day with our fast delivery service</p>', unsafe_allow_html=True)

        # Pagination dots
        st.markdown('<p>•  •</p>', unsafe_allow_html=True)

        # Button to switch page
        if st.button("Continue"):
            st.session_state.page = 'landing'  # Move to the landing page
        st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.page == 'landing':
    # Here you can implement the Landing page content
    st.write("Welcome to the Landing Page! This will contain the main content of your app.")
