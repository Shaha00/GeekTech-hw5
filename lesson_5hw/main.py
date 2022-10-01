import random
import time
from termcolor import cprint


 
bal = 1000
nums = ['0', '1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16', '17','18','19','20','21','22','23','24','25','26','27','28','28','29','30']
print('Ваш баланс ' , bal , '$')

print("Выбираем слоту...")
time.sleep(4)

choice = random.choices(nums)
if choice == ['2']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 2X$')
    print('Ваш баланс ' , bal * 2, '$')
    
elif choice == ['4']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 4X$')
    print('Ваш баланс ' , bal * 4, '$')
    
elif choice == ['6']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 4X$')
    print('Ваш баланс ' , bal * 4 , '$')
    
elif choice == ['8']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 8X$')
    print('Ваш баланс ', bal * 8, '$')
    
elif choice == ['10']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 10X $')
    print('Ваш баланс ', bal * 10, '$')
    
elif choice == ['12']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 12X $')
    print('Ваш баланс ', bal * 12, '$')
    
elif choice == ['14']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 14X $')
    print('Ваш баланс ', bal * 14, '$')
    
elif choice == ['16']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 16X $')
    print('Ваш баланс ', bal * 16, '$') 
    
elif choice == ['18']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 18X $')
    print('Ваш баланс ', bal * 18, '$')
    
    
elif choice == ['20']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 20X $')
    print('Ваш баланс ', bal * 20, '$')  
    
elif choice == ['22']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 22X $')
    print('Ваш баланс ', bal * 22, '$')
    
elif choice == ['24']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 24X $')
    print('Ваш баланс ', bal * 24, '$')

elif choice == ['26']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 26X $')
    print('Ваш баланс ', bal * 26, '$')
    
elif choice == ['28']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 28X $')
    print('Ваш баланс ', bal * 28, '$')

elif choice == ['30']:
    cprint(*choice, color="red", attrs=['bold'])
    print('ваш выйграш 30x $')
    print('Ваш баланс ', bal * 30, '$')
    
elif choice == ['0']:
    print(choice)
    print('+0$')
    print('Ваш баланс ', bal, '$')
else:
    cprint(*choice, color="grey", attrs=["bold"])
    print('выйгыша нет')
    cprint('Ваш баланс ', bal, '$')



    