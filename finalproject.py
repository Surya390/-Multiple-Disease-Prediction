# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:24:14 2023

@author: adity
"""

import pandas as pd
import joblib
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("D:/GIET Project/models/final_diabetic_model_project.sav", 'rb'))

heart_disease_model = pickle.load(open("D:/GIET Project/models/final_heart_disease_model_project.sav",'rb'))

parkinsons_model = pickle.load(open("D:/GIET Project/models/final_parkinsons_model_project.sav", 'rb'))

breast_model = pickle.load(open("D:/GIET Project/models/final_breast_cancer_model_project.sav", 'rb'))

stroke_model= pickle.load(open("D:/GIET Project/models/final_stroke_model_project.sav", 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction','Breast Cancer Prediction','Stroke Prediction'],icons=['bandaid','heart','medical','person','person'],
                          default_index=0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = """The person is diabetic 
          
Diet:
1.Follow a balanced diet rich in vegetables, lean proteins, whole grains, and healthy fats.
2.Monitor carbohydrate intake and focus on complex carbohydrates with a low glycemic index.
3.Limit sugary foods and beverages, including desserts, sodas, and fruit juices.
4.Control portion sizes to manage blood sugar levels and weight.

Physical Activity:
1.Engage in regular exercise, aiming for at least 150 minutes of moderate-intensity aerobic activity per week.
2.Incorporate strength training to improve muscle mass and metabolism.
3.Consult a healthcare professional before starting a new exercise routine.

Medication and Monitoring:
1.Take prescribed medications as directed by your healthcare provider.
2.Monitor blood sugar levels regularly using a glucose meter.
3.Keep track of your results and share them with your healthcare team.

Lifestyle:
1.Aim for consistent sleep patterns, aiming for 7-9 hours of quality sleep each night.
2.Manage stress through relaxation techniques like deep breathing, meditation, or yoga.
3.Avoid smoking and limit alcohol consumption.

Hydration:
1.Drink plenty of water throughout the day to stay hydrated.

Regular Check-ups:
1.Schedule regular visits with your healthcare team, including your doctor, endocrinologist, and dietitian.

Foot Care:
1.Inspect your feet daily for any cuts, sores, or changes. Report any issues to your healthcare provider.

Emergency Preparedness:
1.Keep a source of fast-acting sugar (like glucose tablets) with you in case of low blood sugar (hypoglycemia).
2.Wear a medical alert bracelet indicating you have diabetes.

Education and Support:
1.Learn about diabetes management through reputable sources and classes.
2.Seek support from friends, family, or support groups to stay motivated and informed."""
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect.')
        
        
     
   # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = """The person is having heart disease


Some Precautions are

1.Medical Consultation: Schedule regular check-ups with a healthcare provider, especially if there is a family history of heart disease or if you are experiencing symptoms such as chest pain, shortness of breath, or fatigue.

2.Healthy Diet: Adopt a heart-healthy diet rich in fruits, vegetables, whole grains, lean proteins, and low-fat dairy products. Limit the intake of saturated and trans fats, cholesterol, salt, and added sugars.

3.Regular Exercise: Engage in regular physical activity. Aim for at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous-intensity aerobic exercise per week, along with muscle-strengthening activities on two or more days a week.

4.Maintain a Healthy Weight: Achieve and maintain a healthy weight through a combination of a balanced diet and regular physical activity.

5.Quit Smoking: If you smoke, quitting is one of the most significant steps you can take to improve heart health. Smoking is a major risk factor for heart disease.

6.Limit Alcohol Consumption: If you choose to drink alcohol, do so in moderation. This typically means up to one drink per day for women and up to two drinks per day for men.

7.Manage Stress: Practice stress-reduction techniques such as deep breathing, meditation, yoga, or other activities that help promote relaxation.

8.Take Medications as Prescribed: If prescribed medications for heart conditions, take them as directed by your healthcare provider. Follow up regularly to monitor their effectiveness and any potential side effects.

9.Monitor Blood Pressure and Cholesterol Levels: Regularly check and manage blood pressure and cholesterol levels as advised by your healthcare provider. High blood pressure and high cholesterol are significant risk factors for heart disease.

