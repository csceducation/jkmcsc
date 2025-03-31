""" import os
import django
import random
from faker import Faker
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csc_app.settings')
django.setup()

from apps.enquiry.models import Enquiry
from apps.staffs.models import Staff
from apps.corecode.models import Time
from apps.course.models import CourseModel
fake = Faker()
def bulk_upload_students(csv_file_path):
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    student = Student(
                        username=row['username'],
                        password=row['password'],
                        student_name=row['student_name'],
                        enrol_no=row['enrol_no'],
                        rel_name=row['rel_name'],
                        rel_occupation=row['rel_occupation'],
                        m_name=row['m_name'],
                        date_of_birth=row['date_of_birth'],
                        age=row['age'],
                        gender=row['gender'],
                        religion=row['religion'],
                        community=row['community'],
                        occupation=row['occupation'],
                        student_company_name=row['student_company_name'],
                        aadhar_no=row['aadhar_no'],
                        mobile_number=row['mobile_number'],
                        alt_number=row['alt_number'],
                        email=row['email'],
                        passport=row['passport'],
                        address=row['address'],
                        address1=row['address1'],
                        address2=row['address2'],
                        taluka=row['taluka'],
                        district=row['district'],
                        pincode=row['pincode'],
                        date_of_admission=row['date_of_admission'],
                        course_id=row['course_id'],
                        total_fee=row['total_fee'],
                        remark=row['remark'],
                    )
                    student.save()
                except ValidationError as e:
                    print(f"Error saving student {row['student_name']}: {e}")

    # Example CSV headings:
    # username,password,student_name,enrol_no,rel_name,rel_occupation,m_name,date_of_birth,age,gender,religion,community,occupation,student_company_name,aadhar_no,mobile_number,alt_number,email,passport,address,address1,address2,taluka,district,pincode,date_of_admission,course_id,total_fee,remark


def create_fake_enquiry():
    # Assuming you have some Staff and CourseModel objects already created
    staff = Staff.objects.filter().first()
    course = CourseModel.objects.filter().first()

    enquiry = Enquiry.objects.create(
        enquiry_no=fake.unique.bothify(text='ENQ####'),
        name=fake.name(),
        f_name=fake.name_male() if fake.boolean() else fake.name_female(),
        address=fake.address(),
        address1=fake.secondary_address(),
        address2=fake.secondary_address(),
        taluka=fake.city(),
        district=fake.state(),
        pincode=fake.postcode(),
        mobile_number=fake.phone_number(),
        alternate_mobile_number=fake.phone_number(),
        email=fake.email(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=80),
        gender=random.choice([choice[0] for choice in Enquiry.GENDER_CHOICES]),
        student_role=random.choice([choice[0] for choice in Enquiry.STUDENT_ROLE_CHOICES]),
        student_company_name=fake.company() if random.choice([True, False]) else None,
        enquiry_date=fake.date_this_year(),
        counsellor=staff,
        counsellor_remark=fake.text(),
        enquiry_status="Following",
        expected_date=fake.date_this_year(),
        qualification=fake.text(max_nb_chars=50),
        qualification_status=random.choice([choice[0] for choice in Enquiry.QUALIFICATION_STATUS_CHOICES]),
        studying_year=fake.random_int(min=1, max=5),
        studying_course=fake.job(),
        student_college_name=fake.company(),
        need_of_study=random.choice([choice[0] for choice in Enquiry.NEED_CHOICES]),
        known_csc=random.choice([choice[0] for choice in Enquiry.KNOWN_CSC_CHOICES]),
        course_to_join=course,
        new_course=fake.word()
    )

    # Add many-to-many field values
    #times = Time.objects.get(id=1)
    #enquiry.time_to_study.set(times)

    enquiry.save()

# Create multiple fake enquiries
for _ in range(10):
    create_fake_enquiry()
 """

import csv
from faker import Faker

fake = Faker()

# Define the CSV file path
csv_file_path = 'sample.csv'

# Define the CSV headings
csv_headings = [
    "username", "password", "student_name", "enrol_no", "rel_name", "rel_occupation", "m_name", "date_of_birth", "age",
    "gender", "religion", "community", "occupation", "student_company_name", "aadhar_no", "mobile_number", "alt_number",
    "email", "passport", "address", "address1", "address2", "taluka", "district", "pincode", "date_of_admission",
    "course_id", "total_fee", "remark"
]
from faker import Faker
fake = Faker()
# Generate 5 rows of data
rows = []
for _ in range(5):
    row = [
        fake.user_name(), fake.password(), fake.name(), fake.random_int(min=1000, max=9999), fake.name(),
        fake.job(), fake.name(), fake.date_of_birth(minimum_age=18, maximum_age=25), fake.random_int(min=18, max=25),
        fake.random_element(elements=("male", "female")), fake.random_element(elements=("Hindu", "Christian", "Muslim")),
        fake.random_element(elements=("OC", "BC", "MBC", "SC", "ST")), fake.job(), fake.company(), fake.random_int(min=100000000000, max=999999999999),
        fake.phone_number(), fake.phone_number(), fake.email(), fake.file_name(extension="jpg"), fake.address(),
        fake.secondary_address(), fake.secondary_address(), fake.city(), fake.state(), fake.postcode(),
        fake.date_this_decade(), fake.random_int(min=1, max=10), fake.random_int(min=10000, max=50000), fake.sentence()
    ]
    rows.append(row)

# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headings)
    writer.writerows(rows)

print(f"Data saved to {csv_file_path}")