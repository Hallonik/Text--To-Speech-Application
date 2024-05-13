#Building CV Generator by using GUI interface package to enter the  infos. by user
#adding QR to the Cv to access the portfolio website of user directly thorugh a single scan
#In the end a pdf containg all the infos. of user 

from tkinter import *#to generate the gui interface for cv generator
import pyqrcode #to generate QR 
from fpdf import FPDF#to create the pdf
from tkinter import messagebox#to give a pop up message for empty text fields

#inheriting this class from fpdf
class PDFCV(FPDF):
    def header(self):#to add the QR in the header
        self.image("mywebsite.png",10,8,33,title="Portfolio Site")#setting the representaation of QR on pdf

    def footer(self) :#to add footer if present
        pass

    #cv generating func.
    def generate_cv(self,name,email,phone_no,address,skills,work_experience,education,about_me):
        self.add_page()
        self.ln(20)#adding line break or space
        
        #displaying the name
        self.set_font("Times","B",26)#to set the font
        self.cell(0,10,name,new_x="LMARGIN",new_y="NEXT",align="C")

        #Adding contact info. header
        self.ln(5)#to give a line break
        self.set_font("Arial","B",12)#to set the font
        self.cell(0,10,"Contact Information",new_x='LMARGIN',new_y="NEXT",align="L")

        #Adding the contact information
        self.set_font("Arial","B",10)#to set the font
        self.cell(0,5,"Email : {}".format(email),new_x='LMARGIN',new_y="NEXT")
        self.cell(0,5,"Phone No. : {}".format(phone_no),new_x='LMARGIN',new_y="NEXT")
        self.cell(0,5,"Address : {}".format(address),new_x='LMARGIN',new_y="NEXT")


        #Skills
        self.ln(10)#to give a line break
        self.set_font("Arial","B",12)#to set the font for header Skill
        self.cell(0,10,"Skills",new_x='LMARGIN',new_y="NEXT",align="L")

        #Adding Skills
        self.set_font("Arial","B",10)#to set the font for skill info.
        for skill in skills:
            self.cell(0,5,"- {}".format(skill),new_x='LMARGIN',new_y="NEXT")
        


        #Work Experience
        self.ln(10)#to give a line break
        self.set_font("Arial","B",12)#to set the font for header Work expericence
        self.cell(0,10,"Work Experience",new_x='LMARGIN',new_y="NEXT",align="L")

        #Adding  Work experience info.
        self.set_font("Arial","B",10)#to set the font for skill info.
        for expri in work_experience:
            self.cell(0,5,"{} : {}".format(expri["title"],expri["description"]),new_x='LMARGIN',new_y="NEXT")
        

        #Education
        self.ln(10)#to give a line break
        self.set_font("Arial","B",12)#to set the font for header education
        self.cell(0,10,"Education",new_x='LMARGIN',new_y="NEXT",align="L")

        #Adding Educational info.
        self.set_font("Arial","B",10)#to set the font for skill info.
        for edu in education:
            self.cell(0,5,"{} : {}".format(edu["degree"],edu["university"]),new_x='LMARGIN',new_y="NEXT")
        

         #About Me
        self.ln(10)#to give a line break
        self.set_font("Arial","B",12)#to set the font for header About me
        self.cell(0,10,"About Me",new_x='LMARGIN',new_y="NEXT",align="L")

        #Adding info. about my self
        self.set_font("Arial","B",10)#to set the font for about me info.
        self.multi_cell(0,5,about_me)   

                          
        

        self.output("cv1.pdf")#any name for the pdf can be given in my case its cv1.pdf



