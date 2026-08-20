class Hospital:
    hospital_name="City Hospital"
    @classmethod
    def change_hospital(cls,new_name):
        cls.hospital_name=new_name
        return f"The hospital name changed to:{new_name}"

h1=Hospital()
print(h1.change_hospital("Apollo"))