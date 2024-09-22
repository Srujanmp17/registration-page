from flask import *
app=Flask(__name__)

@app.route('/reg',methods=['POST','GET'])
def register():
    print(request.method)
    if request.method=="POST":
         name=request.form['name']
         age=request.form['age']
         email=request.form['email']
         phone=request.form['phone']
         father_name=request.form['father_name']
         mother_name=request.form['mother_name']
         course=request.form['course']
         return redirect(url_for('success'))
    else:
         return render_template('register.html')
         
@app.route('/sucess')
def success():
     return render_template('done.html')

if __name__=="__main__":
     app.run(debug=True)
         