10.Get Enough Sleep: Aim for 7-9 hours of quality sleep each night. Poor sleep can contribute to various health issues, including heart problems.       
          
          """
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz) Average vocal fundamental frequency')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz) Maximum vocal fundamental frequency')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)  Minimum vocal fundamental frequency')
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)  Several measures of variation in fundamental frequency')
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)  Several measures of variation in fundamental frequency')
        
    with col1:
        RAP = st.number_input('MDVP:RAP  Several measures of variation in fundamental frequency')
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ  Several measures of variation in fundamental frequency')
        
    with col3:
        DDP = st.number_input('Jitter:DDP  Several measures of variation in fundamental frequency')
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer ( Several measures of variation in amplitude)')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)  Several measures of variation in amplitude')
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3 ( Several measures of variation in amplitude)')
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5 ( Several measures of variation in amplitude)')
        
    with col3:
        APQ = st.number_input('MDVP:APQ ( Several measures of variation in amplitude)')
        
    with col4:
        DDA = st.number_input('Shimmer:DDA ( Several measures of variation in amplitude)')
        
    with col5:
        NHR = st.number_input('NHR (Two measures of ratio of noise to tonal components in the voice)')
        
    with col1:
        HNR = st.number_input('HNR (Two measures of ratio of noise to tonal components in the voice)')
        
    with col2:
        RPDE = st.number_input('RPDE (Two nonlinear dynamical complexity measures)')
        
    with col3:
        DFA = st.number_input('DFA (Signal fractal scaling exponent)')
        
    with col4:
        spread1 = st.number_input('spread1 ( Three nonlinear measures of fundamental frequency variation)')
        
    with col5:
        spread2 = st.number_input('spread2 ( Three nonlinear measures of fundamental frequency variation)')
        
    with col1:
        D2 = st.number_input('D2 (Two nonlinear dynamical complexity measures)')
        
    with col2:
        PPE = st.number_input('PPE (Three nonlinear measures of fundamental frequency variation)')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = """The person has Parkinson's disease
          
 Some Precautions are

1.Medication Adherence: Follow the prescribed medication regimen provided by your healthcare professional. Consistent use of prescribed medications is crucial for managing symptoms effectively.

2.Regular Medical Check-ups: Schedule regular check-ups with your healthcare provider to monitor the progression of the disease and adjust treatment plans as needed.

3.Exercise Regularly: Engage in regular physical activity, as it can help improve flexibility, balance, and overall mobility. Consult with a physical therapist to develop an exercise plan tailored to your needs and abilities.

4.Maintain a Healthy Diet: A balanced and nutritious diet is important for overall health. Consider consulting with a dietitian to ensure you are getting the right nutrients and managing any potential swallowing difficulties.

5.Fall Prevention: Due to balance and coordination issues associated with Parkinson's disease, take precautions to prevent falls. This may include removing tripping hazards in the home, using handrails, and considering assistive devices if needed.

6.Speech and Swallowing Therapy: If you experience speech or swallowing difficulties, consider working with a speech therapist who specializes in Parkinson's disease. They can provide exercises and strategies to enhance communication and manage swallowing issues.

7.Manage Stress: Stress can exacerbate symptoms of Parkinson's disease. Incorporate stress-reducing activities into your routine, such as mindfulness, relaxation techniques, or hobbies that bring you joy.

8.Adapt the Environment: Make your living space more Parkinson's-friendly by installing grab bars, ramps, or other modifications that enhance safety and accessibility.

9.Stay Socially Connected: Maintain social connections with friends, family, and support groups. Emotional well-being is an essential aspect of managing Parkinson's disease.

10.Prioritize Sleep: Ensure you get adequate and quality sleep. Establish a bedtime routine and create a comfortable sleep environment to support good sleep hygiene.

11.Stay Informed: Stay informed about Parkinson's disease, its symptoms, and the latest research. Knowledge empowers individuals and their caregivers to make informed decisions about treatment and lifestyle adjustments.         
          
          """
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
   
    
    
    
# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
        
    with col2:
        mean_texture = st.text_input('Mean Texture')
    
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')
    
    with col1:
        mean_area = st.text_input('Mean Area')
    
    with col2:
        mean_smoothness = st.text_input('Mean Smoothness')
    

    
    
    # code for Prediction
    breast_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breast_prediction = breast_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_texture]])
        
        if (breast_prediction[0] == 1):
          breast_diagnosis = """The person is suffered in Breast Cancer
          
          
              Certainly, here are some breast cancer prevention steps :

- **Regular Self-Exams:** Perform monthly breast self-exams to detect any changes or abnormalities.

- **Clinical Breast Exams:** Have regular clinical breast exams by a healthcare provider as recommended by your age and risk factors.

- **Mammograms:** Schedule mammograms at the recommended intervals, typically starting at age 40 or earlier if you have higher risk factors.

- **Healthy Lifestyle:** Adopt a healthy lifestyle, including:
  - **Diet:** Maintain a balanced diet with plenty of fruits and vegetables.
  - **Exercise:** Engage in regular physical activity, aiming for at least 150 minutes per week.
  - **Limit Alcohol:** If you consume alcohol, do so in moderation or consider eliminating it.
  - **Quit Smoking:** If you smoke, seek assistance to quit smoking.

- **Breastfeeding:** If you have the opportunity, consider breastfeeding, as it may reduce breast cancer risk.

- **Hormone Therapy:** Discuss the risks and benefits of hormone replacement therapy with your healthcare provider, and use it only when necessary.

- **Know Your Family History:** Understand your family's history of breast cancer and other cancers. This information can help you and your healthcare provider assess your risk.

