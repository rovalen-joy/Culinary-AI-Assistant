import streamlit as st
import openai

from openai import AsyncOpenAI
from openai import OpenAI

# Set up the async OpenAI client
client = AsyncOpenAI(api_key=st.secrets["API_key"])

async def generate_response(question, context):
    model = "gpt-3.5-turbo"

    completion = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question},
                  {"role": "system", "content": context}]
    )
    return completion.choices[0].message.content

async def app():
    st.text("Submitted By:\n"
            "Rovalen Joy U. Calaguing\n"
            "BSCS 3A AI\n"
            "Intelligent Systems (CCS 229)\n"
            "West Visayas State University\n")
    
    st.title("Chefmate: A Culinary AI Assistant")
    
    st.image("Chefmate_img.png")

    st.write(
        """
        Welcome to Chefmate! Tell me what you're craving, any dietary preferences or restrictions, and I'll suggest the perfect recipe just for you. 
        Dive into a world of flavors tailored to your taste and nutritional needs.
        """
    )

    # Multi-level prompting: Step 1
    craving = st.text_input("What are you craving? (e.g., 'something sweet')")

    if craving:
        # Multi-level prompting: Step 2
        cuisine_type = st.selectbox("Select a cuisine type", ['Any', 'American', 'Italian', 'Chinese', 'Indian', 'Mexican', 'Japanese', 'French', 'Thai', 'Other'])

        # Display an additional text input field if the user selects 'Other'
        if cuisine_type == 'Other':
            other_cuisine = st.text_input("Please specify the cuisine type")
            if other_cuisine:
                cuisine_type = other_cuisine

        #Multi-level prompting: Step 3
        calories = st.slider("Preferred calorie range", 100, 1000, 500)

        #Multi-level prompting: Step 4
        ingredients = st.text_input("Preferred ingredients (comma-separated)")
        allergies = st.text_input("Any allergies?")
        nutritional_goals = st.text_input("Nutritional goals (e.g., low-carb, high-protein)")
        skill_level = st.selectbox("Your cooking skill level", ['Beginner', 'Intermediate', 'Advanced'])

      # Context for AI generation based on the user's input
        context = (f"Generate a recipe suggestion based on craving: {craving}, cuisine type: {cuisine_type}, "
                f"calorie limit: {calories}, ingredients: {ingredients}, allergies: {allergies}, "
                f"nutritional goals: {nutritional_goals}, skill level: {skill_level}. "
                "Please include the nutritional information.")
        question = "What should I cook?"

        # Button to generate response
        if st.button("Find Recipe"):
            if question and context:
                response = await generate_response(question, context)
                recipe, nutrition = response.split('\n\n', 1)
                st.write("Suggested Recipe:")
                st.write(recipe)
                st.write("Nutritional Information per Serving:")
                nutrition_details = nutrition.replace(',', '\n').strip()
                st.markdown(nutrition_details, unsafe_allow_html=True)
            else:
                st.error("Please make sure you don't leave any field blank.")


# Run the app
if __name__ == "__main__":
    import asyncio
    asyncio.run(app())
