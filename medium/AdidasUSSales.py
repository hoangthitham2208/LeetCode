import pandas as pd
import plotly.figure_factory as ff
import streamlit as st
import plotly.express as px
import os
import matplotlib as plt
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title='Adidas US Sales', page_icon=':bar_chart', layout='centered')

st.title(' :bar_chart: Adidas Sales EDA')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(':file_folder: Upload a file', type=(['csv', 'txt', 'xlsx', 'xls']))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding='ISO-8859-1')
else:
    os.chdir(r"C:\Users\FPT SHOP\IdeaProjects\Streamlit")
    df = pd.read_csv('AdidasUS.csv', encoding='ISO-8859-1')

df['Total Sales'] = df['Total Sales'].str.replace('[\\$,]', '', regex=True)
df['Operating Profit'] = df['Operating Profit'].replace('[\\$,]', '', regex=True)
df['Units Sold'] = df['Units Sold'].replace('[\\,]', '', regex=True)

# Chuyển đổi cột sang kiểu dữ liệu số thực
df['Total Sales'] = df['Total Sales'].astype(float)
df['Operating Profit'] = df['Operating Profit'].astype(float)
df['Units Sold'] = df['Units Sold'].astype(float)

col1, col2 = st.columns(2)
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], format="%d/%m/%Y")


# Getting the min and max date 
startDate = pd.to_datetime(df['Invoice Date']).min()
endDate = pd.to_datetime(df['Invoice Date']).max()

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date', startDate))

with col2:
    date2 = pd.to_datetime(st.date_input('End Date', endDate))

df = df[(df['Invoice Date'] >= date1) & (df['Invoice Date'] <= date2)].copy()

st.sidebar.header('Choose your filter: ')
# Create for Region
region = st.sidebar.multiselect('Pick your Region', df['Region'].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df['Region'].isin(region)]

# Create for State
state = st.sidebar.multiselect('Pick the State', df2['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2['State'].isin(state)]

# Create for City
city = st.sidebar.multiselect("Pick the City", df3['City'].unique())

# Filter the data based on Region, State,City
if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df['Region'].isin(region)]
elif not region and not city:
    filtered_df = df[df['State'].isin(state)]
elif state and city:
    filtered_df = df3[df['State'].isin(state) & df3['City'].isin(city)]
elif region and city:
    filtered_df = df3[df['Region'].isin(region) & df3['City'].isin(city)]
elif region and state:
    filtered_df = df3[df['Region'].isin(region) & df3['State'].isin(state)]
elif city:
    filtered_df = df3[df3['City'].isin(city)]
else:
    filtered_df = df3[df3['Region'].isin(region) & df3['State'].isin(state) & df3['City'].isin(city)]

product_df = filtered_df.groupby(by=['Product'], as_index=False)['Total Sales'].sum()

with col1:
    st.subheader('Product wise Sales')
    fig = px.bar(product_df, x='Product', y='Total Sales',
                 template='seaborn')
    st.plotly_chart(fig, use_container_width=True, height=200)

with col2:
    st.subheader('Region wise Sales')
    fig = px.pie(filtered_df, values='Total Sales', names='Region', hole=0.5)
    fig.update_traces(text=filtered_df["Region"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns(2)
with cl1:
    with st.expander("Product_ViewData"):
        st.write(product_df.style.background_gradient(cmap="Blues"))
        csv = product_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="product.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

with cl2:
    with st.expander("Region_ViewData"):
        region = filtered_df.groupby(by="Region", as_index=False)["Total Sales"].sum()
        st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Region.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

filtered_df["month_year"] = filtered_df["Invoice Date"].dt.to_period("M")
st.subheader('Time Series Analysis')

linechart = pd.DataFrame(
    filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Total Sales"].sum()).reset_index()
fig2 = px.line(linechart, x="month_year", y="Total Sales", labels={"Sales": "Amount"}, height=500, width=1000,
               template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')

# Create a treem based on Region, State, Product
st.subheader("Hierarchical view of Sales using TreeMap")
fig3 = px.treemap(filtered_df, path=["Region", "State", "Product"], values="Total Sales", hover_data=["Total Sales"],
                  color="Product")
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

chart1, chart2 = st.columns(2)
with chart1:
    st.subheader('Retailer wise Sales')
    fig = px.pie(filtered_df, values="Total Sales", names="Retailer", template="ggplot2")
    fig.update_traces(text=filtered_df["Retailer"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader('Sale Method wise Sales')
    fig = px.pie(filtered_df, values="Total Sales", names="Sales Method", template="plotly_white")
    fig.update_traces(text=filtered_df["Sales Method"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

st.subheader(":point_right: Month wise Product Sales Summary")
with st.expander("Summary_Table"):
    df_sample = df[0:5][["Region", "State", "City", "Product", "Total Sales", "Operating Profit", "Units Sold"]]
    fig = ff.create_table(df_sample, colorscale="Cividis")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Month wise  Table")
    filtered_df["month"] = filtered_df["Invoice Date"].dt.month_name()
    product_Year = pd.pivot_table(data=filtered_df, values="Total Sales", index=["Product"], columns="month")
    st.write(product_Year.style.background_gradient(cmap="Blues"))

# Create a scatter plot
data1 = px.scatter(filtered_df, x="Total Sales", y="Operating Profit", size="Units Sold")
data1['layout'].update(title="Relationship between Total Sales and Operating Profits using Scatter Plot.",
                       titlefont=dict(size=20), xaxis=dict(title="Total Sales", titlefont=dict(size=19)),
                       yaxis=dict(title="Operating Profit", titlefont=dict(size=19)))
st.plotly_chart(data1, use_container_width=True)

with st.expander("View Data"):
    st.write(filtered_df.iloc[:500, 1:20:2].style.background_gradient(cmap="Oranges"))
