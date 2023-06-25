"""
Author: Andrew Benedictus Jamesie
Date: 25/06/2023
This is the app.py module.
Usage:
- Main streamlit file
- Run the streamlit dashboard
"""

import datetime
import pandas as pd
import streamlit as st
from dashboard.func import (
  create_df_yr, create_df_holiday, create_df_working_day,
  create_df_weathersit, create_df_season, sidebar, year,
  month, hour, holiday, working_day, weathersit, season
)


if __name__ == '__main__':
  st.header('🚴🏻‍♂️ Bike Sharing Dashboard')

  DF_CLEAN_PATH = 'dataset/data.csv'
  DF_HOUR_PATH = 'dataset/hour.csv'

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
  NAME = "[Andrew Benedictus Jamesie](http://linkedin.com/in/andrewbjamesie 'Andrew Benedictus Jamesie | LinkedIn')"
  COPYRIGHT = 'Copyright © ' + str(year_now) + ' ' + NAME
  st.caption(COPYRIGHT)
