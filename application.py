"""
This script runs the FlaskWebProject application using a development server.
"""

import os
from FlaskWebProject import app

if __name__ == '__main__':
    # Detect container or Azure environment
    if os.path.exists('/.dockerenv') or os.environ.get('WEBSITE_SITE_NAME'):
        HOST = '0.0.0.0'
        PORT = 5000
    else:
        HOST = os.environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(os.environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555

    # Use SSL only for local development
    if HOST == 'localhost':
        app.run(HOST, PORT, ssl_context='adhoc')
    else:
        app.run(HOST, PORT)
