from flask import Flask, render_template, url_for

app=Flask(__name__)

photos=[
        {'id':1,'filename':'cliff.jpeg','caption':"guy jumping from the cliff"},
        {'id':2,'filename':'strawberry.jpeg','caption':"strawberry is yummy"},
        {'id':3,'filename':'tiger.jpeg','caption':"tiger is walking"}

]
    
    
    

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html",photos=photos)

@app.route('/photo/<int:id>')
def photo(id):
    for photo in photos:
        if photo['id']==id:
            p=photo
            break
    return render_template('photo.html',photo=p)



if __name__=="__main__":
    app.run(debug=True)