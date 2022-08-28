# demo-charts
Simple REST API to impliment the Complaint Management,
and Also created APIs two pass the data for charts.


# Register / Login
I have created Register / Login APIs for registering new user and login the user.

# JWT-Token
I have used Jwt token for Authentication.

# Model:
I have created model into complaint.models file to storing the complaints of user.

# APIs
1. user can add new Complaint.                      (POST : http://127.0.0.1:8000/complaint/complaint/)
2. User can check his complaints in detail.         (GET : http://127.0.0.1:8000/complaint/complaint/)
3. Admin(Worker) can review the Complaint ("PROGRESS" / "COMPLETED")
                                                    (PUT : http://127.0.0.1:8000/complaint/admin-review-complaint/)
4. Admin can see all the Complaints.                (GET : http://127.0.0.1:8000/complaint/admin-review-complaint/)

# Data for Chart APIs   (AllowAny):
1. to get User-complaints with percentage of COMPLETED complaints 
        (GET : http://127.0.0.1:8000/complaint/chart/user-complaint-count/)
2. to get Total Complaints with COMPLETED percentage. 
        (GET : http://127.0.0.1:8000/complaint/chart/all-complaint/)


# Published Postman Documentation
https://documenter.getpostman.com/view/19442321/VUxKTUhB
# Extreted Postman Collection with Examples:
-> I have added the Exported file at : "postman_documentation/glib_test_api_doc_.json"

# Admin User
Admin user : Amit / password123#

# hit admin to check the database
http://127.0.0.1:8000/admin

# Super user
admin / admin




# steps to follow
open terminal

# create Virtual environment:
python3 -m venv venv

# activate venv
source venv/bin/activate

# clone the project
git clone https://github.com/paras1244/demo_glib.git

cd demo_glib

# installing dependeicies
pip install -r requirements.txt

# run the project
python3 manage.py runserver
