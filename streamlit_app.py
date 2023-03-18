import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Week 1 - Data and visualization")
st.markdown("Here we can see the dataframe created from the raw data of AirBnB Amsterdam.")

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above 11000 rupees per night
dataframe = dataframe[dataframe["Price"] <= 11000]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "₹ " + dataframe["Price"].round(2).astype(str) # <--- CHANGE THIS POUND SYMBOL IF YOU CHOSE CURRENCY OTHER THAN POUND
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "Johan Cruyff Arena", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("The map below shows all the Airbnb listings less than ₹11000 with a light blue dot and Johan Cruyff Arena with a dark blue dot.")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    zoom=9,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
