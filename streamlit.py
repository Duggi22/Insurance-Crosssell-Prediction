import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('C://Users//satis//Desktop//Submission//trained_model.sav','rb'))
df = pickle.load(open('C://Users//satis//Desktop//Submission//df.pkl','rb'))

def prediction(Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium,Policy_Sales_Channel, Vintage ):
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1

    if Driving_License == "NO":
        Driving_License = 0
    elif Driving_License == "YES":
        Driving_License = 1

    if Previously_Insured == "NO":
        Previously_Insured = 0
    elif Previously_Insured == "YES":
        Previously_Insured = 1

    if Vehicle_Age == "0-12months":
        Vehicle_Age = 1
    elif Vehicle_Age == "13-24 Months":
        Vehicle_Age = 0
    elif Vehicle_Age == "More than 24 Months":
        Vehicle_Age = 2

    if Vehicle_Damage == "Yes":
        Vehicle_Damage = 1
    else:
        Vehicle_Damage = 0

    prediction = model.predict(
        [[Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium,Policy_Sales_Channel, Vintage]])
    if prediction == 0:
        pred = 'Target customer may not buy Vehicle Insurance from us'
    else:
        pred = 'Target customer is likely to buy Vehicle Insurance too from us '
    return pred


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:Orange;padding:25px"> 
    <h1 style ="color:Black;text-align:center;">  Health Insurance Cross Sell Prediction App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header('Enter the below details of the targeted customer ')
    Gender = st.selectbox('Gender', ('Male', 'Female'))
    Age = st.slider('Age', min_value=15, max_value=100, step=1)
    Previously_Insured = st.selectbox('Previously_Insured', ('YES', "NO"))
    Driving_License = st.selectbox('Driving licence', ('YES', "NO"))
    st.markdown('Unique code for the region of the customer')
    Region_Code = st.selectbox('Region_code', df['Policy_Sales_Channel'].unique())
    Vehicle_Age = st.selectbox('Vehicle_Age', ('0-12months', '13-24 Months', 'More than 24 Months'))
    Vehicle_Damage = st.selectbox('Did customer vehicle has been damaged previously', ('Yes', 'NO'))
    #Annual_Premium = st.number_input('Annual_Premium', min_value=5000, max_value=100000, step=500)
    Annual_Premium = st.number_input('Enter the Annual_Premium')
    st.markdown(
        'Policy Sales Channel - Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.')
    Policy_Sales_Channel = st.selectbox('Policy_Sales_Channel', df['Policy_Sales_Channel'].unique())
    st.markdown('Vintage - No.of months customer is with Company')
    Vintage = st.slider('Vintage', min_value=0, max_value=600, step=1)
    result = ""
    if st.button("Predict"):
        result = prediction(Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium,Policy_Sales_Channel, Vintage)
        st.success('  {}'.format(result))



if __name__=='__main__':
    main()