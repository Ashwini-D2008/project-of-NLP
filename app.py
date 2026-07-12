import streamlit as st

# Page configuration
st.set_page_config(page_title="Course Recommendation System",page_icon="🎓",layout="wide")

# Header
st.title("🎓 NLP Course Recommendation System")
st.markdown("Find the best courses based on your skills and interests.")

# Hero section
st.markdown("""
---
### Enter Your Skills
Example: `python, machine learning, data science`
""")

# Input box
skills = st.text_input("Enter your skills",placeholder="python, machine learning, nlp")

# Recommend button
if st.button("🔍 Recommend Courses"):
    
    # Example recommendations
    recommended_courses = ["AI For Everyone","Machine Learning","Python for Everybody","Deep Learning Specialization","Data Science Specialization"]

    st.success("Recommended Courses")

    # Display as cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""**AI For Everyone**
        Organization: DeepLearning.AI
        
        Difficulty: Beginner
        """)

    with col2:
        st.info("""
        **Machine Learning**
        
        Organization: Stanford University
        
        Difficulty: Intermediate
        """)

    with col3:
        st.info("""
        **Python for Everybody**
        
        Organization: University of Michigan
        
        Difficulty: Beginner
        """)

    st.info("""
    **Deep Learning Specialization**
    
    Organization: DeepLearning.AI
    
    Difficulty: Intermediate
    """)

    st.info("""
    **Data Science Specialization**
    
    Organization: Johns Hopkins University
    
    Difficulty: Beginner
    """)