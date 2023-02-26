import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from Overview import load_data

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
month_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


st.subheader("Statistics Summary of Crude Oil")
data = pd.read_csv('data/price_month.csv')
data3 = load_data()[3]

def side_display():
  hide = """
  <style>
  thead tr th:first-child {display:none}
  tbody th {display:none}
  </style>
  """
  st.markdown(hide, True)
  st.sidebar.subheader('Price Stats (US$/Barrel)')
  price = data3.iloc[:,:3]
  prod = data3.iloc[:, 4:7]
  exp = data3.iloc[:, 6:]
  st.sidebar.table(price)
  st.sidebar.subheader('Production Stats (mbd)')
  st.sidebar.table(prod)
  st.sidebar.subheader('Export Stats (mbd)')
  st.sidebar.table(exp)
side_display()

if st.checkbox('Show raw data', key='price'):
    st.subheader("Price by Month")
    st.write(data)


# Plotting data
def add_line(price, color):
    fig.add_trace(go.Scatter(x=data.Month, y=data[price],
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
                  ),
                   legend = dict(
                    orientation='h',
                    xanchor="right",
                    x=0.8,
                    font = dict(
                      family="Courier",
                      size=12,
                    #   color='white'
                    ),
                    # bgcolor='olive',
                    bordercolor='blue',
                    borderwidth=.5
                  )
                  )
fig.update_yaxes(showticklabels=False)
st.plotly_chart(fig, use_container_width=True)

data1 = pd.read_csv('data/prod_month.csv')
if st.checkbox('Show raw data', key='prod'):
    st.subheader('Production by Month')
    st.write(data1)
    
# Plotting Data
def add_line(price, color):
    fig.add_trace(go.Scatter(x=data1.Month, y=data1[price],
                            name=price, mode= 'lines+markers+text',
                            text= data1[price], textposition='top center',
                            line=dict(color=color, 
                                      width=3, dash='dot'),
                            textfont=dict(
                                size=10
                            )))
fig = go.Figure()
add_line('Min_Production', 'firebrick')
add_line('Avg_Production', 'royalblue')
add_line('Max_Production', 'forestgreen')

fig.update_layout(title='Summary of crude oil production by month', width=850,
                  yaxis_title = 'Production (mbd)',
                  xaxis = dict(
                      tickvals = month_order, 
                      ticktext = month_short
                  ),
                   legend = dict(
                    orientation='h',
                    xanchor="right",
                    x=0.9,
                    font = dict(
                      family="Courier",
                      size=12,
                    #   color='white'
                    ),
                    # bgcolor='olive',
                    bordercolor='blue',
                    borderwidth=.5
                  )
                  )
fig.update_yaxes(showticklabels=False)
st.plotly_chart(fig, use_container_width=True)