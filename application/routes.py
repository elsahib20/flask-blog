from application.models import Posts
# import render_template function from the flask module
from flask import render_template, redirect, url_for
# import the app object from the ./application/__init__.py
from application import app, db
# import PostForm from application.forms
from application.forms import PostForm
# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 postData = Posts.query.all()
 return render_template('home.html', title='Home', posts=postData)
 
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    return render_template('register.html', title="Register")

@app.route('/posts', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('posts.html', title='Post', form=form)