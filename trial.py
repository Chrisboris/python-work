def power(number, power_to_raise):
        # 2^3= 2*2*2
        if power_to_raise == 0:
                print(1)
        else:
                return(number * power(number, power_to_raise))
          
results = power(3 ,3)
print(results)   