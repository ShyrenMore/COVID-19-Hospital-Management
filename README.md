# _Covid19 hospital management_

### Problem Statement (PS) :

- Create a COVID-19 patients management and tracking web application for a Hospital
- The user/admin will enter name, address, current COVID-19 symptoms, contact details, Health details and will assign a bed to the respective patient
- Only the management can insert and modify patient data
- Create a dashboard for hospital management where they could see status of recovered, admitted, deceased patients and bed availability

### Deployment

<p>As mentioned in PS it was specifically mentioned that only staff can insert and modify patient data so we only have a login page,</p> 
<p>You can try either of the below combinations for log in </p>

- dheeraj.lalwani – hello_1_world
- jay.bhavsar – hello_3_world
- Shyren.More – hello_2_world

The webapp is deployed [here](https://hospital-management-covid19.herokuapp.com/)

### Screenshots and workflow


### Login page

![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/login.png)

<p>The login is only for staff members and admin who will enter staff details in database</p>

### Dashboard

![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/Dashboard_notPublic.png)

- Clean aesthetic User Interface, which changes dynamically as per the status of patient changes
- In bed availability grid the red color indicates that bed is occupied else available
- It is one of the two pages available for public to view

### Add Patient page
![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/add_patient1.PNG)
- Here you can add patient for storing it to the db. Patient's relative contact details are also taken to check if the relative has contacted COVID virus
- Bed numbers which are available are only shown
- Information filled here, will make changes in dashboard dynamically

![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/add_patient2.PNG)
- Since there are relatively more COVID patients than any other viruses/diseases, a checklist for COVID symptoms only is present

### Patient list
![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/patientlist.png)
- Here you can search patients wrt to name, bed no. doctor assigned and status
- You can also find update button to update the patient details. 

### Update form
![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/update.PNG)
- This is where the actual updates for individual patients are done

### About 
![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/About_1.PNG)
![](https://github.com/ShyrenMore/COVID-19-Hospital-Management/blob/master/Screenshots/About_2.PNG)
- This is the other page public can view, this is just to create an awareness.

<!-- about us & view patient -->
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
