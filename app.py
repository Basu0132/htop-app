from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get required details
    name = "Basavaraj Haravi"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    # Get IST Time
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get top command output (Linux/Mac)
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = str(e)

    # HTML Response
    response = f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time: {server_time}
    
    Top Output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
