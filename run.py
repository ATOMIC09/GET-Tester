import requests
from time import sleep

while True:
    url1 = str(input("Enter First Half URL : "))
    url2 = str(input("Enter First Past URL : "))
    num_range = int(input("Enter Range : "))

    for i in range(num_range):
        full_url = url + str(i)
        print(full_url)
    #x = requests.get(full_url)

    #print(f"\nResult : {x.status_code}\n")
    #print("============")