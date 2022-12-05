"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.title('Customer Churn Prediction')
uploaded_file = st.file_uploader("Upload your Customer Churn data(.csv only)")
if uploaded_file is not None:
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # #st.write(string_data)

    # # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


option = st.selectbox(
    'Choose to predict the model ...',
    (
        'KNN - K-Nearest Neighbour', 
        'Decision Tree Classifier', 
        'Random Forest Classifer',
        'Logistic Regression',
        'SVC - Support Vector Classifer',
        'ADABOOST - Adaptive Boosting',
        'ANN - Artificial Neural Network',
        'XGBoost - Extreme Gradient Boosting',
        'Voting Classifier'
    ))

st.write('Model selected:', option)

st.button('Predict')

st.markdown("""---""")
st.header('Result : ')
a=10
st.subheader('Percentage of Customer retains - ~'+ str(a)+'%')


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

g_labels = ['Male', 'Female']
c_labels = ['No', 'Yes']
# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=g_labels, values=30, name="Gender"),
              1, 1)
fig.add_trace(go.Pie(labels=c_labels, values=20, name="Churn"),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name", textfont_size=16)

fig.update_layout(
    title_text="Gender and Churn Distributions",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Gender', x=0.16, y=0.5, font_size=20, showarrow=False),
                 dict(text='Churn', x=0.84, y=0.5, font_size=20, showarrow=False)])
fig.show()

