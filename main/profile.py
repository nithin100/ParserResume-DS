class Profile:

    skillset = []

    def __init__(self,name,mobile,email):
        self.name = name
        self.mobile = mobile
        self.email = email

    def add_skill(self,skill):
        self.skillset.append(skill)
