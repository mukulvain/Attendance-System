from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods = ['GET', 'POST'])
def index():

    if(request.method == 'GET'):
        return render_template('sentiment.html')
    else:
        text = request.form.get('text')
        polarity = TextBlob(text).polarity
        subjectivity = TextBlob(text).subjectivity
        return render_template('result.html', polarity=polarity,subjectivity=subjectivity)

if __name__ == "__main__":
    app.run(debug=True)