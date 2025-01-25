#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import * 
from functools import partial
from tkinter import filedialog
from tkinter.messagebox import askyesno


# In[6]:


def readTableResearch(filename):
    try:
        xl = pd.ExcelFile(filename)
        df1 = xl.parse('Researchers')
        df1.fillna("NULL", inplace=True)
    except Exception:
        df1 = pd.read_csv(filename)
        df1.fillna("NULL", inplace=True)
    return df1


def getVTARCrank(dataframe, value):
    return dataframe.loc[dataframe[' Rank (VT-ARC)'] == value]


# Get value info with range from table in specific column
# E.g. format: In column "Rank", the value range is: left(1) <= Result < right(5)
# E.g. Parameter: (dataframe, "Rank", "<=", "<", 1, 5)
# dataframe: data of table
# condition1: condition set for left filter
# condition2: condition set for right filter
# left: left value of condition
# right: right value of condition


def rangeFilter(dataframe, columnName, condition1, condition2, left, right):
    if (left > right):
        if (condition1 == ">" and condition2 == ">"):
            return dataframe.loc[(dataframe[columnName] > right) & (dataframe[columnName] < left)]
        elif (condition1 == ">" and condition2 == ">="):
            return dataframe.loc[(dataframe[columnName] >= right) & (dataframe[columnName] < left)]
        elif (condition1 == ">=" and condition2 == ">"):
            return dataframe.loc[(dataframe[columnName] > right) & (dataframe[columnName] <= left)]
        elif (condition1 == ">=" and condition2 == ">="):
            return dataframe.loc[(dataframe[columnName] >= right) & (dataframe[columnName] <= left)]
        else:
            return "INVALID CONDITION"
    else:
        if (condition1 == "<" and condition2 == "<"):
            return dataframe.loc[(dataframe[columnName] < right) & (dataframe[columnName] > left)]
        elif (condition1 == "<" and condition2 == "<="):
            return dataframe.loc[(dataframe[columnName] <= right) & (dataframe[columnName] > left)]
        elif (condition1 == "<=" and condition2 == "<"):
            return dataframe.loc[(dataframe[columnName] < right) & (dataframe[columnName] >= left)]
        elif (condition1 == "<=" and condition2 == "<="):
            return dataframe.loc[(dataframe[columnName] <= right) & (dataframe[columnName] >= left)]
        else:
            return "INVALID CONDITION"
    


# Get rank value with range from table
# E.g. format: left(1) <= Result < right(5)
# E.g. Parameter: (dataframe, "<=", "<", 1, 5)
# dataframe: data of table
# condition1: condition set for left filter
# condition2: condition set for right filter
# left: left value of condition
# right: right value of condition


def getRankRange(dataframe, condition1, condition2, left, right):
    return rangeFilter(dataframe, ' Rank (VT-ARC)', condition1, condition2, left, right)


# Get source value from table
# dataframe: data of table
# source_type: specific string required


def getVTARCsource(dataframe, source_type):
    return dataframe.loc[dataframe['Source'] == source_type]


# Get first name value from table
# dataframe: data of table
# string: specific string required


def getVTARCfirstName(dataframe, string):
    return dataframe.loc[dataframe['Name'] == string]


# Get last name value from table
# dataframe: data of table
# string: specific string required


def getVTARClastName(dataframe, string):
    return dataframe.loc[dataframe['Last Name'] == string]


# Get institution name value from table
# dataframe: data of table
# string: specific string required


def getVTARCinstitution(dataframe, string):
    return dataframe.loc[dataframe['Institution'] == string]


# Get title value from table
# dataframe: data of table
# string: specific string required


def getVTARCtitle(dataframe, string):
    return dataframe.loc[dataframe['Title'] == string]


# Get domain value from table
# dataframe: data of table
# string: specific string required


def getVTARCdomain(dataframe, string):
    return dataframe.loc[dataframe['Domain'] == string]


# Get gender value from table
# dataframe: data of table
# string: specific string required


def getVTARCgender(dataframe, string):
    return dataframe.loc[dataframe['Gender'] == string]


# Get topic value from table
# dataframe: data of table
# string: specific string required


def getVTARCtopic(dataframe, string):
    return dataframe.loc[dataframe['Topic'] == string]


