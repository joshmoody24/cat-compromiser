import datetime

app = Flask(__name__)

# File to store POST request data
DATA_FILE = 'data.txt'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Append the POST data to the file
        with open(DATA_FILE, 'a') as file:
            file.write(str(datetime.datetime.now()) + '\n' + request.data.decode() + '\n')

    # Read the content of the file to display
    content = []
    with open(DATA_FILE, 'r') as file:
        content = file.readlines()

    # Render the content in a list on a simple webpage
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cat Listener</title>
        </head>
        <body>
            <h1>Remote Cat Logs</h1>
            {% for line in content %}
            {{ line }}
            <br>
            {% endfor %}
        </body>
        </html>
    ''', content=content)

if __name__ == '__main__':
    app.run(debug=True)
