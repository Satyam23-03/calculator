from pyngrok import ngrok
import subprocess
import time
import webbrowser

# Start the Flask server in a separate process
flask_process = subprocess.Popen(['py', 'app.py'])

try:
    # Create an HTTP tunnel on port 5000
    public_url = ngrok.connect(5000).public_url
    print(f' * Public URL: {public_url}')
    print(' * Share this URL with your friends!')
    print(' * Press Ctrl+C to stop')
    
    # Keep the script running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print('\n * Shutting down...')
    flask_process.terminate()
    ngrok.kill()
