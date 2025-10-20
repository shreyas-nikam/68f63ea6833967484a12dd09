id: 68f63ea6833967484a12dd09_user_guide
summary: AI-Readiness score - Gemini-2.5-Flash User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI Career Navigator & Pathway Planner

## Step 1: Welcome to the AI Career Navigator & Pathway Planner
Duration: 00:05:00

Welcome to the AI Career Navigator & Pathway Planner, a powerful application designed to help you understand and navigate the evolving landscape of AI-enabled careers. In a world increasingly driven by Artificial Intelligence, understanding your readiness for future job roles is crucial. This application introduces the **AI-Readiness Score (AI-R)** framework, a comprehensive model that quantifies your preparedness by balancing your individual capabilities with market opportunities.

<aside class="positive">
This tool is invaluable for **career planning**, identifying **skill gaps**, and exploring **potential career pathways** in the AI era. It helps you make informed decisions about your professional development.
</aside>

The core of this application revolves around a key formula for calculating your AI-Readiness Score ($AI-R$):

$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

Let's break down what these components mean:

*   **$V^R(t)$ (Idiosyncratic Readiness)**: This represents *your individual capabilities and preparedness*. It's about your personal skills, expertise, and adaptability in relation to AI technologies. Think of it as your internal readiness score.
*   **$H^R(t)$ (Systematic Opportunity)**: This reflects the *external market demand and opportunities* for AI-enabled roles. It considers factors like job growth, wage premiums, and how accessible these jobs are. This is the market's readiness for you.
*   **$\alpha$ (Weight on Individual Factors)**: A parameter (between 0 and 1) that determines how much emphasis is placed on your individual capabilities ($V^R$) versus market opportunities ($H^R$) in the overall score. If $\alpha$ is high, individual skills matter more; if low, market opportunities are more dominant.
*   **$\beta$ (Synergy Coefficient)**: A positive coefficient that amplifies your AI-Readiness Score when your individual capabilities ($V^R$) strongly align with market opportunities ($H^R$). It captures the idea that a good match between you and the market is more than the sum of its parts.
*   **$\text{Synergy}\%(V^R, H^R)$**: This component quantifies the alignment or "fit" between your unique skills and the specific demands of a target market opportunity. A high synergy percentage means your skills are particularly well-suited for a particular job market.

Throughout this guide, we will explore each of these components in detail, allowing you to interact with the application and understand how various factors influence your AI-Readiness Score. The application is designed to facilitate dynamic "what-if" scenario planning, helping you visualize how different learning pathways and career choices could impact your future career prospects.

To get started, navigate using the sidebar on the left. You'll begin on "Page 1: Introduction & Data".

## Step 2: Understanding the Application Interface and Data
Duration: 00:07:00

On **Page 1: Introduction & Data**, you'll find the foundation of our analysis: global parameters and synthetic datasets.

### Global Parameters
The first section allows you to adjust the global weighting parameters, $\alpha$ and $\beta$, which are crucial for the overall AI-Readiness Score calculation.

*   **Weight on Individual Factors ($\alpha$)**: Use the slider to adjust this value.
    *   A higher $\alpha$ means your individual readiness ($V^R$) plays a larger role in your overall AI-R score.
    *   A lower $\alpha$ means market opportunity ($H^R$) has a greater influence.
    *   Consider what balance is most appropriate for your career strategy. For example, if you believe personal upskilling is paramount, you might increase $\alpha$.
*   **Synergy Coefficient ($\beta$)**: This slider controls the impact of the Synergy component.
    *   A higher $\beta$ means that a strong alignment between your skills and market needs will significantly boost your AI-R score.
    *   This coefficient highlights the importance of a good match, rewarding you for targeting roles where your skills are highly valued.

<aside class="positive">
Experiment with these parameters to see how they change the relative importance of individual effort vs. market dynamics in your overall AI-Readiness.
</aside>

### Synthetic Dataframes
Below the global parameters, you'll see several dataframes:

*   **Individual Profiles Data**: This dataframe contains sample data representing a user's skills, experience, education, and other personal attributes. When you move to Page 2, you'll be able to customize these values.
*   **Occupational Data**: This shows various job roles, their AI enhancement potential, growth rates, wage information, and more. This data feeds into the Systematic Opportunity ($H^R$) calculation.
*   **Learning Pathways Data**: This dataframe lists different learning programs or courses and their projected impact on your AI-Fluency, Domain-Expertise, and Adaptive-Capacity. This is key for the "what-if" simulations.
*   **Occupation Required Skills Data**: This outlines the specific skills and their importance required for different occupations. This data is critical for calculating the Synergy component.
*   **Individual Skills Data**: This dataframe represents the skills and proficiency scores of a sample individual. You'll interact with this more directly when calculating Synergy.

These synthetic datasets provide a realistic context for exploring the AI-Readiness framework without needing to input all your personal data initially. They allow you to understand how the calculations work with representative figures.

