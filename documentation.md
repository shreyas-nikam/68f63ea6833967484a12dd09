id: 68f63ea6833967484a12dd09_documentation
summary: AI-Readiness score - Gemini-2.5-Flash Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Navigating AI-Enabled Careers: An AI-Readiness Score Codelab

## Introduction to the AI Career Navigator & Pathway Planner
Duration: 0:15:00

Welcome to the **AI Career Navigator & Pathway Planner** Codelab! In this comprehensive guide, we'll explore a powerful Streamlit application designed to help individuals understand and enhance their readiness for AI-enabled careers. The core of this application is the **AI-Readiness Score (AI-R)** framework, a parametric model that quantifies an individual's preparedness by integrating both personal capabilities and prevailing market opportunities.

<aside class="positive">
<b>Why is this important?</b> As AI transforms industries, understanding how to adapt, acquire new skills, and identify suitable career paths becomes crucial. This application provides a structured approach to evaluate your current standing and strategically plan your professional development in the evolving AI landscape.
</aside>

The AI-R framework is invaluable for:
*   **Career Transitioners**: Identifying high-potential AI roles and the skills needed to bridge gaps.
*   **Students**: Guiding educational choices towards future-proof careers.
*   **Professionals**: Assessing current AI competencies and planning for upskilling.
*   **Organizations**: Benchmarking talent and designing targeted training programs.

### The Core AI-Readiness Score Formula

The AI-Readiness Score for an individual $i$ at time $t$ is defined by the following central formula:

$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

Where:
*   $V^R(t)$ is the **Idiosyncratic Readiness**, representing an individual's intrinsic capabilities and preparedness.
*   $H^R(t)$ is the **Systematic Opportunity**, representing external market demand and opportunities for specific occupations.
*   $\alpha \in [0,1]$ is a weighting factor that determines the relative importance of individual capabilities versus market opportunities in the overall score.
*   $\beta > 0$ is the **Synergy coefficient**, which amplifies the AI-Readiness Score when there's a strong alignment between individual readiness and market opportunities.
*   Both $V^R$ and $H^R$ are normalized to a scale of $[0, 100]$.
*   $\text{Synergy}\%$ is also normalized to $[0, 100]$ percentage units.

This framework enables dynamic "what-if" scenario planning, allowing you to explore how different learning pathways and career transitions could impact your future career prospects.

### Learning Goals for this Codelab
By the end of this codelab, you will be able to:
*   Understand the key components and calculations behind the AI-Readiness Score.
*   Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.
*   Evaluate the potential impact of various learning pathways on individual skill development.
*   Analyze different career paths based on market demand and personal capabilities.
*   Navigate and understand the Streamlit application's structure and functionalities.

### Application Architecture

The application is structured into three main pages, each focusing on different aspects of the AI-R score calculation, orchestrated by a central `app.py` file and supported by utility functions in `utils.py`.

```mermaid
graph TD
    A[app.py - Main Application] --> B{Streamlit Sidebar Navigation};
    B --> C[Page 1: Introduction & Data];
    B --> D[Page 2: Idiosyncratic Readiness (V^R)];
    B --> E[Page 3: Systematic Opportunity (H^R) & Simulation];

    C --> C1[Global Parameters Configuration];
    C --> C2[Display Synthetic DataFrames];

    D --> D1[User Input for V^R Components];
    D --> D2[Calculate V^R (using utils.py)];
    D --> D3[Visualize V^R Breakdown];

    E --> E1[Select Target Occupation];
    E --> E2[User Input for H^R & Synergy Parameters];
    E --> E3[Calculate H^R & Synergy (using utils.py)];
    E --> E4[Calculate Final AI-R Score];
    E --> E5[Visualize H^R & AI-R Breakdown];
    E --> E6[Simulate Learning Pathway Impact (using utils.py)];
    E --> E7[Visualize Pathway Impact];

    C1 & C2 & D1 & D2 & D3 & E1 & E2 & E3 & E4 & E5 & E6 & E7 --> F[utils.py - Core Calculation Functions];
    F --> G[Synthetic Data Generation];
```
*Figure 1: Overall Application Architecture Diagram*

