import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from Overview import load_data as ld

@st.cache_data
def load_data():
  data = pd.read_csv('data/price_year.csv', index_col=0)
  data1 = pd.read_csv('data/prod_year.csv')
  data2 = pd.read_csv('data/2021vs2022.csv')
  return [data, data1, data2]

df = load_data()
data = df[0]
data1 = df[1]
data2 = df[2]
data3 = ld()[3]

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

month_order = ['February', 'April', 'June', 'August', 'October', 'November', 'December']
month_short = [ 'Feb', 'Apr', 'Jun', 'Aug', 'Oct', 'Nov', 'Dec']

st.markdown("<h2> <center> Yearly Statistics Summary of Crude Oil</center></h2>", True)

with st.expander('Summary of Crude Oil Price by Year', True):
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

  fig.update_layout(title='Crude oil price by year', width=950,
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


with st.expander('Summary of Crude Oil Production by Year'):
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

  fig.update_layout(title='Crude oil production by year', width=950,
                    yaxis_title = 'Production (mbd)',
                    legend = dict(
                      orientation='h',
                      xanchor="right",
                      x=0.82,
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


with st.expander('Comparing Year 2021 Crude Oil Production with Year 2022'):
  if st.checkbox('Show raw data', key='2021vs2022'):
    st.subheader('Comparing 2021 Crude Oil Production with Year 2022')
    st.write(data2)

  # Visualizing data
  def add_line(total_prod, color):
      ex = total_prod
      name = ex[-4:] + ' Production'
      fig.add_trace(go.Scatter(x=data2.month, y=data2[total_prod],
                              name=name, mode='lines+markers+text',
                              text=data2[total_prod], textposition='bottom left',
                              line=dict(color=color, 
                                          width=3, dash='dot'),
                              textfont=dict(size=10)))
  fig = go.Figure()
  add_line('total_prod_2021', 'royalblue')
  add_line('total_prod_2022', 'firebrick')


  fig.update_layout(title='Comparing year 2021 crude oil production with year 2022', width=950,
                    yaxis_title = 'Production (mbd)',
                    xaxis= dict(
                        tickvals= month_order,
                        ticktext= month_short
                    ),
                    legend = dict(
                      orientation='h',
                      xanchor="right",
                      x=0.82,
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
  st.plotly_chart(fig, True)
  """ The above charts depicts that production is decreasing. 
  Will it increase next month? We don't know untill we have the data for that month.
  """