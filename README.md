# Dumroo AI Query System

> A natural language query interface for school admin panel with role-based access control and Supabase integration

## 🎯 Project Overview

This system allows school administrators to ask questions in plain English and get instant answers about students, homework, quizzes, and performance - all while ensuring they can only access data within their assigned scope. It features secure authentication, cloud database integration with Supabase, and comprehensive role-based access control.

## ✨ Key Features

- 🗣️ **Natural Language Queries** - Ask questions like you're talking to a colleague
- 🔒 **Role-Based Access Control** - Admins only see data they have permission to access
- 🔐 **Secure Authentication** - Streamlit-based login system with session management
- ☁️ **Cloud Database** - Integrated with Supabase for scalable data storage
- 📊 **Real-Time Data Analysis** - Instant results with clear visualizations
- 💾 **Export Capability** - Download query results as CSV
- 📱 **Responsive Design** - Works on desktop and tablets
- 🎨 **Clean UI** - Professional interface built with Streamlit
- 📜 **Query History** - Track all queries within your session
- ⚡ **Caching** - Optimized performance with intelligent data caching

---

## 🚀 Quick Start (10 Minutes)

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Supabase account (free at https://supabase.com)
- Git (optional, for cloning)

### Step 1: Setup Supabase

1. Create a free account at [Supabase](https://supabase.com)
2. Create a new project
3. Get your **Project URL** and **API Key** from the settings
4. Keep these credentials safe - you'll need them next

### Step 2: Setup Project

1. **Clone or Download this repository**
```bash
git clone https://github.com/Prathamkathare1/Admin_portal.git
cd dumroo-ai-query-system
```

2. **Open Terminal/Command Prompt and navigate to project folder**
```bash
cd dumroo-ai-query-system
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

### Step 3: Configure Credentials

1. **Create a `.env` file** in the project root (same folder as `main.py`):
```
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here
```

2. **Update `.streamlit/secrets.toml`** for Streamlit Cloud:
```toml
SUPABASE_URL = "your_supabase_url_here"
SUPABASE_KEY = "your_supabase_key_here"
```

### Step 4: Run the Application

```bash
streamlit run main.py
```

The app will automatically open at `http://localhost:8501`

**That's it! You're ready to go! 🎉**

---

## 📖 How to Use

### Step 1: Login

The application opens with a secure login page:
- **Email:** Enter your admin email
- **Password:** Enter your password
- **Note:** Demo credentials are available (see Credentials section below)

### Step 2: Select Your Admin Profile

After login, in the sidebar you'll see admin profile selection:
- **Mr. Rajesh Singh** - Grade 8, Class A, North
- **Ms. Lakshmi Reddy** - Grade 9, South (all classes)
- **Mr. Anil Patel** - Grade 8, North (all classes)

Your access scope is displayed showing exactly what data you can access.

### Step 3: Ask Questions

Type your question in plain English. Here are some examples:

#### Example Query 1: Homework Status
```
Which students haven't submitted their homework yet?
```
**Result:** List of students with pending homework submissions

#### Example Query 2: Performance Data
```
Show me performance data for Grade 8
```
**Result:** Quiz scores and performance metrics

#### Example Query 3: Low Performers
```
Who are the low-performing students?
```
**Result:** Students scoring below 70%

#### Example Query 4: Attendance
```
Show me attendance data
```
**Result:** Attendance rates for all accessible students

### Step 4: View & Export Results

- Results display in a clean, sortable table format
- **Download Results** - Click the CSV button to export
- **Query History** - View your last 5 queries in the expandable history section
- **Connection Status** - Real-time Supabase connection indicator in sidebar

---

## 🎓 Example Queries You Can Try

### Homework & Assignments
- "Which students haven't submitted their homework yet?"
- "Show me all students' homework status"
- "List students with pending assignments"

### Performance & Scores
- "Show me performance data for Grade 8"
- "Who are the low-performing students?"
- "Show me quiz scores for all students"
- "Display performance data"

### Attendance
- "Show me attendance data"
- "Who has low attendance?"
- "List attendance rates"

### General
- "List all students"
- "Show me all student information"
- "Display complete student list"

---

## 🔐 Security & Access Control

### Role-Based Access Control (RBAC)

Each admin can ONLY access data for:
- ✅ Their assigned grade
- ✅ Their assigned class(es)
- ✅ Their assigned region

**Example:**
- Mr. Singh (Grade 8, Class A, North) can see only Grade 8, Class A students in North
- Ms. Reddy (Grade 9, South) can see all Grade 9 students in South
- They CANNOT see each other's data

This ensures data privacy and security! 🔒

### Authentication

- Secure login with email/password verification
- Session-based authentication using Streamlit's session_state
- Automatic logout when closing the app
- No credentials stored in code - all stored in `.env` or Streamlit Secrets

### Data Validation

- All database queries are validated
- Credentials must be present before app runs
- Error messages guide users if setup is incomplete
- Fallback to CSV files if database connection fails

---

## 📁 Project Structure

```
dumroo-ai-query-system/
│
├── main.py                    # Main application file (production)
├── app.py                     # Alternative app file
├── login.py                   # Standalone login module
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
├── .gitignore                 # Git ignore rules
├── .env                       # Environment variables (NOT in git)
│
├── .streamlit/
│   └── secrets.toml           # Streamlit Cloud secrets (NOT in git)
│
└── Data/
    ├── students.csv           # Student data (backup)
    └── quizzes.csv            # Quiz schedule data (backup)
```

---

## 💾 Data Structure

### Student Data (Supabase Table: `students`)

Required columns:
- `name` (TEXT) - Student name
- `grade` (INTEGER) - Grade/Year
- `class` (TEXT) - Class section
- `region` (TEXT) - Geographic region
- `homework_status` (TEXT) - 'submitted' or 'pending'
- `quiz_score` (FLOAT) - Latest quiz score (0-100)
- `quiz_name` (TEXT) - Name of quiz taken
- `attendance_rate` (FLOAT) - Attendance percentage (0-100)

### Quiz Data (Supabase Table: `quizzes`)

Required columns:
- `quiz_name` (TEXT) - Name of the quiz
- `grade` (INTEGER) - Grade level
- `class` (TEXT) - Class section
- `region` (TEXT) - Region
- `subject` (TEXT) - Subject name
- `scheduled_date` (DATE) - When quiz is scheduled
- `total_marks` (FLOAT) - Maximum marks

---

## 🛠️ Environment Setup

### Local Development (.env file)

Create `.env` file with:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Streamlit Cloud Deployment

Add secrets in Streamlit Cloud dashboard:
1. Go to your app on [Streamlit Cloud](https://share.streamlit.io)
2. Click **"Manage app"** → **"Settings"** → **"Secrets"**
3. Add the same variables from your `.env` file

### Environment Variables

| Variable | Required | Example |
|----------|----------|---------|
| `SUPABASE_URL` | Yes | `https://fpbtcjhaozpkkrtbvpjk.supabase.co` |
| `SUPABASE_KEY` | Yes | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |

---

## 🔧 Customization

### Adding Your Own Data

#### Option 1: Use Supabase Cloud Database
1. Create tables with the same schema as above
2. Import your CSV files to Supabase
3. App will automatically pull from cloud

#### Option 2: Use Local CSV Files
1. Edit CSV files in `data/` folder
2. Keep the same column names
3. App falls back to CSV if database isn't available

### Modifying Access Control Rules

Edit the `ADMIN_ROLES` dictionary in `main.py`:

```python
ADMIN_ROLES = {
    'admin1': {
        'name': 'Your Name',
        'grade': 8,
        'class': 'A',
        'region': 'North',
        'description': 'Your description'
    },
    # Add more roles here
}
```

### Extending Query Processing

Add more keywords to `process_natural_language_query()` function:

```python
elif any(keyword in query for keyword in ['your_keyword']):
    # Your custom processing logic
    response['success'] = True
    response['data'] = filtered_data
    response['message'] = "Your custom message"
```

---

## 🔐 Demo Credentials

### Test Accounts

| Name | Email | Password | Grade | Class | Region |
|------|-------|----------|-------|-------|--------|
| Mr. Rajesh Singh | rajesh@school.com | admin123 | 8 | A | North |
| Ms. Lakshmi Reddy | lakshmi@school.com | admin123 | 9 | All | South |
| Mr. Anil Patel | anil@school.com | admin123 | 8 | All | North |

**⚠️ Important:** Change these credentials in production!

---

## 📊 Testing the System

### Test Case 1: Role-Based Filtering
1. Login as Mr. Rajesh Singh
2. Query: "List all students"
3. **Expected:** Only Grade 8, Class A, North students
4. Logout and login as Ms. Lakshmi Reddy
5. Same query
6. **Expected:** Only Grade 9, South students (completely different results!)

### Test Case 2: Homework Tracking
1. Query: "Which students haven't submitted homework?"
2. **Expected:** List of students with "pending" status
3. Verify they're all within your admin scope
4. Compare results when logged in as different admin

### Test Case 3: Performance Analysis
1. Query: "Who are the low-performing students?"
2. **Expected:** Students with quiz scores below 70%
3. Verify results match your access scope

### Test Case 4: CSV Export
1. Run any query
2. Click "📥 Download Results as CSV"
3. **Expected:** CSV file downloads to your computer

---

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free!)

1. Push your code to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. Go to [Streamlit Cloud](https://share.streamlit.io)

3. Click "New app"

4. Select your GitHub repo and `main.py`

5. Add secrets in Settings:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`

6. Your app is now live!

### Deploy to Other Platforms

#### Docker Deployment
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "main.py"]
```

Build and run:
```bash
docker build -t dumroo-admin .
docker run -p 8501:8501 dumroo-admin
```

---

## 🐛 Troubleshooting

### Issue: "Supabase credentials not found"

**Solution:**
1. Check `.env` file exists in project root
2. Verify `SUPABASE_URL` and `SUPABASE_KEY` are set
3. For Streamlit Cloud: add secrets in dashboard settings
4. Restart the application

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 8501 is already in use"

**Solution:**
```bash
streamlit run main.py --server.port 8502
```

### Issue: Data not loading from Supabase

**Solution:**
1. Verify Supabase connection status indicator (sidebar)
2. Check your internet connection
3. Verify API key is correct
4. Ensure tables exist in Supabase
5. Check Supabase dashboard for any errors
6. App will fallback to CSV files if database unavailable

### Issue: Login always fails

**Solution:**
1. Verify you're using correct email from ADMIN_ROLES
2. Check password matches (default: `admin123`)
3. Check for spaces or typos in credentials
4. Try different admin account

### Issue: "Connection refused" error

**Solution:**
1. Check internet connection
2. Verify Supabase project is active
3. Ensure API key hasn't been revoked
4. Try restarting the app
5. Check Supabase status at status.supabase.com

---

## 📈 Performance Tips

### Optimize Database Queries

```python
# Good - Caches for 60 seconds
@st.cache_data(ttl=60)
def load_student_data():
    return supabase.table('students').select("*").execute()

# Less efficient - No caching
def load_student_data_uncached():
    return supabase.table('students').select("*").execute()
```

### Use Specific Columns

```python
# Good - Only load needed columns
supabase.table('students').select("name,grade,class").execute()

# Less efficient - Load everything
supabase.table('students').select("*").execute()
```

### Pagination for Large Datasets

```python
# For 1000+ records
response = supabase.table('students').select("*").range(0, 100).execute()
```

---

## 🚀 Future Enhancements

### Bonus Features (Optional)
- 🤖 AI-powered queries using LangChain/OpenAI
- 📈 Data visualizations (charts and graphs)
- 📧 Email notifications for pending tasks
- 📱 Mobile app version
- 🗣️ Voice input capability
- 🌐 Multi-language support

### Advanced Features
- Real-time analytics dashboard
- Advanced data export (Excel, PDF)
- Bulk operations and updates
- Parent portal integration
- SMS notifications
- Detailed audit logs
- Custom report generation

---

## 🛡️ Security Best Practices

1. **Never commit `.env` file** - It's in `.gitignore` for a reason
2. **Rotate API keys regularly** - Change Supabase keys quarterly
3. **Use strong passwords** - In production, use proper authentication
4. **Enable RLS on Supabase** - Row Level Security for database tables
5. **Audit logs** - Track all admin activities
6. **HTTPS only** - Ensure all connections are encrypted
7. **Validate input** - Sanitize all user inputs

---

## 📝 Technical Details

### Tech Stack
- **Python 3.8+** - Programming language
- **Streamlit** - Web interface framework
- **Pandas** - Data manipulation and analysis
- **Supabase** - Cloud database & authentication
- **python-dotenv** - Environment variable management

### Code Quality
- ✅ Clean, readable code with comments
- ✅ Modular function design
- ✅ Comprehensive error handling
- ✅ Type hints where appropriate
- ✅ Follows Python best practices (PEP 8)
- ✅ Efficient data caching

### Requirements File

```
streamlit>=1.29.0
pandas>=2.0.0
python-dotenv>=1.0.0
supabase>=2.0.0
```

---

## 📊 Project Statistics

- **Total Lines of Code:** ~500+
- **Main File:** main.py (~490 lines)
- **Supporting Files:** app.py, login.py
- **Documentation:** Comprehensive README
- **Test Coverage:** Manual testing with 3 roles × 6 query types
- **Query Types Supported:** 6+ types (homework, performance, attendance, quizzes, student list, general)

---

## ✅ Assignment Compliance

### Core Requirements
- ✅ Natural language querying in plain English
- ✅ Structured data source (Supabase cloud + CSV fallback)
- ✅ Role-based access control (3 admin roles)
- ✅ Data filtering based on admin scope
- ✅ Clean, working, well-commented code

### Bonus Features Implemented
- ✅ Secure authentication system
- ✅ Interactive Streamlit interface
- ✅ Multiple example queries
- ✅ Query history tracking
- ✅ Modular code structure
- ✅ CSV export functionality
- ✅ Cloud database integration
- ✅ Error handling & validation
- ✅ Professional documentation

### Deliverables
- ✅ GitHub repository ready
- ✅ Complete README documentation
- ✅ 6+ documented example queries
- ✅ Clean, well-commented code
- ✅ Environment configuration ready
- ✅ Deployment instructions included

---

## 📄 License

This project is created for educational purposes as part of the Dumroo.ai assignment.

---

## 🙋‍♂️ Support

If you encounter any issues:

1. **Check Troubleshooting Section** - Most issues are covered above
2. **Verify Setup** - Ensure all steps were followed correctly
3. **Check Logs** - Look at terminal output for error messages
4. **Supabase Docs** - Visit https://supabase.com/docs for database help
5. **Streamlit Docs** - Visit https://docs.streamlit.io for framework help

---

## 📞 Contact & Information

**Project:** Dumroo AI Query System  
**Repository:** https://github.com/Prathamkathare1/Admin_portal  
**Version:** 1.0  
**Date:** December 2024  
**Purpose:** Educational Assignment

---

## 🎉 Ready to Get Started?

```bash
# Navigate to project folder
cd dumroo-ai-query-system

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "SUPABASE_URL=your_url" > .env
echo "SUPABASE_KEY=your_key" >> .env

# Run the application
streamlit run main.py
```

**Visit:** `http://localhost:8501`

**Login with demo credentials and start querying! 🚀**

---

## 🎓 Learning Outcomes

By using this system, you'll learn:
- ✅ Natural language processing basics
- ✅ Role-based security implementation
- ✅ Cloud database integration
- ✅ Streamlit web development
- ✅ Python data manipulation
- ✅ Session management
- ✅ Error handling & validation
- ✅ Professional code architecture

---

**Built with ❤️ for education and learning**