# Get description value from table
# dataframe: data of table
# string: specific string required


def getVTARCdescription(dataframe, string):
    return dataframe.loc[dataframe['Research Description'] == string]


# Get field value from table
# dataframe: data of table
# string: specific string required


def getVTARCfield(dataframe, string):
    return dataframe.loc[dataframe['Research Fields'] == string]


# Get other key value from table
# dataframe: data of table
# key: specific key required


def getVTARCotherKey(dataframe, key):
    return dataframe.loc[dataframe['Other Key notes'] == key]


# Get relevant link value from table
# dataframe: data of table
# link: specific string required


def getVTARCrelevantLinks(dataframe, link):
    return dataframe.loc[dataframe['Relevant links'] == link]


# Get email value from table
# dataframe: data of table
# email: specific string required


def getVTARCemail(dataframe, email):
    return dataframe.loc[dataframe['email'] == email]


# Get first name value from table
# dataframe: data of table
# site: specific site required


def getVTARCwebsite(dataframe, site):
    return dataframe.loc[dataframe['Website'] == site]


# Get first name value from table
# dataframe: data of table
# num: specific value required


def getVTARCpubCount(dataframe, num):
    return dataframe.loc[dataframe['Pub Count'] == num]


# Get pub count value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getPubCountRange(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARCpubCount(dataframe, left)
    return rangeFilter(dataframe, 'Pub Count', condition1, condition2, left, right)


# Get cite count value from table
# dataframe: data of table
# num: specific num required


def getVTARCciteCount(dataframe, num):
    return dataframe.loc[dataframe['Citation count'] == num]


# Get cite count value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getCiteCountRange(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARCciteCount(dataframe, left)
    return rangeFilter(dataframe, 'Citation count', condition1, condition2, left, right)


# Get H-index value from table
# dataframe: data of table
# index: specific index required


def getVTARChindex(dataframe, index):
    return dataframe.loc[dataframe['H-Index'] == index]


# Get index range value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getIndexRange(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARChindex(dataframe, left)
    return rangeFilter(dataframe, 'H-Index', condition1, condition2, left, right)


# Get H5-index value from table
# dataframe: data of table
# index: specific index required


def getVTARCh5index(dataframe, index):
    return dataframe.loc[dataframe['H5-Index (5year)'] == index]


# Get H5 index value with range from table
# dataframe: data of table
# condition: condition set for filter
# left: left value of condition
# right: right value of condition


def getH5Range(dataframe, condition1, condition2, left, right):
    if (left == right):
        return getVTARCh5index(dataframe, left)
    return rangeFilter(dataframe, 'H5-Index (5year)', condition1, condition2, left, right)


# Get id value from table
# dataframe: data of table
# num: specific id number required


def getVTARCid(dataframe, num):
    return dataframe.loc[dataframe['ID'] == num]


# Add limitation to column
# dataframe: data of table
# columnName: according to which coloumn
# key: specific keyword to filter


def limitation(dataframe, columnName, keyword):
    return dataframe.loc[dataframe[columnName] == keyword]



def strconvert(content, isInt):
    if content == "NULL":
        return
    if isInt:
        int(content)
        return str(content)
    else:
        return str(content)


# In[11]:


def onepiece(i, mycursor, csv):
    data = csv.iloc[i]
    sql = "INSERT INTO list (rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, id, invited_attend, attended) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val0 = strconvert(data[0], True)
    val1 = strconvert(data[1], True)
    val2 = strconvert(data[2], False)
    val3 = strconvert(data[3], False)
    val4 = strconvert(data[4], False)
    val5 = strconvert(data[5], False)
    val6 = strconvert(data[6], False)
    val7 = strconvert(data[7], False)
    val8 = strconvert(data[8], False)
    val9 = strconvert(data[9], False)
    val10 = strconvert(data[10], False)
    val11 = strconvert(data[11], False)
    val12 = strconvert(data[12], False)
    val13 = strconvert(data[13], False)
    val14 = strconvert(data[14], False)
    val15 = strconvert(data[15], False)
    val16 = strconvert(data[16], False)
    val17 = strconvert(data[17], True)
    val18 = strconvert(data[18], True)
    val19 = strconvert(data[19], True)
    val20 = strconvert(data[20], True)
    val21 = strconvert(data[21], True)
    val22 = strconvert(data[22], False)
    val23 = strconvert(data[23], False)
    val = [val0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23]
    mycursor.execute(sql, val)


