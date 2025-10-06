# run.py
from app import app  # Import the Flask app instance from app/__init__.py

# This is needed for Vercel deployment
# Vercel will look for 'app' in this file

if __name__ == "__main__":
    # Only run the development server locally, not on Vercel
    app.run(host="0.0.0.0", port=5000, debug=True)
