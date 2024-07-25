class Father:
    def father_speak():
        return "Father class"
class Mother:
     def mother_speak():
        return "Mother class"
class Kid(Father,Mother):
    def Kid_speak():
        return "I am Kid having properties of Mother and Father"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.Kid_speak())
