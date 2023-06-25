"""
Author: Andrew Benedictus Jamesie
Date: 25/06/2023
This is the func.py module.
Usage:
- Initiate all functions for streamlit dashboard
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.style.use('dark_background')


def create_df_yr(df):
  """Initialize the function to get the year DataFrame

  Args:
      df (DataFrame): DataFrame of the dataset used

  Returns:
      DataFrame: DataFrame that has been processed for the year attribute
  """
  df_year = df.groupby('yr').instant.nunique().reset_index()
  df_year.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_year


def create_df_holiday(df):
  """Initialize the function to get the holiday DataFrame

  Args:
      df (DataFrame): DataFrame of the dataset used

  Returns:
      DataFrame: DataFrame that has been processed for the holiday attribute
  """
  df_holiday = df.groupby('holiday').instant.nunique().reset_index()
  df_holiday.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_holiday


def create_df_working_day(df):
  """Initialize the function to get the working day DataFrame

  Args:
      df (DataFrame): DataFrame of the dataset used

  Returns:
      DataFrame: DataFrame that has been processed for the working day attribute
  """
  df_workingday = df.groupby('workingday').instant.nunique().reset_index()
  df_workingday.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_workingday


def create_df_weathersit(df):
  """Initialize the function to get the weathersit DataFrame

  Args:
      df (DataFrame): DataFrame of the dataset used

  Returns:
      DataFrame: DataFrame that has been processed for the weathersit attribute
  """
  df_weathersit = df.groupby('weathersit').instant.nunique().reset_index()
  df_weathersit.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_weathersit


def create_df_season(df):
  """Initialize the function to get the season DataFrame

  Args:
      df (DataFrame): DataFrame of the dataset used

  Returns:
      DataFrame: DataFrame that has been processed for the season attribute
  """
  df_season = df.groupby('season').instant.nunique().reset_index()
  df_season.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_season


def sidebar(df):
  """Initialize the function to create sidebar

  Args:
      df (DataFrame): DataFrame of the dataset used

  Returns:
      date_input: date input
  """
  df['dteday'] = pd.to_datetime(df['dteday'])
  min_date = df['dteday'].min()
  max_date = df['dteday'].max()

  with st.sidebar:
    st.image('./assets/bike-sharing.png')

    def on_change():
      st.session_state.date = date

    date = st.date_input(
      label='Rentang Waktu',
      value=[min_date, max_date],
      min_value=min_date,
      max_value=max_date,
      on_change=on_change
    )

    return date


def year(df):
  """Initialize the function to create year plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.subheader('Tahun')

  fig, ax = plt.subplots(figsize=(20, 12.6))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='yr', ascending=False),
    x='sum',
    y='yr',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Per Tahun',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Tahun', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def month(df):
  """Initialize the function to create month plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.subheader('Bulan')

  fig, ax = plt.subplots(figsize=(20, 12))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='mnth', ascending=False),
    x='cnt',
    y='mnth',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Per Bulan',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Bulan', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def hour(df):
  """Initialize the function to create hour plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.subheader('Jam')

  fig, ax = plt.subplots(figsize=(20, 12))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='hr', ascending=False),
    x='cnt',
    y='hr',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Per Jam',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Jam', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=24, padding=20)
  st.pyplot(fig)


def holiday(df):
  """Initialize the function to create holiday plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.write('Hari Libur')

  fig, ax = plt.subplots(figsize=(16, 18))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='holiday', ascending=False),
    x='holiday',
    y='sum',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Berdasarkan Hari Libur',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel(None)
  ax.set_ylabel('Jumlah', fontsize=40)
  ax.tick_params(axis='x', labelsize=35)
  ax.tick_params(axis='y', labelsize=35)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def working_day(df):
  """Initialize the function to create working day plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.write('Hari Kerja')

  fig, ax = plt.subplots(figsize=(16, 18))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='workingday', ascending=False),
    x='workingday',
    y='sum',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Berdasarkan Hari Kerja',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel(None)
  ax.set_ylabel('Jumlah', fontsize=40)
  ax.tick_params(axis='x', labelsize=35)
  ax.tick_params(axis='y', labelsize=35)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def weathersit(df):
  """Initialize the function to create weathersit plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.subheader('Cuaca')

  fig, ax = plt.subplots(figsize=(20, 10))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='weathersit', ascending=False),
    x='sum',
    y='weathersit',
    orient='h',
    ax=ax,
  )
  
  ax.set_title(
    'Jumlah Bike Sharing Berdasarkan Cuaca',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Cuaca', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def season(df):
  """Initialize the function to create season plot

  Args:
      df (DataFrame): DataFrame of the dataset used
  """
  st.subheader('Musim')

  fig, ax = plt.subplots(figsize=(20, 10))
  plt.grid(color='lightgray', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='season', ascending=False),
    x='sum',
    y='season',
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Jumlah Bike Sharing Berdasarkan Musim',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Jumlah', fontsize=30)
  ax.set_ylabel('Musim', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)
