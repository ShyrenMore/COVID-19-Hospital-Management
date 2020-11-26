# *Covid hospital management*

### Problem Statement: 
- Create a COVID-19 patients management and tracking web application for a Hospital
- The user/admin will enter name, address, current COVID-19 symptoms, contact details, Health details and will assign a bed to the respective patient 
- Only the management can insert and modify patient data
- Create a dashboard for hospital management where they could see status of recovered, admitted, deceased patients and bed availability 

### Tech Stack
- Frontend
	- HTML5
	- CSS3
	- JQuery
    - Bootstrap4
- Backend
    - Django framework
- Database
    - SQLite

### Local Setup
- Clone repository.
- Setup virtual environment
- Exceute `pip install -r requirements.txt`.
- run `python manage.py runserver`.
- Go to `127.0.0.1::8000` in your web browser.

## Screenshots & description

## *login page*
![](https://github.com/ShyrenMore/CodersLegion/blob/master/screenshots/login_form.PNG)
<p>The login is only for staff members and admin who will enter staff details in database</p>

## *View Patient list*
![](https://github.com/ShyrenMore/CodersLegion/blob/master/screenshots/patient_list.PNG)
<p>The name, bed no, status, and update option are rendered, there is also a typeahead feature and dropdown for bed numbers and doctors in the search panel</p>

## *Add Patient page*
![](https://github.com/ShyrenMore/CodersLegion/blob/master/screenshots/add_patient_1.PNG)
<p>Here you can add patient for storing it to the db. Patient's relative contact details were also taken to check if the relative has contacted COVID virus</p>

![](https://github.com/ShyrenMore/CodersLegion/blob/master/screenshots/add_patient_2.PNG)
<p>Since there are relatively more COVID patients than any other viruses/diseases, a checklist for COVID symptoms only is present</p>


<!-- ### Clean aesthetic User Interface, which changes dynamically as per the status of patient changes... -->

<!-- login page -->
<!-- dashboard(with and without sidenav) -->
<!-- add patient form -->
<!-- update patient form -->
<!-- view patient table -->

