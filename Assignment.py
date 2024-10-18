class College:
    def __init__(self, name, location, year):
        self.name = name
        self.location = location
        self.year = year
    def display_info(self):
        print(f"College Name: {self.name}")
        print(f"Location: {self.location}")
        print(f" Year: {self.year}")
    def college_age(self):
        current_year = 2024 
        age = current_year - self.year
        print(f"{self.name} is {age} years old.")
my_college = College("Islamia University", "Bhawalpur ", 2020)
my_college.display_info()
my_college.college_age()