import streamlit 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

streamlit.title('My Moms new healthy dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeat')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothing')
streamlit.text('🐔 Hard-boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# let's put a pick list here, so that user can pick the fruit he wants to include
streamlit.multiselect("Pick the furit: ", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
