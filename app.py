from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def index():
    ans=""
    if request.method=="POST":
        name=request.form['name']
        age=request.form['age']
        if int(age)>=18:
            ans=f"{name} you can Vote"
        elif int(age)<0:
            ans="Invalid input"
        else:
            ans=f"{name} you can't Vote since you are age is below 18"
        
        return render_template('index.html',ans=ans)               
    return render_template('index.html')

    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 