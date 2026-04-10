from flask import Flask, render_template
from events import events as list_events

app = Flask(__name__)

@app.route('/')
@app.route('/events')
def events():
    events_sort = sorted(list_events, key=lambda event: event['time'])
    return render_template('events.html', events=events_sort)


app.run(debug=True)