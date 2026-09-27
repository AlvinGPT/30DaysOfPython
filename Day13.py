def exponentiate(base,power):
    return base**power
print(exponentiate(12,12))
def process_string(text):
    return text.strip().lower()
print(process_string("White     "))
data = ("Tom Hardy", "English", 42)  # name, nationality, age
def dict_process(data):
    return {"name" : data[0], "nationality" : data[1], "age" : data[2]}
def prime_chk(num):
    no = 2
    while no <= num:
        if no == num:
            return True
        elif (num % no) == 0 :
            return False
        else: 
            no += 1
print(prime_chk(24))
