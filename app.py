from flask import Flask, request, render_template, jsonify
import logging
import os
from model.generator import BusinessPlanGenerator

# Configure logging
log_file = 'app.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class BusinessPlanError(Exception):
    """Custom exception for business plan generation errors."""
    pass

api_key = os.getenv('API_KEY')
generator = BusinessPlanGenerator(api_key)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST','GET'])
def generate():
    try:
        data = request.json
        if not data or 'business_idea' not in data:
            logging.error("Invalid input data: %s", data)
            return jsonify({"error": "Invalid input. Please provide a business idea."}), 400

        business_idea = data.get('business_idea')
        result = generator.generate_business_plan(business_idea)

        if result is None:
            raise BusinessPlanError("Business plan generation failed.")

        return jsonify(result), 200
    except UnsupportedMediaType:
        logging.error("Unsupported Media Type: Request must be JSON.")
        return jsonify({"error": "Unsupported Media Type. Please send a request with Content-Type 'application/json'."}), 415

    except BusinessPlanError as e:
        logging.error("Business plan generation error: %s", str(e))
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        logging.exception("An unexpected error occurred: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


if __name__ == '__main__':
    if not os.path.exists(log_file):
        open(log_file, 'w').close()  # Create the log file if it doesn't exist
    app.run(debug=True)
