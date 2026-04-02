from flask import Flask,render_template # The Flask,render_template class is importing from the flask to create a web applications from Flask and to connect to pass to code to html reder_template
app=Flask(__name__) # app is Flask instance. __name__ tells to Flask where the application located so the flask can resource the web application



@app.route('/')
def home_page():
    return render_template("home.html",name="Divya Manikaran",company="Velon company")

@app.route('/home')
def home():
    return render_template("home.html",name="Divya Manikaran",company="Velon company")

@app.route('/about')
def about():
    return render_template("about.html",name="Divya Manikaran",company="Velon company")

@app.route('/contact')
def contact():
    return render_template("contact.html",name="Divya Manikaran",company="Velon company")

if __name__ =="__main__" :
    app.run(debug=True)