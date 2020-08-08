"""
Main module of the server file
"""

# 3rd party moudles
from app import connex_app

if __name__ == "__main__":
    connex_app.run(debug=True)
