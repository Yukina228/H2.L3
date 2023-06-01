import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>JFHHOSHSU938204702VNLCUGOLMLV94850l03740=2lfvbp"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
     return password
    
def coin():
    flip = random.randint(1,2)

    if flip == 1:
        return 'Орёл!'
    else:  
        return 'Решка!'

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)
