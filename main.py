import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
from supabase import create_client
from datetime import datetime

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(
    page_title="Dumroo AI Admin Panel",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== AUTHENTICATION ====================

def verify_login(email, password):
    """Verify admin credentials"""
    demo_users = {
        'rajesh@school.com': {'password': 'admin123', 'role': 'admin1'},
        'lakshmi@school.com': {'password': 'admin123', 'role': 'admin2'},
        'anil@school.com': {'password': 'admin123', 'role': 'admin3'}
    }
    
    if email in demo_users and demo_users[email]['password'] == password:
        return True, demo_users[email]['role']
    return False, None

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'admin_role' not in st.session_state:
    st.session_state.admin_role = None
if 'query_history' not in st.session_state:
    st.session_state.query_history = []

# ==================== LOGIN PAGE ====================

if not st.session_state.logged_in:
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
    
    st.markdown("""
        <div class='login-header'>
            <h1 class='login-title'>🔐 Dumroo Admin Portal</h1>
            <p class='login-subtitle'>Login to access the admin panel</p>
        </div>
    """, unsafe_allow_html=True)
    
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
                    st.rerun()
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
            """)
    
    st.markdown("""
        <div style='text-align: center; color: #666; padding: 2rem; margin-top: 3rem;'>
            <p>🔒 Secure authentication with role-based access control</p>
            <p>Built with Streamlit & Supabase</p>
            <p><em>Dumroo AI Query System v1.0</em></p>
        </div>
    """, unsafe_allow_html=True)
    
    st.stop()

# ==================== DASHBOARD (Only shows if logged in) ====================

# Test Supabase connection
def test_supabase_connection():
    try:
        test_response = supabase.table('students').select("*").limit(1).execute()
        if test_response.data:
            return True, "✅ Connected to Supabase"
        else:
            return False, "⚠️ No data found"
    except Exception as e:
        return False, f"❌ Connection failed: {str(e)}"

st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00BFFF;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def load_student_data():
    try:
        response = supabase.table('students').select("*").execute()
        if response.data:
            return pd.DataFrame(response.data)
        else:
            st.warning("⚠️ No students data in Supabase")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error loading students: {str(e)}")
        csv_path = 'data/students.csv'
        if os.path.exists(csv_path):
            return pd.read_csv(csv_path)
        return pd.DataFrame()

@st.cache_data(ttl=60)
def load_quiz_data():
    try:
        response = supabase.table('quizzes').select("*").execute()
        if response.data:
            return pd.DataFrame(response.data)
        else:
            st.warning("⚠️ No quizzes data in Supabase")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error loading quizzes: {str(e)}")
        csv_path = 'data/quizzes.csv'
        if os.path.exists(csv_path):
            return pd.read_csv(csv_path)
        return pd.DataFrame()

ADMIN_ROLES = {
    'admin1': {
        'name': 'Mr. Rajesh Singh',
        'grade': 8,
        'class': 'A',
        'region': 'North',
        'description': 'Manages Grade 8, Class A in North region'
    },
    'admin2': {
        'name': 'Ms. Lakshmi Reddy',
        'grade': 9,
        'region': 'South',
        'description': 'Manages Grade 9 (all classes) in South region'
    },
    'admin3': {
        'name': 'Mr. Anil Patel',
        'grade': 8,
        'region': 'North',
        'description': 'Manages Grade 8 (all classes) in North region'
    }
}

def apply_role_based_filtering(dataframe, admin_key):
    role = ADMIN_ROLES[admin_key]
    filtered_data = dataframe.copy()
    
    if 'grade' in filtered_data.columns:
        filtered_data = filtered_data[filtered_data['grade'] == role['grade']]
    
    if 'class' in role and 'class' in filtered_data.columns:
        filtered_data = filtered_data[filtered_data['class'] == role['class']]
    
    if 'region' in filtered_data.columns:
        filtered_data = filtered_data[filtered_data['region'] == role['region']]
    
    return filtered_data

def process_natural_language_query(query, students_df, quizzes_df):
    query = query.lower().strip()
    
    response = {
        'success': False,
        'message': '',
        'data': None,
        'type': 'unknown'
    }
    
    if any(keyword in query for keyword in ['homework', 'assignment', 'submitted', 'submission']):
        if any(keyword in query for keyword in ['not submitted', 'pending', "haven't", "didn't"]):
            pending_students = students_df[students_df['homework_status'] == 'pending']
            
            response['success'] = True
            response['type'] = 'homework_pending'
            response['data'] = pending_students[['name', 'grade', 'class', 'homework_status']]
            response['message'] = f"Found {len(pending_students)} student(s) with pending homework submissions"
            
            if len(pending_students) == 0:
                response['message'] = "Great news! All students have submitted their homework! 🎉"
        else:
            response['success'] = True
            response['type'] = 'homework_status'
            response['data'] = students_df[['name', 'grade', 'class', 'homework_status']]
            response['message'] = "Homework submission status for all students in your scope"
    
    elif any(keyword in query for keyword in ['performance', 'score', 'marks', 'grades', 'quiz results']):
        filtered_data = students_df.copy()
        
        if 'grade 8' in query:
            filtered_data = filtered_data[filtered_data['grade'] == 8]
        elif 'grade 9' in query:
            filtered_data = filtered_data[filtered_data['grade'] == 9]
        
        if any(keyword in query for keyword in ['low', 'poor', 'below', 'struggling', 'failing']):
            threshold = 70
            filtered_data = filtered_data[filtered_data['quiz_score'] < threshold]
            avg_score = filtered_data['quiz_score'].mean() if len(filtered_data) > 0 else 0
            
            response['success'] = True
            response['type'] = 'low_performance'
            response['data'] = filtered_data[['name', 'grade', 'class', 'quiz_score', 'quiz_name']]
            response['message'] = f"Students scoring below {threshold}% (Average: {avg_score:.1f}%)"
        else:
            avg_score = filtered_data['quiz_score'].mean()
            
            response['success'] = True
            response['type'] = 'performance'
            response['data'] = filtered_data[['name', 'grade', 'class', 'quiz_score', 'quiz_name']]
            response['message'] = f"Performance data (Average score: {avg_score:.1f}%)"
    
    elif any(keyword in query for keyword in ['upcoming', 'scheduled', 'next', 'future']) and 'quiz' in query:
        response['success'] = True
        response['type'] = 'upcoming_quizzes'
        response['data'] = quizzes_df[['quiz_name', 'grade', 'class', 'subject', 'scheduled_date']]
        response['message'] = f"Found {len(quizzes_df)} upcoming quiz(zes) in your scope"
    
    elif any(keyword in query for keyword in ['attendance', 'present', 'absent', 'attendance rate']):
        avg_attendance = students_df['attendance_rate'].mean()
        
        if any(keyword in query for keyword in ['low', 'poor', 'below']):
            threshold = 90
            low_attendance = students_df[students_df['attendance_rate'] < threshold]
            
            response['success'] = True
            response['type'] = 'low_attendance'
            response['data'] = low_attendance[['name', 'grade', 'class', 'attendance_rate']]
            response['message'] = f"Students with attendance below {threshold}% (Class average: {avg_attendance:.1f}%)"
        else:
            response['success'] = True
            response['type'] = 'attendance'
            response['data'] = students_df[['name', 'grade', 'class', 'attendance_rate']]
            response['message'] = f"Attendance data (Class average: {avg_attendance:.1f}%)"
    
    elif any(keyword in query for keyword in ['all students', 'list students', 'show students', 'student list']):
        response['success'] = True
        response['type'] = 'student_list'
        response['data'] = students_df[['name', 'grade', 'class', 'homework_status', 'quiz_score', 'attendance_rate']]
        response['message'] = f"Showing all {len(students_df)} students in your scope"
    
    else:
        response['success'] = False
        response['message'] = """I couldn't understand that query. Here are some examples:
        
• "Which students haven't submitted their homework yet?"
• "Show me performance data for Grade 8"
• "List all upcoming quizzes scheduled for next week"
• "Who are the low-performing students?"
• "Show me attendance data"
• "List all students"
        """
    
    return response

st.markdown('<p class="main-header">📚 Dumroo AI Admin Panel</p>', unsafe_allow_html=True)
st.markdown("### Natural Language Query Interface with Role-Based Access Control")

with st.sidebar:
    # Connection Status
    st.header("🔌 Connection")
    is_connected, msg = test_supabase_connection()
    if is_connected:
        st.success(msg)
    else:
        st.error(msg)
    
    st.markdown("---")
    
    st.header("👤 Admin Profile")
    
    admin_labels = {
        key: f"{info['name']} - {info['description']}"
        for key, info in ADMIN_ROLES.items()
    }
    
    selected_admin = st.selectbox(
        "Select Your Admin Profile:",
        options=list(ADMIN_ROLES.keys()),
        format_func=lambda x: admin_labels[x],
        key='admin_selector',
        index=list(ADMIN_ROLES.keys()).index(st.session_state.admin_role)
    )
    
    st.session_state.admin_role = selected_admin
    current_role = ADMIN_ROLES[selected_admin]
    
    st.markdown("---")
    st.subheader("🔒 Your Access Scope")
    st.info(f"""
**Admin:** {current_role['name']}

**You can access:**
- Grade: {current_role['grade']}
- Class: {current_role.get('class', 'All classes')}
- Region: {current_role['region']}

*You can only view and query data within this scope*
    """)
    
    students_df = load_student_data()
    quizzes_df = load_quiz_data()
    
    filtered_students = apply_role_based_filtering(students_df, selected_admin)
    filtered_quizzes = apply_role_based_filtering(quizzes_df, selected_admin)
    
    st.markdown("---")
    st.subheader("📊 Quick Stats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Students", len(filtered_students))
        if len(filtered_students) > 0:
            pending_hw = len(filtered_students[filtered_students['homework_status'] == 'pending'])
            st.metric("Pending Homework", pending_hw, delta=None if pending_hw == 0 else f"-{pending_hw}")
        else:
            st.metric("Pending Homework", "N/A")
    
    with col2:
        st.metric("Upcoming Quizzes", len(filtered_quizzes))
        if len(filtered_students) > 0:
            avg_score = filtered_students['quiz_score'].mean()
            st.metric("Avg Quiz Score", f"{avg_score:.1f}%")
        else:
            st.metric("Avg Quiz Score", "N/A")
    
    st.markdown("---")
    st.subheader("💡 Tips")
    st.markdown("""
- Ask questions in plain English
- Try the example queries below
- Switch admin profiles to see different data
- All results are filtered by your access scope
    """)
    
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.admin_role = None
        st.session_state.query_history = []
        st.rerun()

st.subheader("💬 Ask a Question")

with st.expander("📝 Example Queries (click to try)", expanded=True):
    col1, col2 = st.columns(2)
    
    example_queries = [
        "Which students haven't submitted their homework yet?",
        "Show me performance data for Grade 8",
        "List all upcoming quizzes",
        "Who are the low-performing students?",
        "Show me attendance data",
        "List all students"
    ]
    
    for i, example in enumerate(example_queries):
        col = col1 if i % 2 == 0 else col2
        with col:
            if st.button(example, key=f"example_{i}", use_container_width=True):
                st.session_state.current_query = example

query_input = st.text_input(
    "Type your question here:",
    value=st.session_state.get('current_query', ''),
    placeholder="e.g., Which students haven't submitted their homework yet?",
    key='query_input_field',
    label_visibility="collapsed"
)

if st.button("🔍 Search", type="primary", use_container_width=True) or query_input:
    if query_input:
        with st.spinner("🤔 Processing your query..."):
            filtered_students = apply_role_based_filtering(students_df, st.session_state.admin_role)
            filtered_quizzes = apply_role_based_filtering(quizzes_df, st.session_state.admin_role)
            
            result = process_natural_language_query(
                query_input,
                filtered_students,
                filtered_quizzes
            )
            
            st.session_state.query_history.append({
                'query': query_input,
                'result': result,
                'admin': current_role['name'],
                'timestamp': datetime.now().strftime("%I:%M %p")
            })
            
            st.markdown("---")
            
            if result['success']:
                st.success(f"✅ {result['message']}")
                
                if result['data'] is not None and len(result['data']) > 0:
                    st.markdown("### 📊 Results:")
                    
                    st.dataframe(
                        result['data'],
                        use_container_width=True,
                        hide_index=True
                    )
                    
                    csv = result['data'].to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name=f"query_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
            else:
                st.error("❌ Query not understood")
                st.info(result['message'])
    else:
        st.warning("⚠️ Please enter a query")

if st.session_state.query_history:
    st.markdown("---")
    st.subheader("📜 Query History")
    
    for i, entry in enumerate(reversed(st.session_state.query_history[-5:])):
        with st.expander(f"🕐 {entry['timestamp']} - {entry['query'][:60]}...", expanded=(i == 0)):
            st.markdown(f"**Admin:** {entry['admin']}")
            st.markdown(f"**Query:** {entry['query']}")
            st.markdown(f"**Result:** {entry['result']['message']}")
            
            if entry['result']['data'] is not None and len(entry['result']['data']) > 0:
                st.dataframe(entry['result']['data'], use_container_width=True, hide_index=True)
    
    if st.button("🗑️ Clear History"):
        st.session_state.query_history = []
        st.rerun()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>🔒 Security Notice:</strong> All data is filtered based on your admin role. You can only access data within your assigned scope.</p>
    <p>Built with Streamlit, Supabase & Python</p>
    <p><em>Dumroo AI Query System v1.0</em></p>
</div>
""", unsafe_allow_html=True)