## Step 1: Setting up the Application and Understanding Data
Duration: 0:10:00

In this step, we will get the Streamlit application up and running. We'll also explore how the application initializes its data and global parameters, which are crucial for the AI-Readiness Score calculations.

### 1.1 Application Structure

The application is divided into several Python files:
*   `app.py`: The main Streamlit entry point. It sets up the page configuration, title, sidebar navigation, and loads the respective page modules based on user selection.
*   `utils.py`: Contains all the core calculation functions for $V^R$, $H^R$, Synergy, and AI-R, as well as the synthetic data generation logic.
*   `application_pages/page1.py`: Handles the introduction, global parameter settings, and display of synthetic data.
*   `application_pages/page2.py`: Manages user inputs for Idiosyncratic Readiness ($V^R$) components and visualizes the results.
*   `application_pages/page3.py`: Focuses on Systematic Opportunity ($H^R$), Synergy, and the Pathway Simulation.

### 1.2 Running the Application

First, ensure you have Streamlit installed. If not, you can install it via pip:
```console
pip install streamlit pandas plotly
```

Save the provided `app.py` and `application_pages/utils.py`, `application_pages/page1.py`, `application_pages/page2.py`, `application_pages/page3.py` files in appropriate directories. The `application_pages` directory should be a subdirectory of where `app.py` is located.

To run the application, navigate to the directory containing `app.py` in your terminal and execute:

```console
streamlit run app.py
```

This will open the Streamlit application in your web browser.

### 1.3 Global Parameters and Synthetic Data

The application starts on "Page 1: Introduction & Data". Here, you can configure the global weighting parameters for the AI-Readiness Score and inspect the synthetic datasets used.

<aside class="positive">
<b>Tip:</b> The use of synthetic data ensures that you can immediately interact with the application and see calculations without needing to provide real data. This is excellent for demonstration and development purposes.
</aside>

#### Global Parameters

You can adjust the `alpha` and `beta` parameters directly on this page using sliders. These values are stored in Streamlit's session state, making them accessible across all pages.

*   **Weight on Individual Factors ($\alpha$)**: This slider controls the emphasis placed on your personal capabilities ($V^R$) versus market opportunities ($H^R$) in the final AI-R score. A higher $\alpha$ means more weight on $V^R$.
*   **Synergy Coefficient ($\beta$)**: This coefficient amplifies the impact of the synergy component, which measures the alignment between your skills and market demand. A higher $\beta$ means greater reward for strong alignment.

#### Synthetic Dataframes

The application generates several dataframes, each representing a crucial piece of information for the AI-R calculations. These are displayed directly on Page 1:
*   `individual_profiles_df`: Contains base information about a user's individual capabilities.
*   `occupational_data_df`: Provides data on various occupations, including AI enhancement scores, growth rates, and wages.
*   `learning_pathways_df`: Defines different learning pathways and their projected impact on individual skills.
*   `occupation_required_skills_df`: Lists the skills required for specific occupations and their importance.
*   `individual_skills_df`: Details the skills an individual possesses and their proficiency.

These dataframes are generated by the `generate_synthetic_data()` function in `utils.py`.

```python
# From utils.py
def generate_synthetic_data():
    individual_profiles_data = {
        'user_id': [1], 'prompting_score': [0.75], 'tools_score': [0.6],
        'understanding_score': [0.8], 'datalit_score': [0.9],
        # ... other data
    }
    individual_profiles_df = pd.DataFrame(individual_profiles_data)
    # ... similar generation for other dataframes
    return individual_profiles_df, occupational_data_df, learning_pathways_df, occupation_required_skills_df, individual_skills_df
```