# In[4]:


def mysql_connect(hoststr, userstr, passwordstr, databasestr):
    if ':' in hoststr:
        [hostval, portval] = hoststr.split(":")
    else:
        hostval = hoststr
        portval = 3306
    
    mydb = mysql.connector.connect(host=hostval,
                                   port=portval,
                                   user=userstr,
                                   password=passwordstr,
                                   database=databasestr)
    return mydb


# In[20]:


def xlsx_to_csv(filename, targetname):
    table = readTableResearch(filename)
    output = pd.DataFrame(table)
    output.to_csv(targetname+".csv", index=False, header=True)
    return targetname+".csv"


# In[21]:


def whole_table_input(db, csv_table):
    purified = readTableResearch(csv_table)
    rows = purified.shape[0]
    for i in range(rows):
        onepiece(i, db.cursor(), purified)


# In[31]:


def oneline_input(db, data):
    sql = "INSERT INTO list (rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, id, invited_attend, attended) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val0 = strconvert(data[0], True)
    val1 = strconvert(data[1], True)
    val2 = strconvert(data[2], False)
    val3 = strconvert(data[3], False)
    val4 = strconvert(data[4], False)
    val5 = strconvert(data[5], False)
    val6 = strconvert(data[6], False)
    val7 = strconvert(data[7], False)
    val8 = strconvert(data[8], False)
    val9 = strconvert(data[9], False)
    val10 = strconvert(data[10], False)
    val11 = strconvert(data[11], False)
    val12 = strconvert(data[12], False)
    val13 = strconvert(data[13], False)
    val14 = strconvert(data[14], False)
    val15 = strconvert(data[15], False)
    val16 = strconvert(data[16], False)
    val17 = strconvert(data[17], True)
    val18 = strconvert(data[18], True)
    val19 = strconvert(data[19], True)
    val20 = strconvert(data[20], True)
    val21 = strconvert(data[21], True)
    if statInv == 1:
        val22 = "YES"
    elif statInv == 2:
        val22 = "NO"
    if statAt == 1:
        val23 = "YES"
    elif statAt == 2:
        val23 = "NO"
    val = [val0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23]
    db.cursor().execute(sql, val)


# In[32]:


def handle_input(db, rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, actualid, statInv, statAt):
    sql = "INSERT INTO list (rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, id, invited_attend, attended) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val0 = strconvert(rank_other, True)
    val1 = strconvert(rank_vtarc, True)
    val2 = strconvert(rank_justification, False)
    val3 = strconvert(source, False)
    val4 = strconvert(name, False)
    val5 = strconvert(last_name, False)
    val6 = strconvert(institution, False)
    val7 = strconvert(title, False)
    val8 = strconvert(domain, False)
    val9 = strconvert(gender, False)
    val10 = strconvert(topic, False)
    val11 = strconvert(description, False)
    val12 = strconvert(fields, False)
    val13 = strconvert(key_notes, False)
    val14 = strconvert(links, False)
    val15 = strconvert(email, False)
    val16 = strconvert(website, False)
    val17 = strconvert(pub, True)
    val18 = strconvert(citation, True)
    val19 = strconvert(hindex, True)
    val20 = strconvert(h5index, True)
    val21 = strconvert(actualid, True)
    if statInv == 1:
        val22 = "YES"
    elif statInv == 2:
        val22 = "NO"
    if statAt == 1:
        val23 = "YES"
    elif statAt == 2:
        val23 = "NO"
    val = [val0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23]
    db.cursor().execute(sql, val)


# In[95]:


def update_rank_other_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET rank_other = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET rank_other = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[96]:


def update_rank_vtarc_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET rank_vtarc = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET rank_vtarc = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)

def update_just_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET rank_justification = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET rank_justification = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)
    
def update_source_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET source = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET source = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)

# In[97]:


def update_name_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET name = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET name = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[98]:


def update_last_name_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET last_name = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET last_name = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[99]:


def update_institution_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET institution = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET institution = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[100]:


