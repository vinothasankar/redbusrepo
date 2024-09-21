# importing libraries
import pandas as pd
import pymysql
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

b_lists=[]
b_type=[]
b_star=[]


#setting up streamlit page
slt.set_page_config(layout="wide")
slt.title("REDBUS MINI PROJECT")
web=option_menu(menu_title="Project by: S.Vinodha",options=["Project Info","Redbus Info Tracking Tool"],orientation="horizontal")
#Home page  setting
if web=="Project Info":
     slt.header("TechStack")
     slt.subheader(":red[SELENIUM:]")
     slt.markdown("Tool to Automate Web Browser and Web Scrapping")
     slt.subheader(":red[PANDA:]")
     slt.markdown("Data manipulation , Cleaning and Preprocessing")
     slt.subheader(":red[MYSQL:]")
     slt.markdown("To establish connection to SQL database]")
     slt.subheader(":red[STREAMLIT:]")
     slt.markdown("Develop Interactive Application")
          

#States and routes page setting
if web=="Redbus Info Tracking Tool":
     s= slt.sidebar.selectbox("Select State",["Andra Pradesh","Kerala","Telangana","Goa","Rajasthan","South Bengal","Himachal","Assam",
                                     "Uttar Pradesh","West Bengal","Chandigarh","Punjab","North Bengal","Bihar","Kadamba","West Bengal South","Jammu and Kashmir"])
     
     if s=="Kerala":
        df_bus=pd.read_csv("C:/Users/ncssa/Downloads/kerala_bus_details.csv")
     elif s=="Andra Pradesh": 
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/ap_bus_details.csv")    
     elif s=="Telangana":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/Telangana_bus_details.csv")
     elif s=="Goa":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/kadamba_bus_details.csv")
     elif s=="Rajasthan":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/rajasthan_bus_details.csv")
     elif s=="South Bengal":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/sb_bus_details.csv")
     elif s=="Jammu and Kashmir":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/jk_bus_details.csv")
     elif s=="Himachal":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/himachal_bus_details.csv")
     elif s=="Assam":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/assam_bus_details.csv")
     elif s=="Uttar Pradesh":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/up_bus_details.csv")
     elif s=="West Bengal":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/wb_bus_details.csv")
     elif s=="Chandigarh":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/chandigarh_bus_details.csv")
     elif s=="Punjab":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/punjab_bus_details.csv")
     elif s=="North Bengal":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/northbengal_bus_details.csv")
     elif s=="Bihar":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/bihar_bus_details.csv")
     elif s=="Kadamba":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/kaac_bus_details.csv")
     elif s=="West Bengal South":
          df_bus=pd.read_csv("C:/Users/ncssa/Downloads/westbengalsouth_bus_details.csv")

     for i,r in df_bus.iterrows():
          b_lists.append(r["Route_Name"])
          b_type.append(r["Bus_Type"])
          b_star.append(r["Star_Rating"])
     
     k=slt.sidebar.selectbox("Select route",list(set(b_lists)))
     df = df_bus[df_bus["Route_Name"]==k]
     conn=pymysql.connect(host='localhost', user='root', passwd='Vinodha@123', database='redbus') 
     my_cursor = conn.cursor()
     query1=f'''select distinct Bus_Type from dbusdata where Route_Name="{k}" '''
     my_cursor.execute(query1)
     out=my_cursor.fetchall()
     df1 = pd.DataFrame(out,columns=["BusType"])
     t=slt.sidebar.selectbox("Select Bus type",list(set(df1["BusType"])))
     df = df[df["Bus_Type"]==t]

     select_fare=slt.sidebar.radio("Select busfare range",("all","50-500","500-1000","1000 and above"))
     if select_fare=="all":
          query3=f'''select * from dbusdata where Route_Name="{k}" and Bus_Type="{t}" '''
          my_cursor.execute(query3)
          out=my_cursor.fetchall()
          df=pd.DataFrame(out,columns=["Id","Route_Name","Route_Link","Bus_Name","Bus_Type","Departing_time","Duration","Reaching_Time","Star_Rating","Price","Seats_Availability"])

     elif select_fare=="50-500":
          query3=f'''select * from dbusdata where Route_Name="{k}" and Bus_Type="{t}" and Price Between 50 and 500'''
          my_cursor.execute(query3)
          out=my_cursor.fetchall()
          df=pd.DataFrame(out,columns=["Id","Route_Name","Route_Link","Bus_Name","Bus_Type","Departing_time","Duration","Reaching_Time","Star_Rating","Price","Seats_Availability"])

     elif select_fare=="500-1000":
          query3=f'''select * from dbusdata where Route_Name="{k}" and Bus_Type="{t}" and Price Between 500 and 1000'''
          my_cursor.execute(query3)
          out=my_cursor.fetchall()
          df=pd.DataFrame(out,columns=["Id","Route_Name","Route_Link","Bus_Name","Bus_Type","Departing_time","Duration","Reaching_Time","Star_Rating","Price","Seats_Availability"])

     elif select_fare=="1000 and above":
          query3=f'''select * from dbusdata where Route_Name="{k}" and Bus_Type="{t}" and Price >1000'''
          my_cursor.execute(query3)
          out=my_cursor.fetchall()
          df=pd.DataFrame(out,columns=["Id","Route_Name","Route_Link","Bus_Name","Bus_Type","Departing_time","Duration","Reaching_Time","Star_Rating","Price","Seats_Availability"])



     df = df.drop(columns=['Route_Name','Route_Link','Duration'])
     slt.write(len(df),"Buses Found")
     slt.write(df.rename(columns={'Bus_Name': 'Bus Name','Bus_Type': 'Bus Type','Departing_Time': 'Departing Time','Duration': 'Duration','Reaching_Time': 'Reaching Time',
                             'Star_Rating': 'Star Rating','Price': 'Price','Seat_Availability': 'Available Seats'}))
