import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('data/price_year.csv', index_col=0)

st.subheader('Yearly Statistics Summary of Crude Oil')

if st.checkbox('Show raw data', key='price'):
    st.subheader('Price by Year')
    st.write(data)
    
# Plotting Data
def add_line(price, color):
    fig.add_trace(go.Scatter(x=data.Year, y=data[price],
                            name=price, line=dict(color=color, 
                                                    width=3, dash='dot')))
fig = go.Figure()
add_line('Min_Price', 'firebrick')
add_line('Avg_Price', 'royalblue')
add_line('Max_Price', 'forestgreen')

fig.update_layout(title='Summary of crude oil price by year', width=950,
                  yaxis_title = 'Price (US$/Barrel)',
                   legend = dict(
                    orientation='h',
                    xanchor="right",
                    x=0.75,
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
st.plotly_chart(fig, use_container_width=True) 

data1 = pd.read_csv('data/prod_year.csv')

if st.checkbox('Show raw data', key='prod'):
    st.subheader('Production by Year')
    st.write(data1)
    
# Plotting Data
def add_line(price, color):
    fig.add_trace(go.Scatter(x=data1.Year, y=data1[price],
                            name=price, line=dict(color=color, 
                                                            width=3, dash='dot')))
fig = go.Figure()
add_line('Min_Production', 'firebrick')
add_line('Avg_Production', 'royalblue')
add_line('Max_Production', 'forestgreen')

fig.update_layout(title='Summary of crude oil production by year', width=950,
                  yaxis_title = 'Production (mbd)',
                  legend = dict(
                    orientation='h',
                    xanchor="right",
                    x=0.85,
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
st.plotly_chart(fig, True)


hide = """
<style>
thead tr th:first-child {display:none}
tbody th {display:none}
</style>
"""

from Overview import load_data
data3 = load_data()[3]
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