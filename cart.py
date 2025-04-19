
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('cleaned_df.csv', index_col= 0)

start_date = st.sidebar.date_input('Start Date', value= df.order_date.min(), min_value= df.order_date.min(), max_value= df.order_date.max())

end_date = st.sidebar.date_input('End Date', value= df.order_date.min(), min_value= df.order_date.min(), max_value= df.order_date.max())

state = st.sidebar.multiselect('State', df.state.unique())

top_n = st.sidebar.slider('Top N', min_value= 1, max_value= 30)

df_filtered = df[(df.order_date >= str(start_date)) & (df.order_date <= str(end_date))]

df_filtered =  df_filtered[(df_filtered.state.isin(state))]

st.dataframe(df_filtered)

product_count = df_filtered.product_name.value_counts().head(top_n).reset_index()

st.markdown(f"""<h1 style="color:white;text-align:center;"> Top {top_n} Popular Products </h1>""", unsafe_allow_html= True)

st.plotly_chart(px.bar(product_count, x= 'product_name', y= 'count'))
