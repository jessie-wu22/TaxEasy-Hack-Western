from flask import Flask, render_template, url_for, request, redirect
import os
from werkzeug.utils import secure_filename

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# route for home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/upload", methods=['GET','POST'])
def upload():
   
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    filename = ""
    for upload in request.files.getlist("file"):
        print(upload)
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("upload.html", image_name=filename)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


###### random code but it doesn't affect anything 
ButtonPressed = 0        
@app.route('/button', methods=["GET", "POST"])
def button():
    # sends data to backend for processing
    if request.method == "POST":
        ## GET request to backend
    
    # receives file from backend to download
    return render_template("button.html", ButtonPressed = ButtonPressed)




if __name__ == "__main__":
    app.run(port=4555, debug=True)




# import os

# from flask import Flask, request, render_template, send_from_directory

# __author__ = 'ibininja'

# app = Flask(__name__)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# @app.route("/")
# def index():
#     return render_template("upload.html")


# @app.route("/upload", methods=['POST'])
# def upload():
   
#     target = os.path.join(APP_ROOT, 'images/')
#     print(target)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#     for upload in request.files.getlist("file"):
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#         # This is to verify files are supported
#         ext = os.path.splitext(filename)[1]
#         if (ext == ".jpg") or (ext == ".png"):
#             print("File supported moving on...")
#         else:
#             render_template("Error.html", message="Files uploaded are not supported...")
#         destination = "/".join([target, filename])
#         print("Accept incoming file:", filename)
#         print("Save it to:", destination)
#         upload.save(destination)

#     # return send_from_directory("images", filename, as_attachment=True)
#     return render_template("complete.html", image_name=filename)


# @app.route('/upload/<filename>')
# def send_image(filename):
#     return send_from_directory("images", filename)


# if __name__ == "__main__":
#     app.run(port=4555, debug=True)
