from flask import Flask , jsonify, request
import json
import numpy as np
import pickle
import pandas as pd


app = Flask(__name__)

department_Finance = 0
department_HR = 0
department_Legal = 0
department_Operations = 0
department_Procurement = 0
department_RD = 0  # department_R&D
department_SalesMarketing = 0  # department_Sales & Marketing
department_Technology = 0
region_region_2 = 0
region_region_3 = 0
region_region_4 = 0
region_region_5 = 0
region_region_6 = 0
region_region_7 = 0
region_region_8 = 0
region_region_9 = 0
region_region_10 = 0
region_region_11 = 0
region_region_12 = 0
region_region_13 = 0
region_region_14 = 0
region_region_15 = 0
region_region_16 = 0
region_region_17 = 0
region_region_18 = 0
region_region_19 = 0
region_region_20 = 0
region_region_21 = 0
region_region_22 = 0
region_region_23 = 0
region_region_24 = 0
region_region_25 = 0
region_region_26 = 0
region_region_27 = 0
region_region_28 = 0
region_region_29 = 0
region_region_30 = 0
region_region_31 = 0
region_region_32 = 0
region_region_33 = 0
region_region_34 = 0
education_Below = 0
education_Master = 0
recruitment_channel_referred = 0
recruitment_channel_sourcing = 0
gender_m = 0
no_of_trainings_log = 0
age_log = 0
previous_year_rating = 0
length_of_service_log = 0
kpi = 0
awards = 0
avg_training_score_log = 0

