import AAS.AAS as AAS
from time import perf_counter,sleep
from requests import get
from nest_asyncio import apply
import asyncio
apply()

def verify(d,json=True):
    f=0
    for i in d:
        if json:
            if len(list(i.keys()))==0:
                f+=1
        else:
            if len(list(i.json().keys()))==0:
                f+=1
    return f

async def main(): 
    nasa=AAS.AAS_URLInterface(600)
    r=['https://jsonplaceholder.typicode.com/todos/']*600
    r=[n+str(i+1) for i,n in enumerate(r)]
    x=perf_counter()
    f=await nasa.map([await nasa.request(url) for url in r])
    print("Time Taken to do Requests -",round((perf_counter()-x)*100)/100)
    x=perf_counter()
    u=[get(url) for url in r]
    print("Time Taken to do Requests -",round((perf_counter()-x)*100)/100)

    
    print("Verification His -",verify(u,False),"Faults")


asyncio.run(main())