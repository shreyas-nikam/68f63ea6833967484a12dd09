
import streamlit as st
import pandas as pd
import plotly.express as px
from application_pages.utils import generate_synthetic_data

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.markdown("""
### AI Career Navigator & Pathway Planner

This application explores the AI-Readiness Score (AI-R) framework, a parametric model designed to quantify an individual's preparedness for AI-enabled careers. The AI-R score helps in navigating career transitions by considering both individual capabilities and market opportunities.

### Learning Goals
- Understand the key insights contained in the uploaded document and supporting data.
- Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.
- Evaluate the potential impact of various learning pathways on individual skill development and career readiness.
- Analyze different career paths based on market demand and personal capabilities through "what-if" scenarios.

The core formula for the AI-Readiness Score for an individual $i$ at time $t$ is defined as:
""")
st.latex(r""" AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) """)
st.markdown("""
Where:
-   $V^R(t)$ is the Idiosyncratic Readiness (individual capability).
-   $H^R(t)$ is the Systematic Opportunity (market demand).
-   $\alpha \in [0,1]$ is the weight on individual vs. market factors.
-   $\beta > 0$ is the Synergy coefficient.
-   Both $V^R$ and $H^R$ are normalized to $[0, 100]$.
-   $\text{Synergy}\%$ is also normalized to $[0, 100]$ percentage units.

This framework allows for dynamic "what-if" scenario planning, enabling users to understand how different learning pathways and career transitions impact their future career prospects.
""")


# Initialize session state for data and parameters
if "individual_profiles_df" not in st.session_state:
    st.session_state.individual_profiles_df, st.session_state.occupational_data_df, \
    st.session_state.learning_pathways_df, st.session_state.occupation_required_skills_df, \
    st.session_state.individual_skills_df = generate_synthetic_data()


# Initialize global parameters if not already in session_state
if 'alpha' not in st.session_state:
    st.session_state.alpha = 0.6
if 'beta' not in st.session_state:
    st.session_state.beta = 0.15


page = st.sidebar.selectbox(label="Navigation", options=["Page 1: Introduction & Data", "Page 2: Idiosyncratic Readiness (V^R)", "Page 3: Systematic Opportunity (H^R) & Simulation"])

if page == "Page 1: Introduction & Data":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2: Idiosyncratic Readiness (V^R)":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3: Systematic Opportunity (H^R) & Simulation":
    from application_pages.page3 import run_page3
    run_page3()
