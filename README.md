# CCS 229 Intelligent Systems: Final Project

## Submitted By:
Rovalen Joy U. Calaguing <br>
BSCS 3A AI <br>
West Visayas State University <br>

## Project Title: Chefmate: Crafted for Your Cravings

## Project Overview
<div align="justify">
Chefmate is a generative AI application developed for the final project of the CCS 229 Intelligent Systems course. This intelligent system interacts with users through multi-level prompting and leverages OpenAI's GPT-3.5-turbo API to generate customized food recommendations. Users can input their craving type, calorie preferences, ingredient preferences, allergies, nutritional goals, and cooking skill level to receive personalized recipes.
</div>

## Features
- **Multi-level Prompting**: Chefmate uses a series of sequential prompts to gather detailed user input. Initially, users specify their cravings (e.g., "something sweet"), followed by selecting a cuisine type (e.g., "Italian", "Mexican"). Further refinement includes setting a preferred calorie range through a slider, specifying preferred ingredients, listing any allergies, stating nutritional goals (e.g., "low-carb"), and indicating their cooking skill level (e.g., "Beginner"). This step-by-step approach ensures a comprehensive understanding of user preferences.
- **GPT-3.5 Integration**: Utilizes OpenAI's GPT-3.5 API to generate creative and personalized text formats based on user inputs.
- **Success Messages**: Chefmate provides informative success messages at each step of the multi-level prompting process, acknowledging the user's inputs and confirming their selections.
- **Celebratory Animation**: Upon generating a recipe, Chefmate celebrates the suggestion with animated balloons, adding a delightful touch to the user experience.
- **User-Friendly Interface**: Developed using Streamlit, the interface is intuitive and easy to navigate, providing a seamless user experience.

## Setup and Installation
### Prerequisites
- Python 3.1
- Streamlit
- OpenAI API key
