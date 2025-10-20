# QuLab: AI Career Navigator & Pathway Planner

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Table of Contents

1.  [Project Title and Description](#project-title-and-description)
2.  [Features](#features)
3.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
4.  [Usage](#usage)
5.  [Project Structure](#project-structure)
6.  [Technology Stack](#technology-stack)
7.  [Contributing](#contributing)
8.  [License](#license)
9.  [Contact](#contact)

---

## 1. Project Title and Description

**QuLab: AI Career Navigator & Pathway Planner** is an interactive Streamlit application designed to help individuals understand and enhance their preparedness for AI-enabled careers. It implements the **AI-Readiness Score (AI-R)** framework, a parametric model that quantifies an individual's career readiness by balancing personal capabilities with market opportunities.

The core of the application revolves around the AI-Readiness Score, defined by the formula:

$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

Where:
*   $V^R(t)$ represents **Idiosyncratic Readiness**, measuring an individual's personal capabilities (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
*   $H^R(t)$ represents **Systematic Opportunity**, quantifying external market factors and demand for specific occupations.
*   $\alpha \in [0,1]$ is a weighting factor that balances the importance of individual capabilities versus market opportunities.
*   $\beta > 0$ is the **Synergy coefficient**, amplifying the AI-Readiness Score when individual skills align well with market demands.

This application allows users to input their skills and experience, explore various occupational data, and simulate the impact of different learning pathways on their AI-Readiness Score, enabling dynamic "what-if" scenario planning for career development.

## 2. Features

*   **Interactive AI-Readiness Score (AI-R) Calculation**: Calculate a comprehensive score based on individual capabilities and market opportunities.
*   **Idiosyncratic Readiness (V^R) Assessment**:
    *   Input and evaluate AI-Fluency (Technical AI Skills, AI-Augmented Productivity, Critical AI Judgment, AI Learning Velocity).
    *   Input and evaluate Domain-Expertise (Education Foundation, Practical Experience, Specialization Depth).
    *   Input and evaluate Adaptive-Capacity (Cognitive Flexibility, Social-Emotional Intelligence, Strategic Career Management).
    *   Visualize the breakdown of V^R and its sub-components.
*   **Systematic Opportunity (H^R) Analysis**:
    *   Select target AI-enabled occupations from a pre-defined dataset.
    *   Evaluate H^R based on AI-enhancement potential, job growth projections, wage premiums, and entry accessibility.
    *   Adjust market-related parameters (e.g., growth and regional multipliers).
    *   Visualize the breakdown of H^R and its sub-components.
*   **Synergy Calculation**:
    *   Quantify the alignment between individual skills and required skills for a target occupation.
    *   Consider individual experience via a timing factor.
    *   Calculate a Synergy percentage to enhance the overall AI-R score.
*   **Learning Pathway Simulation**:
    *   Select from predefined learning pathways (e.g., Prompt Engineering, AI for Financial Analysis).
    *   Simulate the impact of pathway completion and mastery on individual capabilities ($V^R$) and the overall AI-R score.
    *   Compare current versus projected AI-R scores and their components.
*   **Dynamic Data Input & Visualization**: Utilize Streamlit sliders, select boxes, and data editors for interactive input, with immediate visualization of results using Plotly charts.
*   **Synthetic Data for Demonstration**: The application comes pre-loaded with synthetic data, making it ready to run and demonstrate without requiring external data uploads.

## 3. Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your system.
*   Python 3.7+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/quolab-ai-career-navigator.git
    cd quolab-ai-career-navigator
    ```
    (Replace `your-username/quolab-ai-career-navigator` with the actual repository path if it's hosted.)

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    Create a `requirements.txt` file in the root directory of your project with the following content:
    ```
    streamlit
    pandas
    numpy
    plotly
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## 4. Usage

To run the Streamlit application:

1.  Ensure your virtual environment is activated.
2.  Navigate to the project's root directory in your terminal.
3.  Execute the following command:

    ```bash
    streamlit run app.py
    ```

This will open the application in your default web browser (usually at `http://localhost:8501`).

**Basic Usage Flow:**

*   **Page 1: Introduction & Data**: View the project overview, adjust global $\alpha$ and $\beta$ parameters, and inspect the synthetic datasets used.
*   **Page 2: Idiosyncratic Readiness (V^R)**: Input your personal scores for various AI-Fluency, Domain-Expertise, and Adaptive-Capacity sub-components using sliders and select boxes. Click "Calculate V^R Score" to see your personal readiness and its breakdown.
*   **Page 3: Systematic Opportunity (H^R) & Simulation**:
    *   Select a "Target Occupation" to calculate market opportunity ($H^R$).
    *   Adjust `lambda` and `gamma` multipliers for market dynamics.
    *   Use the data editor to modify your individual skills and compare them against required skills for synergy calculation.
    *   Click "Calculate AI-Readiness Score" to get your overall AI-R score, including H^R and Synergy, and their contributions.
    *   In the "Pathway Simulation" section, select a learning pathway, adjust completion and mastery scores, and click "Simulate Pathway Impact" to see how it affects your AI-R score.

## 5. Project Structure

```
.
├── application_pages/
│   ├── __init__.py
│   ├── page1.py          # Introduction, global parameters, data display
│   ├── page2.py          # Idiosyncratic Readiness (V^R) inputs and calculations
│   ├── page3.py          # Systematic Opportunity (H^R), Synergy, AI-R, and pathway simulation
│   └── utils.py          # All core calculation functions and synthetic data generation
├── app.py                # Main Streamlit application entry point and navigation
└── requirements.txt      # List of Python dependencies
```

## 6. Technology Stack

*   **Python**: The primary programming language.
*   **Streamlit**: For building interactive web applications with pure Python.
*   **Pandas**: For data manipulation and analysis.
*   **Plotly**: For creating interactive visualizations and charts.
*   **NumPy**: For numerical operations, especially within calculation functions.

## 7. Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## 8. License

This project is licensed under the MIT License - see the `LICENSE` file for details (if applicable, otherwise state 'No License Specified').

## 9. Contact

For questions, feedback, or collaborations, please reach out:

*   **QuantUniversity (QuLab)**: [https://www.quantuniversity.com](https://www.quantuniversity.com)
*   **Project Maintainer**: (Your Name/Team Name or placeholder)
*   **Email**: [your.email@example.com](mailto:your.email@example.com) (or placeholder)

---

## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)
