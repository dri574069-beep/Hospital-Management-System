from django.shortcuts import render,redirect
import json
from .models import login,patient_info,patient_contact_info,patient_emergency_con,patient_Medical_info,doctor_perinfo,Doctors_contact_info,DoctorsProfessionInfo,adminInfo,Department,doctors_hos_infp,doctors_schedule,recep_person_info,recep_contact_info,recep_employ_info,ambulance_info,driver_info,maintenance_info,Nurse_Personal_info,nurse_contact_info,nurse_employee_info,nurse_work_info,floor_info,beds_info,medicine,room_info,appointments

from .forms import loginInfo,ptientInfo,patientnorInfo,doctorPersonalInfo,DoctorsData,adminForms,DepartmentForms,docInfoForms,recep_perInfo,recep_contact,ambulanceInfo,ambdriverAndmainInfo,nursePerInfo,NurseEmployInfo,floorsInfo,bedsInfo,appointment,medForms,checkPass,roomsInfo
from werkzeug.security import generate_password_hash,check_password_hash
import os
# Create your views here.
def user_login(request):
    form=loginInfo()
    if request.method=="POST":
        form=loginInfo(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            hashed_password=generate_password_hash(password)
            savePass(request,email,hashed_password)
            return redirect("checkpass")
    return render(request,"index.html",{"forms":form})

def savePass(request,email,hashed_password):
        if  not login.objects.filter(email=email).exists():
             login.objects.create(
                         password=hashed_password,
                         email=email
                     )
     #    doctor_perinfo.objects.all().delete()
     #    Doctors_contact_info.objects.all().delete()
     #    doctors_hos_infp.objects.all().delete()
     #    doctors_schedule.objects.all().delete()
        request.session["email"]=email
def checkpass(request):
     email=request.session.get("email")
     log=login.objects.get(email=email)
     hashed_password=log.password
     passw=checkPass()
     if request.method=="POST":
          passw=checkPass(request.POST)
          if passw.is_valid():
               password=passw.cleaned_data["password"]
               if check_password_hash(hashed_password,password):
                    return redirect("home")
               else:
                    return redirect("checkpass")
     return render(request,"checkPass.html",{"pass":passw})
def home(request):
     return render(request,"homepage.html")
def patientdataForms(request):
    patientData=patientnorInfo()
    if request.method=="POST":
        patientData=patientnorInfo(request.POST)
        if patientData.is_valid():
            phone_number=patientData.cleaned_data["phone_number"]
            email=patientData.cleaned_data["email"]
            address=patientData.cleaned_data["address"]
            city=patientData.cleaned_data["city"]
            country=patientData.cleaned_data["country"]
            emergency_contact_name=patientData.cleaned_data["emergency_contact_name"]
            emergency_number=patientData.cleaned_data["emergency_number"]
            allergies=patientData.cleaned_data["allergies"]
            height=patientData.cleaned_data["height"]
            weight=patientData.cleaned_data["weight"]
            importantPatientData(request,phone_number,email,address,city,country,emergency_contact_name,emergency_number,allergies,height,weight)
    return render(request,"patientInfo.html",{"Infos":patientData})
def importantPatientData(request,phone_number,email,address,city,country,emergency_contact_name,emergency_number,allergies,height,weight):
     patients=patient_emergency_con.objects.create(
          emergency_con_name=emergency_contact_name,
          emergency_number=emergency_number
     )
     request.session["pat_id"]=patients.id
     patient_contact_info.objects.create(
          phone_number=phone_number,
          email=email,
          address=address,
          city=city,
          country=country
     )
     patient_Medical_info.objects.create(
          allergies=allergies,
          height=height,
          weight=weight
     ) 
def patientData(request):
        Pdatas=ptientInfo()
        if request.method=="POST":
            Pdatas=ptientInfo(request.POST)
            if Pdatas.is_valid():
                name=Pdatas.cleaned_data["name"]
                date_of_birth=Pdatas.cleaned_data["date_of_birth"]
                age=Pdatas.cleaned_data["age"]
                gender=Pdatas.cleaned_data["gender"]
                blood_group=Pdatas.cleaned_data["blood_group"]
                martial_status=Pdatas.cleaned_data["martial_status"]
                nationality=Pdatas.cleaned_data["nationality"]
                getData(name,date_of_birth,age,gender,blood_group,martial_status,nationality)
        return render(request,"patientData.html",{"Datas":Pdatas})
def getData(name,date_of_birth,age,gender,blood_group,martial_status,nationality):
        patient_info.objects.create(
            full_name=name,
            date_of_birth=date_of_birth,
            age=age,
            gender=gender,
            blood_group=blood_group,
            martial_status=martial_status,
            nationality=nationality
        )
def create_admin():
    password=os.environ.get("PASSWORD")
    new_pass=generate_password_hash(password)
    adminInfo.objects.create(
        name=os.environ.get("NAME"),
        email=os.environ.get("EMAIL"),
        password=new_pass
    )
def getAdminData(request):
    adminForm=adminForms()
    password=os.environ.get("PASSWORD")
    new_pass=generate_password_hash(password)
    if request.method=="POST":
         adminForm=adminForms(request.POST)
         if adminForm.is_valid():
              name=adminForm.cleaned_data["name"]
              email=adminForm.cleaned_data["email"]
              password=adminForm.cleaned_data["password"]
              check_data(name,email,password,new_pass)
              return redirect("show_docData")
    return render(request,"adminPage.html",{"forms":adminForm})
def check_data(name,email,password,new_pass):
    if name==os.environ.get("NAME") and email==os.environ.get("EMAIL") and  check_password_hash(new_pass,password):
          print("welcome")
    else:
         return redirect("getAdminData")
def show_docData(request):
     name=request.session.get("name")
     doctors_name=doctor_perinfo.objects.all()
     infos=Department.objects.all()
     doc_num=Doctors_contact_info.objects.all()
     return render(request,"HospitalHistory.html",{"names":doctors_name,"dataas":infos,"con_infos":doc_num})
def doctorsInfoForms(request): 
    print("making form for doctors personal data is running")
    formsData=doctorPersonalInfo()
    if request.method=="POST":
        formsData=doctorPersonalInfo(request.POST)   
        if formsData.is_valid():
            name=formsData.cleaned_data["name"] 
            specialization=formsData.cleaned_data["specialization"]
            gender=formsData.cleaned_data["gender"]
            date_of_birth=formsData.cleaned_data["date_of_birth"]
            nationality=formsData.cleaned_data["nationality"]
            savingDoctorPerData(request,name,specialization,gender,date_of_birth,nationality)
            show_docData(request)
            return redirect("makingDoctorsForms")
    return render(request,"DoctorPerInfo.html",{"information":formsData})
def savingDoctorPerData(request,name,specialization,gender,date_of_birth,nationality):
    print("saving doctors personal data is running")
    doc=doctor_perinfo.objects.create(
            full_name=name,
            specialization=specialization,
            gender=gender,
            date_of_birth=date_of_birth,
            nationality=nationality
        )
    request.session["doc_id"]=doc.id
def makingDoctorsForms(request):
    DocData=DoctorsData()
    if request.method=="POST":
             DocData=DoctorsData(request.POST)
             if DocData.is_valid():
                  phone_number=DocData.cleaned_data["phone_number"]
                  email=DocData.cleaned_data["email"]
                  address=DocData.cleaned_data["address"]
                  city=DocData.cleaned_data["city"]
                  department=DocData.cleaned_data["department"]
                  country=DocData.cleaned_data["country"]
                  medical_lincense_num=DocData.cleaned_data["medical_lincense_num"]
                  qualification=DocData.cleaned_data["qualification"]
                  university=DocData.cleaned_data["university"]
                  years_of_experience=DocData.cleaned_data["years_of_experience"]
                  biography=DocData.cleaned_data["biography"]
                  saveDoctorInfos(request,phone_number,email,address,department,city,country,medical_lincense_num,qualification,university,years_of_experience,biography)
    return render(request,"DoctorsData.html",{"DoctorDatas":DocData})
def saveDoctorInfos(request,phone_number,email,address,department,city,country,medical_lincense_num,qualification,university,years_of_experience,biography):
        doc_id=request.session.get("doc_id")
        doctor=doctor_perinfo.objects.get(id=doc_id)
        doctor_id=doctor.id
        Doctors_contact_info.objects.create(
               per_id_id=doctor_id,
               phone_number=phone_number,
               email=email,
               address=address,
               city=city,
               country=country,
                         )  
        DoctorsProfessionInfo.objects.create(
                    pro_id_id=doctor_id,
                    medical_lincense_num=medical_lincense_num,
                    qualification=qualification,
                    department=department,
                    university=university,
                    years_of_experience=years_of_experience,
                    biography=biography
                         )
def dep_forms(request):
    dep_forms=DepartmentForms()
    if request.method=="POST":
        dep_forms=DepartmentForms(request.POST)
        if dep_forms.is_valid():
             dep_name=dep_forms.cleaned_data["dep_name"]
             dep_code=dep_forms.cleaned_data["dep_code"]
             dep_head=dep_forms.cleaned_data["dep_head"]
             description=dep_forms.cleaned_data["description"]
             location=dep_forms.cleaned_data["location"]
             opening_time=dep_forms.cleaned_data["opening_time"]
             closing_time=dep_forms.cleaned_data["closing_time"]
             status=dep_forms.cleaned_data["status"]
             savingDepInfo(request,dep_name,dep_code,dep_head,description,location,opening_time,closing_time,status)
    return render(request,"departmentStuff.html",{"deps_infos":dep_forms})
def savingDepInfo(request,dep_name,dep_code,dep_head,description,location,opening_time,closing_time,status):
    doctors=doctor_perinfo.objects.all()
    count=0
    for doc in doctors:
        count+=1
    department=Department.objects.create(
          department_name=dep_name,
          department_code=dep_code,
          department_head=dep_head,
          description=description,
          location=location,
          opening_time=opening_time,
          closing_time=closing_time,
          status=status,
          total_doctors=count
     )
    request.session["dep_id"]=department.id
def ShowDocsInfo(request,id):
     Data=doctor_perinfo.objects.filter(id=id)
     contact_data=Doctors_contact_info.objects.filter(per_id_id=id)
     profession_data=DoctorsProfessionInfo.objects.filter(pro_id_id=id)
     doctor_info=doctors_hos_infp.objects.filter(res_id_id=id)
     return render(request,"ShowDoctorsData.html",{"datas":Data,"con_tact":contact_data,"pro_datas":profession_data,"docs":doctor_info})
def showDepartmentInfo(request,department_name):
      cons=Department.objects.filter(department_name=department_name)
      return render(request,"showDepInfo.html",{"deps":cons})
def makeDoctorsForms(request):
     doctorsFacts=docInfoForms()
     if request.method=="POST":
          doctorsFacts=docInfoForms(request.POST)
          if doctorsFacts.is_valid():
               joining_date=doctorsFacts.cleaned_data['joining_date']
               employment_type=doctorsFacts.cleaned_data["employment_type"]
               office_num=doctorsFacts.cleaned_data["office_num"]
               status=doctorsFacts.cleaned_data["status"]
               workingDays=doctorsFacts.cleaned_data["workingDays"]
               start_time=doctorsFacts.cleaned_data["start_time"]
               end_time=doctorsFacts.cleaned_data["end_time"]
               saveThatDoctorInfo(request,joining_date,employment_type,office_num,status,workingDays,start_time,end_time)
     return render(request,"doctorsRanInfo.html",{"doctor_dataa":doctorsFacts})
def saveThatDoctorInfo(request,joining_date,employment_type,office_num,status,workingDays,start_time,end_time):
    id=request.session.get("doc_id")
    doctors=doctor_perinfo.objects.get(id=id)
    doctor_id=doctors.id
    if doctors_hos_infp.objects.all().exists():
     doctors_hos_infp.objects.create(
               res_id_id=doctor_id,
               joining_date=joining_date,
               employment_type=employment_type,
               office_num=office_num,
               status=status,
     )
     if doctors_hos_infp.objects.all().exists():
          doctors_schedule.objects.create(
               doc_id_id=doctor_id,
               working_days=workingDays,
               start_time=start_time,
               end_time=end_time
          )
def fetchRecapPerInfo(request):
     recepPerInfo=recep_perInfo()
     if request.method=="POST":
          recepPerInfo=recep_perInfo(request.POST)
          if recepPerInfo.is_valid():
               name=recepPerInfo.cleaned_data["name"]
               date_of_birth=recepPerInfo.cleaned_data["date_of_birth"]
               gender=recepPerInfo.cleaned_data["gender"]
               nationality=recepPerInfo.cleaned_data["nationality"]
               saveRecepPerInfo(request,name,date_of_birth,gender,nationality)
               return redirect("fetchnorrecepdata")
     return render(request,"enterRecepPerInfo.html",{"perDatas":recepPerInfo})
def saveRecepPerInfo(request,name,date_of_birth,gender,nationality):
     recep=recep_person_info.objects.create(
          full_name=name,
          date_of_birth=date_of_birth,
          gender=gender,
          nationality=nationality
     )
     request.session["recep_id"]=recep.id
def fetchnorrecepdata(request):
     receData=recep_contact()
     if request.method=="POST":
          receData=recep_contact(request.POST)
          if receData.is_valid():
               phone_number=receData.cleaned_data["phone_number"]
               email=receData.cleaned_data["email"]
               address=receData.cleaned_data["address"]
               city=receData.cleaned_data["city"]
               country=receData.cleaned_data["country"]
               emergency_contact_name=receData.cleaned_data["emergency_contact_name"]
               emergency_contact_number=receData.cleaned_data["emergency_contact_number"]
               joining_date=receData.cleaned_data["joining_date"]
               salary=receData.cleaned_data["salary"]
               status=receData.cleaned_data["status"]
               desk_number=receData.cleaned_data["desk_number"]
               shift_start_time=receData.cleaned_data["shift_start_time"]
               shift_end_time=receData.cleaned_data["shift_end_time"]
               saveSimrecepData(request,phone_number,email,address,city,desk_number,country,emergency_contact_name,emergency_contact_number,joining_date,salary,status,shift_start_time,shift_end_time)
     return render(request,"recepSimDataFroms.html",{"SimDatas":receData})
def saveSimrecepData(request,phone_number,email,address,city,desk_number,country,emergency_contact_name,emergency_contact_number,joining_date,salary,status,shift_start_time,shift_end_time):
     id=request.session.get("recep_id")
     re_id=recep_person_info.objects.get(id=id)
     recepcontact=recep_contact_info.objects.create(
          recep_id=re_id,
          phone_number=phone_number,
          email=email,
          address=address,
          city=city,
          country=country,
          emergency_contact_name=emergency_contact_name,
          emergency_contact_number=emergency_contact_number
     )
     recepInfo=recep_employ_info.objects.create(
          sec_id=re_id,
          joining_date=joining_date,
          salary=salary,
          status=status,
          desk_number=desk_number,
          shift_start_time=shift_start_time,
          shift_end_time=shift_end_time
     )
def ShowReceoOerData(request):
     id=request.session.get("recep_id")
     per_datas=recep_person_info.objects.filter(id=id)
     contact_data=recep_contact_info.objects.filter(recep_id=id)
     emp_data=recep_employ_info.objects.filter(sec_id=id)
     return render(request,"showRecepPerData.html",{"per_data":per_datas,"contact_data":contact_data,"emp_data":emp_data})
def makeambforms(request):
     am_info=ambulanceInfo()
     if request.method=="POST":
          am_info=ambulanceInfo(request.POST)
          if am_info.is_valid():
               ambulance_num=am_info.cleaned_data["ambulance_num"]
               vehicle_model=am_info.cleaned_data["vehicle_model"]
               registration_number=am_info.cleaned_data["registration_number"]
               manufacturing_year=am_info.cleaned_data["manufacturing_year"]
               capacity=am_info.cleaned_data["capacity"]
               saveaminfo(request,ambulance_num,vehicle_model,registration_number,manufacturing_year,capacity)
               return redirect("addAmNorInfo")
     return render(request,"ambulanceinfoForms.html",{"amb_info":am_info})
def saveaminfo(request,ambulance_num,vehicle_model,registration_number,manufacturing_year,capacity):
     savedAmInfo=ambulance_info.objects.create(
          ambulance_number=ambulance_num,
          vehicle_model=vehicle_model,
          registration_number=registration_number,
          manufacturing_year=manufacturing_year,
          capacity=capacity,
     )
     request.session["am_id"]=savedAmInfo.id
def addAmNorInfo(request):
     am_info_forms=ambdriverAndmainInfo()
     if request.method=="POST":
          am_info_forms=ambdriverAndmainInfo(request.POST)
          if am_info_forms.is_valid():
               assigned_hospital=am_info_forms.cleaned_data["assigned_hospital"]
               assigned_staff=am_info_forms.cleaned_data["assigned_staff"]
               availability_status=am_info_forms.cleaned_data["availability_status"]
               service_date=am_info_forms.cleaned_data["service_date"]
               next_service_date=am_info_forms.cleaned_data["next_service_date"]
               maintenance_notes=am_info_forms.cleaned_data["maintenance_notes"]
               fuel_status=am_info_forms.cleaned_data["fuel_status"]
               saveamNorInfo(request,assigned_hospital,assigned_staff,availability_status,service_date,next_service_date,maintenance_notes,fuel_status)
     return render(request,"ambulanceInfo2.html",{"am_info":am_info_forms})
def saveamNorInfo(request,assigned_hospital,assigned_staff,availability_status,service_date,next_service_date,maintenance_notes,fuel_status):
     id=request.session.get("am_id")
     amb_id=ambulance_info.objects.get(id=id)
     driver_info.objects.create(
          ambu_id=amb_id,
          assigned_hospital=assigned_hospital,
          assigned_staff=assigned_staff,
          availability_status=availability_status,
     )
     maintenance_info.objects.create(
          amser_id=amb_id,
          service_date=service_date,
          next_service_date=next_service_date,
          maintenance_notes=maintenance_notes,
          fuel_status=fuel_status
     )
def getAmbukancesInfo(request):
     ambId=request.session.get("am_id")
     amb_info=ambulance_info.objects.filter(id=ambId)
     dri_info=driver_info.objects.filter(ambu_id=ambId)
     main_info=maintenance_info.objects.filter(amser_id=ambId)
     return render(request,"showAmdulanceInfo.html",{"amb_info":amb_info,"dri_info":dri_info,"main_info":main_info})
def enterNurseInfo(request):
     nurse_info=nursePerInfo()
     if request.method=="POST":
          nurse_info=nursePerInfo(request.POST)
          if nurse_info.is_valid():
               name=nurse_info.cleaned_data["name"]
               date_of_birth=nurse_info.cleaned_data["date_of_birth"]
               gender=nurse_info.cleaned_data["gender"]
               blood_group=nurse_info.cleaned_data["blood_group"]
               nationality=nurse_info.cleaned_data["nationality"]
               phone_number=nurse_info.cleaned_data["phone_number"]
               email=nurse_info.cleaned_data["email"]
               address=nurse_info.cleaned_data["address"]
               city=nurse_info.cleaned_data["city"]
               country=nurse_info.cleaned_data["country"]
               saveNursePerInfo(request,name,date_of_birth,gender,blood_group,nationality,phone_number,email,address,city,country)
     return render(request,"nurseDataForms.html",{"nurseInfo":nurse_info})
def saveNursePerInfo(request,name,date_of_birth,gender,blood_group,nationality,phone_number,email,address,city,country):
     nursePerdata=Nurse_Personal_info.objects.create(
          full_name=name,
          date_of_birth=date_of_birth,
          gender=gender,
          blood_group=blood_group,
          nationality=nationality
     )
     request.session["nurse_id"]=nursePerdata.id
     nurse_id=request.session.get("nurse_id")
     nurses=Nurse_Personal_info.objects.get(id=nurse_id)
     nurse_id=nurses.id
     nurse_contact_info.objects.create(
          nurse_id=nurses,
          phone_number=phone_number,
          email=email,
          address=address,
          city=city,
          country=country
     )
def showNurseInfo(request):
     nurse_id=request.session.get("nurse_id")
     nurse_info=Nurse_Personal_info.objects.filter(id=nurse_id)
     nurseNorInfo=nurse_contact_info.objects.filter(nurse_id=nurse_id)
     nurseEmploy=nurse_employee_info.objects.filter(nu_id=nurse_id)
     nurseWork=nurse_work_info.objects.filter(se_id=nurse_id)
     return render(request,"showNurseData.html",{"nurse_info":nurse_info,"normalInfo":nurseNorInfo,"NurseEmp":nurseEmploy,"NurseWork":nurseWork})
def makeNurseEmployForms(request):
     nurse_empInfo=NurseEmployInfo()
     if request.method=="POST":
          nurse_empInfo=NurseEmployInfo(request.POST)
          if nurse_empInfo.is_valid():
               department=nurse_empInfo.cleaned_data["department"]
               qualification=nurse_empInfo.cleaned_data["qualification"]
               nursing_license_number=nurse_empInfo.cleaned_data["nursing_license_number"]
               years_of_experience=nurse_empInfo.cleaned_data["years_of_experience"]
               joining_date=nurse_empInfo.cleaned_data["joining_date"]
               employment_type=nurse_empInfo.cleaned_data["employment_type"]
               salary=nurse_empInfo.cleaned_data["salary"]
               status=nurse_empInfo.cleaned_data["status"]
               shift_start=nurse_empInfo.cleaned_data["shift_start"]
               shift_end=nurse_empInfo.cleaned_data["shift_end"]
               saveNurseEmpInfo(request,department,qualification,nursing_license_number,years_of_experience,joining_date,employment_type,salary,status,shift_start,shift_end)
     return render(request,"nurseEmpInfo.html",{"nurseEmp":nurse_empInfo})
def saveNurseEmpInfo(request,department,qualification,nursing_license_number,years_of_experience,joining_date,employment_type,salary,status,shift_start,shift_end):
     nurse_id=request.session.get("nurse_id")
     id=Nurse_Personal_info.objects.get(id=nurse_id)
     nurse_employee_info.objects.create(
          nu_id=id,
          department=department,
          qualification=qualification,
          nursing_license_number=nursing_license_number,
          years_of_experience=years_of_experience,
          joining_date=joining_date,
          employment_type=employment_type,
          salary=salary,
          status=status
     )
     nurse_work_info.objects.create(
          se_id=id,
          shift_start=shift_start,
          shift_end=shift_end
     )
def FloorInfo(request):
     floorInfo=floorsInfo()
     if request.method=="POST":
          floorInfo=floorsInfo(request.POST)
          if floorInfo.is_valid():
               floor_name=floorInfo.cleaned_data["floor_name"]
               floor_num=floorInfo.cleaned_data["floor_num"]
               floor_description=floorInfo.cleaned_data["floor_description"]
               saveFlooInfo(request,floor_name,floor_num,floor_description)
     return render(request,"floorForms.html",{"floorForms":floorInfo})
def saveFlooInfo(request,floor_name,floor_num,floor_description):
     floors=floor_info.objects.create(
          floor_name=floor_name,
          floor_num=floor_num,
          floor_description=floor_description
     )
     request.session["floor_id"]=floors.id
     floor_id=request.session.get("floor_id")
     floors=floor_info.objects.get(id=floor_id)
     floor_num=floors.floor_num
     dep=Department.objects.create(
          floor_number=floor_num
     )
def showFloorInfo(request):
     floor_id=request.session.get("floor_id")
     floor=floor_info.objects.filter(id=floor_id)
     return render(request,"showfloorInfo.html",{"floors":floor})
def bedsInfoForms(request):
     beds=bedsInfo()
     if request.method=="POST":
          beds=bedsInfo(request.POST)
          if beds.is_valid():
               bed_number=beds.cleaned_data["bed_number"]
               room_no=beds.cleaned_data["room_no"]
               bed_type=beds.cleaned_data["bed_type"]
               floor_number=beds.cleaned_data["floor_number"]
               bed_status=beds.cleaned_data["bed_status"]
               assigned_date=beds.cleaned_data["assigned_date"]
               discharge_date=beds.cleaned_data["discharge_date"]
               saveBedsInfo(request,bed_number,room_no,bed_type,floor_number,bed_status,assigned_date,discharge_date)
     return render(request,"bedsForms.html",{"bedsForms":beds})
def saveBedsInfo(request,bed_number,room_no,bed_type,floor_number,bed_status,assigned_date,discharge_date):
     dep_id=request.session.get("dep_id")
     deps=Department.objects.get(id=dep_id)
     deps_name=deps.department_name
     bedsinfo=beds_info.objects.create(
          bed_number=bed_number,
          room_no=room_no,
          bed_type=bed_type,
          floor_number=floor_number,
          department=deps_name,
          bed_status=bed_status,
          assigned_date=assigned_date,
          discharge_date=discharge_date
     )
     request.session["bed_id"]=bedsinfo.id
def showbedsInfo(request):
     bed_id=request.session.get("bed_id")
     beds=beds_info.objects.filter(id=bed_id)
     return render(request,"showBeds.html",{"beds":beds})
def AppointmentForms(request):
     appointinfo=appointment()
     if request.method=="POST":
          appointinfo=appointment(request.POST)
          if appointinfo.is_valid():
               patient=appointinfo.cleaned_data["patient"]
               doctor=appointinfo.cleaned_data["doctor"]
               appointment_date=appointinfo.cleaned_data["appointment_date"]
               appointment_time=appointinfo.cleaned_data["appointment_time"]
               reason_for_visit=appointinfo.cleaned_data["reason_for_visit"]
               booked_date=appointinfo.cleaned_data["booked_date"]
               saveappointnfo(request,patient,appointment_date,doctor,appointment_time,reason_for_visit,booked_date)
     return render(request,"appointForms.html",{"appoint":appointinfo})
def saveappointnfo(request,patient,appointment_date,doctor,appointment_time,reason_for_visit,booked_date):
     appointmentInfo=appointments.objects.create(
          patient=patient,
          doctor=doctor,
          appointment_date=appointment_date,
          appointment_time=appointment_time,
          reason_for_visit=reason_for_visit,
          booked_date=booked_date
     )
     request.session["app_id"]=appointmentInfo.id
def showappointinfo(request):
     id=request.session.get("app_id")
     appoInfo=appointments.objects.filter(id=id)
     return render(request,"showAppointInfo.html",{"app_info":appoInfo})
def medInfoForms(request):
     meds=medForms()
     if request.method=="POST":
          meds=medForms(request.POST)
          if meds.is_valid():
               medicine_name=meds.cleaned_data["medicine_name"]
               generic_name=meds.cleaned_data["generic_name"]
               category=meds.cleaned_data["category"]
               dosage_form=meds.cleaned_data["dosage_form"]
               strength=meds.cleaned_data["strength"]
               manufacturer=meds.cleaned_data["manufacturer"]
               quantity_in_stock=meds.cleaned_data["quantity_in_stock"]
               unit_price=meds.cleaned_data["unit_price"]
               expiry_date=meds.cleaned_data["expiry_date"]
               prescription_required=meds.cleaned_data["prescription_required"]
               status=meds.cleaned_data["status"]
               saveMedInfo(request,medicine_name,generic_name,category,dosage_form,strength,manufacturer,quantity_in_stock,unit_price,expiry_date,prescription_required,status)
     return render(request,"medsForm.html",{"med":meds})
def saveMedInfo(request,medicine_name,generic_name,category,dosage_form,strength,manufacturer,quantity_in_stock,unit_price,expiry_date,prescription_required,status):
     medicines=medicine.objects.create(
          medicine_name=medicine_name,
          generic_name=generic_name,
          category=category,
          dosage_form=dosage_form,
          strength=strength,
          manufacturer=manufacturer,
          quantity_in_stock=quantity_in_stock,
          unit_price=unit_price,
          expiry_date=expiry_date,
          prescription_required=prescription_required,
          status=status
     )
     request.session["med_id"]=medicines.id
def roomsForm(request):
     room=roomsInfo()
     if request.method=="POST":
          room=roomsInfo(request.POST)
          if room.is_valid():
               room_number=room.cleaned_data["room_number"]
               room_type=room.cleaned_data['room_type']
               floor_number=room.cleaned_data["floor_number"]
               department=room.cleaned_data["department"]
               capacity=room.cleaned_data["capacity"]
               occupied_beds=room.cleaned_data["occupied_beds"]
               available_beds=room.cleaned_data["available_beds"]
               room_status=room.cleaned_data["room_status"]
               daily_charge=room.cleaned_data["daily_charge"]
               saveinfo(request,room_number,room_type,floor_number,department,capacity,occupied_beds,available_beds,room_status,daily_charge)
     return render(request,"roomsform.html",{"room":room})
def saveinfo(request,room_number,room_type,floor_number,department,capacity,occupied_beds,available_beds,room_status,daily_charge):
     roomsInfo=room_info.objects.create(
          room_number=room_number,
          room_type=room_type,
          floor_number=floor_number,
          department=department,
          capacity=capacity,
          occupied_beds=occupied_beds,
          available_beds=available_beds,
          room_status=room_status,
          daily_charge=daily_charge
     )
     request.session["room_id"]=roomsInfo.id
def showroomInfo(request):
     room_id=request.session.get("room_id")
     room_infos=room_info.objects.filter(id=room_id)
     return render(request,"showroomsinfo.html",{"rooms":room_infos})
def patient(request):
     return render(request,"patienthomepage.html")
def showappointmentforadmin(request):
     appointment=appointments.objects.all()
     return render(request,"apoointinfoforadmin.html",{"appointments":appointment})
def showdocsinfo(request):
     doctors=doctor_perinfo.objects.all()
     return render(request,"doctorsinfoforpatients.html",{"docs":doctors})
def patientinfotpadmin(request):   
     perinfo=patient_info.objects.all()
     contactinfo=patient_contact_info.objects.all()
     emerconinfo=patient_emergency_con.objects.all()
     medicalinfo=patient_Medical_info.objects.all()
     return render(request,"showpatientinfo.html",{"perinfo":perinfo,"contactinfo":contactinfo,"emerconinfo":emerconinfo,"medicalinfo":medicalinfo})
def showhospital(request):
     return render(request,"HospitalHistory.html")