- **Genetic Testing:** Consider genetic testing if you have a strong family history of breast cancer or other risk factors that suggest a higher genetic risk.

- **Maintain a Healthy Weight:** Aim to maintain a healthy body weight, as obesity is linked to an increased risk of breast cancer, especially after menopause.

- **Limit Exposure to Environmental Toxins:** Minimize exposure to environmental toxins and chemicals that may be linked to breast cancer risk.

- **Breast Health Education:** Educate yourself about breast health, risk factors, and the importance of early detection.

- **Regular Healthcare:** Attend regular healthcare check-ups and screenings, not just for breast cancer but for overall health and wellness.

Remember that while these steps can help reduce your risk, they cannot guarantee prevention. It's important to consult with a healthcare professional for personalized advice and to create a breast health plan tailored to your individual risk factors and needs."""
        else:
          breast_diagnosis = 'The person is not suffered in breast cancer'
        
    st.success(breast_diagnosis)   



# Stroke Prediction Page
if (selected == 'Stroke Prediction'):
    
    # page title
    st.title('Stroke Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.number_input('Enter the Gender Type: \
                               1=Male\
                               0=Female')
        
    with col2:
        age = st.number_input('Enter Your Age')
    
    with col3:
        hypertension = st.number_input('Enter if You have hypertension\
                                     yes=1\
                                     No=0')
    
    with col1:
        heart_disease = st.number_input('Heart Disease Status\
                                      yes=1\
                                      N0=0')
    
    with col2:
        ever_married= st.number_input('Enter Your maratial Status\
                                    yes=1\
                                    No=0')
    
    with col3:
        work_type = st.number_input('Enter Your workType\
                                  Govt Job=0\
                                  private=2\
                                 self employed=3'\
                                     )
    
    with col1:
        residence_type = st.number_input('Diabetes Pedigree Function value\
                                       Urban=1\
                                       Rural=0')
    
    with col2:
        avg_glucose_level = st.number_input('Enter Average Glucose Level')
         
    with col3:
        bmi = st.number_input('BMI value', key='bmi_input')   
        
    with col1:
        smoking_status=st.number_input("smoking Status\
                                     Unknown=0\
                                    formerly smoked=1\
                                        never smoked=2\
                                            smokes=3")
    
    
    # code for Prediction
    stroke_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Stroke Test Result'):
        stroke_prediction = stroke_model.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status]])
        
        if (stroke_prediction[0] == 1):
          stroke_diagnosis = """The person is suffered in Stroke Diagnosis
          
          
          Certainly, here are some key steps for stroke prevention in bullet point format:

- **Blood Pressure Control:**
  - Monitor your blood pressure regularly.
  - Maintain a healthy lifestyle with a balanced diet, regular exercise, and limited salt intake.
  - Take prescribed medications if you have high blood pressure.

- **Healthy Diet:**
  - Eat a diet rich in fruits, vegetables, whole grains, and lean proteins.
  - Limit saturated and trans fats, as well as cholesterol.
  - Control portion sizes to manage weight.

- **Regular Physical Activity:**
  - Engage in at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous-intensity aerobic exercise per week.
  - Include strength training exercises in your routine.

- **Maintain a Healthy Weight:**
  - Aim for a healthy body mass index (BMI) through diet and exercise.

- **Quit Smoking:**
  - If you smoke, seek support to quit.
  - Avoid exposure to secondhand smoke.

- **Limit Alcohol Intake:**
  - Consume alcohol in moderation, if at all.
  - Women should limit to one drink per day, and men to two drinks per day.

- **Manage Diabetes:**
  - If you have diabetes, keep blood sugar levels under control through medication, diet, and exercise.

- **Medication Adherence:**
  - If prescribed medications (such as blood thinners) to reduce stroke risk, take them as directed.

- **Regular Healthcare Check-Ups:**
  - Attend regular medical check-ups and follow your healthcare provider's advice.

- **Manage Atrial Fibrillation (AFib):**
  - If you have AFib, work with your healthcare provider to manage and treat it effectively.

- **Manage Other Health Conditions:**
  - Control other chronic health conditions like high cholesterol and heart disease.

- **Healthy Lifestyle Choices:**
  - Manage stress through relaxation techniques, mindfulness, and hobbies.
  - Get enough sleep to promote overall health.

- **Stay Informed:**
  - Educate yourself and your loved ones about the signs and symptoms of stroke and act quickly if they occur.

- **Home Safety:**
  - Make your home safer by reducing fall hazards, securing handrails, and using non-slip mats in the bathroom.

- **Stroke Risk Assessment:**
  - Understand your personal stroke risk factors and discuss them with your healthcare provider to create a tailored prevention plan.

Stroke prevention is essential for maintaining good health and well-being. Consult with a healthcare provider for personalized guidance and recommendations based on your specific health profile and risk factors.
          """
        else:
          stroke_diagnosis = 'The person is not suffered in stroke diagnosis'
        
    st.success(stroke_diagnosis)


