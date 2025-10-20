
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("Page 1: Introduction & Data")
    st.markdown("""
    This section prepares the environment by importing necessary libraries and generating synthetic datasets that will be used throughout the application. The datasets are designed to be lightweight and representative of the data structures described in the AI-Readiness Score paper.

    ### Synthetic Data Generation
    This section generates synthetic data for individual profiles, occupational opportunities, learning pathways and skill requirements. This data is designed to mimic real-world scenarios and provide a basis for calculating and visualizing the AI-Readiness Score. The synthetic data will ensure that the calculations can be tested even without access to real user data.
    """)

    st.subheader("Global Parameters")
    st.markdown("Adjust the global weighting parameters for the AI-Readiness Score calculation.")
    
    # Global Parameters
    st.session_state.alpha = st.slider(
        label="Weight on Individual Factors (\\alpha)",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.alpha,
        step=0.01,
        help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score."
    )
    st.session_state.beta = st.slider(
        label="Synergy Coefficient (\\beta)",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.beta,
        step=0.01,
        help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity."
    )

    st.subheader("Synthetic Dataframes")
    st.markdown("Explore the synthetic data used for the AI-Readiness Score calculations.")

    st.write("#### Individual Profiles Data (`individual_profiles_df`)")
    st.dataframe(st.session_state.individual_profiles_df)

    st.write("#### Occupational Data (`occupational_data_df`)")
    st.dataframe(st.session_state.occupational_data_df)

    st.write("#### Learning Pathways Data (`learning_pathways_df`)")
    st.dataframe(st.session_state.learning_pathways_df)

    st.write("#### Occupation Required Skills Data (`occupation_required_skills_df`)")
    st.dataframe(st.session_state.occupation_required_skills_df)

    st.write("#### Individual Skills Data (`individual_skills_df`)")
    st.dataframe(st.session_state.individual_skills_df)
