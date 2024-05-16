import streamlit as st
import openai

from openai import AsyncOpenAI

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
        st.success(f"Yum! You're craving {craving}. That sounds delicious!")

        # Multi-level prompting: Step 2
        cuisine_type = st.selectbox("Select a cuisine type", ['', 'American', 'Italian', 'Chinese', 'Indian', 'Mexican', 'Japanese', 'French', 'Thai', 'Other'])

        if cuisine_type:
            if cuisine_type == 'Other':
                other_cuisine = st.text_input("Please specify the cuisine type")
                if other_cuisine:
                    cuisine_type = other_cuisine
                    st.success(f"Great choice! We'll go with {cuisine_type} cuisine.")
            else:
                st.success(f"Awesome! {cuisine_type} cuisine is a fantastic choice.")

            # Multi-level prompting: Step 3
            calories = st.text_input("Preferred calorie range")
            if calories:
                st.success(f"Got it! We'll aim for around {calories} calories per serving.")

                # Multi-level prompting: Step 4
                ingredients = st.text_input("Preferred ingredients (comma-separated)")
                if ingredients:
                    st.success(f"Perfect! We'll include these ingredients: {ingredients}.")

                    allergies = st.text_input("Any allergies? Type 'none' if you have no allergies.")
                    if allergies:
                        if allergies.lower() == 'none':
                            st.success("Great! You don't have any allergies to worry about.")
                        else:
                            st.success(f"Thanks for letting us know. We'll avoid these allergens: {allergies}.")

                        nutritional_goals = st.text_input("Nutritional goals (e.g., low-carb, high-protein)")
                        if nutritional_goals:
                            st.success(f"Excellent! We'll keep your goal of {nutritional_goals} in mind.")

                            skill_level = st.selectbox("Your cooking skill level", ['', 'Beginner', 'Intermediate', 'Advanced'])
                            if skill_level:
                                st.success(f"Great! We'll tailor the recipe to your {skill_level} cooking skills.")
                            
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
                                        st.write("Here's a delicious recipe just for you!")
                                        st.write(recipe)
                                        st.write("Nutritional Information per Serving:")
                                        nutrition_details = nutrition.replace(',', '\n').strip()
                                        st.markdown(nutrition_details, unsafe_allow_html=True)
                                        st.balloons()  # Celebrate the suggestion with balloons
                                    else:
                                        st.error("Please make sure you don't leave any field blank.")

# Run the app
if __name__ == "__main__":
    import asyncio
    asyncio.run(app())