#func. to  generate the CV
def generate_cv_pdf():
    #extracting data fron the text boxes
    name=entry_name.get()
    email=entry_email.get()
    phone_no=entry_phone.get()
    address=entry_address.get()
    website=entry_website.get()
    skills=entry_skills.get("1.0",END).strip().split("\n")#since it contains multiple lines we have to mention the starting and ending,strip() func. to remove all spaces after a line,split() func. to split every skill to a new line
    
    #create empty list to store the experience and education contents
    work_experience=[]
    education=[]




    work_experience_lines=entry_experience.get("1.0",END).strip().split("\n")#to get the texts from Experience text box
    #to get the job title : description part separetely
    for line in work_experience_lines:
        title,description=line.split(":")
        work_experience.append({'title':title.strip(),'description':description.strip()})


    education_lines=entry_education.get("1.0",END).strip().split("\n")#to get the texts from Experience text box
    #to get the degree : university part separetely
    for line in education_lines:
        degree,university=line.split(":")
        education.append({'degree':degree.strip(),'university':university.strip()})#the splitted parts are again appended
    
    about_me=entry_about_me.get("1.0",END)#data from about me text box extracted


    #Create QR code
    qrcode=pyqrcode.create(website)#QR for the website entered gets created
    qrcode.png("mywebsite.png",scale=6)#imge of the QR


    #checking validation of inputs if not present gives a proper message
    if not name or not email or not phone_no or not address or not skills or not education or not work_experience or not about_me:
        messagebox.showerror("Error ! Please fill all the details")
        return 
    
    cv=PDFCV()
    cv.generate_cv(name,email,phone_no,address,skills,work_experience,education,about_me)

 



window=Tk()#to create a window for the interface
window.title(" CV Generator ")#adding title for the window

#creation of labels and entry fields

#NAME
label_name=Label(window,text="Name : ")#label for name that asks the user to enter the name
label_name.pack()#to display the label_name's contents  on window interface

entry_name=Entry(window,width=50)#to create a text box on interface to enter  the name
entry_name.pack()

#EMail
label_email=Label(window,text="Email ID : ")#label for email that asks the user to enter the email
label_email.pack()#to display the label_email's contents  on window interface

entry_email=Entry(window,width=50)#to create a text box on interface to enter  the email
entry_email.pack()

#PHONE NUMBER
label_phone=Label(window,text="Phone Number : ")#label for phone no. that asks the user to enter the  phone no.
label_phone.pack()#to display the label_phone's contents  on window interface

entry_phone=Entry(window,width=50)#to create a text box on interface to enter  the phone no.
entry_phone.pack()


#ADDRESS
label_address=Label(window,text="Address : ")#label for address that asks the user to enter the address
label_address.pack()#to display the label_address's contents  on window interface

entry_address=Entry(window,width=50)#to create a text box on interface to enter  the address
entry_address.pack()


#PORTFOLIO WEBSITE
label_website=Label(window,text="Website : ")#label for website that asks the user to enter the website
label_website.pack()#to display the label_website's contents  on window interface

entry_website=Entry(window,width=50)#to create a text box on interface to enter  the website
entry_website.pack()


#text box to enter the skills in which 
# every skill will be displayed in a single line during o/p
label_skills=Label(window,text="Skills (Enter one skill per line)")
label_skills.pack()
entry_skills=Text(window,height=5)
entry_skills.pack()


#text box to enter the educational details
label_education=Label(window,text="Education ( Enter one  per line in format : 'Degree' : 'University')")
label_education.pack()
entry_education=Text(window,height=5)
entry_education.pack()



#textbox to enter the experience details
label_experience=Label(window,text="Experience (Enter one  per line in format : 'Job Title' : 'Description')")
label_experience.pack()
entry_experience=Text(window,height=5)
entry_experience.pack()


#textbox to enter the details about myself
label_about_me=Label(window,text="About Me : ")
label_about_me.pack()
entry_about_me=Text(window,height=5)
entry_about_me.pack()


#button to generate the CV
button_generate=Button(window,text=" Generate CV ",command=generate_cv_pdf)#generate_cv_pdf func. is called to create the pdf
button_generate.pack()




window.mainloop()