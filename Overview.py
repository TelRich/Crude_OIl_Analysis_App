import streamlit as st
import pandas as pd
import plotly.graph_objs as go


st.markdown("<h1 style='text-align: center; color: White;'>NIGERIA CRUDE OIL ANALYSIS</h1>", unsafe_allow_html=True)

with st.expander('About Nigerian Crude OIl', expanded=True):
  st.markdown("<h2 style='text-align:center;'>Nigeria Export Crude Oil Production and Price</h2>", unsafe_allow_html=True)

  st.markdown("""<center>

  According to [Wikipedia](https://en.wikipedia.org/wiki/Petroleum_industry_in_Nigeria#:~:text=Nigeria%20is%20the%20largest%20oil,paraffinic%20and%20low%20in%20sulfur.), 
  Nigeria is the largest oil and gas producer in Africa. [Crude oil](https://en.wikipedia.org/wiki/Petroleum) from the [Niger delta basin](https://en.wikipedia.org/wiki/Niger_Delta) 
  comes in two types: [light](https://en.wikipedia.org/wiki/Light_crude_oil), and comparatively [heavy](https://en.wikipedia.org/wiki/Heavy_crude_oil) – the lighter has around 36 gravity 
  while the heavier has 20–25 gravity. Both types are [paraffinic](https://en.wikipedia.org/wiki/Alkane) and low in [sulfur](https://en.wikipedia.org/wiki/Sulfur).Nigeria's economy and 
  budget have been largely supported from income and revenues generated from the petroleum industry since 1960. Statistics as at February 2021 shows that the Nigerian oil sector contributes 
  to about 9% of the entire [GDP](https://en.wikipedia.org/wiki/Gross_domestic_product) of the nation. Nigeria is the largest oil and gas producer in Africa, a major exporter of crude oil 
  and petroleum products to the United States of America. In 2010, Nigeria exported over one million barrels per day to the United States of America, representing 9% of the U.S. total 
  crude oil and petroleum products imports and over 40% of Nigeria exports.

  </center>""", unsafe_allow_html=True)

  st.image("https://cdn08.allafrica.com/download/pic/main/main/csiid/00410084:4f39f9cb5c0f3b30f3087c8a62f45009:arc614x376:w735:us1.jpg")

@st.cache_data
def load_data():
  data = pd.read_csv('data/export_by_yr.csv')
  data1 = pd.read_csv('data/price_3_yrs.csv')
  data2 = pd.read_csv('data/prod_price_diff.csv')
  data3 = pd.read_csv('data/stat.csv', index_col=0)
  data4 = pd.read_csv('data/avg_com.csv')
  return [data, data1, data2, data3, data4]


data=load_data()[0]
data1=load_data()[1]
data2=load_data()[2]
data3=load_data()[3]
data4 = load_data()[4]

hide = """
<style>
thead tr th:first-child {display:none}
tbody th {display:none}
</style>
"""

def side_display():
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

month_order = ['February', 'April', 'June', 'August', 'October', 'November', 'December']
month_short = [ 'Feb', 'Apr', 'Jun', 'Aug', 'Oct', 'Nov', 'Dec']


with st.expander('Crude Oil Price with Three Years Gap'):
  # Plotting Data
  def add_year(price_year, color):
      price = price_year
      name = price[5:] + ' Price'
      fig.add_trace(go.Scatter(x=data1.month, y=data1[price_year],
                              name=name, line=dict(color=color, 
    
                                                              width=3, dash='dot')))
  if st.checkbox('Show raw data', key='Price'):
      st.subheader("Crude Oil Price with three year differnce")
      st.write(data1)

  fig = go.Figure()
  add_year('Price2006', 'firebrick')
  add_year('Price2009', 'royalblue')
  add_year('Price2012', 'goldenrod')
  add_year('Price2015', 'darkturquoise')
  add_year('Price2018', 'forestgreen')
  add_year('Price2021', 'darkgrey')
  fig.update_layout(title='Crude oil price with three years gap', width=750,
                    yaxis_title = 'Price (US$/Barrel)',
                    xaxis = dict(
                        tickvals = month_order, 
                        ticktext = month_short
                    ),
                    legend = dict(
                      orientation='h',
                      xanchor="right",
                      x=1,
                      font = dict(
                        family="Courier",
                        size=12,
                        # color='white'
                      ),
                      # bgcolor='olive',
                      bordercolor='blue',
                      borderwidth=.5
                    )
                    )
  st.plotly_chart(fig, use_container_width=True)
  """

  2012 looks like an ouliear but then, 
  we are viewing the year with three years gap. 
  The price is clustered between 35 and 85(US%/Barrel).


  """

exp2 = st.expander('Crude Oil Production with Three Years Gap')
with exp2:
  if st.checkbox('Show raw data', key='Prod'):
      st.subheader("Crude Oil Production with three years difference")
      st.write(data2)

  # Plotting data
  def add_year(price_year, color):
      price = price_year
      name = price[4:] + ' Production'
      fig.add_trace(go.Scatter(x=data2.month, y=data2[price_year],
                              name=name, line=dict(color=color, 
                                                              width=3, dash='dot')))
  fig = go.Figure()
  add_year('Prod2006', 'firebrick')
  add_year('Prod2009', 'royalblue')
  add_year('Prod2012', 'goldenrod')
  add_year('Prod2015', 'darkturquoise')
  add_year('Prod2018', 'forestgreen')
  add_year('Prod2021', 'darkgrey')

  fig.update_layout(title='Crude oil production with three years gap', width=850,
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
                        # color='white'
                      ),
                      # bgcolor='olive',
                      bordercolor='blue',
                      borderwidth=.5
                    )
                    )
  
  st.plotly_chart(fig,use_container_width=True)
  
  """
  From the visual above, production started decreasing after 2012. 
  """

exp3 = st.expander(label='Comparing Overall Average with Yearly Average')
with exp3:
  if st.checkbox('Show raw data', key='avg'):
    st.subheader('Overall Average vs Yearly Average')
    st.write(data4)
    
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=data4.Year, y=data4.Year_avg_export,
                              name='Year_avg_export', mode= 'lines+markers+text',
                              text= data4.Year_avg_export, textposition='top right',
                              line=dict(color='royalblue', 
                                          width=3, dash='dot'),
                              textfont=dict(size=11)))

  fig.add_trace(go.Scatter(x=data4.Year, y=data4.Overall_avg_export,
                              name='Overall_avg_export', line=dict(color='firebrick', 
                                                              width=3, dash='dot')))

  fig.update_layout(title='Comparing yearly average of crude oil exported with overall average, 1.58mbd', width=950,
                    yaxis_title = 'Production (mbd)',
                    legend = dict(
                      orientation='h',
                      xanchor="right",
                      x=0.75,
                      font = dict(
                        family="Courier",
                        size=12,
                        # color='white'
                      ),
                      # bgcolor='olive',
                      bordercolor='blue',
                      borderwidth=.5
                    )
                    )
  fig.update_yaxes(showticklabels=False)
  st.plotly_chart(fig, use_container_width=True)

