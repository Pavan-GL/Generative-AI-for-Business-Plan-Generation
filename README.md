# Business Plan Generator

A web application that utilizes generative AI to assist entrepreneurs in creating comprehensive business plans. This tool guides users through key components and generates text based on their business ideas.

## Features

- User-friendly interface for inputting business ideas.
- Generates structured business plans including executive summary, market analysis, and financial projections.
- Real-time text generation using OpenAI's language model.
- Export and copy options for generated plans.

## Technologies Used

- **Backend**: Flask (Python)
- **AI Model**: OpenAI's GPT-3.5 Turbo
- **Frontend**: HTML, CSS, JavaScript
- **Database**: (Optional, if you choose to implement user data storage)

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- OpenAI API Key

## Installation

1. Clone the repository:

   ```bash
   git clone https://gitlab.com/yourusername/business-plan-generator.git
   cd business-plan-generator


Install the required dependencies:


pip install -r requirements.txt
Set up your OpenAI API key:

Open model/generator.py and replace 'YOUR_OPENAI_API_KEY' with your actual API key.
Usage
Run the Flask application:

python app.py
Open your web browser and go to http://127.0.0.1:5000.

Enter your business idea in the provided text area and click the "Generate Business Plan" button.

The generated business plan will be displayed below.