Once you are familiar with the global parameters and data, use the sidebar to navigate to **"Page 2: Idiosyncratic Readiness (V^R)"**.

## Step 3: Calculating Your Idiosyncratic Readiness ($V^R$)
Duration: 00:10:00

Now that we understand the foundational data, let's delve into **Page 2: Idiosyncratic Readiness (V^R)**. This section focuses on quantifying *your* personal preparedness for AI-driven careers. Your $V^R$ score is a holistic measure, built from three main components: **AI-Fluency**, **Domain-Expertise**, and **Adaptive-Capacity**.

You will interact with sliders and selection boxes to input your current capabilities, which are pre-populated with data from the synthetic individual profile. Feel free to adjust these values to reflect your own profile or to explore different scenarios.

### AI-Fluency Sub-Components
This section measures your ability to interact with, utilize, and adapt to AI technologies.

*   **Technical AI Skills ($S_{i,1}$)**:
    *   **Prompting Score**: Your proficiency in crafting effective prompts for AI systems.
    *   **Tools Score**: Your skill in using AI-powered tools and platforms.
    *   **Understanding Score**: Your comprehension of AI concepts and their implications.
    *   **Datalit Score**: Your data literacy in an AI context.
    *   *Adjust these scores (0.0 - 1.0) to reflect your confidence and expertise in these areas.*
*   **AI-Augmented Productivity ($S_{i,2}$)**:
    *   **Output Quality with/without AI**: Your perceived quality of work output.
    *   **Time with/without AI**: The time taken to complete a task.
    *   *These inputs help calculate how much AI enhances your productivity.*
*   **Critical AI Judgment ($S_{i,3}$)**:
    *   **Errors Caught/Total AI Errors**: Your ability to identify mistakes made by AI.
    *   **Appropriate Trust Decisions/Total Decisions**: Your judgment in deciding when and how much to trust AI outputs.
    *   *This component highlights your ability to critically assess and work alongside AI.*
*   **AI Learning Velocity ($S_{i,4}$)**:
    *   **Delta Proficiency**: Your change in skill level related to AI.
    *   **Delta T Hours Invested**: The hours you've spent on AI-related learning.
    *   *This measures how quickly you acquire new AI skills.*

### Domain-Expertise Sub-Components
This part quantifies your specialized knowledge and skills within a particular field, which is vital even in AI-driven roles.

*   **Education Level**: Select your highest attained education level.
*   **Years Experience**: Input your total years of professional experience.
*   **Specialization Depth**:
    *   **Portfolio Score**: Quality and relevance of your professional portfolio.
    *   **Recognition Score**: Professional recognition and awards.
    *   **Credentials Score**: Relevant certifications and credentials.
    *   *These scores (0.0 - 1.0) indicate how specialized and recognized you are in your domain.*

### Adaptive-Capacity Sub-Components
Your ability to adjust to new conditions, learn new skills, and manage your career effectively.

*   **Cognitive Flexibility**: Your capacity to switch between different concepts or tasks.
*   **Social-Emotional Intelligence**: Your ability to understand and manage emotions, crucial for collaboration.
*   **Strategic Career Management**: Your proactive approach to career planning and development.
*   *These scores (0 - 100) measure your soft skills and readiness for change.*

Once you've adjusted all the inputs to your satisfaction, click the **"Calculate V^R Score"** button.

The application will then display your calculated **Idiosyncratic Readiness (V^R)** score, normalized to 0-100. Below this, you'll see interactive bar charts breaking down your $V^R$ into its main components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) and further into their respective sub-components. These visualizations are incredibly helpful for identifying your strengths and areas for improvement.

