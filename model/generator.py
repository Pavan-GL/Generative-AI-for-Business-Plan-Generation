import openai
import logging
import os
# Configure logging
log_file = 'business_plan_generator.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class OpenAIAPIError(Exception):
    """Custom exception for OpenAI API errors."""
    pass


class BusinessPlanGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_business_plan(self, business_idea):
        prompt = (
            f"Create a comprehensive business plan for the following idea: {business_idea}. "
            "Include sections like executive summary, market analysis, and financial projections."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content']

        except Exception as e:
            logging.exception("An unexpected error occurred: %s", str(e))
            raise OpenAIAPIError("An unexpected error occurred while generating the business plan.")


# Example usage
if __name__ == '__main__':
    api_key = os.getenv('API_KEY')
    generator = BusinessPlanGenerator(api_key)

    try:
        business_idea = "Wholesale cloth sale"
        business_plan = generator.generate_business_plan(business_idea)
        print(business_plan)

    except OpenAIAPIError as e:
        print(f"Error: {str(e)}")
