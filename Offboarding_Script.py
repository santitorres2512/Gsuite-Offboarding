from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText                                             
import smtplib
import csv
import sys
import email                                                                   
import mailparser                                                              
import imaplib                                                                 
import requests
import json
import gspread
#import datetime
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta             

#from gspread.models import Cell
#import gspread
#from getpass import getpass
#import urllib.parse as urlparse
#from urllib.parse import parse_qs
#import time



'''
Credentials = []

with open('File.csv') as csvfile:                                              # Selects the data base "DB.csv"  
    datareader = csv.reader(csvfile)
    for line in datareader:                                                    # Searches among the rows contained in the "DB.csv"
        Credentials.append(line)
        
CTAcc = Credentials[0][0]
CTPass = Credentials[0][1]
MyAcc = Credentials[1][0]
GPass = Credentials[1][1]
WPass = Credentials[2][1]
 



###########################GMAIL SENDING A  PI FUNCTION########################## 

def send_email(subject, msg):
    try:                                                                  #It will access the server using Gmail credentials
        server = smtplib.SMTP('smtp.outlook.com', 587)                       #Process starts
        server.ehlo()
        server.starttls()
        server.login(CTAcc,'ycfwcwahyqkyryut')
        message = 'Subject: {}\n\n{}'.format(subject,msg)                 #function for upload and set up the subject and message 
        server.sendmail(CTAcc, 'storres@cloudtask.com', message)            # sends the message
                
        server.quit()
        print('\nEmail sent succefully!') 
        print('\nhello')                               #Process finished.
                
    except:
        print('Email failed.')
                
###############################################################################
'''
auth = ("16561801813-nfgauhqs54jc77ldtsr6cih1vo6atsae.apps.googleusercontent.com", "yQGiGC4xia7m4IluBQxY5sSX")

params = {
  "grant_type":"refresh_token",
  "refresh_token":"1//04-tuRRo0i5VrCgYIARAAGAQSNwF-L9IrheYuNOA8W5L7KpLL6l-gxsybhYUp0OITru34urIURh9oh6gnQCinV5D3MD9U__jqP28"
}

url = "https://oauth2.googleapis.com/token"

ret = requests.post(url, auth=auth, data=params)

print(ret)


AccessTokenJson = json.loads(ret.text)
AccessToken = str(AccessTokenJson["access_token"])


headers2 = {'Accept':'application/json'}

url2 = "https://7f7a4efac527336d106feba28c6aca597971c95f:x@api.bamboohr.com/api/gateway.php/cloudtaskhr/v1/reports/185?fd=no"

response = requests.get(url2,headers=headers2)
#print("Report--> ",response.text)
ReportJson = json.loads(response.text)


EmployeeList = ReportJson["employees"]


file = open('data_file.csv', 'w') 

csv_writer = csv.writer(file) 

count = False
  
for emp in EmployeeList: 
    if count == False: 
          
        header = ('ID','Employee #','First Name','Middle Name','Last Name','Status','Gender','Work Email','LindkedIn URL','Hire Date','Termination Date','Employment Status','Termination Type','Elegible For Re-hire','Job Information Date','Location','Division','Department','Job Title','Reporting to') 
        csv_writer.writerow(header) 
        count = True
       
    csv_writer.writerow(emp.values()) 
  
file.close() 
  
with open('data_file.csv') as data_file:
    with open('data_file_out.csv', 'w',newline='') as data_file_out:
        writer = csv.writer(data_file_out)
        i=0
        for row in csv.reader(data_file):
            if (i%2)!=0:
                i=i+1
                continue
                
            if (i%2)==0:
                writer.writerow(row)
                i=i+1

