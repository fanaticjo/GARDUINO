"""This file is part of GARDUINO.GARDUINO is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 of the License,or(at your option) any later version . 
GARDUINO is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details.You should have received a copy of the GNU General Public License along with GARDUINO.
If not, see <http://www.gnu.org/licenses/>. """


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
