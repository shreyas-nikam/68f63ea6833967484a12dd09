
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from application_pages.utils import (
    calculate_ai_enhancement_potential,
    calculate_job_growth_projection,
    calculate_wage_premium,
    calculate_entry_accessibility,
    calculate_base_opportunity_score,
    calculate_growth_multiplier,
    calculate_regional_multiplier,
    calculate_systematic_opportunity,
    calculate_skills_match_score,
    calculate_timing_factor,
    calculate_alignment_factor,
    calculate_synergy_percentage,
    calculate_ai_readiness_score,
    simulate_pathway_impact,
    calculate_idiosyncratic_readiness,
    calculate_ai_fluency,
    calculate_domain_expertise,
    calculate_adaptive_capacity,
    calculate_technical_ai_skills,
    calculate_ai_augmented_productivity,
    calculate_critical_ai_judgment,
    calculate_ai_learning_velocity,
    calculate_education_foundation,
    calculate_practical_experience,
    calculate_specialization_depth
)

def run_page3():
    st.header("Page 3: Systematic Opportunity (H^R) & Pathway Simulation")
    st.markdown("""
    This section focuses on **Systematic Opportunity ($H^R$)**, which quantifies market demand for your skills, and allows you to **simulate the impact of learning pathways** on your overall AI-Readiness Score.

    ### Systematic Opportunity ($H^R$)
    $H^R$ is a measure of external market factors, including job growth, wage premiums, and entry accessibility for specific occupations. It is influenced by base opportunity and market multipliers.
    """)

    # Initialize session state for occupation selection and HR inputs
    if "selected_occupation" not in st.session_state:
        st.session_state.selected_occupation = st.session_state.occupational_data_df['occupation_name'].iloc[0]
    if "lambda_val" not in st.session_state:
        st.session_state.lambda_val = 0.3
    if "gamma_val" not in st.session_state:
        st.session_state.gamma_val = 0.2
    if "max_possible_skills_match" not in st.session_state:
        st.session_state.max_possible_skills_match = 100
    if "individual_skills_for_synergy" not in st.session_state:
        st.session_state.individual_skills_for_synergy = st.session_state.individual_skills_df.copy()

    st.subheader("Systematic Opportunity ($H^R$) Inputs")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.selected_occupation = st.selectbox(
            "Target Occupation",
            options=st.session_state.occupational_data_df['occupation_name'].tolist(),
            index=st.session_state.occupational_data_df['occupation_name'].tolist().index(st.session_state.selected_occupation),
            help="Select a target occupation to calculate your market opportunity ($H^R$) based on its attributes."
        )
    with col2:
        st.session_state.lambda_val = st.slider(
            "Lambda value for Growth Multiplier (\\lambda)",
            min_value=0.0,
            max_value=1.0,
            value=st.session_state.lambda_val,
            step=0.01,
            help="Adjust $\lambda$ to dampen volatility in job posting growth."
        )
        st.session_state.gamma_val = st.slider(
            "Gamma value for Regional Multiplier (\\gamma)",
            min_value=0.0,
            max_value=1.0,
            value=st.session_state.gamma_val,
            step=0.01,
            help="Adjust $\gamma$ for regional market influence."
        )

    st.subheader("Synergy Inputs")
    st.markdown("Synergy measures the alignment between your individual skills and market demands.")

    required_skills_for_selected_occupation = st.session_state.occupation_required_skills_df[
        st.session_state.occupation_required_skills_df['occupation_name'] == st.session_state.selected_occupation
    ].copy()

    st.markdown("#### Required Skills for Selected Occupation")
    st.dataframe(required_skills_for_selected_occupation)

    st.markdown("#### Your Individual Skills")
    edited_individual_skills = st.data_editor(
        st.session_state.individual_skills_for_synergy,
        num_rows="dynamic",
        key="individual_skills_editor"
    )
    st.session_state.individual_skills_for_synergy = edited_individual_skills

    st.session_state.max_possible_skills_match = st.number_input(
        "Max Possible Skills Match",
        min_value=1,
        max_value=200,
        value=st.session_state.max_possible_skills_match,
        help="The maximum possible score for skills matching (e.g., 100 for a perfect match of 100%)."
    )

    if st.button("Calculate AI-Readiness Score (H^R and Synergy)"):
        # Ensure V^R is calculated first if not present
        if "vr_score" not in st.session_state:
            st.warning("Please calculate Idiosyncratic Readiness (V^R) on Page 2 first.")
        else:
            current_occupation_data = st.session_state.occupational_data_df[
                st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation
            ].iloc[0]

            # Calculate H^R components
            ai_enhancement_potential = calculate_ai_enhancement_potential(current_occupation_data['ai_enhancement_score'])
            job_growth_projection = calculate_job_growth_projection(current_occupation_data['job_growth_rate_g'])
            wage_premium = calculate_wage_premium(current_occupation_data['ai_skilled_wage'], current_occupation_data['median_wage'])
            entry_accessibility = calculate_entry_accessibility(current_occupation_data['education_years_required'], current_occupation_data['experience_years_required'])
            base_opportunity_score = calculate_base_opportunity_score(ai_enhancement_potential, job_growth_projection, wage_premium, entry_accessibility)
            growth_multiplier = calculate_growth_multiplier(current_occupation_data['current_job_postings'], current_occupation_data['previous_job_postings'], st.session_state.lambda_val)
            regional_multiplier = calculate_regional_multiplier(current_occupation_data['local_demand'], current_occupation_data['national_avg_demand'], current_occupation_data['remote_work_factor'], st.session_state.gamma_val)
            hr_score = calculate_systematic_opportunity(base_opportunity_score, growth_multiplier, regional_multiplier) * 100 # Normalize to 0-100

            # Calculate Synergy components
            skills_match_score = calculate_skills_match_score(st.session_state.individual_skills_for_synergy, required_skills_for_selected_occupation)
            timing_factor = calculate_timing_factor(st.session_state.individual_profile['years_experience'])
            alignment_factor = calculate_alignment_factor(skills_match_score, st.session_state.max_possible_skills_match, timing_factor)
            synergy_percentage = calculate_synergy_percentage(st.session_state.vr_score, hr_score, alignment_factor)

            # Calculate Final AI-R Score
            ai_r_score = calculate_ai_readiness_score(st.session_state.vr_score, hr_score, synergy_percentage, st.session_state.alpha, st.session_state.beta)

            st.session_state.hr_score = hr_score
            st.session_state.skills_match_score = skills_match_score
            st.session_state.timing_factor = timing_factor
            st.session_state.alignment_factor = alignment_factor
            st.session_state.synergy_percentage = synergy_percentage
            st.session_state.ai_r_score = ai_r_score

            st.success(f"AI-Readiness Score Calculated! Your AI-R Score: {ai_r_score:.2f}")

    if "ai_r_score" in st.session_state:
        st.subheader("Calculated AI-Readiness Score")
        col_score1, col_score2, col_score3, col_score4 = st.columns(4)
        with col_score1:
            st.metric(label="V^R Score", value=f"{st.session_state.vr_score:.2f}")
        with col_score2:
            st.metric(label="H^R Score", value=f"{st.session_state.hr_score:.2f}")
        with col_score3:
            st.metric(label="Synergy%", value=f"{st.session_state.synergy_percentage:.2f}")
        with col_score4:
            st.metric(label="AI-R Score", value=f"{st.session_state.ai_r_score:.2f}")

        st.markdown("#### H^R Components Breakdown")
        hr_components_data = {
            "Component": ["AI-Enhancement Potential", "Job Growth Projection", "Wage Premium", "Entry Accessibility"],
            "Score": [calculate_ai_enhancement_potential(st.session_state.occupational_data_df[st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation].iloc[0]['ai_enhancement_score']) * 100,
                      calculate_job_growth_projection(st.session_state.occupational_data_df[st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation].iloc[0]['job_growth_rate_g']),
                      calculate_wage_premium(st.session_state.occupational_data_df[st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation].iloc[0]['ai_skilled_wage'], st.session_state.occupational_data_df[st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation].iloc[0]['median_wage']) * 100,
                      calculate_entry_accessibility(st.session_state.occupational_data_df[st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation].iloc[0]['education_years_required'], st.session_state.occupational_data_df[st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation].iloc[0]['experience_years_required']) * 100
                     ]
        }
        hr_components_df = pd.DataFrame(hr_components_data)
        fig_hr = px.bar(hr_components_df, x="Component", y="Score", title="H^R Base Components",
                        labels={"Score": "Score (0-100%)"},
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_hr)

        st.markdown("#### Overall AI-Readiness Score Contribution")
        overall_scores_data = {
            "Component": ["V^R", "H^R", "Synergy%"],
            "Score": [st.session_state.alpha * st.session_state.vr_score,
                      (1 - st.session_state.alpha) * st.session_state.hr_score,
                      st.session_state.beta * st.session_state.synergy_percentage]
        }
        overall_scores_df = pd.DataFrame(overall_scores_data)
        fig_overall = px.pie(overall_scores_df, names="Component", values="Score", title="Overall AI-R Score Contribution",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_overall)

    st.subheader("Pathway Simulation")
    st.markdown("""
    Simulate the impact of different learning pathways on your AI-Readiness Score. Choose a pathway and adjust completion and mastery levels to see projected changes.
    """)

    if "selected_pathway" not in st.session_state:
        st.session_state.selected_pathway = st.session_state.learning_pathways_df['pathway_name'].iloc[0]
    if "pathway_completion_score" not in st.session_state:
        st.session_state.pathway_completion_score = 1.0
    if "pathway_mastery_score" not in st.session_state:
        st.session_state.pathway_mastery_score = 1.0

    st.session_state.selected_pathway = st.selectbox(
        "Select Learning Pathway",
        options=st.session_state.learning_pathways_df['pathway_name'].tolist(),
        index=st.session_state.learning_pathways_df['pathway_name'].tolist().index(st.session_state.selected_pathway),
        help="Simulate the impact of completing a learning pathway with a certain completion and mastery level."
    )
    st.session_state.pathway_completion_score = st.slider(
        "Pathway Completion Score", 0.0, 1.0, st.session_state.pathway_completion_score, 0.05,
        help="Your level of completion for the selected pathway. (Scale: 0.0 - 1.0)"
    )
    st.session_state.pathway_mastery_score = st.slider(
        "Pathway Mastery Score", 0.0, 1.0, st.session_state.pathway_mastery_score, 0.05,
        help="Your level of mastery achieved in the selected pathway. (Scale: 0.0 - 1.0)"
    )

    if st.button("Simulate Pathway Impact"):
        if "vr_score" not in st.session_state or "hr_score" not in st.session_state:
            st.warning("Please calculate the initial AI-Readiness Score first.")
        else:
            selected_pathway_data = st.session_state.learning_pathways_df[
                st.session_state.learning_pathways_df['pathway_name'] == st.session_state.selected_pathway
            ].iloc[0]

            # Recalculate AI-Fluency, Domain-Expertise, Adaptive-Capacity based on current profile
            profile = st.session_state.individual_profile
            s1_current = calculate_technical_ai_skills(profile['prompting_score'], profile['tools_score'], profile['understanding_score'], profile['datalit_score'])
            s2_current = calculate_ai_augmented_productivity(profile['output_quality_with_ai'], profile['output_quality_without_ai'], profile['time_without_ai'], profile['time_with_ai'])
            s3_current = calculate_critical_ai_judgment(profile['errors_caught'], profile['total_ai_errors'], profile['appropriate_trust_decisions'], profile['total_decisions'])
            s4_current = calculate_ai_learning_velocity(profile['delta_proficiency'], profile['delta_t_hours_invested'])
            ai_fluency_current = calculate_ai_fluency(s1_current, s2_current, s3_current, s4_current)

            education_foundation_current = calculate_education_foundation(profile['education_level'])
            practical_experience_current = calculate_practical_experience(profile['years_experience'])
            specialization_depth_current = calculate_specialization_depth(profile['portfolio_score'], profile['recognition_score'], profile['credentials_score'])
            domain_expertise_current = calculate_domain_expertise(education_foundation_current, practical_experience_current, specialization_depth_current)

            adaptive_capacity_current = calculate_adaptive_capacity(profile['cognitive_flexibility'], profile['social_emotional_intelligence'], profile['strategic_career_management'])

            # Simulate impact on V^R components
            ai_fluency_new, domain_expertise_new, adaptive_capacity_new = simulate_pathway_impact(
                ai_fluency_current,
                domain_expertise_current,
                adaptive_capacity_current,
                selected_pathway_data['pathway_type'],
                selected_pathway_data['impact_ai_fluency'],
                selected_pathway_data['impact_domain_expertise'],
                selected_pathway_data['impact_adaptive_capacity'],
                st.session_state.pathway_completion_score,
                st.session_state.pathway_mastery_score
            )

            # Recalculate new V^R
            vr_score_new = calculate_idiosyncratic_readiness(ai_fluency_new, domain_expertise_new, adaptive_capacity_new) * 100

            # Recalculate new Synergy with new V^R (H^R assumed to be same for pathway simulation)
            # Re-calculate individual skills df with potential pathway impacts if applicable (this is complex and not explicitly defined for skills, so will use current for simplicity for now)
            # For a more robust solution, skills data should also be dynamically updated based on pathway impact
            skills_match_score_new = calculate_skills_match_score(st.session_state.individual_skills_for_synergy, required_skills_for_selected_occupation)
            timing_factor_new = calculate_timing_factor(st.session_state.individual_profile['years_experience'])
            alignment_factor_new = calculate_alignment_factor(skills_match_score_new, st.session_state.max_possible_skills_match, timing_factor_new)

            synergy_percentage_new = calculate_synergy_percentage(vr_score_new, st.session_state.hr_score, alignment_factor_new)

            # Calculate new AI-R Score
            ai_r_score_new = calculate_ai_readiness_score(vr_score_new, st.session_state.hr_score, synergy_percentage_new, st.session_state.alpha, st.session_state.beta)

            st.session_state.vr_score_new = vr_score_new
            st.session_state.synergy_percentage_new = synergy_percentage_new
            st.session_state.ai_r_score_new = ai_r_score_new

            st.success(f"Pathway Impact Simulated! New AI-R Score: {ai_r_score_new:.2f}")

    if "ai_r_score_new" in st.session_state:
        st.subheader("Simulated Pathway Impact")
        st.markdown("Comparison of your current AI-Readiness Score with the projected score after completing the selected pathway.")

        col_sim1, col_sim2 = st.columns(2)
        with col_sim1:
            st.metric(label="Current AI-R Score", value=f"{st.session_state.ai_r_score:.2f}")
        with col_sim2:
            st.metric(label="Projected AI-R Score", value=f"{st.session_state.ai_r_score_new:.2f}")

        comparison_data = {
            "Metric": ["V^R", "H^R", "Synergy%", "AI-R"],
            "Current Score": [st.session_state.vr_score, st.session_state.hr_score, st.session_state.synergy_percentage, st.session_state.ai_r_score],
            "Projected Score": [st.session_state.vr_score_new, st.session_state.hr_score, st.session_state.synergy_percentage_new, st.session_state.ai_r_score_new]
        }
        comparison_df = pd.DataFrame(comparison_data)

        fig_comparison = px.bar(comparison_df.melt(id_vars="Metric", var_name="Type", value_name="Score"),
                                x="Metric", y="Score", color="Type", barmode="group",
                                title="Current vs. Projected AI-Readiness Scores",
                                labels={"Score": "Score (0-100%)"},
                                color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig_comparison)



