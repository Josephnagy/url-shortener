from flask import Flask, render_template, request, redirect, url_for
import json
import os.path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {} #initialize url dict (key=shortened_url) : (value=real_url)

        #check if json file exists
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        #if shortened_url has already been used, return to homepage 
        if request.form['code'] in urls.keys():
            return redirect(url_for('home')) #redirect user back to homepage

        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home')) #redirect user back to homepage
