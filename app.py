from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'john Doe',
        'title': 'Blog Post',
        'content': 'first blog content',
        'date': 'August 17, 2018'                    
    },
    {
        'author':'jane Doe',
        'title': 'Blog Post',
        'content': 'first blog content',
        'date': 'August 17, 2018'                    
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)    