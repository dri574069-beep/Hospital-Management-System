from django.shortcuts import render,redirect
import json
import smtplib
from django.contrib.auth.decorators import login_required
from .models import users_login,patient_info,patient_contact_info,patient_emergency_con,patient_Medical_info,doctor_perinfo,Doctors_contact_info,DoctorsProfessionInfo,adminInfo,Department,doctors_hos_infp,doctors_schedule,recep_person_info,recep_contact_info,recep_employ_info,ambulance_info,driver_info,maintenance_info,Nurse_Personal_info,nurse_contact_info,nurse_employee_info,nurse_work_info,floor_info,beds_info,medicine,room_info,appointments
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import loginInfo,ptientInfo,patientnorInfo,doctorPersonalInfo,DoctorsData,adminForms,DepartmentForms,docInfoForms,recep_perInfo,recep_contact,ambulanceInfo,ambdriverAndmainInfo,nursePerInfo,NurseEmployInfo,floorsInfo,bedsInfo,appointment,medForms,checkPass,roomsInfo,deletePatientData,deletepatientContData,deleteEmerInfoPat,deletePatientMedInfo,DeleteNurseData,deleteNurseConInfo,DeleteNuseEmpInfos,DeleteNurseWorksInfo,deleteBeds,deleteApp,deleteRooms,deleteFloorsInfo,delRecepInformation,deleterecepEmpInfo,delRecepEmpInfo,deleteAmbulance,deleteDep,DeleteDoc,deleteMeds
from werkzeug.security import generate_password_hash,check_password_hash
import os
# Create your views here.
def user_login(request):
    form=loginInfo()
    if request.method=="POST":
        form=loginInfo(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            if  User.objects.filter(email=email).exists():
               print("user already exists")
               return redirect("checkpass")
            User.objects.create_user(
               username=username,
               password=password,
               email=email
               )
            return redirect("checkpass")
    return render(request,"index.html",{"forms":form})
def checkpass(request):
     log=checkPass()
     if request.method=="POST":
          log=checkPass(request.POST)
          if log.is_valid():
               username=log.cleaned_data["username"]
               password=log.cleaned_data["password"]
               user=authenticate(
                    request,
                    username=username,
                    password=password
               )
               if user is not None:
                    login(request,user)
                    print("welcome")
                    return redirect("home")
               else:
                    print("invalid username or password")
                    return redirect("checkpass")
     return render(request,"checkPass.html",{"pass":log})
@login_required
def home(request):
     return render(request,"homepage.html")
@login_required
def patientdataForms(request,id):
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
            importantPatientData(id,phone_number,email,address,city,country,emergency_contact_name,emergency_number,allergies,height,weight)
            return redirect("patient")
    return render(request,"patientInfo.html",{"Infos":patientData,"id":id})
def importantPatientData(id,phone_number,email,address,city,country,emergency_contact_name,emergency_number,allergies,height,weight):
     patient=patient_info.objects.get(id=id)
     patients=patient_emergency_con.objects.create(
          pat_id=patient,
          emergency_con_name=emergency_contact_name,
          emergency_number=emergency_number
     )
     patient_contact_info.objects.create(
          pat_id=patient,
          phone_number=phone_number,
          email=email,
          address=address,
          city=city,
          country=country
     )
     patient_Medical_info.objects.create(
          pat_id=patient,
          allergies=allergies,
          height=height,
          weight=weight
     ) 
@login_required
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
                patient_id=getData(name,date_of_birth,age,gender,blood_group,martial_status,nationality)
                return redirect("patientdataForms",id=patient_id)
        return render(request,"patientData.html",{"Datas":Pdatas})
def getData(name,date_of_birth,age,gender,blood_group,martial_status,nationality):
        patient=patient_info.objects.create(
            full_name=name,
            date_of_birth=date_of_birth,
            age=age,
            gender=gender,
            blood_group=blood_group,
            martial_status=martial_status,
            nationality=nationality
        )
        return patient.id
@login_required
def hospitalHistory(request):
     return render(request,"HospitalHistory.html")
def create_admin(request):
    if not adminInfo.objects.exists():
          password=os.environ.get("newPassword")
          new_pass=generate_password_hash(password)
          admin=adminInfo.objects.create(
               name=os.environ.get("NAME"),
               email=os.environ.get("EMAIL"),
               password=new_pass
          )
    return redirect("getAdminData")
def getAdminData(request):
    adminForm=adminForms()
    admin=adminInfo.objects.first()
    if not admin:
         return redirect("create_admin")
    email=admin.email
    passw=admin.password
    if request.method=="POST":
         adminForm=adminForms(request.POST)
         if adminForm.is_valid():
              name=adminForm.cleaned_data["name"]
              email=adminForm.cleaned_data["email"]
              password=adminForm.cleaned_data["password"]
              if name==os.environ.get("NAME") and email==os.environ.get("EMAIL") and  check_password_hash(passw,password):
                    user, created = User.objects.get_or_create(
                              username="admin",
                              defaults={"email": email}
                    )

                    if created:
                         user.set_password(password)
                         user.save()

                    login(request, user)

                    print("welcome")
                    return redirect("show_docData")
              else:
                    return redirect("getAdminData")
    return render(request,"adminPage.html",{"forms":adminForm})
@login_required
def show_docData(request):
     # name=request.session.get("name")
     doctors_name=doctor_perinfo.objects.all()
     infos=Department.objects.all()
     doc_num=Doctors_contact_info.objects.all()
     return render(request,"HospitalHistory.html",{"names":doctors_name,"dataas":infos,"con_infos":doc_num})
@login_required
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
            doc_id=savingDoctorPerData(request,name,specialization,gender,date_of_birth,nationality)
            return redirect("makingDoctorsForms",id=doc_id)
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
    return doc.id
@login_required
def makingDoctorsForms(request,id):
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
                  saveDoctorInfos(id,phone_number,email,address,department,city,country,medical_lincense_num,qualification,university,years_of_experience,biography)
    return render(request,"DoctorsData.html",{"DoctorDatas":DocData,"id":id})
def saveDoctorInfos(id,phone_number,email,address,department,city,country,medical_lincense_num,qualification,university,years_of_experience,biography):
        doctors=doctor_perinfo.objects.get(id=id)
        Doctors_contact_info.objects.create(
               per_id_id=doctors.id,
               phone_number=phone_number,
               email=email,
               address=address,
               city=city,
               country=country,
                         )  
        DoctorsProfessionInfo.objects.create(
                    pro_id_id=doctors.id,
                    medical_lincense_num=medical_lincense_num,
                    qualification=qualification,
                    department=department,
                    university=university,
                    years_of_experience=years_of_experience,
                    biography=biography
                         )
@login_required
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
             dep_id=savingDepInfo(request,dep_name,dep_code,dep_head,description,location,opening_time,closing_time,status)
    return render(request,"departmentStuff.html",{"deps_infos":dep_forms})
def savingDepInfo(request,dep_name,dep_code,dep_head,description,location,opening_time,closing_time,status):
    count=DoctorsProfessionInfo.objects.filter(department=dep_name).count()
    department=Department.objects.create(
          user=request.user,
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
    return department.id
@login_required
def ShowDocsInfo(request,id):
     Data=doctor_perinfo.objects.filter(id=id)
     contact_data=Doctors_contact_info.objects.filter(per_id_id=id)
     profession_data=DoctorsProfessionInfo.objects.filter(pro_id_id=id)
     doctor_info=doctors_hos_infp.objects.filter(res_id_id=id)
     return render(request,"ShowDoctorsData.html",{"datas":Data,"con_tact":contact_data,"pro_datas":profession_data,"docs":doctor_info})
@login_required
def showDepartmentInfo(request,department_name):
      cons=Department.objects.filter(department_name=department_name)
      return render(request,"showDepInfo.html",{"deps":cons})
@login_required
def fetchRecapPerInfo(request):
     recepPerInfo=recep_perInfo()
     if request.method=="POST":
          recepPerInfo=recep_perInfo(request.POST)
          if recepPerInfo.is_valid():
               name=recepPerInfo.cleaned_data["name"]
               date_of_birth=recepPerInfo.cleaned_data["date_of_birth"]
               gender=recepPerInfo.cleaned_data["gender"]
               nationality=recepPerInfo.cleaned_data["nationality"]
               recep_id=saveRecepPerInfo(request,name,date_of_birth,gender,nationality)
               return redirect("fetchnorrecepdata",id=recep_id)
     return render(request,"enterRecepPerInfo.html",{"perDatas":recepPerInfo})
def saveRecepPerInfo(request,name,date_of_birth,gender,nationality):
     recep=recep_person_info.objects.create(
          full_name=name,
          date_of_birth=date_of_birth,
          gender=gender,
          nationality=nationality
     )
     return recep.id
@login_required
def fetchnorrecepdata(request,id):
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
               saveSimrecepData(request,id,phone_number,email,address,city,desk_number,country,emergency_contact_name,emergency_contact_number,joining_date,salary,status,shift_start_time,shift_end_time)
     return render(request,"recepSimDataFroms.html",{"SimDatas":receData,"id":id})
def saveSimrecepData(request,id,phone_number,email,address,city,desk_number,country,emergency_contact_name,emergency_contact_number,joining_date,salary,status,shift_start_time,shift_end_time):
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
@login_required
def recephome(request):
     recep=recep_person_info.objects.all()
     return render(request,"receptionist.html",{"recep":recep})
# def recepData(request):
#      recep=recep_person_info.objects.all()
#      return render(request,"receptionist.html",{"recep":recep})
@login_required
def ShowReceoOerData(request,id):
     per_datas=recep_person_info.objects.filter(id=id)
     contact_data=recep_contact_info.objects.filter(recep_id=id)
     emp_data=recep_employ_info.objects.filter(sec_id=id)
     return render(request,"showRecepPerData.html",{"per_data":per_datas,"contact_data":contact_data,"emp_data":emp_data})
@login_required
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
               amb_id=saveaminfo(request,ambulance_num,vehicle_model,registration_number,manufacturing_year,capacity)
               return redirect("addAmNorInfo",id=amb_id)
     return render(request,"ambulanceinfoForms.html",{"amb_info":am_info})
def saveaminfo(request,ambulance_num,vehicle_model,registration_number,manufacturing_year,capacity):
     savedAmInfo=ambulance_info.objects.create(
          ambulance_number=ambulance_num,
          vehicle_model=vehicle_model,
          registration_number=registration_number,
          manufacturing_year=manufacturing_year,
          capacity=capacity,
     )
     return savedAmInfo.id
@login_required
def addAmNorInfo(request,id):
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
               saveamNorInfo(request,id,assigned_hospital,assigned_staff,availability_status,service_date,next_service_date,maintenance_notes,fuel_status)
     return render(request,"ambulanceInfo2.html",{"am_info":am_info_forms,"id":id})
def saveamNorInfo(request,id,assigned_hospital,assigned_staff,availability_status,service_date,next_service_date,maintenance_notes,fuel_status):
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
@login_required
def ambHome(request):
     amb=ambulance_info.objects.all()
     return render(request,"ambulance.html",{"amb":amb})
@login_required
def getAmbukancesInfo(request,id):
     amb_info=ambulance_info.objects.filter(id=id)
     dri_info=driver_info.objects.filter(ambu_id=id)
     main_info=maintenance_info.objects.filter(amser_id=id)
     return render(request,"showAmdulanceInfo.html",{"amb_info":amb_info,"dri_info":dri_info,"main_info":main_info})
@login_required
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
               nurse_id=saveNursePerInfo(request,name,date_of_birth,gender,blood_group,nationality,phone_number,email,address,city,country)
               return redirect("makeNurseEmployForms",id=nurse_id)
     return render(request,"nurseDataForms.html",{"nurseInfo":nurse_info})
def saveNursePerInfo(request,name,date_of_birth,gender,blood_group,nationality,phone_number,email,address,city,country):
     nursePerdata=Nurse_Personal_info.objects.create(
          full_name=name,
          date_of_birth=date_of_birth,
          gender=gender,
          blood_group=blood_group,
          nationality=nationality
     )
     nurse_contact_info.objects.create(
          nurse_id=nursePerdata,
          phone_number=phone_number,
          email=email,
          address=address,
          city=city,
          country=country
     )
     return nursePerdata.id
@login_required
def NurseHome(request):
     Nurse=Nurse_Personal_info.objects.all()
     return render(request,"Nurse.html",{"nurse":Nurse})
@login_required
def showNurseInfo(request,id):
     nurse_info=Nurse_Personal_info.objects.filter(id=id)
     nurseNorInfo=nurse_contact_info.objects.filter(nurse_id=id)
     nurseEmploy=nurse_employee_info.objects.filter(nu_id=id)
     nurseWork=nurse_work_info.objects.filter(se_id=id)
     return render(request,"showNurseData.html",{"nurse_info":nurse_info,"normalInfo":nurseNorInfo,"NurseEmp":nurseEmploy,"NurseWork":nurseWork})
@login_required
def makeNurseEmployForms(request,id):
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
               saveNurseEmpInfo(request,id,department,qualification,nursing_license_number,years_of_experience,joining_date,employment_type,salary,status,shift_start,shift_end)
     return render(request,"nurseEmpInfo.html",{"nurseEmp":nurse_empInfo,"id":id})
def saveNurseEmpInfo(request,id,department,qualification,nursing_license_number,years_of_experience,joining_date,employment_type,salary,status,shift_start,shift_end):
     nurse_id=Nurse_Personal_info.objects.get(id=id)
     nurse_employee_info.objects.create(
          nu_id=nurse_id,
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
          se_id=nurse_id,
          shift_start=shift_start,
          shift_end=shift_end
     )
@login_required
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
     floors=floor_info.objects.get(id=floors.id)
     floor_num=floors.floor_num
     return floors.id
@login_required
def floorsHome(request):
     floor=floor_info.objects.all()
     return render(request,"floors.html",{"floor":floor}) 
@login_required
def showFloorInfo(request,id):
     floor=floor_info.objects.filter(id=id)
     return render(request,"showfloorInfo.html",{"floors":floor})
@login_required
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
     bedsinfo=beds_info.objects.create(
          user=request.user,
          bed_number=bed_number,
          room_no=room_no,
          bed_type=bed_type,
          floor_number=floor_number,
          bed_status=bed_status,
          assigned_date=assigned_date,
          discharge_date=discharge_date
           )
@login_required
def bedhome(request):
     beds=beds_info.objects.all()
     return render(request,"bedshome.html",{"beds":beds})
# def allbeds(request):
#      beds=beds_info.objects.all()
#      return render(request,"bedsHome.html",{"beds":beds})
@login_required
def showbedsInfo(request,id):
     beds=beds_info.objects.filter(id=id)
     return render(request,"showBeds.html",{"beds":beds})
@login_required
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
               # email=os.environ.get("EMAIL")
               # sender=email
               # email_password=os.environ.get("APP_PASSWORDS")
               # reciever=email
               # message=f"Some one booked an appointment : Patient name : {patient}  appointed_date : {appointment_date} appointment-time : {appointment_time}"
               # server=smtplib.SMTP("smtp.gmail.com",587)
               # server.starttls()
               # server.login(sender,email_password)
               # server.sendmail(sender,reciever,message)
               # server.quit()
               # print("email sent!!")
               app_id=saveappointnfo(request,patient,appointment_date,doctor,appointment_time,reason_for_visit,booked_date)
               return redirect("showappointinfo")
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
     return appointmentInfo.id
@login_required
def showappointinfo(request):
     # id=request.session.get("app_id")
     appoInfo=appointments.objects.filter(patient=request.user.username)
     return render(request,"showAppointInfo.html",{"app_info":appoInfo})
@login_required
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
               med_id=saveMedInfo(request,medicine_name,generic_name,category,dosage_form,strength,manufacturer,quantity_in_stock,unit_price,expiry_date,prescription_required,status)
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
     return medicines.id
@login_required
def medsHome(request):
     med=medicine.objects.all()
     return render(request,"medicines.html",{"med":med})
# def allMeds(request):
#      med=medicine.objects.all()
#      return render(request,"medicines.html",{"med":med})
@login_required
def showMeds(request,id):
     med=medicine.objects.filter(id=id)
     return render(request,"medsinfo.html",{"med":med})
@login_required
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
     return render(request,"roomsForm.html",{"room":room})
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
@login_required
def roomshome(request):
     rooms=room_info.objects.all()
     return render(request,"rooms.html",{"rooms":rooms})
# def allrooms(request):
#      rooms=room_info.objects.all()
#      return render(request,"rooms.html",{"rooms":rooms})
@login_required
def showroomInfo(request,id):
          room_infos=room_info.objects.filter(id=id)
          return render(request,"showroomsinfo.html",{"rooms":room_infos,"id":id})
@login_required
def patient(request):
     return render(request,"patienthomepage.html")
@login_required
def showappointmentforadmin(request):
     appointment=appointments.objects.all()
     return render(request,"apoointinfoforadmin.html",{"appointments":appointment})
@login_required
def showdocsinfo(request):
     doctors=doctor_perinfo.objects.all()
     return render(request,"doctorsinfoforpatients.html",{"docs":doctors})
@login_required
def patientinfotpadmin(request):   
     perinfo=patient_info.objects.all()
     contactinfo=patient_contact_info.objects.all()
     emerconinfo=patient_emergency_con.objects.all()
     medicalinfo=patient_Medical_info.objects.all()
     return render(request,"showpatientinfo.html",{"perinfo":perinfo,"contactinfo":contactinfo,"emerconinfo":emerconinfo,"medicalinfo":medicalinfo})
@login_required
def showhospital(request):
     return render(request,"HospitalHistory.html")
@login_required
def deletePatient(request):
     patientdata=deletePatientData()
     if request.method=="POST":
          patientdata=deletePatientData(request.POST)
          if patientdata.is_valid():
               patientId=patientdata.cleaned_data["patientId"]
               patient=patient_info.objects.filter(id=patientId).first()
               if patient:
                    patId=patientId
                    patient.delete()
                    return redirect("patientinfotpadmin")
               else:
                    print("already deleted")
     return render(request,"showpatientinfo.html",{"patientdata":patientdata})
@login_required
def deletePatientContactInfo(request):
     coninfo=deletepatientContData()
     if request.method=="POST":
          coninfo=deletepatientContData(request.POST)
          if coninfo.is_valid():
               patientcontactId=coninfo.cleaned_data["patientcontactId"]
               patient=patient_contact_info.objects.filter(id=patientcontactId).first()
               if patient:
                    patientId=patientcontactId
                    patient.delete()
                    return redirect("patientinfotpadmin")
               else:
                    print("object dosent exists")
     return render(request,"showpatientinfo.html",{"coninfo":coninfo})
@login_required
def deleteEmPatient(request):
     emInfo=deleteEmerInfoPat()
     if request.method=="POST":
          emInfo=deleteEmerInfoPat(request.POST)
          if emInfo.is_valid():
               patientemercontactId=emInfo.cleaned_data["patientemercontactId"]
               patient=patient_emergency_con.objects.filter(id=patientemercontactId).first()
               if patient:
                    patientId=patientemercontactId
                    patient.delete()
                    return redirect("patientinfotpadmin")
               else:
                    print("object dosent exists")
     return render(request,'showpatientinfo.html')
@login_required
def deletePatientMedInfos(request):
     medInfo=deletePatientMedInfo()
     if request.method=="POST":
          medInfo=deletePatientMedInfo(request.POST)
          if medInfo.is_valid():
               patientMedInfo=medInfo.cleaned_data["patientMedInfo"]
               patient=patient_Medical_info.objects.filter(id=patientMedInfo).first()
               if patient:
                    patientInfo=patientMedInfo
                    patient.delete()
                    return redirect("patientinfotpadmin")
               else:
                    print("object dosent exists")
     return render(request,"showpatientinfo.html")
@login_required
def deleteNursesData(request):
     Nursedata=DeleteNurseData()
     if request.method=="POST":
          Nursedata=DeleteNurseData(request.POST)
          if Nursedata.is_valid():
               NurseId=Nursedata.cleaned_data["NurseId"]
               nurse=Nurse_Personal_info.objects.filter(id=NurseId).first()
               if nurse:
                    nurse.delete()
                    return redirect("NurseHome")
               else:
                    print("object dosent exists")
     return render(request,"showNurseData.html")
@login_required
def deleteBurseCOntactInfo(request):
     ConInfo=deleteNurseConInfo()
     if request.method=="POST":
          ConInfo=deleteNurseConInfo(request.POST)
          if ConInfo.is_valid():
               NurseCOnId=ConInfo.cleaned_data["NurseCOnId"]
               nurse=nurse_contact_info.objects.filter(id=NurseCOnId).first()
               if nurse:
                    nurseId=NurseCOnId
                    nurse.delete()
                    return redirect("NurseHome")
               else:
                    print("object dosent exists")
     return render(request,"showNurseData.html")
@login_required
def deleteNurseEmpInfo(request):
     NurseCon=DeleteNuseEmpInfos()
     if request.method=="POST":
          NurseCon=DeleteNuseEmpInfos(request.POST)
          if NurseCon.is_valid():
               NurseEmId=NurseCon.cleaned_data["NurseEmId"]
               nurse=nurse_employee_info.objects.filter(id=NurseEmId).first()
               if nurse:
                    NurseId=NurseEmId
                    nurse.delete()
                    return redirect("NurseHome")
               else:
                    print("object dosent exists")
     return render(request,"showNurseData.html")
@login_required
def deleteNursesWorkInfo(request):
     WorkInfo=DeleteNurseWorksInfo()
     if request.method=="POST":
          WorkInfo=DeleteNurseWorksInfo(request.POST)
          if WorkInfo.is_valid():
               NurseWorkId=WorkInfo.cleaned_data["NurseWorkId"]
               nurse=nurse_work_info.objects.filter(id=NurseWorkId).first()
               if nurse:
                    NurseId=NurseWorkId
                    nurse.delete()
                    return redirect("NurseHome")
               else:
                    print("object dosent exists")
     return render(request,"ShowNurseData.html")
@login_required
def deleteBedsInfo(request):
     beds=deleteBeds()
     if request.method=="POST":
          beds=deleteBeds(request.POST)
          if beds.is_valid():
               bedsId=beds.cleaned_data["bedsId"]
               beds=beds_info.objects.filter(id=bedsId).first()
               if beds:
                    bedId=bedsId
                    beds.delete()
                    return redirect("bedhome")
               else:
                    print("objects dosent exists")
     return render(request,"showBeds.html")
@login_required
def deleteAppointmentsInfo(request):
     app=deleteApp()
     if request.method=="POST":
          app=deleteApp(request.POST)
          if app.is_valid():
               appId=app.cleaned_data["appId"]
               appointment=appointments.objects.filter(id=appId).first()
               if appointment:
                    appointment.delete()
                    return redirect("showappointmentforadmin")
               else:
                    print("object dosent exists")
     return render(request,"apoointinfoforadmin.html")
@login_required
def deleteRoomsInfos(request):
     room=deleteRooms()
     if request.method=="POST":
          room=deleteRooms(request.POST)
          if room.is_valid():
               roomId=room.cleaned_data["roomId"]
               rooms=room_info.objects.filter(id=roomId).first()
               if rooms:
                    roomsId=roomId
                    rooms.delete()
                    return redirect("roomshome")
               else:
                    print("object does not exist")
     return render(request,"showroomsinfo.html")
@login_required
def delFloorsInfo(request):
     floorInfo=deleteFloorsInfo()
     if request.method=="POST":
          floorInfo=deleteFloorsInfo(request.POST)
          if floorInfo.is_valid():
               floorId=floorInfo.cleaned_data["floorId"]
               floor=floor_info.objects.filter(id=floorId).first()
               if floor:
                    floor.delete()
                    return redirect("floorsHome")
               else:
                    print("object dosent exists")
     return render(request,"showfloorInfo.html")
@login_required
def delRecepInfo(request):
     receps=delRecepInformation()
     if request.method=="POST":
          receps=delRecepInformation(request.POST)
          if receps.is_valid():
               recepId=receps.cleaned_data["recepId"]
               recep=recep_person_info.objects.filter(id=recepId).first()
               if recep:
                    recepIds=recepId
                    recep.delete()
                    return redirect("recephome")
               else:
                    print("object dosent exists")
     return render(request,"showRecepPerData.html")
@login_required
def delRecepConInfo(request):
     conInfo=deleterecepEmpInfo()
     if request.method=="POST":
          conInfo=deleterecepEmpInfo(request.POST)
          if conInfo.is_valid():
               continfoId=conInfo.cleaned_data["continfoId"]
               Con=recep_contact_info.objects.filter(id=continfoId).first()
               if Con:
                    contId=continfoId
                    Con.delete()
                    return redirect("recephome")
               else:
                    print("object does not exists")
     return render(request,"showRecepPerData.html")
@login_required
def deleteRecepEmpInfo(request):
     emps=delRecepEmpInfo()
     if request.method=="POST":
          emps=delRecepEmpInfo(request.POST)
          if emps.is_valid():
               empId=emps.cleaned_data["empId"]
               recep=recep_employ_info.objects.filter(id=empId).first()
               if recep:
                    empIds=empId
                    recep.delete()
                    return redirect("recephome")
               else:
                    print("object does not exists")
     return render(request,"showRecepPerData.html")
@login_required
def delAmb(request):
     ambInfo=deleteAmbulance()
     if request.method=="POST":
          ambInfo=deleteAmbulance(request.POST)
          if ambInfo.is_valid():
               ambId=ambInfo.cleaned_data['ambId']
               amb=ambulance_info.objects.filter(id=ambId).first()
               if amb:
                    amb.delete()
                    return redirect("ambHome")
               else:
                    print("object dosent exist")
     return render(request,"showAmdulanceinfo.html")
@login_required
def delDep(request):
     deps=deleteDep()
     if request.method=="POST":
          deps=deleteDep(request.POST)
          if deps.is_valid():
               depId=deps.cleaned_data["depId"]
               dep=Department.objects.filter(id=depId).first()
               if dep:
                    department_name=dep.department_name
                    dep.delete()
                    return redirect("hospitalHistory")
               else:
                    print("object dosent exists")
     return render(request,"showDepInfo.html")
@login_required
def delDoctor(request):
     docs=DeleteDoc()
     if request.method=="POST":
          docs=DeleteDoc(request.POST)
          if docs.is_valid():
               docId=docs.cleaned_data["docId"]
               doc=doctor_perinfo.objects.filter(id=docId).first()
               if doc:
                    docsId=docId
                    doc.delete()
                    return redirect("hospitalHistory")
               else:
                    print("object dosent exist")
     return render(request,"ShowDoctorsData.html")
@login_required
def deletemeds(request):
     meds=deleteMeds()
     if request.method=="POST":
          meds=deleteMeds(request.POST)
          if meds.is_valid():
               medId=meds.cleaned_data["medId"]
               med=medicine.objects.filter(id=medId).first()
               if med:
                    med.delete()
                    return redirect("medsHome")
               else:
                    print("object dosent exist")
     return render(request,"medsinfo.html")