def update_title_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET title = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET title = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[101]:


def update_domain_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET domain = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET domain = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[102]:


def update_gender_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET gender = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET gender = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[103]:


def update_topic_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET topic = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET topic = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[104]:


def update_description_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET description = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET description = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[105]:


def update_fields_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET fields = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET fields = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[106]:


def update_key_notes_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET key_notes = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET key_notes = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[107]:


def update_links_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET links = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET links = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[108]:


def update_email_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET email = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET email = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[109]:


def update_website_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET website = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET website = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[110]:


def update_pub_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET pub = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET pub = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[111]:


def update_hindex(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET hindex = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET hindex = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[112]:


def update_h5index_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET h5index = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET h5index = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[113]:


def update_citation_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET citation = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET citation = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)


# In[114]:


def update_actualid_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET id = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        sql = "UPDATE vtarc.list SET id = %s WHERE uniq = %s"
        val = [value, id_in_db]
        db.cursor().execute(sql, val)

def update_invite_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET invited_attend = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        if value == 1:
            result = "YES"
        elif value == 2:
            result = "NO"
        sql = "UPDATE vtarc.list SET invited_attend = %s WHERE uniq = %s"
        val = [result, id_in_db]
        db.cursor().execute(sql, val)

def update_attend_info(db, id_in_db, value, na):
    if na:
        sql = "UPDATE vtarc.list SET attended = NULL WHERE uniq = %s"
        val = [id_in_db]
        db.cursor().execute(sql, val)
    else:
        if value == 1:
            result = "YES"
        elif value == 2:
            result = "NO"
        sql = "UPDATE vtarc.list SET attended = %s WHERE uniq = %s"
        val = [result, id_in_db]
        db.cursor().execute(sql, val)

def delete_uniq(db, id_in_db):
    sql = "DELETE FROM vtarc.list WHERE uniq = %s"
    val = [id_in_db]
    db.cursor().execute(sql, val)


def delete_row():
    db = mysql_connect(host.get(), username.get(), password.get(), database.get())
    delete_uniq(db, uni_idnum.get())

def updateInfo():
    try:
        updmsg = "Do you really want to update info at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=updmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            if not rank.get() == "":
                update_rank_other_info(db, uni_idnum.get(), rank.get(), False)

            if not rankvtac.get() == "":
                update_rank_vtarc_info(db, uni_idnum.get(), rankvtac.get(), False)

            if not just.get() == "":
                update_just_info(db, uni_idnum.get(), just.get(), False)

            if not source.get() == "":
                update_source_info(db, uni_idnum.get(), source.get(), False)

            if not name.get() == "":
                update_name_info(db, uni_idnum.get(), name.get(), False)

            if not lname.get() == "":
                update_last_name_info(db, uni_idnum.get(), lname.get(), False)

            if not inst.get() == "":
                update_institution_info(db, uni_idnum.get(), inst.get(), False)

            if not title.get() == "":
                update_title_info(db, uni_idnum.get(), title.get(), False)

            if not domain.get() == "":
                update_domain_info(db, uni_idnum.get(), domain.get(), False)

            if not gender.get() == "":
                update_gender_info(db, uni_idnum.get(), gender.get(), False)

            if not topic.get() == "":
                update_topic_info(db, uni_idnum.get(), topic.get(), False)

            if not descrip.get() == "":
                update_description_info(db, uni_idnum.get(), descrip.get(), False)

            if not field.get() == "":
                update_fields_info(db, uni_idnum.get(), field.get(), False)

            if not keynotes.get() == "":
                update_key_notes_info(db, uni_idnum.get(), keynotes.get(), False)

            if not links.get() == "":
                update_links_info(db, uni_idnum.get(), links.get(), False)

            if not email.get() == "":
                update_email_info(db, uni_idnum.get(), email.get(), False)

            if not website.get() == "":
                update_website_info(db, uni_idnum.get(), website.get(), False)

            if not pub.get() == "":
                update_pub_info(db, uni_idnum.get(), pub.get(), False)

            if not cite.get() == "":
                update_citation_info(db, uni_idnum.get(), cite.get(), False)

            if not h.get() == "":
                update_hindex(db, uni_idnum.get(), h.get(), False)

            if not h5.get() == "":
                update_h5index_info(db, uni_idnum.get(), h5.get(), False)

            if not intid.get() == "":
                update_actualid_info(db, uni_idnum.get(), intid.get(), False)

            if not statusInv.get() == 0:
                update_invite_info(db, uni_idnum.get(), statusInv.get(), False)

            if not statusAt.get() == 0:
                update_attend_info(db, uni_idnum.get(), statusAt.get(), False)

            db.commit()
            db.close()
            messagebox.showinfo(title="Message", message="Information update successful!")
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_row():
    try:
        delmsg = "Do you really want to clear row "+ uni_idnum.get()
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            delete_uniq(db, uni_idnum.get())
            db.commit()
            db.close()
            msg = "Row at Unique ID " +  uni_idnum.get()  + " cleared successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_rank_other():
    try:
        delmsg = "Do you really want to clear Rank Other at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_rank_other_info(db, uni_idnum.get(), rank.get(), True)
            db.commit()
            db.close()
            msg = "Clear Rank Other at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_rank_vtarc():
    try:
        delmsg = "Do you really want to clear Rank VT-ARC at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_rank_vtarc_info(db, uni_idnum.get(), rankvtac.get(), True)
            db.commit()
            db.close()
            msg = "Clear Rank VT-ARC at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_rank_just():
    try:
        delmsg = "Do you really want to clear Rank Justification at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_just_info(db, uni_idnum.get(), just.get(), True)
            db.commit()
            db.close()
            msg = "Clear Rank Justification at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            

