import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from Overview import load_data

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
month_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


st.markdown("<h2 align='center'> Statistics Summary of Crude Oil</h2>", True)

@st.cache_data
def ld_data():
    data = pd.read_csv('data/price_month.csv')
    data1 = pd.read_csv('data/prod_month.csv')
    data2 = pd.read_csv('data/mnth_diff.csv')
    return [data, data1, data2]

data = ld_data()[0]
data1 = ld_data()[1]
data2 = ld_data()[2]
data3 = load_data()[3]

@st.cache_data
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
  st.sidebar.image("https://cdn08.allafrica.com/download/pic/main/main/csiid/00410084:4f39f9cb5c0f3b30f3087c8a62f45009:arc614x376:w735:us1.jpg")

  
side_display()

with st.expander('Summary of Crude Oil Price by Month', True):
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

    fig.update_layout(title='Crude oil price by month', width=850,
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
    st.markdown("""
                From the plot above, we can see that average price of crude oil
                increase as the year starts and decrease towards the end.
                
                """)

with st.expander('Summary of Crude Oil Production by Month'):
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

    fig.update_layout(title='Crude oil production by month', width=850,
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
    
with st.expander('Changes in Production between 2021 and 2022'):
    if st.checkbox('Show raw data', key='mnth_diff'):
        st.subheader('Production in 2021 and 2022')
        st.write(data2)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data2.month, y=data2.Percentage_change, text=data2.Percentage_change))
    fig.update_layout(title='Percentage change of crude oil production between 2021 and 2022',
                    yaxis_title= 'Pecentage change', width= 700,
                    xaxis= dict(
                        tickvals = month_order,
                        ticktext= month_short
                    ))
    fig.update_yaxes(showticklabels=False)
    st.plotly_chart(fig, True)
    st.markdown("""<center>
    The above bar chart is showing the percentage difference between months in 2021 and months in 2022. Production increase by 4% in 2022 compared to 
    January in 2021, afterwards there has not been a positive difference between other months.
    </center>""", True)