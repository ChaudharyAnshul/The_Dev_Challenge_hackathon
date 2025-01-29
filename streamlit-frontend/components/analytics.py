import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import configparser

config = configparser.ConfigParser()
config.read('./configuration.properties')


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error("Failed to fetch data")


def show_analytics_dashboard():
    # Change this if your backend runs on a different address
    backend_url = config['APIs']['base_url_auth']

    st.title('Job Analytics Dashboard')

    # Fetch data from backend
    job_counts = fetch_data(f"{backend_url}analyticsRoute/job_counts")
    job_title_counts = fetch_data(
        f"{backend_url}analyticsRoute/job_title_counts")
    salaries = fetch_data(f"{backend_url}analyticsRoute/salaries")
    employment_types = fetch_data(
        f"{backend_url}analyticsRoute/employment_types")

    # Display job density map by state
    st.header('Job Density Map by State')
    fig = px.choropleth(job_counts,
                        locations="STATE",
                        locationmode='USA',
                        color="COUNT",
                        scope="usa",
                        labels={'COUNT': 'Count'},
                        title="Job Density Across the US by State")
    st.plotly_chart(fig)

    # Display box plot of salaries
    st.header('Box Plot of Salaries')
    fig_min_salary = px.box(salaries, 
                            title="Plot of Minimum Salaries", color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig_min_salary)

    fig_max_salary = px.box(salaries,
                            title="Plot of Maximum Salaries", color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig_max_salary)

if __name__ == "__main__":
    show_analytics_dashboard()
