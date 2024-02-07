import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
# some = st.text_input("Enter something...")
# url = "https://unsplash.com/s/photos/{some}".format(some=some)
# st.markdown("check out this [link](%s)" % url)

st.set_page_config(page_title="Web Scrapper", page_icon="🌐", layout="wide")
with st.form("Search"):
    list = []
    key = st.text_input("Enter your keyword!!")
    search = st.form_submit_button("Search")
    #sending req to the url
placeholder = st.empty()    
if key:
    page = requests.get(f"https://unsplash.com/s/photos/{key}")
    soup = BeautifulSoup(page.content,'html.parser')
    rows = soup.find_all("div",class_ = "ripi6")
    # print(len(rows))
    # print(page.status_code)
    col1,col2 = placeholder.columns(2)
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img",class_ = "tB6UZ a5VGX")
            list = img["srcset"].split("?")
            anchor = figures[i].find("a",class_ = "rEAWd")
            print(anchor["href"])
            if i == 0:
                col1.image(list[0])
                btn = col1.button("Download",key=str(index)+str(i))
                # print(str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            else:
                col2.image(list[0])
                btn = col2.button("Download",key=str(index)+str(i))
                # print(str(index)+str(i))
                # print("else part")
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])    
                # print(list[0])
                # print("\n\n")
                # st.image(img["src"])
                # st.caption(img["alt"])

    