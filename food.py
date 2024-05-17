import streamlit as st
import openai

from openai import AsyncOpenAI

# Set up the async OpenAI client
client = AsyncOpenAI(api_key=st.secrets["API_key"])

# Function to generate feedback for user inputs using OpenAI's API
async def generate_feedback(prompt, context):
    model = "gpt-3.5-turbo"
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Main application function
async def app():
    st.text("Submitted By:\n"
            "Rovalen Joy U. Calaguing\n"
            "BSCS 3A AI\n"
            "Intelligent Systems (CCS 229)\n"
            "West Visayas State University\n")
    
    # Display title and image
    st.title("Chefmate: A Culinary AI Assistant")
    st.image("Chefmate_img.png")

    # Introduction text
    st.write(
        """
        Welcome to Chefmate! Tell me what you're craving, any dietary preferences or restrictions, and I'll suggest the perfect recipe just for you. 
        Dive into a world of flavors tailored to your taste and nutritional needs.
        """
    )

    # System context for feedback generation
    system_context = "You are a friendly assistant providing brief and positive acknowledgments for user inputs."

    # Multi-level prompting: Step 1
    craving = st.text_input("What are you craving? (e.g., 'something sweet')")
    if craving:
        feedback = await generate_feedback(f"I'm craving {craving}. Please acknowledge positively.", system_context)
        st.write(feedback)

        # Multi-level prompting: Step 2
        cuisine_type = st.selectbox("Select a cuisine type", ['', 'American', 'Italian', 'Chinese', 'Indian', 'Mexican', 'Japanese', 'French', 'Thai', 'Other'])
        if cuisine_type:
            if cuisine_type == 'Other':
                other_cuisine = st.text_input("Please specify the cuisine type")
                if other_cuisine:
                    cuisine_type = other_cuisine
                    feedback = await generate_feedback(f"I want {cuisine_type} cuisine. Please acknowledge positively.", system_context)
                    st.write(feedback)
            else:
                feedback = await generate_feedback(f"I want {cuisine_type} cuisine. Please acknowledge positively.", system_context)
                st.write(feedback)

            # Multi-level prompting: Step 3
            dietary_restrictions = st.text_area("Any dietary restrictions or preferences? (e.g., 'low-carb, no peanuts, under 500 calories')")
            if dietary_restrictions:
                feedback = await generate_feedback(f"My dietary restrictions/preferences are: {dietary_restrictions}. Please acknowledge positively.", system_context)
                st.write(feedback)

                # Multi-level prompting: Step 4
                ingredients = st.text_input("Preferred ingredients (comma-separated)")
                if ingredients:
                    feedback = await generate_feedback(f"I prefer these ingredients: {ingredients}. Please acknowledge positively.", system_context)
                    st.write(feedback)

                    # Multi-level prompting: Step 5
                    skill_level = st.selectbox("Your cooking skill level", ['', 'Beginner', 'Intermediate', 'Advanced'])
                    if skill_level:
                        feedback = await generate_feedback(f"My cooking skill level is {skill_level}. Please acknowledge positively.", system_context)
                        st.write(feedback)
                        
                        # Context for AI generation based on the user's input
                        context = (f"Generate a recipe suggestion based on craving: {craving}, cuisine type: {cuisine_type}, "
                                f"dietary restrictions: {dietary_restrictions}, ingredients: {ingredients}, "
                                f"skill level: {skill_level}. Please include the nutritional information.")
                        question = "What should I cook?"

                        # Button to generate response
                        if st.button("Find Recipe"):
                            if question and context:
                                # Generate recipe suggestion
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

# Function to generate the recipe response
async def generate_response(question, context):
    model = "gpt-3.5-turbo"
    completion = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content

# Run the app
if __name__ == "__main__":
    import asyncio
    asyncio.run(app())
