from urllib.request import Request, urlopen   #rest api 
from itertools import cycle   #infinite cycle
import re
gen = cycle([0])
file=open("test.txt","a+");
file.write("temp");
file.write("\t");
file.write("humid");
file.write("\t");
file.write("soil");
file.write("\n");
file.close();
for elt in gen:
           request=Request('http://blynk-cloud.com/d86fc7a6a5794a468965170dfad1ace9/get/v5'); #temp
           response_bodyt=str(urlopen(request).read());
           response_bodyt=re.sub(r'\D',"",response_bodyt)
           request1=Request('http://blynk-cloud.com/d86fc7a6a5794a468965170dfad1ace9/get/v6'); #humidity
           response_bodyh=str(urlopen(request1).read());
           response_bodyh=re.sub(r'\D',"",response_bodyh)
           request2=Request('http://blynk-cloud.com/d86fc7a6a5794a468965170dfad1ace9/get/v7'); #soil
           response_bodys=str(urlopen(request2).read());
           response_bodys=re.sub(r'\D',"",response_bodys)
           file=open("test.txt","a+");
           file.write(response_bodyt);
           file.write("\t");
           file.write(response_bodyh);
           file.write("\t");
           file.write(response_bodys);
           file.write("\n");
           file.close()