def del_source():
    try:
        delmsg = "Do you really want to clear Source at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_source_info(db, uni_idnum.get(), source.get(), True)
            db.commit()
            db.close()
            msg = "Clear Source at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            
                            
def del_name():
    try:
        delmsg = "Do you really want to clear Name at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_name_info(db, uni_idnum.get(), name.get(), True)
            db.commit()
            db.close()
            msg = "Clear Name at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return 
                            
def del_lname():
    try:
        delmsg = "Do you really want to clear Last Name at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_last_name_info(db, uni_idnum.get(), lname.get(), True)
            db.commit()
            db.close()
            msg = "Clear Last Name at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return 

def del_inst():
    try:
        delmsg = "Do you really want to clear Institution at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_institution_info(db, uni_idnum.get(), inst.get(), True)
            db.commit()
            db.close()
            msg = "Clear Institution at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                             

def del_title():
    try:
        delmsg = "Do you really want to clear Title at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_title_info(db, uni_idnum.get(), title.get(), True)
            db.commit()
            db.close()
            msg = "Clear Title at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            

def del_domain():
    try:
        delmsg = "Do you really want to clear Domain at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_domain_info(db, uni_idnum.get(), domain.get(), True)
            db.commit()
            db.close()
            msg = "Clear Domain at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return    
                            
def del_gender():
    try:
        delmsg = "Do you really want to clear Gender at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_gender_info(db, uni_idnum.get(), gender.get(), True)
            db.commit()
            db.close()
            msg = "Clear Gender at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_topic():
    try:
        delmsg = "Do you really want to clear Topic at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_topic_info(db, uni_idnum.get(), topic.get(), True)
            db.commit()
            db.close()
            msg = "Clear Topic at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return                            

def del_desc():
    try:
        delmsg = "Do you really want to clear Description at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_description_info(db, uni_idnum.get(), descrip.get(), True)
            db.commit()
            db.close()
            msg = "Clear Description at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_fields():
    try:
        delmsg = "Do you really want to clear Fields at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_fields_info(db, uni_idnum.get(), field.get(), True)
            db.commit()
            db.close()
            msg = "Clear Fields at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return   
                            
