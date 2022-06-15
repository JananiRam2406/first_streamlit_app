import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega 3 & Blueberry Oatmeal')

streamlit.text('Kale,Spinach & Rocket smoothie')

streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response 
streamlit.header('Fruityvice Furit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
#create the repeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/+this_fruit_choice") 
  fruityvice_normalize=pandas.json_normalize(fruity_response.json())
  return fruityvice_normalized


#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit advice!')
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("please select a fruit to get information.")
  else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
fruity_choice = streamlit.text_input('What Fruit would you like informatiopn about?', 'kiwi')
streamlit.write('The user entered', fruity_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruity_choice)



#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

#don't run anything past here while we troubleshoot
streamlit.stop()

import snowflake.connector
streamlit.header("the fruit load list contains:")
#snowfalke-related functions
def get_fruit_load_list():
  with my_cnx.cursor()as my_cur:
    mycur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
#add a button to load the fruit
if streamlit.button('get fruit load list'):
       my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
       my_data_rows = get_fruit_load_list()
       streamlit.header("the fruit load list contains:")
       streamlit.dataframe(my_data_rows)
#allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')



streamlit.write('Thanks for adding ', add_my_fruit)

#this will not work correctly,but just go with it for now
my_cur.execute("insert into fruit_load_list values('from streamlit')")





