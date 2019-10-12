# Python program to extract emails From 
# the String By Regular Expression. 

# Importing module required for regular 
# expressions

import re 

# Example string 
#s = '235 Asansol Engineering College, Asansol EIE amarganguly@rediffmail.com 236 Asansol Engineering College, Asansol EIE mailto_intekhab@rediffmail.com 237 Asansol Engineering College, Asansol EIE papan.ec11@gmail.com 238 Asansol Engineering College, Asansol EIE avi.chiranjib@gmail.com 239 Asansol Engineering College, Asansol EIE rf.billaha@gmail.com 240 Asansol Engineering College, Asansol EIE a_billaha@yahoo.co.in 241 Asansol Engineering College, Asansol EIE bikas.mondal143@gmail.com 242 Asansol Engineering College, Asansol EIE lipikamandal81@gmail.com 243 Asansol Engineering College, Asansol EIE ashmi.chakraborty@gmail.com 244 Asansol Engineering College, Asansol EIE syed@syedafzal.in 245 Asansol Engineering College, Asansol CSE monish_chatterjee@yahoo.com246 Asansol Engineering College, Asansol CSE monishchatterjee@rediffmail.com 247 Asansol Engineering College, Asansol CSE shibsankar.bala@gmail.com 248 Asansol Engineering College, Asansol CSE sandip_9500@rediffmail.com 249 Asansol Engineering College, Asansol CSE dr.bady_g@rediffmail.com 250 Asansol Engineering College, Asansol CSE simantahazra2@rediffmail.com 251 Asansol Engineering College, Asansol CSE ujjwal.kamila@gmail.com 252 Asansol Engineering College, Asansol CSE uddaloksen81@gmail.com 253 Asansol Engineering College, Asansol CSE pranabes7@gmail.com 254 Asansol Engineering College, Asansol CSE shatabdi.mondal@gmail.com 255 Asansol Engineering College, Asansol CSE lumbinibhaumik@gmail.com 256 Asansol Engineering College, Asansol CSE chatterjee_vedatrayee@rediffmail.com 257 Asansol Engineering College, Asansol CSE syed@syedafzal.in258 Asansol Engineering College, Asansol EE rajan_maa@rediffmail.com 259 Asansol Engineering College, Asansol EE nirsha_apurba@rediffmail.com260 Asansol Engineering College, Asansol EE kaushikneogi@rediffmail.com 261 Asansol Engineering College, Asansol EE sucharita_biet@rediffmail.com262 Asansol Engineering College, Asansol EE rps_crj@yahoo.co.in 263 Asansol Engineering College, Asansol EE agamani_chakraborty@yahoo.co.in 264 Asansol Engineering College, Asansol EE dharmbirprasad@yahoo.com 265 Asansol Engineering College, Asansol ECE sambitsmondal@gmail.com 266 Asansol Engineering College, Asansol ECE asok_km650@rediffmail.com 267 Asansol Engineering College, Asansol ECE sumanta.karmakar@gmail.com 268 Asansol Engineering College, Asansol ECE amit_kr_rai@yahoo.co.in 269 Asansol Engineering College, Asansol ECE soumencccp1234@rediffmail.com 270 Asansol Engineering College, Asansol ECE khushi_banerjee@rediffmail.com 271 Asansol Engineering College, Asansol ECE jeetnics@rediffmail.com 272 Asansol Engineering College, Asansol ECE sgoswami76@gmail.com 273 Asansol Engineering College, Asansol ECE das_rupam@rediffmail.com 274 Asansol Engineering College, Asansol ECE dipdur83@yahoo.co.in 275 Asansol Engineering College, Asansol ECE shiv123charan@rediffmail.com 276 Asansol Engineering College, Asansol ECE mailarindambiswas@yahoo.co.in 277 Asansol Engineering College, Asansol ECE chanak.soumen@gmail.com 278 Asansol Engineering College, Asansol ECE niratyay.biswas@gmail.com 279 Asansol Engineering College, Asansol ECE saswata.cmeri@gmail.com 280 Asansol Engineering College, Asansol ECE kousikroy002@gmail.com 281 Asansol Engineering College, Asansol IT anup.mukhopadhyay@gmail.com 282 Asansol Engineering College, Asansol IT avishekbanerji@gmail.com 283 Asansol Engineering College, Asansol IT debabrata2007@gmail.com 284 Asansol Engineering College, Asansol IT biplabaectnp@gmail.com 285 Asansol Engineering College, Asansol IT victordas.2005@gmail.com286 Asansol Engineering College, Asansol IT sujoy19806@gmail.com 287 Asansol Engineering College, Asansol IT sudipkumarde@gmail.com 288 Asansol Engineering College, Asansol IT rakshit_rinku@rediffmail.com 289 Asansol Engineering College, Asansol IT sheuli.chakraborty@gmail.com 290 Asansol Engineering College, Asansol ME principal.aecwb@gmail.com 291 Asansol Engineering College, Asansol ME aecdeba.me@gmail.com 292 Asansol Engineering College, Asansol ME aecpassport@gmail.com 293 Asansol Engineering College, Asansol ME prabir941@gmail.com 294 Asansol Engineering College, Asansol ME hatisamir@gmail.com 295 Asansol Engineering College, Asansol ME ashes_m12@rediffmail.com 296 Asansol Engineering College, Asansol ME sramesh2031@gmail.com 297 Asansol Engineering College, Asansol ME das96deb@gmail.com 298 Asansol Engineering College, Asansol ME anishdebjgec@gmil.com'

# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times
f=open(r"C:\Users\Farhan\AppData\Local\Programs\Python\Python37-32\data.txt",'r')
contents=f.read()

c=0
for i in contents:
  if(i=='@'):
    c+=1
print(c)

lst = re.findall('\S+@\S+', contents)
n=25

c=0
for i in lst:
  for j in i:
    if(j=='@'):
      c+=1
  
print(c)


#print(contents)
#print(lst)
q=open(r"C:\Users\Farhan\AppData\Local\Programs\Python\Python37-32\emails.txt","w+")

count=0
for i in lst:
 
  count+=1
  if(count%n==n-1):
    lst.insert(count, "njrfarhandasilva10@gmail.com")
    count+=1
#print(lst[:25])

index=0
for i in lst:
 
  #print(i)
  q.write(i)
  q.write(",")
  if(index%n==n-1):
    q.write("                      ")
    q.write("                      ")
  
  index+=1
#last case
if(len(lst)%n!=25):
  q.write("njrfarhandasilva10@gmail.com")
  q.write(",")
  
  
f.close()
q.close()
