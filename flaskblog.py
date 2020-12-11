from flask import Flask, request, render_template

app = Flask(__name__)

posts = [
    {
        'author' : 'Amir Sahil',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : '12th December 2020'
    },
    {
        'author' : 'Dheeraj Ponnaganti',
        'title' : 'Blog Post 2',
        'content' : 'Secont post content',
        'date_posted' : '12th December 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', blogposts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug = True)