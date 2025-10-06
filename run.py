from app import app  # assuming your __init__.py creates Flask app

# Expose app for Vercel
app = app

if __name__ == "__main__":
    app.run(debug=True)
