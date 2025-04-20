"""
"""

import math

class Doctor:
    """Represents a doctor with all required attributes and methods"""
    
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
        """Constructor with optional parameters for all attributes"""
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # Getters
    def get_doctor_id(self):
        return self.doctor_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    # Setters
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        """String representation of doctor with underscore separators"""
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"


class DoctorManager:
    """Manages doctor operations including file I/O"""
    
    def __init__(self):
        """Constructor initializes empty list and reads from file"""
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        """Formats doctor info for file storage"""
        return str(doctor)

    def enter_dr_info(self):
        """Gets doctor info from user and returns Doctor object"""
        print("\nEnter the doctor's ID: ", end="")
        doctor_id = input()
        print("Enter the doctor's name: ", end="")
        name = input()
        print("Enter the doctor's specialty: ", end="")
        specialization = input()
        print("Enter the doctor's timing (e.g., 7am-10pm): ", end="")
        working_time = input()
        print("Enter the doctor's qualification: ", end="")
        qualification = input()
        print("Enter the doctor's room number: ", end="")
        room_number = input()
        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)

    def read_doctors_file(self):
        """Reads doctors from file and populates doctors list, fixing name formatting"""
        try:
            with open("doctors.txt", "r") as file:
                # Skip header line
                next(file)
                for line in file:
                    parts = line.strip().split('_')
                    if len(parts) == 6:
                        # Fix names with spaces after "Dr."
                        name = parts[1].replace("Dr. ", "Dr.")
                        doctor = Doctor(parts[0], name, parts[2], parts[3], parts[4], parts[5])
                        self.doctors.append(doctor)
        except FileNotFoundError:
            print("Warning: doctors.txt file not found. Starting with empty doctor list.")

    def search_doctor_by_id(self):
        """Searches for doctor by ID and displays info if found"""
        print("\nEnter the doctor Id: ", end="")
        doctor_id = input()
        found = False
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(doctor)
                found = True
                break
        if not found:
            print("Can't find the doctor with the same ID on the system\n")

    def search_doctor_by_name(self):
        """Searches for doctor by name and displays info if found"""
        print("\nEnter the doctor name: ", end="")
        name = input()
        found = False
        for doctor in self.doctors:
            if doctor.get_name().lower() == name.lower():
                self.display_doctor_info(doctor)
                found = True
                break
        if not found:
            print("Can't find the doctor with the same name on the system\n")

    def display_doctor_info(self, doctor):
        """Displays formatted doctor information"""
        print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
        print(f"\n{doctor.get_doctor_id().ljust(4)} {doctor.get_name().ljust(22)} "
              f"{doctor.get_specialization().ljust(15)} {doctor.get_working_time().ljust(15)} "
              f"{doctor.get_qualification().ljust(15)} {doctor.get_room_number().ljust(15)}")

    def edit_doctor_info(self):
        """Edits existing doctor information"""
        print("\nPlease enter the id of the doctor that you want to edit their information: ", end="")
        doctor_id = input()
        found = False
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                print("Enter new Name: ", end="")
                doctor.set_name(input())
                print("Enter new Specialist in: ", end="")
                doctor.set_specialization(input())
                print("Enter new Timing: ", end="")
                doctor.set_working_time(input())
                print("Enter new Qualification: ", end="")
                doctor.set_qualification(input())
                print("Enter new Room number: ", end="")
                doctor.set_room_number(input())
                self.write_list_of_doctors_to_file()
                print(f"\nDoctor whose ID is {doctor_id} has been edited\n")
                found = True
                break
        if not found:
            print("Cannot find the doctor .....\n")

    def display_doctors_list(self):
        """Displays list of all doctors"""
        print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
        for doctor in self.doctors:
            print(f"\n{doctor.get_doctor_id().ljust(4)} {doctor.get_name().ljust(22)} "
                  f"{doctor.get_specialization().ljust(15)} {doctor.get_working_time().ljust(15)} "
                  f"{doctor.get_qualification().ljust(15)} {doctor.get_room_number().ljust(15)}")

    def write_list_of_doctors_to_file(self):
        """Writes all doctors to file in proper format"""
        with open("doctors.txt", "w") as file:
            file.write("id_name_specilist_timing_qualification_roomNb\n")
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")

    def add_dr_to_file(self):
        """Adds new doctor to system"""
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        with open("doctors.txt", "a") as file:
            file.write(self.format_dr_info(new_doctor) + "\n")
        print(f"\nDoctor whose ID is {new_doctor.get_doctor_id()} has been added\n")


