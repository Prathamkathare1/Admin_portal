import streamlit as st
from supabase import create_client
from dotenv import load_dotenv
import os
import time

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(
    page_title="Login - Dumroo Admin",
    page_icon="🔐",
    layout="centered"
)

def verify_login(email, password):
    """Verify admin credentials"""
    try:
        # Demo credentials for testing
        demo_users = {
            'rajesh@school.com': {'password': 'admin123', 'role': 'admin1'},
            'lakshmi@school.com': {'password': 'admin123', 'role': 'admin2'},
            'anil@school.com': {'password': 'admin123', 'role': 'admin3'}
        }
        
        if email in demo_users and demo_users[email]['password'] == password:
            return True, demo_users[email]['role']
        return False, None
    except Exception as e:
        st.error(f"Login error: {str(e)}")
        return False, None

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'admin_role' not in st.session_state:
    st.session_state.admin_role = None

# If already logged in, show success and redirect info
if st.session_state.logged_in:
    st.success("✅ You are already logged in!")
    st.info("👉 Please close this tab and open the main app using: `streamlit run app.py`")
    
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.admin_role = None
        st.rerun()
    st.stop()

# Custom CSS
st.markdown("""
    <style>
    .login-header {
        text-align: center;
        padding: 2rem;
    }
    .login-title {
        color: #00BFFF;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .login-subtitle {
        color: #666;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Login UI
st.markdown("""
    <div class='login-header'>
        <h1 class='login-title'>🔐 Dumroo Admin Portal</h1>
        <p class='login-subtitle'>Login to access the admin panel</p>
    </div>
""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 👤 Admin Login")
        st.markdown("<br>", unsafe_allow_html=True)
        
        email = st.text_input("📧 Email", placeholder="admin@school.com")
        password = st.text_input("🔑 Password", type="password", placeholder="Enter password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Login", use_container_width=True, type="primary"):
            if email and password:
                success, role = verify_login(email, password)
                
                if success:
                    st.session_state.logged_in = True
                    st.session_state.admin_role = role
                    st.success("✅ Login successful!")
                    st.balloons()
                    st.info("🎯 Now run this command in a NEW terminal window:")
                    st.code("streamlit run app.py", language="bash")
                    st.warning("⚠️ Keep this window open and open app.py in a new terminal!")
                else:
                    st.error("❌ Invalid credentials. Please try again.")
            else:
                st.warning("⚠️ Please enter both email and password")
        
        st.markdown("---")
        
        with st.expander("📋 Demo Credentials (For Testing)"):
            st.markdown("""
            **Test Accounts:**
            
            **1. Mr. Rajesh Singh** (Grade 8, Class A, North)
            - Email: `rajesh@school.com`
            - Password: `admin123`
            
            **2. Ms. Lakshmi Reddy** (Grade 9, South)
            - Email: `lakshmi@school.com`
            - Password: `admin123`
            
            **3. Mr. Anil Patel** (Grade 8, North)
            - Email: `anil@school.com`
            - Password: `admin123`
            
            ---
            
            *Use any of these credentials to test the system*
            """)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem; margin-top: 3rem;'>
        <p>🔒 Secure authentication with role-based access control</p>
        <p>Built with Streamlit & Supabase</p>
        <p><em>Dumroo AI Query System v1.0</em></p>
    </div>
""", unsafe_allow_html=True)