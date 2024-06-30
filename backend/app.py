from flask import Flask, render_template, send_from_directory
import os
from dataFetchFile import textbooksData

textbooks_link = "https://docs.google.com/spreadsheets/d/1xI19BIX49dks6SqWn1H1IMq07ppVvrIS/export?format=csv"

file_path = "../frontend/public"
app = Flask(__name__, template_folder=file_path, static_url_path='/static', static_folder=file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(file_path, filename)

@app.route('/textbooks.html')
def textbooks():
    subs_count, subjects_info, textbooks = textbooksData(textbooks_link)
    
    return render_template("textbooks.html", subs_count = subs_count, subs_info = subjects_info, textbooks = textbooks)
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)