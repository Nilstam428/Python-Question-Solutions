# Q what is **kwargs ? explain with function's example ?
#here we taake n no. of keyword arguments for getting arguments for the function

def data(**details):
    for key, value in details.items():
        print(f"{key} : {value}")
        
data(name = "Nilesh", age=22, location = "Chittorgarh")

# It produces dictionary as a output        







# dictionary

# for key , values in dict.items():
#     print(f"{key} : {values}")