@app.route('/', methods=['GET','POST'])
def value():

    if request.method == "POST":
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        dept = request_data['dept']#done
        region = request_data['region']#done
        education = request_data['education']
        gender = request_data['gender']
        recruitment_channel = request_data['recruitment_channel']
        global no_of_trainings_log
        global age_log
        global previous_year_rating
        global length_of_service_log
        global kpi
        global awards
        global avg_training_score_log
        no_of_trainings_log = np.log(int(request_data['no_of_trainings']))
        age_log = np.log(int(request_data['age']))
        previous_year_rating = int(request_data['previous_year_rating'])
        length_of_service_log = np.log(int(request_data['length_of_service']))
        kpi = int(request_data['kpi'])
        awards = int(request_data['awards'])
        avg_training_score_log = np.log(int(request_data['avg']))
        print(age_log,no_of_trainings_log,avg_training_score_log,length_of_service_log)
        global department_Finance
        global department_HR
        global department_Legal
        global department_Operations
        global department_Procurement
        global department_RD # department_R&D
        global department_SalesMarketing
        global department_Technology
        global region_region_2
        global region_region_3
        global region_region_4
        global region_region_5
        global region_region_6
        global region_region_7
        global region_region_8
        global region_region_9
        global region_region_10
        global region_region_11
        global region_region_12
        global region_region_13
        global region_region_14
        global region_region_15
        global region_region_16
        global region_region_17
        global region_region_18
        global region_region_19
        global region_region_20
        global region_region_21
        global region_region_22
        global region_region_23
        global region_region_24
        global region_region_25
        global region_region_26
        global region_region_27
        global region_region_28
        global region_region_29
        global region_region_30
        global region_region_31
        global region_region_32
        global region_region_33
        global region_region_34
        global education_Below   # education_Below Secondary
        global education_Master
        global recruitment_channel_referred
        global recruitment_channel_sourcing
        global gender_m

        if dept == 'Sales & Marketing':
            department_Finance = 0
            department_HR = 0
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 1 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'Operations':
            department_Finance = 0
            department_HR = 0
            department_Legal = 0
            department_Operations = 1
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'Technology':
            department_Finance = 0
            department_HR = 0
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 1
        elif dept ==  'R&D':
            department_Finance = 0
            department_HR = 0
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 0
            department_RD = 1 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'Procurement':
            department_Finance = 0
            department_HR = 0
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 1
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'Finance':
            department_Finance = 1
            department_HR = 0
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'HR':
            department_Finance = 0
            department_HR = 1
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'Legal':
            department_Finance = 0
            department_HR = 0
            department_Legal = 1
            department_Operations = 0
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        elif dept == 'Analytics':
            department_Finance = 0
            department_HR = 0
            department_Legal = 0
            department_Operations = 0
            department_Procurement = 0
            department_RD = 0 #department_R&D
            department_SalesMarketing = 0 #department_Sales & Marketing
            department_Technology = 0
        if region=='region_7':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=1
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_22':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=1
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_19':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=1
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_23':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=1
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_26':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=1
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_2':
            region_region_2=1
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_20':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=1
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_34':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=1
        elif region=='region_1':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_4':
            region_region_2=0
            region_region_3 = 0
            region_region_4=1
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_29':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=1
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_31':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=1
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_15' :
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=1
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_14':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=1
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_11':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=1
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_5':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=1
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_28':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=1
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_17':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=1
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region== 'region_12' :
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=1
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_21':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=1
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_8':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=1
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_32':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=1
            region_region_33=0
            region_region_34=0
        elif region=='region_6':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=1
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_33':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=1
            region_region_34=0
        elif region=='region_24':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=1
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_3':
            region_region_2=0
            region_region_3 = 1
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region=='region_9':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=1
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=0
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        elif region== 'region_18':
            region_region_2=0
            region_region_3 = 0
            region_region_4=0
            region_region_5=0
            region_region_6=0
            region_region_7=0
            region_region_8=0
            region_region_9=0
            region_region_10=0
            region_region_11=0
            region_region_12=0
            region_region_13=0
            region_region_14=0
            region_region_15=0
            region_region_16=0
            region_region_17=0
            region_region_18=1
            region_region_19=0
            region_region_20=0
            region_region_21=0
            region_region_22=0
            region_region_23=0
            region_region_24=0
            region_region_25=0
            region_region_26=0
            region_region_27=0
            region_region_28=0
            region_region_29=0
            region_region_30=0
            region_region_31=0
            region_region_32=0
            region_region_33=0
            region_region_34=0
        if education=="Master's & above":
            education_Below=0# education_Below Secondary
            education_Master=1 #education_Master's & above
        elif education=="Bachelor's":
            education_Below=0# education_Below Secondary
            education_Master=0 #education_Master's & above
        elif education=="Below Secondary":
            education_Below=1# education_Below Secondary
            education_Master=0 #education_Master's & above
        if gender=="male":
            gender_m=1
        else:
            gender_m=0
        if recruitment_channel == 'sourcing':
            recruitment_channel_referred=0
            recruitment_channel_sourcing=1
        elif recruitment_channel == 'referred':
            recruitment_channel_referred=1
            recruitment_channel_sourcing=0
        elif recruitment_channel == 'other':
            recruitment_channel_referred=0
            recruitment_channel_sourcing=0
        d= {'department_Finance': department_Finance,
                 'department_HR':department_HR,
                 'department_Legal':department_Legal,
                 'department_Operations': department_Operations,
                 'department_Procurement': department_Procurement,
                 'department_R&D':department_RD,
                 'department_Sales & Marketing': department_SalesMarketing,
                 'department_Technology': department_Technology,
                 'region_region_10': region_region_10,
                 'region_region_11': region_region_11,
                 'region_region_12':region_region_12,
                 'region_region_13': region_region_13,
                 'region_region_14': region_region_14,
                 'region_region_15': region_region_15,
                 'region_region_16': region_region_16,
                 'region_region_17': region_region_17,
                 'region_region_18': region_region_18,
                 'region_region_19': region_region_19,
                 'region_region_2': region_region_2,
                 'region_region_20': region_region_20,
                 'region_region_21': region_region_21,
                 'region_region_22': region_region_22,
                 'region_region_23': region_region_23,
                 'region_region_24': region_region_24,
                 'region_region_25': region_region_25,
                 'region_region_26': region_region_26,
                 'region_region_27': region_region_27,
                 'region_region_28': region_region_28,
                 'region_region_29': region_region_29,
                 'region_region_3': region_region_3,
                 'region_region_30': region_region_30,
                 'region_region_31':region_region_31,
                 'region_region_32': region_region_32,
                 'region_region_33': region_region_33,
                 'region_region_34': region_region_34,
                 'region_region_4': region_region_4,
                 'region_region_5': region_region_5,
                 'region_region_6': region_region_6,
                 'region_region_7': region_region_7,
                 'region_region_8': region_region_8,
                 'region_region_9': region_region_9,
                 'education_Below Secondary': education_Below,
                 "education_Master's & above": education_Master,
                 'gender_m':gender_m,
                 'recruitment_channel_referred': recruitment_channel_referred,
                 'recruitment_channel_sourcing':recruitment_channel_sourcing,
                 'no_of_trainings_log': no_of_trainings_log,
                 'age_log': age_log,
                 'previous_year_rating':previous_year_rating,
                 'length_of_service_log': length_of_service_log,
                 'KPIs_met >80%': kpi,
                 'awards_won?':awards,
                 'avg_training_score_log': avg_training_score_log}
        try:
            df = pd.DataFrame(data=d, index=[0])
            loaded_model = pickle.load(open(r"pima2.pickle.dat", "rb"))
            y_pred = loaded_model.predict(df.values)
            print(y_pred)
            if(y_pred[0]==1):
                return jsonify({'result': "yes"})
            elif(y_pred[0]==0):
                return jsonify({'result': "no"})
        except Exception as e:
            return jsonify({'result': str(e)+"ERROR"})
    else:
        return ''


if __name__=="__main__":
    app.run()