def del_keynote():
    try:
        delmsg = "Do you really want to clear Key Notes at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_key_notes_info(db, uni_idnum.get(), keynotes.get(), True)
            db.commit()
            db.close()
            msg = "Clear Key Notes at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_links():
    try:
        delmsg = "Do you really want to clear Links at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_links_info(db, uni_idnum.get(), links.get(), True)
            db.commit()
            db.close()
            msg = "Clear Links at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_email():
    try:
        delmsg = "Do you really want to clear E-mail at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_email_info(db, uni_idnum.get(), email.get(), True)
            db.commit()
            db.close()
            msg = "Clear E-mail at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_website():
    try:
        delmsg = "Do you really want to clear Website at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_website_info(db, uni_idnum.get(), website.get(), True)
            db.commit()
            db.close()
            msg = "Clear Website at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_pub():
    try:
        delmsg = "Do you really want to clear Pub at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_pub_info(db, uni_idnum.get(), pub.get(), True)
            db.commit()
            db.close()
            msg = "Clear Pub at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_cite():
    try:
        delmsg = "Do you really want to clear Citation at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_citation_info(db, uni_idnum.get(), cite.get(), True)
            db.commit()
            db.close()
            msg = "Clear Citation at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_hindex():
    try:
        delmsg = "Do you really want to clear H-index at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_hindex(db, uni_idnum.get(), h.get(), True)
            db.commit()
            db.close()
            msg = "Clear H-index at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_h5index():
    try:
        delmsg = "Do you really want to clear H5-index at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_h5index_info(db, uni_idnum.get(), h5.get(), True)
            db.commit()
            db.close()
            msg = "Clear H5-index at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def del_id():
    try:
        delmsg = "Do you really want to clear ID at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_actualid_info(db, uni_idnum.get(), intid.get(), True)
            db.commit()
            db.close()
            msg = "Clear ID at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_invite():
    try:
        delmsg = "Do you really want to clear Invited at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_invite_info(db, uni_idnum.get(), statusInv.get(), True)
            db.commit()
            db.close()
            msg = "Clear Invited to attend at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return

def del_attend():
    try:
        delmsg = "Do you really want to clear Attend at unique id " + uni_idnum.get() + "?"
        res = messagebox.askquestion(title="Confirm", message=delmsg)
        if res == 'yes' :
            db = mysql_connect(host.get(), username.get(), password.get(), database.get())
            update_attend_info(db, uni_idnum.get(), statusAt.get(), True)
            db.commit()
            db.close()
            msg = "Clear Attend at Unique ID " +  uni_idnum.get()  + " successful!"
            messagebox.showinfo(title="Message", message=msg)
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
                            
def Close():
    tkWindow.destroy()
    

def inputTable():
    filename = filedialog.askopenfilename()
    table = xlsx_to_csv(filename, "temp")
    db = mysql_connect(host.get(), username.get(), password.get(), database.get())
    try:
        whole_table_input(db, table)
        db.commit()
        db.close()
        messagebox.showinfo(title="Message", message="Upload successful!")
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
    
def inputHandInfo():
    db = mysql_connect(host.get(), username.get(), password.get(), database.get())
    try:
        handle_input(db, rank.get(), rankvtac.get(), just.get(), source.get(), name.get(), lname.get(), inst.get(), title.get(), domain.get(), gender.get(), topic.get(), descrip.get(), field.get(), keynotes.get(), links.get(), email.get(), website.get(), pub.get(), cite.get(), h.get(), h5.get(), intid.get(), statusInv.get(), statusAt.get())
        db.commit()
        db.close()
        messagebox.showinfo(title="Message", message="Information input successful!")
    except Exception as e:
        db.close()
        messagebox.showerror(title="Error", message=e)
    return
    

#window
tkWindow = Tk()  
tkWindow.geometry('1300x600')   
tkWindow.title('VT-ARC Database Input Management Panel')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").place(x = 170, y = 60)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x = 130, y = 90)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x = 172, y = 120)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x = 130, y = 150)

#hostlabel and host entry box
hostLabel = Label(tkWindow,text="Host").place(x = 182, y = 180)
host = StringVar()
hostEntry = Entry(tkWindow, textvariable=host).place(x = 130, y = 210)

#databaselabel and database entry box
databaseLabel = Label(tkWindow,text="Database").place(x = 172, y = 240)
database = StringVar()
databaseEntry = Entry(tkWindow, textvariable=database).place(x = 130, y = 270)

#idlabel and id entry box
idLabel = Label(tkWindow,text="Unique ID").place(x = 800, y = 10)
uni_idnum = StringVar()
idEntry = Entry(tkWindow, textvariable=uni_idnum).place(x = 760, y = 40)
                            
Button(tkWindow, text= "X", command=del_row).place(x = 890, y = 35)