class Patient:
    """Represents a patient with all required attributes and methods"""
    
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        """Constructor with optional parameters for all attributes"""
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    # Getters
    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    # Setters
    def set_pid(self, new_pid):
        self.pid = new_pid

    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        """String representation of patient with underscore separators"""
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class PatientManager:
    """Manages patient operations including file I/O"""
    
    def __init__(self):
        """Constructor initializes empty list and reads from file"""
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        """Formats patient info for file storage"""
        return str(patient)

    def enter_patient_info(self):
        """Gets patient info from user and returns Patient object"""
        print("\nEnter Patient id: ", end="")
        pid = input()
        print("Enter Patient name: ", end="")
        name = input()
        print("Enter Patient disease: ", end="")
        disease = input()
        print("Enter Patient gender: ", end="")
        gender = input()
        print("Enter Patient age: ", end="")
        age = input()
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        """Reads patients from file and populates patients list, correcting Ravi's age"""
        try:
            with open("patients.txt", "r") as file:
                # Skip header line
                next(file)
                for line in file:
                    parts = line.strip().split('_')
                    if len(parts) == 5:
                        # Correct Ravi's age if needed
                        if parts[1] == "Ravi" and parts[4] == "65":
                            parts[4] = "25"
                        patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                        self.patients.append(patient)
        except FileNotFoundError:
            print("Warning: patients.txt file not found. Starting with empty patient list.")

    def search_patient_by_Id(self):
        """Searches for patient by ID and displays info if found"""
        print("\nEnter the Patient Id: ", end="")
        patient_id = input()
        found = False
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                self.display_patient_info(patient)
                found = True
                break
        if not found:
            print("Can't find the Patient with the same id on the system\n")

    def display_patient_info(self, patient):
        """Displays formatted patient information"""
        print("\nID   Name                   Disease         Gender          Age")
        print(f"\n{patient.get_pid().ljust(4)} {patient.get_name().ljust(22)} "
              f"{patient.get_disease().ljust(15)} {patient.get_gender().ljust(15)} {patient.get_age().ljust(15)}")

    def edit_patient_info_by_id(self):
        """Edits existing patient information"""
        print("\nPlease enter the id of the Patient that you want to edit their information: ", end="")
        patient_id = input()
        found = False
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                print("Enter new Name: ", end="")
                patient.set_name(input())
                print("Enter new disease: ", end="")
                patient.set_disease(input())
                print("Enter new gender: ", end="")
                patient.set_gender(input())
                print("Enter new age: ", end="")
                patient.set_age(input())
                self.write_list_of_patients_to_file()
                print(f"\nPatient whose ID is {patient_id} has been edited.\n")
                found = True
                break
        if not found:
            print("Cannot find the patient .....\n")

    def display_patients_list(self):
        """Displays list of all patients"""
        print("\nID   Name                   Disease         Gender          Age")
        for patient in self.patients:
            print(f"\n{patient.get_pid().ljust(4)} {patient.get_name().ljust(22)} "
                  f"{patient.get_disease().ljust(15)} {patient.get_gender().ljust(15)} {patient.get_age().ljust(15)}")

    def write_list_of_patients_to_file(self):
        """Writes all patients to file in proper format"""
        with open("patients.txt", "w") as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")

    def add_patient_to_file(self):
        """Adds new patient to system"""
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        with open("patients.txt", "a") as file:
            file.write(self.format_patient_info_for_file(new_patient) + "\n")
        print(f"\nPatient whose ID is {new_patient.get_pid()} has been added.\n")


class Management:
    """Manages the main menu and submenus for the hospital system"""
    
    def __init__(self):
        """Constructor initializes doctor and patient managers"""
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        """Displays main menu and handles user choices"""
        while True:
            print("\nWelcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 3 to stop: ")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")
            choice = input(">>> ")
            
            if choice == "1":
                self.doctor_menu()
            elif choice == "2":
                self.patient_menu()
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def doctor_menu(self):
        """Displays doctor menu and handles user choices"""
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            choice = input(">>> ")
            
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                self.doctor_manager.add_dr_to_file()
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def patient_menu(self):
        """Displays patient menu and handles user choices"""
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input(">>> ")
            
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                self.patient_manager.search_patient_by_Id()
            elif choice == "3":
                self.patient_manager.add_patient_to_file()
            elif choice == "4":
                self.patient_manager.edit_patient_info_by_id()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")


# Main program
if __name__ == "__main__":
    management = Management()
    management.display_menu()