## Step 2: Exploring Idiosyncratic Readiness ($V^R$)
Duration: 0:25:00

Now, let's delve into the first major component of the AI-Readiness Score: **Idiosyncratic Readiness ($V^R$)**. This score represents your individual capabilities and preparedness for AI-driven careers. It's a composite score derived from three primary dimensions: AI-Fluency, Domain-Expertise, and Adaptive-Capacity. Each of these dimensions is further broken down into measurable sub-components.

### 2.1 The $V^R$ Framework

$$ V^R_i(t) = w_1 \cdot \text{AI-Fluency}_i(t) + w_2 \cdot \text{Domain-Expertise}_i(t) + w_3 \cdot \text{Adaptive-Capacity}_i(t) $$
Where $w_1, w_2, w_3$ are weights (default $w_1=0.45, w_2=0.35, w_3=0.20$ as seen in `calculate_idiosyncratic_readiness` function).

Navigate to **"Page 2: Idiosyncratic Readiness (V^R)"** using the sidebar. Here, you'll find various sliders and select boxes allowing you to input your personal scores for each sub-component.

### 2.2 AI-Fluency

AI-Fluency ($S_{i, \text{Fluency}}$) measures your ability to effectively interact with, utilize, and adapt to AI technologies. It's composed of four sub-dimensions:
1.  **Technical AI Skills ($S_{i,1}$)**: Proficiency in crafting prompts, using AI tools, understanding AI concepts, and data literacy.
    $$ S_{i,1} = \frac{\text{Prompting} + \text{Tools} + \text{Understanding} + \text{Data Literacy}}{4} $$
2.  **AI-Augmented Productivity ($S_{i,2}$)**: The efficiency and quality improvement gained when using AI.
    $$ S_{i,2} = \frac{\text{Output Quality with AI}}{\text{Output Quality without AI}} \times \frac{\text{Time without AI}}{\text{Time with AI}} $$
3.  **Critical AI Judgment ($S_{i,3}$)**: Your ability to identify AI errors and make appropriate trust decisions.
    $$ S_{i,3} = 1 - \frac{1}{2} \left( \frac{\text{Errors Caught}}{\text{Total AI Errors}} + \frac{\text{Appropriate Trust Decisions}}{\text{Total Decisions}} \right) $$
4.  **AI Learning Velocity ($S_{i,4}$)**: How quickly you acquire new AI-related knowledge and skills.
    $$ S_{i,4} = \frac{\Delta \text{Proficiency}}{\Delta t_{\text{hours invested}}} $$
The overall AI-Fluency is a weighted sum of these four sub-scores:
$$ \text{AI-Fluency} = 0.1 \cdot S_{i,1} + 0.2 \cdot S_{i,2} + 0.3 \cdot S_{i,3} + 0.4 \cdot S_{i,4} $$

You can adjust the sliders within the "AI-Fluency Sub-Components" expander to see how these inputs influence your scores.

<aside class="negative">
<b>Warning:</b> Ensure "Output Quality without AI" and "Time with AI" are not zero when adjusting $S_{i,2}$ inputs, as this would lead to division by zero. The `utils.py` functions handle this gracefully by returning 0.0, but it's good to be aware.
</aside>

### 2.3 Domain-Expertise

Domain-Expertise ($E_{i, \text{Domain}}$) measures your specialized knowledge and skills within a particular field. It's composed of:
1.  **Education Foundation ($E_{\text{education}}$)**: Your highest attained education level.
    *   PhD: 1.0, Master's: 0.8, Bachelor's: 0.6, etc.
2.  **Practical Experience ($E_{\text{experience}}$)**: Your total years of professional experience.
    $$ E_{\text{experience}} = \frac{\text{Years Experience}}{\text{Years Experience} + (1/\gamma)} $$
    (where $\gamma$ is a decay rate, default 0.15)