<aside class="positive">
Pay attention to the breakdown charts. If your **AI-Fluency** or **Adaptive-Capacity** scores are low, it might indicate areas where targeted learning pathways (which we'll explore next) could have a significant impact.
</aside>

Once you have a good understanding of your $V^R$ score, proceed to **"Page 3: Systematic Opportunity (H^R) & Simulation"** using the sidebar.

## Step 4: Exploring Systematic Opportunity ($H^R$) and Synergy
Duration: 00:12:00

On **Page 3: Systematic Opportunity (H^R) & Simulation**, we shift our focus from your individual capabilities to the external market. This section calculates your **Systematic Opportunity ($H^R$)** based on your chosen target occupation, and then combines it with your $V^R$ to determine the **Synergy** between you and the market.

### Systematic Opportunity ($H^R$) Inputs

*   **Target Occupation**: Select an occupation from the dropdown list. This choice is critical as $H^R$ is calculated specifically for that role based on the `Occupational Data` you saw on Page 1. Each occupation has different AI enhancement potential, growth rates, and wage premiums.
*   **Lambda value for Growth Multiplier ($\lambda$)**: Use the slider to adjust $\lambda$. This parameter influences how much weight is given to recent job posting growth. A higher $\lambda$ means recent growth has a stronger positive impact on the opportunity score.
*   **Gamma value for Regional Multiplier ($\gamma$)**: Use the slider to adjust $\gamma$. This parameter determines the influence of local market demand and remote work factors. A higher $\gamma$ means local conditions and remote work options have a greater impact on the opportunity score.

### Synergy Inputs
Synergy is where your individual skills meet market demand. This section requires you to define your skills and compare them against the requirements of the selected target occupation.

*   **Required Skills for Selected Occupation**: This table displays the skills and their importance for your chosen target occupation. This is derived from the `Occupation Required Skills Data`.
*   **Your Individual Skills**: This is an editable table. You can add or modify your skills and assign an `individual_skill_score` (0-100) to each.
    *   Click "Add row" to include new skills you possess.
    *   Adjust the `individual_skill_score` for existing skills.
    *   *The more your skills align with the "Required Skills" and the higher your individual scores, the greater your Synergy will be.*
*   **Max Possible Skills Match**: This input sets the benchmark for a perfect skill match. The default of 100 means a perfect match contributes 100% to the skills alignment.

Once you have reviewed and adjusted the inputs for both $H^R$ and Synergy, click the **"Calculate AI-Readiness Score (H^R and Synergy)"** button.

<aside class="negative">
If you haven't calculated your $V^R$ score on Page 2 yet, you'll receive a warning. Make sure to complete Page 2 first before calculating the full AI-Readiness Score here.
</aside>

### Calculated AI-Readiness Score
After calculation, you'll see your comprehensive AI-Readiness Score broken down:

*   **V^R Score**: Your Idiosyncratic Readiness (from Page 2).
*   **H^R Score**: The Systematic Opportunity score for your chosen occupation.
*   **Synergy%**: The percentage reflecting the alignment between your skills and the chosen occupation's requirements.
*   **AI-R Score**: Your final AI-Readiness Score, incorporating all components and global parameters ($\alpha$, $\beta$).

Visualizations will appear to help you interpret these scores:

*   **H^R Components Breakdown**: A bar chart showing the contributions of AI-Enhancement Potential, Job Growth Projection, Wage Premium, and Entry Accessibility to your $H^R$ score. This helps you understand *why* a particular occupation offers a high (or low) opportunity.
*   **Overall AI-Readiness Score Contribution**: A pie chart illustrating how much $V^R$, $H^R$, and Synergy contribute to your final $AI-R$ score, weighted by $\alpha$ and $\beta$. This provides a quick overview of which aspects are driving your overall readiness.

Take some time to explore different target occupations and adjust your individual skills to see how your $H^R$ and Synergy change, and how they ultimately impact your overall $AI-R$ score. This is where the "what-if" scenario planning truly begins for market exploration.

## Step 5: Simulating Learning Pathways
Duration: 00:08:00

Still on **Page 3: Systematic Opportunity (H^R) & Simulation**, the final section focuses on dynamic **Pathway Simulation**. This powerful feature allows you to explore how investing in different learning pathways could enhance your individual capabilities and, consequently, boost your AI-Readiness Score.

### Pathway Simulation Inputs
*   **Select Learning Pathway**: Choose a pathway from the dropdown list. These pathways, originating from the `Learning Pathways Data`, are designed to impact specific aspects of your Idiosyncratic Readiness ($V^R$), such as AI-Fluency, Domain-Expertise, or Adaptive-Capacity.
*   **Pathway Completion Score**: Use the slider to indicate your level of completion for the selected pathway (0.0 - 1.0). For example, 0.5 for 50% completion.
*   **Pathway Mastery Score**: Use the slider to indicate your level of mastery achieved in the selected pathway (0.0 - 1.0). This reflects how well you've learned the material.

After selecting a pathway and adjusting the completion and mastery scores, click the **"Simulate Pathway Impact"** button.

### Simulated Pathway Impact
The application will then recalculate your potential future scores, assuming you complete the chosen pathway with the specified mastery. You will see:

*   **Current AI-R Score**: Your AI-Readiness Score *before* considering the pathway.
*   **Projected AI-R Score**: Your AI-Readiness Score *after* successfully completing the pathway.

Below this, a **"Current vs. Projected AI-Readiness Scores"** bar chart provides a visual comparison of your $V^R$, $H^R$ (which is assumed to remain constant for this simulation as pathways primarily affect individual skills), Synergy%, and overall $AI-R$ before and after the pathway.

<aside class="positive">
This simulation is incredibly useful for strategic planning. You can evaluate which learning pathways offer the most significant return on investment for your career goals. For instance, if your **AI-Fluency** is low, a pathway focused on "Prompt Engineering Fundamentals" might show a substantial projected increase in your $AI-R$.
</aside>

Experiment with different pathways, completion levels, and mastery scores to identify the most effective strategies for advancing your AI-Readiness. This allows you to envision potential career trajectories and make informed decisions about your professional development journey.

Congratulations! You have now completed the user guide for the AI Career Navigator & Pathway Planner. You've explored how to quantify your individual capabilities, assess market opportunities, understand their synergy, and simulate the impact of learning pathways on your career readiness.
