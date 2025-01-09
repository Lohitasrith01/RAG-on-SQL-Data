import os
from google.cloud import aiplatform

# Initialize Vertex AI with environment variables
def initialize_vertex_ai():
    """
    Initialize Vertex AI with project and location from environment variables.
    """
    project_id = os.getenv("GCP_PROJECT_ID")  # Get project ID from environment variable
    location = os.getenv("GCP_LOCATION", "us-central1")  # Default to 'us-central1' if not set
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")  # Service account key path

    # Ensure credentials are set
    if not credentials_path:
        raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")

    # Initialize Vertex AI
    aiplatform.init(
        project=project_id,
        location=location
    )

def generate_sql(query):
    """
    Use Vertex AI's Large Language Model to generate SQL from a natural language query.
    """
    # Initialize Vertex AI
    initialize_vertex_ai()

    # Define the model to use (e.g., text-bison)
    model_name = "text-bison@001"  # Ensure the model is available in your region
    model = aiplatform.Model(model_name=model_name)

    # Use the model to generate a SQL query
    response = model.predict({
        "instances": [{"content": query}],  # Pass the user query
        "parameters": {
            "temperature": 0.2,             # Control randomness
            "maxOutputTokens": 256,         # Limit the output length
        },
    })

    # Extract and return the generated SQL
    generated_sql = response.predictions[0]["content"]
    return generated_sql

# Example usage
if __name__ == "__main__":
    user_query = "List all students with marks greater than 90."
    print("Generated SQL:", generate_sql(user_query))
