import os
import shutil

# Base directory of the application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Use /tmp for Vercel compatibility (read-only file system)
# Check if running on Vercel (or similar serverless environment)
IS_SERVERLESS = os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME')

if IS_SERVERLESS:
    # Use /tmp directory for serverless environments
    METAR_DATA_DIR = '/tmp/metar_data'
    UPPER_AIR_DATA_DIR = '/tmp/upper_air_data'
else:
    # Use local app directory for development
    METAR_DATA_DIR = os.path.join(BASE_DIR, 'app', 'static', 'metar_data')
    UPPER_AIR_DATA_DIR = os.path.join(BASE_DIR, 'app', 'static', 'upper_air_data')

# Clean the directory only if not in serverless environment
if not IS_SERVERLESS:
    if os.path.exists(METAR_DATA_DIR):
        shutil.rmtree(METAR_DATA_DIR, ignore_errors=True)
    
    if os.path.exists(UPPER_AIR_DATA_DIR):
        shutil.rmtree(UPPER_AIR_DATA_DIR, ignore_errors=True)

# Create the directory if it doesn't exist
try:
    os.makedirs(METAR_DATA_DIR, exist_ok=True)
    os.makedirs(UPPER_AIR_DATA_DIR, exist_ok=True)
except (OSError, PermissionError) as e:
    # If directory creation fails in serverless, directories will be created on-demand
    print(f"Warning: Could not create directories on startup: {e}") 