3.  **Specialization Depth ($E_{\text{specialization}}$)**: Quality of portfolio, professional recognition, and credentials.
    $$ E_{\text{specialization}} = \frac{\text{Portfolio Score} + \text{Recognition Score} + \text{Credentials Score}}{3} $$
The overall Domain-Expertise is a weighted sum:
$$ \text{Domain-Expertise} = 0.125 \cdot E_{\text{education}} + 0.25 \cdot E_{\text{experience}} + 0.625 \cdot E_{\text{specialization}} $$

Adjust the sliders and select box within the "Domain-Expertise Sub-Components" expander.

### 2.4 Adaptive-Capacity

Adaptive-Capacity ($A_{i, \text{Adaptive}}$) represents your ability to adjust to new conditions and learn new skills effectively. It's the average of:
*   **Cognitive Flexibility**: Your capacity to switch between different concepts or tasks.
*   **Social-Emotional Intelligence**: Your ability to understand and manage emotions.
*   **Strategic Career Management**: Your proactive approach to career planning and development.
    $$ \text{Adaptive-Capacity} = \frac{\text{Cognitive Flexibility} + \text{Social-Emotional Intelligence} + \text{Strategic Career Management}}{3} $$

Adjust the sliders within the "Adaptive-Capacity Sub-Components" expander.

### 2.5 Calculating and Visualizing $V^R$

After inputting your scores, click the **"Calculate V^R Score"** button. The application will use the `utils.py` functions to compute your $V^R$ score, normalizing it to a 0-100 scale.

```python
# Snippet from application_pages/page2.py (after button click)
# ... (input gathering)
s1 = calculate_technical_ai_skills(profile['prompting_score'], profile['tools_score'], profile['understanding_score'], profile['datalit_score'])
s2 = calculate_ai_augmented_productivity(profile['output_quality_with_ai'], profile['output_quality_without_ai'], profile['time_without_ai'], profile['time_with_ai'])
s3 = calculate_critical_ai_judgment(profile['errors_caught'], profile['total_ai_errors'], profile['appropriate_trust_decisions'], profile['total_decisions'])
s4 = calculate_ai_learning_velocity(profile['delta_proficiency'], profile['delta_t_hours_invested'])
ai_fluency = calculate_ai_fluency(s1, s2, s3, s4)

education_foundation = calculate_education_foundation(profile['education_level'])
practical_experience = calculate_practical_experience(profile['years_experience'])
specialization_depth = calculate_specialization_depth(profile['portfolio_score'], profile['recognition_score'], profile['credentials_score'])
domain_expertise = calculate_domain_expertise(education_foundation, practical_experience, specialization_depth)

adaptive_capacity = calculate_adaptive_capacity(profile['cognitive_flexibility'], profile['social_emotional_intelligence'], profile['strategic_career_management'])

vr_score = calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity) * 100 # Normalize to 0-100
st.session_state.vr_score = vr_score
```

