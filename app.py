import pandas as pd
import streamlit as st
import plotly.express as px

datashet=pd.read_csv('products_dataset.csv')

st.set_page_config(page_title="Product", layout="wide")

st.sidebar.header("Filter By:")



categories = ["All Categories"] + list(datashet["product_category_name"].value_counts().keys().sort_values())
category = st.sidebar.multiselect(label='kategori', options=categories)

selection_query=datashet.query(
    "product_category_name== @category"
)

st.dataframe(selection_query)

st.title (":green_book: Product")
total_panjang=(selection_query["product_length_cm"].sum())
total_tinggi=(selection_query["product_height_cm"].sum())
total_lebar=(selection_query["product_width_cm"].sum())
avg_berat=round((selection_query["product_weight_g"].mean()), 4)

first_column,second_column,third_column,fourth_column =st.columns(4)

with first_column:
    st.markdown("#### Amount Product Length ")
    st.subheader(f'{total_panjang} cm')
with second_column:
    st.markdown("#### Amount Product Height:")
    st.subheader(f'{total_tinggi} cm')
with third_column:
    st.markdown("####  Amount Product Width:")
    st.subheader(f'{total_lebar} cm')
with fourth_column:
    st.markdown("#### Avarage Product Weight:")
    st.subheader(f'{avg_berat} g')

st.markdown("---")
st.header(':memo: Engagement')

wight_by_category=(selection_query.groupby(by=["product_category_name"]).sum()[["product_weight_g"]])

weight_by_category_barchart=px.bar(wight_by_category,
                                   x='product_weight_g',
                                   y=wight_by_category.index,
                                   title="Avarage Product Weigh",
                                   color_discrete_sequence=["#17f50c"],
                                   )
weight_by_category_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)", xaxis=(dict(showgrid=False)))

wight_by_category_piechart = px.pie (wight_by_category, 
                                     names= wight_by_category.index, 
                                     values='product_weight_g',
                                     title="Avarage Product Weigh",
                                     hole=.3,
                                     color=wight_by_category.index,
                                     color_discrete_sequence=px.colors.sequential.RdPu_r)

left_column, right_column=st.columns(2)
left_column.plotly_chart(weight_by_category_barchart, use_container_width=True)
right_column.plotly_chart(wight_by_category_piechart, use_container_width=True)