#ranklabel and rank id box
rankLabel = Label(tkWindow,text="Rank").place(x = 460, y = 70)
rank = StringVar()
rankEntry = Entry(tkWindow, textvariable=rank).place(x = 460, y = 100)
                            
Button(tkWindow, text= "X", command=del_rank_other).place(x = 590, y = 95)

#rankarclabel and rankarc box
rankvtacLable = Label(tkWindow,text="Rank (VT-ARC)").place(x = 460, y = 130)
rankvtac = StringVar()
rankvtacEntry = Entry(tkWindow, textvariable=rankvtac).place(x = 460, y = 160)
                            
Button(tkWindow, text= "X", command=del_rank_vtarc).place(x = 590, y = 155)

#rankjustificationlabel and box
justLable = Label(tkWindow,text="Rank Justification").place(x = 460, y = 190)
just = StringVar()
justEntry = Entry(tkWindow, textvariable=just).place(x = 460, y = 220)

Button(tkWindow, text= "X", command=del_rank_just).place(x = 590, y = 215)

#sourcelabel and box
sourceLable = Label(tkWindow,text="Source").place(x = 460, y = 250)
source = StringVar()
sourceEntry = Entry(tkWindow, textvariable=source).place(x = 460, y = 280)

Button(tkWindow, text= "X", command=del_source).place(x = 590, y = 275)

#namelabel and box
nameLable = Label(tkWindow,text="Name").place(x = 460, y = 310)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name).place(x = 460, y = 340)

Button(tkWindow, text= "X", command=del_name).place(x = 590, y = 335)
                            
#lastnamelabel and box
lnameLable = Label(tkWindow,text="Last Name").place(x = 460, y = 370)
lname = StringVar()
lnameEntry = Entry(tkWindow, textvariable=lname).place(x = 460, y = 400)

Button(tkWindow, text= "X", command=del_lname).place(x = 590, y = 395)                        
                            
#institutionlabel and box
instLable = Label(tkWindow,text="Institution").place(x = 460, y = 430)
inst = StringVar()
instEntry = Entry(tkWindow, textvariable=inst).place(x = 460, y = 460)

Button(tkWindow, text= "X", command=del_inst).place(x = 590, y = 455)                            
                            
#titlelabel and box
titleLable = Label(tkWindow,text="Title").place(x = 760, y = 70)
title = StringVar()
titleEntry = Entry(tkWindow, textvariable=title).place(x = 760, y = 100)

Button(tkWindow, text= "X", command=del_title).place(x = 890, y = 95)                            
                            
#domainlabel and box
domainCLable = Label(tkWindow,text="Domain").place(x = 760, y = 130)
domain = StringVar()
domainEntry = Entry(tkWindow, textvariable=domain).place(x = 760, y = 160)

Button(tkWindow, text= "X", command=del_domain).place(x = 890, y = 155)                            
                            
#genderlabel and box
genderLable = Label(tkWindow,text="Gender").place(x = 760, y = 190)
gender = StringVar()
genderEntry = Entry(tkWindow, textvariable=gender).place(x = 760, y = 220)

Button(tkWindow, text= "X", command=del_gender).place(x = 890, y = 215)                            
                            
#topiclabel and box
topicLable = Label(tkWindow,text="Topic").place(x = 760, y = 250)
topic = StringVar()
topicEntry = Entry(tkWindow, textvariable=topic).place(x = 760, y = 280)

Button(tkWindow, text= "X", command=del_topic).place(x = 890, y = 275)                            
                            
#descriptionlabel and box
descripLable = Label(tkWindow,text="Description").place(x = 760, y = 310)
descrip = StringVar()
descripEntry = Entry(tkWindow, textvariable=descrip).place(x = 760, y = 340)

Button(tkWindow, text= "X", command=del_desc).place(x = 890, y = 335)                            
                            
#fieldlabel and box
fieldARCLable = Label(tkWindow,text="Fields").place(x = 760, y = 370)
field = StringVar()
fieldEntry = Entry(tkWindow, textvariable=field).place(x = 760, y = 400)

Button(tkWindow, text= "X", command=del_fields).place(x = 890, y = 395)                            
                            
