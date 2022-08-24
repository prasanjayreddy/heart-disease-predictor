# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 11:34:10 2021

@authors: BAASHITH and PRASANJAY
"""

from flask import Flask,redirect,url_for,render_template,request
import pickle
import pandas as pd
import sklearn




app= Flask (__name__)
loaded_modell = pickle.load(open("predict-HeartDisease.pkl","rb"))

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
            
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        
        Sex = request.form['Sex']
        if (Sex == 'F') :
            Sex_F = 1
            Sex_M = 0
        else :
            Sex_F = 0
            Sex_M = 1
            
        ChestPainType = request.form['ChestPainType']
        if (ChestPainType == 'ASY') :
            ChestPainType_ASY = 1
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA = 0
        elif (ChestPainType == 'ATA') :
            ChestPainType_ASY = 0
            ChestPainType_ATA = 1
            ChestPainType_NAP = 0
            ChestPainType_TA = 0
        elif (ChestPainType == 'NAP') :
            ChestPainType_ASY = 0
            ChestPainType_ATA = 0
            ChestPainType_NAP = 1
            ChestPainType_TA = 0
        else :
            ChestPainType_ASY = 0
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA = 1
            
        RestingBP = int(request.form['RestingBP'])
        
        Cholesterol = int(request.form['Cholesterol'])
        
        FastingBS = int(request.form['FastingBS'])
            
        RestingECG = request.form['RestingECG']
        if(RestingECG == 'LVH') :
            RestingECG_LVH = 1
            RestingECG_Normal = 0
            RestingECG_ST = 0
        elif (RestingECG == 'Normal') :
            RestingECG_LVH = 0
            RestingECG_Normal = 1
            RestingECG_ST = 0
        else :
            RestingECG_LVH = 0
            RestingECG_Normal = 0
            RestingECG_ST = 1
            
        MaxHR = int(request.form['MaxHR'])
            
        ExerciseAngina = request.form['ExerciseAngina']
        if(ExerciseAngina == 'N') :
            ExerciseAngina_N = 1
            ExerciseAngina_Y = 0
        else :
            ExerciseAngina_N = 0
            ExerciseAngina_Y = 1
            
        
        Oldpeak = float(request.form['Oldpeak'])
        
        ST_Slope = request.form['ST_Slope']
        if(ST_Slope == 'Down' ) :
            ST_Slope_Down = 1
            ST_Slope_Flat = 0
            ST_Slope_Up = 0
        elif (ST_Slope == 'Flat') :
            ST_Slope_Down = 0
            ST_Slope_Flat = 1
            ST_Slope_Up = 0
        else :
            ST_Slope_Down = 0
            ST_Slope_Flat = 0
            ST_Slope_Up = 1
        
        final_prediction=loaded_modell.predict([[Age, Sex_F, Sex_M, ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingBP, Cholesterol, FastingBS, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, MaxHR, ExerciseAngina_N, ExerciseAngina_Y, Oldpeak, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up]])
    
        
        if (final_prediction == 1) :
            return render_template('index.html',prediction_texts="The Person has Heart Disease {}".format(final_prediction))
        else :
            return render_template('index.html',prediction_texts="The Person Doesnot has Heart Disease {}".format(final_prediction))
        
    else:
        return render_template('index.html')
        
                   
if __name__=='__main__':
    app.run()