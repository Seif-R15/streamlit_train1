import streamlit as st
import pandas as pd

st.title('Customer Churn Prediction')

st.image("https://imgs.search.brave.com/QY0-mh6pmbOCiNC3h1K6OB_T7xdTkEJiVuvKcd_J6CE/rs:fit:1100:700:1/g:ce/aHR0cHM6Ly9uZXdz/ZGFpbHlhcnRpY2xl/cy5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMjAvMDkvNS1F/ZmZlY3RpdmUtVGlw/cy1Uby1SZWR1Y2Ut/Q3VzdG9tZXItQ2h1/cm4uanBn")

df = pd.DataFrame({'What is Churn':['Churn is'],'What can we do':'you can do'})
st.write(df)


x = st.metric('Sales',2500,-12)

gender = st.radio('Gender',('Male','Female'))

SeniorCitizen = st.radio('SeniorCitizen Type',(0,1))

Partner = st.radio('Is There a Partner',('Yes', 'No'))

Dependents = st.radio('Are There Dependents',('Yes', 'No'))

tenure = st.slider('tenure',0,150,50)
st.write('You Choose',tenure)

PhoneService = st.radio('Is There PhoneService',('Yes', 'No'))

MultipleLines = st.selectbox('What is Your MultipleLines Status',('Yes', 'No','No Phone Service'))

InternetService = st.selectbox('InternetService Type',('Fiber optic','DSL','No'))

OnlineSecurity = st.selectbox('OnlineSecurity Type',('Yes', 'No','No Internet Service'))

OnlineBackup = st.selectbox('Online BackUp Type',('Yes', 'No','No Internet Service'))

DeviceProtection = st.selectbox('Device Protection Type',('Yes', 'No','No Internet Service'))

TechSupport = st.selectbox('Device Tech Support Type',('Yes', 'No','No Internet Service'))

StreamingTV = st.selectbox('Streaming TV Type',('Yes', 'No','No Internet Service'))

StreamingMovies = st.selectbox('Streaming Movies Type',('Yes', 'No','No Internet Service'))

contract = st.selectbox('Contract Type',('Month-to-month', 'One year', 'Two year'))

PaperlessBilling   = st.radio('Are There PaperlessBilling  ',('Yes', 'No'))

PaymentMethod = st.selectbox('What is Your PaymentMethod',('Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'))

MonthlyCharges = st.slider('Enter Your Monthly Charges',15,150)
st.write('You Choose',MonthlyCharges)

TotalCharges = st.slider('Enter Your Total Charges',MonthlyCharges,1500)
st.write('You Choose',TotalCharges)

df = pd.DataFrame('Gender')

st.write('Thanks For Using Our Application')