'''
with open('Registers-Users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    database = []
    for row in reader:
        database.append(dict(Email=row['ï»¿Email'],
                             Password=row['Password'],
                             Name=row['Name']))

loggedein u= Fallse


b

while not loggedin:
    Username = input('Username: ')
    Password = getpass("Password: ")
    
    for row in database: 
        Username_File = row['Email']
        Password_File = row['Password']
        Name_File = row['Name']
        if (Username_File == Username and
            Password_File == Password):
            loggedin = True
            print('\nWelcome to the Off-boarding script',row['Name'],'!')
            AdminName = row['Name']
            print("______________________________________________________")
            break
        
    if loggedin is not True:
        print ('\nFailed to sign in, wrong username or password...')
        print("Please try again:")
'''
twentyfour_seven = True
AdminName = "Santiago Torres"
while twentyfour_seven == True:

#####################ACCESS CREDENTIALS ALERTS#################################

    #username= 'offboarding@cloudtask.com'                                     # Credentials for accessing Gmail
    #password='rqtrxxbqvkjjdvbv'

    username= 'helpdesk@cloudtask.com'                                     # Credentials for accessing Gmail
    password='cyrcjyvcbomjttbk'
    

########################GMAIL FETCHING SECTION#################################
    print("\nFetching last off-boarding email alert...\n")
    #mail = imaplib.IMAP4_SSL("outlook.office365.com")                                     # Imaplib access to gmail
    #mail.login(username,password)
    #mail.select("INBOX")    
                            
    mail = imaplib.IMAP4_SSL("imap.gmail.com")                                    # Imaplib access to gmail
    mail.login(username,password)
    mail.select("inbox")     
    
    #labelz=mail.list()
    #print(labelz)

                           # Selects the email's Inbox
    result, data = mail.uid('search', None, 'UID '+ str(169) + ':*')
    InboxItems = data[0].split()
    Recent = InboxItems[-1]
    result2, email_data = mail.uid('fetch', Recent, '(RFC822)')                    # And fetch the content of the most recent email
    raw_email = email_data[0][1].decode("utf-8")
    message1 = mailparser.parse_from_string(raw_email)
    email_message = email.message_from_string(raw_email)                           # To finally parse and save the email's content into a variable
    
    
    if "Employee Termination:" not in email_message['Subject']:
        
        print("Invalid Email Offboarding alert detected with the subject",email_message['Subject'],"...")
        print("Removing non valid Email from 'offboarding@cloudtask.com' Inbox...")
        mail.uid('STORE', Recent , '+FLAGS', '(\Deleted)') 
        mail.expunge()
        print("Invalid Email alert removed, you can execute the script again.")
        sys.exit()
            
    if "Employee Termination:" in email_message['Subject']:
        print("An Off-boarding alert has been received.")
        
        Body = str(email_message) 
        Body2 = Body
        #print(Body2)
        
        #"Employee #: \n                                    </strong><br/>\n                                                526 \n                                        </p>"
        
        sep = 'Subject: Employee Termination: '
        sep2 = '\nContent-Type:'
        rest = str(Body.split(sep2, 1)[0])    
        rest2 = str(rest.split(sep, 1)[1])
        print("Employee: ",rest2)
        Employee_name = rest2
        
        
        sep3 = 'Employee #:'
        sep4 = '<p style='
        rest3 = str(Body2.split(sep3, 1)[1])    
        rest4 = str(rest3.split(sep4, 1)[0])
        numeric_filter = filter(str.isdigit, rest4)
        numeric_string = "".join(numeric_filter)
        EmployeeNumber = int(numeric_string)
        #EmployeeNumber = int(638)
        
        print("Employee Number:",EmployeeNumber)
        
        
        
        
        
        
        
        print("\nVerifying alert...")
        skip = False
        '''with open('Historial.csv') as csvfile:                                                # Selects the data base "DB.csv"  
            datareader = csv.reader(csvfile)
            for line in datareader:                                                    # Searches among the rows contained in the "DB.csv"
                if Employee_name in line:                                                  # And IF finds the user's email in the DB.csv registers
                    print("\n*User found on Script's historial*")
                    print("ALERT: The user got already offboarded by the script, removing already Offboarded user alert...")###-->> TIMESTAMP
                    
                    mail.uid('STORE', Recent , '+FLAGS', '(\Deleted)') 
                    mail.expunge()
                    print("0-0-0-0The Email alert got removed, because the user was already offboarded by the script, closing program...")
                    skip = True
                    if skip == True:
                        print("Case skipped")
                    sys.exit()              
                    '''
            
        if skip == False:
            print("\n*User not found on Script's historial*")
            print("Fetching necessary information (User ID in BambooHR).")
            
            with open('data_file_out.csv',newline='') as f:
                reader=csv.reader(f)
                cells = list(reader)
                                   
                lines=len(list(cells))
                #print("BambooHR Employee list fetched (",lines," rows )")
                
            for single in range(lines):
                if single == 0:
                    continue
                person=cells[single]
                EmployeeNumberCSV = int(person[1])
                if EmployeeNumberCSV == EmployeeNumber:
                    
                    
                    
                    EmployeeID = int(person[0])
                    print("ID:",EmployeeID)
                    print("Employee #:",person[1])
                    #print("Employee Name: "+person[2]+" "+person[4])
                    

               
                    headers = {'Accept':'application/json'}
                    url = "https://7f7a4efac527336d106feba28c6aca597971c95f:x@api.bamboohr.com/api/gateway.php/cloudtaskhr/v1/employees/"+str(EmployeeID)+"/"
                    
                    querystring = {"fields":"firstName,middleName,lastName,fullName1,workEmail,homeEmail,terminationDate,employmentStatus"}
                    response = requests.get(url,headers=headers,params=querystring)
                    
                    
                    ResponseJson = json.loads(response.text)
                    
                    EmployeeStatus = str(ResponseJson['employmentStatus'])
                    EmployeeFullName = str(ResponseJson['fullName1'])
                    EmployeeFirstName = str(ResponseJson['firstName'])
                    EmployeeMiddleName = str(ResponseJson['middleName'])
                    EmployeeLastName = str(ResponseJson['lastName'])
                    EmployeeUsername = str(ResponseJson["workEmail"])
                    EmployeeHomeEmail = str(ResponseJson['homeEmail'])
                    EmployeeTerminationDate = str(ResponseJson['terminationDate'])
                  
                    print("Employee Name: ",EmployeeFullName)
                    print("Work email assigned: ",EmployeeUsername)
                    print("Employment Status: ",EmployeeStatus)
                    
                                            
            
         
            
            
            print("Proceeding to offboard employee...")
    
            
    
            auth = ("16561801813-nfgauhqs54jc77ldtsr6cih1vo6atsae.apps.googleusercontent.com", "yQGiGC4xia7m4IluBQxY5sSX")

            params = {
              "grant_type":"refresh_token",
              "refresh_token":"1//04-tuRRo0i5VrCgYIARAAGAQSNwF-L9IrheYuNOA8W5L7KpLL6l-gxsybhYUp0OITru34urIURh9oh6gnQCinV5D3MD9U__jqP28"
            }
            
            url = "https://oauth2.googleapis.com/token"
            
            ret = requests.post(url, auth=auth, data=params)
            
            print(ret)
            
            AccessTokenJson = json.loads(ret.text)
            AccessToken = str(AccessTokenJson["access_token"])
            
            headers3 = {
                'Authorization': 'Bearer '+AccessToken,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
           
            params3 = (
                ('access_token', AccessToken),
                ('key', 'AIzaSyBzdiZpbiBelKCdTqoAaQCOom8JJz3A2tY'),
            )

            data3 = '{"suspended":true}'

            response2 = requests.put('https://www.googleapis.com/admin/directory/v1/users/'+str(EmployeeUsername)+'', headers=headers3, params=params3, data=data3)
            print(response2)
            print("User offboarded from Gsuite")
                   


            
            #headers = {'Accept':'application/json','Authorization': 'FG3mLVWXDHchLON2EEllkd6D'}
    
            
            #SlackUrl = "x"
        
            #SlackRequest = requests.request("GET", SlackUrl, headers=headers)
                                   
            #SlackUserList = SlackRequest.text
            #UserList = str(SlackUserList)
            #print(UserList["members"]["name"])
            #SlackUrl = "https://slack.com/api/users.remove?token=xoxb-250269185504-1358073218258-JyFUWWaCGWieQBiXLa7elEiB&pretty=1"
    
            #SlackRequest = requests.request("POST", SlackUrl, headers=headers)
            AccessToken = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6InBGVE9QSVZia3lfZ0w5NWswQl9MM0M1TUVfZUdveGE5bzdoUnhONFFtYzQiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wMzM1YTBkOS0zOGZkLTQxZjctYTlmZS01NTA0ODU3N2NiZTQvIiwiaWF0IjoxNjIwOTE0Mjg2LCJuYmYiOjE2MjA5MTQyODYsImV4cCI6MTYyMDkxODE4NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsidXJuOnVzZXI6cmVnaXN0ZXJzZWN1cml0eWluZm8iLCJ1cm46bWljcm9zb2Z0OnJlcTEiLCJ1cm46bWljcm9zb2Z0OnJlcTIiLCJ1cm46bWljcm9zb2Z0OnJlcTMiLCJjMSIsImMyIiwiYzMiLCJjNCIsImM1IiwiYzYiLCJjNyIsImM4IiwiYzkiLCJjMTAiLCJjMTEiLCJjMTIiLCJjMTMiLCJjMTQiLCJjMTUiLCJjMTYiLCJjMTciLCJjMTgiLCJjMTkiLCJjMjAiLCJjMjEiLCJjMjIiLCJjMjMiLCJjMjQiLCJjMjUiXSwiYWdlR3JvdXAiOiIzIiwiYWlvIjoiQVVRQXUvOFRBQUFBMmZ4WXRId2Y5dUtyUm9XTXpzSXdqVGR4SFI5TTJqWnJjM1JFUHJhUWdrQ1JPTDI2dlRRYXdOL2RKTFZrV3JFNE5SeFBxdFEzcXdzdTJlU3U5UW82R3c9PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggZXhwbG9yZXIgKG9mZmljaWFsIHNpdGUpIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlRvcnJlcyBHYWxsbyIsImdpdmVuX25hbWUiOiJTYW50aWFnbyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE4MS4xMjkuNjguMTk0IiwibmFtZSI6IlNhbnRpYWdvICBUb3JyZXMgR2FsbG8iLCJvaWQiOiI0ODhiYjEwNC0yNDQ3LTQ0MzUtOWMzYi00OWVkNzRlZTdhYjciLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDEwMTlEN0NGMSIsInJoIjoiMC5BWFVBMmFBMUFfMDQ5MEdwX2xVRWhYZkw1TFhJaTk3NTJiRklxSzIzU05weVVHUjFBUFkuIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5NYW5hZ2VJZGVudGl0aWVzLkFsbCBVc2VyLlJlYWQgVXNlci5SZWFkV3JpdGUgVXNlci5SZWFkV3JpdGUuQWxsIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiMVBKT2dpZ0dWZmg3UjVDcFZqTUE1MElkcGxMTy1RLWRlSHhuNXlZN3l6VSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJOQSIsInRpZCI6IjAzMzVhMGQ5LTM4ZmQtNDFmNy1hOWZlLTU1MDQ4NTc3Y2JlNCIsInVuaXF1ZV9uYW1lIjoic3RvcnJlc0BjbG91ZHRhc2suY29tIiwidXBuIjoic3RvcnJlc0BjbG91ZHRhc2suY29tIiwidXRpIjoiVmhnNEpkMVNQa1dpTUdCODd0RTRBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiNjJlOTAzOTQtNjlmNS00MjM3LTkxOTAtMDEyMTc3MTQ1ZTEwIiwiYmFmMzdiM2EtNjEwZS00NWRhLTllNjItZDlkMWU1ZTg5MTRiIiwiZmNmOTEwOTgtMDNlMy00MWE5LWI1YmEtNmYwZWM4MTg4YTEyIiwiNjkwOTEyNDYtMjBlOC00YTU2LWFhNGQtMDY2MDc1YjJhN2E4IiwiZjcwOTM4YTAtZmMxMC00MTc3LTllOTAtMjE3OGY4NzY1NzM3IiwiYTllYTg5OTYtMTIyZi00Yzc0LTk1MjAtOGVkY2QxOTI4MjZjIiwiM2Q3NjJjNWEtMWI2Yy00OTNmLTg0M2UtNTVhM2I0MjkyM2Q0IiwiY2YxYzM4ZTUtMzYyMS00MDA0LWE3Y2ItODc5NjI0ZGNlZDdjIiwiZmU5MzBiZTctNWU2Mi00N2RiLTkxYWYtOThjM2E0OWEzOGIxIiwiNDQzNjcxNjMtZWJhMS00NGMzLTk4YWYtZjU3ODc4NzlmOTZhIiwiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19zdCI6eyJzdWIiOiJPRU80TnE5cDA1QjFmaXlEY3VpQkV5WWpTTTg5cER0d18yUGJCWXBHN2JRIn0sInhtc190Y2R0IjoxNjAxNDcyNzc5fQ.dnRHdZ8ExGmrpzc0qFCatn2UCWMsNntMz1qlqtBoNs25GQ0yvSe1Mky933T6IWx1XyHht2LuzLiBnfXt1uQfSsf52YPaZ95DP0YaJPwLJhVletirqPX3sAbpgt8FMmEnnJw0uwSvv5vg9Hr26CefU9KgiQus_QMBEI-a_ye2le1GpYZ5paWpfPClS9rlw45r1aS0DmMe2_CxzOukoJbiL16MXvQSlWog6q_XP33k3uatYNFmzq-9kvqvFDuJYa2qzGBJDT4CZHiZGAHGUm2OkqorhucK4kuQwJb_76Sk7Q6qvH_ub0uIwRh7G0Zwio1nf3ySmXg3N3YgjF2sh5CGHg'                      
            #SlackUserList = SlackRequest.text    
            headers3 = {      
                'Authorization': 'Bearer '+AccessToken,                          
                'Content-Type': 'application/json'
            }
            #('key', 'AIzaSyBzdiZpbiBelKCdTqoAaQCOom8JJz3A2tY'),
            #'Accept': 'application/json',
            #
            #('access_token', AccessToken)
            #params3 = (
                
            #)
            
            #params=params3,

            #data3 = '{"accountEnabled":"false"}'

            #response2 = requests.patch('https://graph.microsoft.com/v1.0/users/'+str(EmployeeUsername)+'', headers=headers3,  data=data3)
            #print(response2)
            #print("User offboarded from Outlook")
            
                        
            ####################################################################################################
            #headers5 = {
            #    'Authorization': 'Bearer eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM0MjQyMyxcImlcIjo3MjgzODgzLFwiY1wiOjQ2MjIzMzQsXCJ1XCI6NjMwOTU3MyxcInJcIjpcIlVTXCIsXCJzXCI6W1wiV1wiLFwiRlwiLFwiSVwiLFwiVVwiLFwiS1wiLFwiQ1wiLFwiRFwiLFwiTVwiLFwiQVwiLFwiTFwiLFwiUFwiXSxcInpcIjpbXSxcInRcIjowfSIsImlhdCI6MTYwMzQ3NDE4NH0.fMHovi6EkQkf6cEwlpdUmMfSmJzyzcKh1eHQtblXLFM',
            #}
            
            #params5 = (
            #    ('me', 'true'),
            #)
            
            #response5 = requests.put('https://www.wrike.com/api/v4/users/{userId}', headers=headers5, params=params5)
            #response5 = requests.get('https://www.wrike.com/api/v4/contacts', headers=headers5)
            #ContactsJson = json.loads(response5.text)
            #print(list(ContactsJson))
                       
            #Notification Email 
            
            print("Sending Tech set up guide email...")
                    
            subject = "Employee Offboarded"                                       #Email is sent notifying admin the user has been ofboarded
            body =  '''<p>Hello team,</p>
<p>The account credentials of '''+EmployeeFullName+''' (<a href="mailto:'''+EmployeeUsername+'''">'''+EmployeeUsername+'''</a>) have been automatically Off-boarded from the following platforms:</p>
<ul>
<li><strong>G-Suite login</strong><em> (Suspended)</em></li>
</ul>
<p><strong>Note:&nbsp;</strong>You have received this email confirmation, being the final step of the automatic Off-boarding process. The offboarding process gets triggered by the employee termination action on BambooHR, if you believe this message is an error, or need to undo the off-boarding action, please contact <a href="mailto:storres@cloudtask.com">storres@cloudtask.com</a>&nbsp;or <a href="mailto:se@cloudtask.com">tsg@cloudtask.com</a>.</p>
<p>Best regards,</p>
<p>&nbsp;</p>
<p>&nbsp;<img src="https://www.linkpicture.com/q/Logo-tsg.png" alt="" width="252" height="105" /></p>
 '''         
     
            msg = MIMEMultipart()
            msg['From'] = "offboarding@cloudtask.com"
            msg['To'] = 'tsg@cloudtask.com'
            #msg['To'] = EmployeeHomeEmail
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body,'html')) 
            server =smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("helpdesk@cloudtask.com",'cyrcjyvcbomjttbk')
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            server.sendmail(msg['From'],username,msg.as_string())
            server.quit()    
            
            
            #print("\nSending Offboarding notification to the distribution list")
            
            
        
            #subject = "Employee Offboarded"                                       #Email is sent notifying admin the user has been ofboarded
            #msg =  "Hello team: \n\nThe employee: "+ EmployeeFullName + ", identified with the username: "+username+ " got automatically Offboarded from the following platforms: \n\n- G-Suite (Account suspended.)\n- Slack (Account deactivated.)\n- Wrike (Account deactivated.) "
            #send_email(subject,msg)                                               #By Calling Google's Gmail API, with the previous message
                
            #print("The Offboarding Email notification has been sent.")
            #print("\n\n**********Program terminated.**********")

            
        
            hour_date_time = datetime.now()
            TimeStamp = str(hour_date_time)
            EmployeeOffboarded = Employee_name
            
            ##################################################################
            
                        
            
            
            
            
            OffboardingDate_Year = TimeStamp[:4]
            OffboardingDate_Month = TimeStamp[5:7]
            OffboardingDate_Day = TimeStamp[8:10]
            
            
            OffboardingHour = TimeStamp[11:19]
            
            OffboardingDate = OffboardingDate_Month+'/'+OffboardingDate_Day+'/'+OffboardingDate_Year
            
            print(OffboardingDate_Year)
            print(OffboardingDate_Month)
            print(OffboardingDate_Day)
            
            print(OffboardingDate)
            print(OffboardingHour)
            
            reader=[EmployeeUsername,OffboardingDate,OffboardingHour]
            
            cells = list(reader)
            lines=len(list(cells))
            
            print("BambooHR Report fetched (",lines," rows )")
            print(reader)
            
            scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
            client = gspread.authorize(creds)
            cellsList = list(reader)
            #for i in range(lines):
            #    for j in range(20):
            #        cellsList.append(Cell(row=i+1, col=j+1, value=cells[i][j]))
            sheet = client.open("Offboarding History").sheet1
            #sheet.update_cells(cellsList)
            #sheet.update_cell('1', '1', 'test')
            sheet.append_row(cellsList)
            sys.exit()            
                        
                        
                        
                        
            
            
            
            
            
            
            
            
            #Registered = False
            #print("\nRegistering Offboarding action on Script's historial...")
            
            #with open('Historial.csv', 'a', newline='') as csvfile:
            #    fieldnames = ['Employee', 'Time_Stamp','User']
            #    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                # Appends the register on the "DB.csv"
            
            #    writer.writerow({'Employee': EmployeeOffboarded, 'Time_Stamp': TimeStamp[0:20]})
            #    Registered =True
                
            #print("*******The Offboarding process has been completed and registered succesfully!********")
            #if Registered == True:
            #    sys.exit()
            
            
           

            

            