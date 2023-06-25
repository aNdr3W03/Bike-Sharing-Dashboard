"""
Author: Andrew Benedictus Jamesie
Date: 25/06/2023
This is the dashboard.py module.
Usage:
- Run the streamlit dashboard
"""

import datetime
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


if __name__ == '__main__':
  st.header('🚴🏻‍♂️ Bike Sharing Dashboard')

  DF_CLEAN_PATH = './dataset/data.csv'
  DF_HOUR_PATH = './dataset/hour.csv'

  df = pd.read_csv(DF_CLEAN_PATH)
  df_hour = pd.read_csv(DF_HOUR_PATH)

  date = sidebar(df)
  if len(date) == 2:
    df_main = df[
      (df["dteday"] >= str(date[0])) & (df["dteday"] <= str(date[1]))
    ]
  else:
    df_main = df[
      (df["dteday"] >= str(st.session_state.date[0])) & (
        df["dteday"] <= str(st.session_state.date[1])
      )
    ]

  with st.container():
    st.subheader('Statistik Berdasarkan Waktu')
    tab_year, tab_month, tab_hour = st.tabs(['Tahun', 'Bulan', 'Jam'])
    df_year = create_df_yr(df_main)

    with tab_year:
      year(df_year)

    with tab_month:
      month(df_main)

    with tab_hour:
      hour(df_hour)

  with st.container():
    st.subheader('Statistik Berdasarkan Hari Libur dan Hari Kerja')
    col_holiday, col_workingday = st.columns([1, 1])

    with col_holiday:
      df_holiday = create_df_holiday(df_main)
      holiday(df_holiday)

      with st.expander('Keterangan'):
        st.write(
          """
          `Not Holiday`: Bukan hari libur  
          `Holiday`: Hari libur (tanggal merah)
          """
        )

    with col_workingday:
      df_workingday = create_df_working_day(df_main)
      working_day(df_workingday)

      with st.expander('Keterangan'):
        st.write(
          """
          `Working Day`: Hari kerja  
          `Holiday`: Hari libur
          """
        )

  with st.container():
    df_weathersit = create_df_weathersit(df_main)
    weathersit(df_weathersit)

    with st.expander('Keterangan'):
      st.write(
        """
        `Mist + Cloudy`: Berkabut dan berawan  
        `Light Snow`: Sedikit bersalju  
        `Clear`: Cuaca cerah
        """
      )

  with st.container():
    df_season = create_df_season(df_main)
    season(df_season)

    with st.expander('Keterangan'):
      st.write(
        """
        `Winter`: Musim Dingin  
        `Summer`: Musim Panas  
        `Springer`: Musim Semi  
        `Fall`: Musim Gugur
        """
      )

  year_now = datetime.date.today().year
  NAME = "[Andrew Benedictus Jamesie](https://www.linkedin.com/in/andrewbjamesie 'Andrew Benedictus Jamesie | LinkedIn')"
  COPYRIGHT = 'Copyright © ' + str(year_now) + ' ' + NAME
  st.caption(COPYRIGHT)