The page will then display your overall $V^R$ score and interactive bar charts showing the breakdown of scores for:
*   $V^R$ components (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
*   AI-Fluency sub-components ($S_{i,1}$ to $S_{i,4}$).
*   Domain-Expertise sub-components ($E_{\text{education}}$, $E_{\text{experience}}$, $E_{\text{specialization}}$).

These visualizations help you understand your strengths and areas for improvement in your individual readiness for AI careers.

## Step 3: Calculating Systematic Opportunity ($H^R$)
Duration: 0:15:00

Now that we've understood individual capabilities with $V^R$, let's shift our focus to external market factors: **Systematic Opportunity ($H^R$)**. This score quantifies the market demand and potential for various AI-enabled occupations. It helps you identify promising career paths based on industry trends, wage premiums, and accessibility.

### 3.1 The $H^R$ Framework

$$ H^R_i(t) = \text{Systematic Opportunity} = \text{Base Opportunity} \times \text{Growth Multiplier} \times \text{Regional Multiplier} $$

Navigate to **"Page 3: Systematic Opportunity (H^R) & Simulation"** using the sidebar.

### 3.2 Base Opportunity Score

The `base_opportunity_score` is derived from four key occupational attributes:
1.  **AI-Enhancement Potential ($A_{\text{enhancement}}$)**: How much an occupation's productivity or nature can be improved by AI.
    $$ A_{\text{enhancement}} = \text{AI Enhancement Score} $$
2.  **Job Growth Projection ($G_{\text{growth}}$)**: Expected growth rate of the occupation.
    $$ G_{\text{growth}} = 50 + (\text{Growth Rate } g \times 100) $$
    (clipped between 0 and 100)
3.  **Wage Premium ($W_{\text{premium}}$)**: The difference in wages for AI-skilled professionals compared to median wages in that occupation.
    $$ W_{\text{premium}} = \frac{\text{AI Skilled Wage} - \text{Median Wage}}{\text{Median Wage}} $$
4.  **Entry Accessibility ($E_{\text{accessibility}}$)**: How easy it is to enter the occupation, considering education and experience requirements.
    $$ E_{\text{accessibility}} = \frac{1}{1 + 0.1 \times (\text{Education Years Required} + \text{Experience Years Required})} $$

The Base Opportunity Score is a weighted sum of these components:
$$ \text{Base Opportunity} = w_1 \cdot A_{\text{enhancement}} + w_2 \cdot G_{\text{growth}} + w_3 \cdot W_{\text{premium}} + w_4 \cdot E_{\text{accessibility}} $$
(default weights $w_1=0.30, w_2=0.30, w_3=0.25, w_4=0.15$)

### 3.3 Market Multipliers

These factors adjust the base opportunity based on dynamic market conditions:
1.  **Growth Multiplier ($M_{\text{growth}}$)**: Accounts for recent changes in job postings, indicating increasing or decreasing demand.
    $$ M_{\text{growth}} = \left( \frac{\text{Current Job Postings}}{\text{Previous Job Postings}} \right)^{\lambda} $$
    Here, $\lambda$ (Lambda value for Growth Multiplier) dampens the volatility from job posting fluctuations. You can adjust it with a slider (default 0.3).
2.  **Regional Multiplier ($M_{\text{regional}}$)**: Adjusts for local demand and remote work possibilities.
    $$ M_{\text{regional}} = 1 + \gamma \times \left( \frac{\text{Local Demand}}{\text{National Avg. Demand}} + \text{Remote Work Factor} - 1 \right) $$
    Here, $\gamma$ (Gamma value for Regional Multiplier) scales the influence of regional market dynamics. You can adjust it with a slider (default 0.2).

### 3.4 Calculating $H^R$

On "Page 3", select a **"Target Occupation"** from the dropdown. The occupational data for the selected role will be used to calculate its $H^R$.

<aside class="positive">
<b>Tip:</b> Experiment with different occupations and lambda/gamma values to see how the Systematic Opportunity changes. This can reveal which factors are most impactful for certain roles.
</aside>

After selecting the occupation and adjusting multipliers, click the **"Calculate AI-Readiness Score (H^R and Synergy)"** button. The application will compute $H^R$, normalizing it to a 0-100 scale.

```python
# Snippet from application_pages/page3.py (after button click)
# ... (occupation selection)
current_occupation_data = st.session_state.occupational_data_df[
    st.session_state.occupational_data_df['occupation_name'] == st.session_state.selected_occupation
].iloc[0]

ai_enhancement_potential = calculate_ai_enhancement_potential(current_occupation_data['ai_enhancement_score'])
job_growth_projection = calculate_job_growth_projection(current_occupation_data['job_growth_rate_g'])
wage_premium = calculate_wage_premium(current_occupation_data['ai_skilled_wage'], current_occupation_data['median_wage'])
entry_accessibility = calculate_entry_accessibility(current_occupation_data['education_years_required'], current_occupation_data['experience_years_required'])
base_opportunity_score = calculate_base_opportunity_score(ai_enhancement_potential, job_growth_projection, wage_premium, entry_accessibility)

growth_multiplier = calculate_growth_multiplier(current_occupation_data['current_job_postings'], current_occupation_data['previous_job_postings'], st.session_state.lambda_val)
regional_multiplier = calculate_regional_multiplier(current_occupation_data['local_demand'], current_occupation_data['national_avg_demand'], current_occupation_data['remote_work_factor'], st.session_state.gamma_val)

hr_score = calculate_systematic_opportunity(base_opportunity_score, growth_multiplier, regional_multiplier) * 100 # Normalize to 0-100
st.session_state.hr_score = hr_score
```

The page will display the calculated $H^R$ score and a bar chart visualizing the contributions of its base components.

## Step 4: Understanding Synergy and the Final AI-Readiness Score
Duration: 0:20:00

With $V^R$ (individual readiness) and $H^R$ (systematic opportunity) calculated, the final step in determining the AI-Readiness Score is to compute the **Synergy component**. Synergy measures how well your individual capabilities align with the demands of a chosen occupation.

### 4.1 The Synergy Component

Synergy ($Synergy\%$) quantifies the alignment between your individual skills and the market's requirements for a specific occupation. It is composed of:
1.  **Skills Match Score**: How well your individual skills align with the required skills for the target occupation, weighted by importance.
    $$ \text{Skills Match Score} = \left( \frac{\sum_{\text{matched skills}} \left( \min(\text{Your Skill Score}, \text{Required Skill Score}) / 100 \right) \times \text{Skill Importance}}{\sum \text{Required Skill Importance}} \right) \times 100 $$
    The `calculate_skills_match_score` function in `utils.py` handles this.
2.  **Timing Factor**: Accounts for the relevance of your experience to current market needs.
    $$ \text{Timing Factor} = 1 + \left( \frac{\text{Years Experience}}{5} \right) \quad \text{if Years Experience} > 0 \text{ else } 1 $$
3.  **Alignment Factor**: Combines the skills match with the timing factor.
    $$ \text{Alignment Factor} = \left( \frac{\text{Skills Match Score}}{\text{Max Possible Match}} \right) \times \text{Timing Factor} $$
    `Max Possible Match` is a configurable value (default 100).

The overall Synergy Percentage is calculated as:
$$ \text{Synergy}\% = \frac{V^R \cdot H^R \cdot \text{Alignment Factor}}{100.0} $$

### 4.2 Inputting Skills for Synergy

On "Page 3", below the $H^R$ inputs, you'll find sections for "Required Skills for Selected Occupation" and "Your Individual Skills".

*   **Required Skills**: This dataframe (`occupation_required_skills_df`) automatically filters to show the skills crucial for your chosen target occupation. It lists `skill_name`, `required_skill_score` (target proficiency), and `skill_importance` (how critical it is).
*   **Your Individual Skills**: This is an editable dataframe (`individual_skills_for_synergy`). You can directly add, remove, or modify your `skill_name` and `individual_skill_score` (your proficiency from 0-100) to accurately reflect your current skill set.

<aside class="positive">
<b>Experiment:</b> Try adding skills that directly match the 'Required Skills' for your selected occupation and increase their scores. Observe how this boosts your Synergy%.
</aside>

After updating your individual skills, ensure you have calculated $V^R$ on Page 2 and then click the **"Calculate AI-Readiness Score (H^R and Synergy)"** button on Page 3.

```python
# Snippet from application_pages/page3.py (after button click, continuing from H^R)
# ... (H^R calculation)
# Calculate Synergy components
skills_match_score = calculate_skills_match_score(st.session_state.individual_skills_for_synergy, required_skills_for_selected_occupation)
timing_factor = calculate_timing_factor(st.session_state.individual_profile['years_experience'])
alignment_factor = calculate_alignment_factor(skills_match_score, st.session_state.max_possible_skills_match, timing_factor)
synergy_percentage = calculate_synergy_percentage(st.session_state.vr_score, hr_score, alignment_factor)

st.session_state.synergy_percentage = synergy_percentage
```

### 4.3 The Final AI-Readiness Score

Once $V^R$, $H^R$, and Synergy% are calculated, the application computes the final AI-R Score using the global parameters $\alpha$ and $\beta$ set on Page 1.

$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

The `calculate_ai_readiness_score` function performs this final aggregation.

```python
# Snippet from application_pages/page3.py (after synergy calculation)
# Calculate Final AI-R Score
ai_r_score = calculate_ai_readiness_score(st.session_state.vr_score, hr_score, synergy_percentage, st.session_state.alpha, st.session_state.beta)
st.session_state.ai_r_score = ai_r_score
```

The page will then display:
*   Your current $V^R$, $H^R$, Synergy%, and the final AI-R Score.
*   A bar chart illustrating the breakdown of $H^R$ base components.
*   A pie chart showing the proportional contribution of $V^R$, $H^R$, and Synergy% to your overall AI-R Score. This is weighted by your chosen $\alpha$ and $\beta$ values.

<aside class="positive">
<b>Interpretation:</b> A high AI-R score indicates strong individual preparedness combined with good market opportunity and alignment. The pie chart is particularly useful for understanding which main component (individual capability, market, or alignment) is driving your overall score and where potential areas for improvement lie.
</aside>

## Step 5: Simulating Learning Pathways
Duration: 0:20:00

One of the most powerful features of the AI Career Navigator is its ability to perform "what-if" scenario planning through **Pathway Simulation**. This allows you to explore how investing in different learning pathways could impact your individual readiness ($V^R$) and, consequently, your overall AI-Readiness Score.

### 5.1 The Pathway Simulation Framework

The application uses the `simulate_pathway_impact` function in `utils.py` to model how a chosen learning pathway modifies your AI-Fluency, Domain-Expertise, and Adaptive-Capacity.

The simulation takes into account:
*   **Current Scores**: Your existing AI-Fluency, Domain-Expertise, and Adaptive-Capacity scores.
*   **Pathway Impact**: Each defined learning pathway has a pre-defined `impact_ai_fluency`, `impact_domain_expertise`, and `impact_adaptive_capacity` (values between 0.0 and 1.0).
*   **Completion Score**: Your assumed level of completion for the pathway (0.0 to 1.0).
*   **Mastery Score**: Your assumed level of mastery achieved within the pathway (0.0 to 1.0).

The new component scores are calculated as:
```python
# Snippet from utils.py
ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score
# Scores are capped at 1.0
```

These updated component scores are then used to recalculate a new projected $V^R$, Synergy%, and ultimately, a new AI-R Score. The $H^R$ score is generally assumed to remain constant in these simulations, as pathways primarily impact individual attributes.

### 5.2 Performing a Simulation

On "Page 3", scroll down to the **"Pathway Simulation"** section.

1.  **Select Learning Pathway**: Choose one of the predefined pathways from the dropdown menu (e.g., "Prompt Engineering Fundamentals", "AI for Financial Analysis"). Each pathway is designed to boost specific aspects of your $V^R$.
    *   Pathways of type 'AI-Fluency' will have a higher `impact_ai_fluency`.
    *   Pathways of type 'Domain+AI Integration' will have a higher `impact_domain_expertise`.
    *   Pathways of type 'Adaptive Capacity' will have a higher `impact_adaptive_capacity`.
2.  **Pathway Completion Score**: Adjust the slider to reflect how much of the pathway you expect to complete (0.0 to 1.0).
3.  **Pathway Mastery Score**: Adjust the slider to reflect your anticipated level of mastery after completing the pathway (0.0 to 1.0).

<aside class="negative">
<b>Prerequisite:</b> Ensure you have already calculated your initial AI-Readiness Score (by clicking the "Calculate AI-Readiness Score" button) before running a simulation. The simulation uses your *current* scores as a baseline.
</aside>

Click the **"Simulate Pathway Impact"** button.

```python
# Snippet from application_pages/page3.py (after Simulate Pathway Impact button click)
# ... (retrieve current V^R components)
selected_pathway_data = st.session_state.learning_pathways_df[
    st.session_state.learning_pathways_df['pathway_name'] == st.session_state.selected_pathway
].iloc[0]

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

vr_score_new = calculate_idiosyncratic_readiness(ai_fluency_new, domain_expertise_new, adaptive_capacity_new) * 100
# ... (recalculate synergy and final AI-R with new vr_score_new)
```

### 5.3 Analyzing Simulation Results

After the simulation, the page will display:
*   Your **Current AI-R Score** versus the **Projected AI-R Score**.
*   A bar chart comparing the "Current Score" and "Projected Score" for $V^R$, $H^R$, Synergy%, and the overall AI-R.

<aside class="positive">
<b>Strategic Planning:</b> Use this simulation to compare different pathways. Which pathway offers the greatest boost to your AI-R score for your target occupation? This data-driven insight can guide your learning and development decisions.
</aside>

This dynamic "what-if" analysis is crucial for making informed career and learning decisions in a rapidly evolving AI landscape.

## Conclusion and Next Steps
Duration: 0:05:00

Congratulations! You have successfully completed the AI-Readiness Score Codelab. You've navigated a comprehensive Streamlit application that breaks down the complex factors influencing preparedness for AI-enabled careers.

Throughout this codelab, you have:
*   Understood the fundamental components of the AI-Readiness Score ($V^R$, $H^R$, Synergy%) and its overarching formula.
*   Explored the detailed sub-components of Idiosyncratic Readiness ($V^R$), including AI-Fluency, Domain-Expertise, and Adaptive-Capacity.
*   Analyzed the factors contributing to Systematic Opportunity ($H^R$), such as AI-enhancement potential, job growth, wage premium, and entry accessibility.
*   Learned how the Synergy component aligns your individual capabilities with market demands.
*   Utilized the application's interactive features to calculate, visualize, and simulate the impact of learning pathways on your AI-Readiness Score.

This framework provides a robust, data-driven tool for career planning in the age of AI. By understanding your current position and strategically planning your development, you can proactively adapt to the transforming job market.

### Further Exploration and Enhancements

Consider these ideas for extending or improving the application:
*   **Real-world Data Integration**: Instead of synthetic data, allow users to upload their resumes, LinkedIn profiles, or perform skill assessments to populate their `individual_skills_df` and `individual_profiles_df`.
*   **Dynamic Weighting**: Introduce more sophisticated mechanisms for determining the weights ($\alpha, \beta, w_i$) based on user preferences, industry benchmarks, or even machine learning models.
*   **Personalized Pathway Recommendations**: Develop an algorithm that suggests optimal learning pathways based on a user's current $V^R$ and their desired target occupation, aiming to maximize their projected AI-R score.
*   **Historical Trend Analysis**: Incorporate historical data for job postings, wages, and skill demands to show trends and predict future opportunities more accurately.
*   **Scenario Comparison**: Allow users to save multiple "what-if" scenarios (e.g., Pathway A vs. Pathway B) and compare their projected AI-R scores side-by-side.
*   **Geographic Specificity**: Enhance the regional multiplier with more granular location-based job market data.

The AI-Readiness Score framework and this Streamlit application provide a solid foundation for empowering individuals to navigate their careers effectively in the rapidly evolving world of AI. Keep learning, keep experimenting, and keep enhancing your AI-Readiness!

```
<button>
  [Download Application Source Code](https://example.com/download-ai-readiness-app)
</button>
