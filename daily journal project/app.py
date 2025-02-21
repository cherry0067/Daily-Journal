from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder for storing journal entries
journal_entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=journal_entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = request.form.get('entry')
    if entry:
        journal_entries.append(entry)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