#keynoteslabel and box
keynotesLable = Label(tkWindow,text="Key Notes").place(x = 760, y = 430)
keynotes = StringVar()
keynotesEntry = Entry(tkWindow, textvariable=keynotes).place(x = 760, y = 460)

Button(tkWindow, text= "X", command=del_keynote).place(x = 890, y = 455)                            
                            
#linkslabel and box
linksLable = Label(tkWindow,text="Links").place(x = 1060, y = 70)
links = StringVar()
linksEntry = Entry(tkWindow, textvariable=links).place(x = 1060, y = 100)

Button(tkWindow, text= "X", command=del_links).place(x = 1190, y = 95)                            
                            
#emaillabel and box
emailLable = Label(tkWindow,text="E-mail").place(x = 1060, y = 130)
email = StringVar()
emailEntry = Entry(tkWindow, textvariable=email).place(x = 1060, y = 160)

Button(tkWindow, text= "X", command=del_email).place(x = 1190, y = 155)                            
                            
#websitelabel and box
websiteLable = Label(tkWindow,text="Website").place(x = 1060, y = 190)
website = StringVar()
websiteEntry = Entry(tkWindow, textvariable=website).place(x = 1060, y = 220)

Button(tkWindow, text= "X", command=del_website).place(x = 1190, y = 215)                            
                            
#publabel and box
pubLable = Label(tkWindow,text="Pub").place(x = 1060, y = 250)
pub = StringVar()
pubEntry = Entry(tkWindow, textvariable=pub).place(x = 1060, y = 280)

Button(tkWindow, text= "X", command=del_pub).place(x = 1190, y = 275)                            
                            
#citationlabel and box
citeLable = Label(tkWindow,text="Citation").place(x = 1060, y = 310)
cite = StringVar()
citeEntry = Entry(tkWindow, textvariable=cite).place(x = 1060, y = 340)

Button(tkWindow, text= "X", command=del_cite).place(x = 1190, y = 335)                            
                            
#hindexlabel and box
hLable = Label(tkWindow,text="H index").place(x = 1060, y = 370)
h = StringVar()
hEntry = Entry(tkWindow, textvariable=h).place(x = 1060, y = 400)

Button(tkWindow, text= "X", command=del_hindex).place(x = 1190, y = 395)                            
                            
#h5indexlabel and box
h5Lable = Label(tkWindow,text="H5 index").place(x = 1060, y = 430)
h5 = StringVar()
h5Entry = Entry(tkWindow, textvariable=h5).place(x = 1060, y = 460)

Button(tkWindow, text= "X", command=del_h5index).place(x = 1190, y = 455)                            
                            
#idlabel and box
idLable = Label(tkWindow,text="ID").place(x = 760, y = 490)
intid = StringVar()
idEntry = Entry(tkWindow, textvariable=intid).place(x = 760, y = 520)

Button(tkWindow, text= "X", command=del_id).place(x = 890, y = 515)

#invitedlabel and box
invLable = Label(tkWindow,text="Invited to Attend").place(x = 460, y = 495)
statusInv = IntVar()
Radiobutton(tkWindow, text= "Yes", variable = statusInv, value=1).place(x = 460, y = 520)
Radiobutton(tkWindow, text= "No", variable = statusInv, value=2).place(x = 530, y = 520)

Button(tkWindow, text= "X", command=del_invite).place(x = 590, y = 515)

#attendedlabel and box
invLable2 = Label(tkWindow,text="Attended").place(x = 1060, y = 495)
statusAt = IntVar() 
Radiobutton(tkWindow, text= "Yes", variable = statusAt, value=1).place(x = 1060, y = 520)
Radiobutton(tkWindow, text= "No", variable = statusAt, value=2).place(x = 1130, y = 520)

Button(tkWindow, text= "X", command=del_attend).place(x = 1190, y = 515)
                                            
Button(tkWindow, text= "Input Information", command=inputHandInfo).place(x = 145, y = 350)
Button(tkWindow, text= "Import Table", command=inputTable).place(x = 155, y = 400)
Button(tkWindow, text= "Update Information", command=updateInfo).place(x = 135, y = 450)
Button(tkWindow, text= "Quit", command=Close).place(x = 180, y = 500)

tkWindow.resizable(False,False)
tkWindow.mainloop()


# In[ ]:




