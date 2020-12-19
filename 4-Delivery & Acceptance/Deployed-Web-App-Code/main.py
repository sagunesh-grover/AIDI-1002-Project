import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import csv
import glob
import joblib
import pandas as pd
import logging
import sys
import sklearn


# logging to Heroku to debug runtime errors
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        im = cv2.imread(image_path)
        im = cv2.GaussianBlur(im,(5,5),2) 
        #cv2.imwrite('static/uploads/'+filename+'_GaussianBlur.png', im)
        #convert to grayscale image
        im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        #cv2.imwrite('static/uploads/'+filename+'_Gray.png', im_gray)
        ret,thresh = cv2.threshold(im_gray,127,255,0)
        #cv2.imwrite('static/uploads/'+filename+'_White.png', thresh)
        contours,_ = cv2.findContours(thresh,1,2)    
        for contour in contours:
            cv2.drawContours(im_gray, contours, -1, (0,255,0), 3)
        #cv2.imwrite('static/uploads/'+filename+'_Contour.png', im_gray)
        #cv2.imshow("window",im_gray)
        area_list = []
        for i in range(5):
            try:
                area = cv2.contourArea(contours[i])
                area_list.append(str(area))
            except:
                area_list.append(str(0))
                
        area = pd.DataFrame(area_list).T

        #run the model
        #convert image to a vector
        

        #load model from disk
        model = joblib.load(r'model/rf2_malaria_detector.pkl')

        prediction = model.predict(area)[0]

        #flash(prediction)
        res = ""
        if prediction == 'Parasitized':
            res = "Has Malaria"
        else:
            res = "Does Not have Malaria"


        flash("This Person "+res)
                
        


        #flash(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        #flash('Image successfully uploaded and displayed')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run()