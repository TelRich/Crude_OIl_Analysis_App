import streamlit as st
import pandas as pd
import plotly.graph_objects as go

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
month_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


st.subheader("Statistics summary of Crude Oil")
data = pd.read_csv('data/price_month.csv')

if st.checkbox('Show raw data'):
    st.subheader("Price by Month")
    st.write(data)


# Plotting data
def add_line(price, color):
    fig.add_trace(go.Scatter(x=data.index, y=data[price],
                            name=price, mode='lines+markers+text',
                            text = data[price], textposition='top center',
                            line=dict(color=color, 
                                      width=3, dash='dot'),
                            textfont=dict(
                                size=10
                            )))
fig = go.Figure()
add_line('Min_Price', 'firebrick')
add_line('Avg_Price', 'royalblue')
add_line('Max_Price', 'forestgreen')

fig.update_layout(title='Summary of crude oil price by month', width=850,
                  yaxis_title = 'Price (US$/Barrel)',
                  xaxis = dict(
                      tickvals = month_order, 
                      ticktext = month_short
                  ))
fig.update_yaxes(showticklabels=False)
st.plotly_chart(fig)
