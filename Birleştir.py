import shutil
#import face_recognition as fr
import os
import cv2
#import face_recognition
import numpy as np
from tkinter import messagebox
import datetime
import random
from tkinter import *

def alinanmetin():
    
    book_name_control = True 
    Found = True
    
    numb_enb = False
   
    no_book = True
    fnames = {}
    
    sit = E1.get()
    sit2 = E2.get()
    
    
    
    no_ipt = False
    if sit == "" or sit2 == "":
        messagebox.showinfo("Title", "> Please fill in all fields.")
        no_ipt = True
    
    if numb_enb == False:
        for i in range(0,len(E1.get())):
            for k in range(0,9):
                if sit[i] == str(k):
                    messagebox.showinfo("Title", "> Please do not enter numbers instead of Name.")
                    numb_enb = True
    
    
    while book_name_control: # True
        
                
        book_name = E1.get()+".jpg" # Take a book name value 
        book_name = book_name.lower()# convert to all text small charecter
        
       
        for fnames in os.walk("./alkit"): #This function is going to /res file and read inside file
            for f in fnames: # It is read res file in side
                alkit_in = f #This is convert to string if we didn't chance it  we use to list structure. 
           
        if alkit_in == []:
            messagebox.showinfo("Title", "> Folder contents are empty, please upload photos.")
           
        for i in alkit_in: #convert to string
            if book_name != i:
                shutil.copy2('./alkit/'+i, "./alkit/"+book_name)
                """
                It is make it copy file because we will remove to file the featcure if we can not do this.
                program will be cros the files  
                """
                os.path.exists("./alkit/"+i)
                os.remove("./alkit/"+i)
            
        os.chdir('C:/Users/Ege/Desktop/nesne') # go to the this file path 
                
        
        
                
        for e in encode: # this function is read in encode list
            
            if book_name == e: # encode in filename compate to book name 
                
                while True:
                    camera = cv2.VideoCapture("alkit/"+book_name)                    
                    ret,kare = camera.read()
                    try:
                        grey_square = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)#convert to grey color
                        obje = cv2.imread("res/"+book_name,0)    
                        res = cv2.matchTemplate(grey_square,obje,cv2.TM_CCOEFF_NORMED)#compare .jpg file
                        face_reco = True
                        old_value = 0.8
                        loc = np.where(res>old_value)
            
        
                
                        for n in zip(*loc[::-1]):
                            # compare is true
                            #print("> Book Found !!! :D")
                            messagebox.showinfo("Title", "> Book Found !!! :D")
                            book_name_control = False
                            Found = False
                            break
                        break
                    except:
                        messagebox.showinfo("Title", "> There was an error in the book matching process, please try again")
                        #print("> There was an error in the book matching process, please try again")
                        break
                            
                    
                        
                    if Found == False:
                        break
                    os.path.exists("./alkit/"+book_name)
                no_book = False
                book_name = book_name.split(".jpg")
                
                #print(">",book_name[0],"Available in the library")
                messagebox.showinfo("Title", ">",book_name[0],"Available in the library")
                
            if encode[-1] == e:
                while_çık = True
                break
        
        if book_name_control == True:  
            break
    
    if no_book == True:
        if no_ipt == False:
            #print(">no book")
            messagebox.showinfo("Title", ">no book")
    else:     
        # close the windows
        camera.release()
        cv2.destroyAllWindows()
    
    
    # If program does not find the search book. it will be not continue
        
        
        
    def get_encoded_faces(ad):
        encoded = {}
        f = ad
        for dirpath, dnames, fnames in os.walk("./faces"):
            for esit in fnames:
                if ad == esit:
                    face = fr.load_image_file("faces/"+f)
                    encoding = fr.face_encodings(face)[0]
                    encoded[f.split(".")[0]] = encoding
                    yüz_var = True
        
        return encoded
    
    
    def classify_face(im,kad):
        
        faces = get_encoded_faces(kad)
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())
        
        img = cv2.imread(im, 1)
     
        face_locations = face_recognition.face_locations(img)
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    
        face_names = []
        for face_encoding in unknown_face_encodings:
            # if program is not find user,make user name unknown
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            name = "Unknown"
    
    
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
        
        if name != "Unknown":
                
            for x in face_names:
                #print(">>",x,"user received a book")
                messagebox.showinfo("Title", ">>",x,"user received a book")
            face_count = len(face_names)
            
            if face_count != 1:
                #print("> !!! Multiple faces found in face recognition")
                messagebox.showinfo("Title", "> !!! Multiple faces found in face recognition")
            else:
                
                We1 = E1.get()
                We2 = E2.get()
                
                f = open("Data.txt", "a")
                f.write(We1+"\n")
                f.write(We2+"\n")
                now = datetime.datetime.now()
                y=int(now.strftime("%Y"))
                m=int(now.strftime("%m"))+1
                d=int(now.strftime("%d"))
                f.write(str(y) + "-" + str(m) + "-" + str(d) + "\n\n")
                
                f.close()    

                #print(">>> The transaction has been successfully completed !")
                messagebox.showinfo("Title", ">>> The transaction has been successfully completed !")
        else:
            #print("No contact identified")
            messagebox.showinfo("Title", "No contact identified")
            
        
    if book_name_control == False:
        
    
        user_face = E2.get()+".jpg"
        user_face = user_face.lower()
        face_tut = {}
        for fnames in os.walk("./facetake"): 
            for f in fnames: 
                face_tut = f 
        if face_tut == []:
            #print("> Folder content is empty, please upload photos")
            messagebox.showinfo("Title", "> Folder content is empty, please upload photos")
    
        for i in face_tut:
            if user_face != i:
                shutil.copy2('./facetake/'+i, "./facetake/"+user_face)
                #Since the name is random, we call it the value we entered.
                os.path.exists("./facetake/"+i)
                os.remove("./facetake/"+i)
    
        
        
            if Found == False:    
                if face_reco == True:
                    #print("")
                    #print("-----------YÜZ TANIMA------------")  
                    #print("Yüz tanıma işlemi sonucu")
                    try:
                        print("recoooooooo")
                        # Eğer yüz tanıma kütüphanesi yoksa bilgisayarda buradan sonra çalışmaz !!!
                        # If there is no facial recognition library, it will not work on the computer after this !!!
                        classify_face("./facetake/"+user_face,user_face)
                    except:
                        print("> İsiminiz sistemde bulunmamaktadır")
                        messagebox.showinfo("Title", "> İsiminiz sistemde bulunmamaktadır")
                        messagebox.showinfo("Title", "Not Sisteminizde face_recognition yok ise çalışmaz")
                    
                    
                    
                    
    # Deletes the contents of the file "facetake"
    for fnames in os.walk("./facetake"): 
        for f in fnames: 
            alkit_in = f 
        for i in alkit_in:
            os.path.exists("./facetake/"+i)
            os.remove("./facetake/"+i)
                   
                    
    # Deletes the contents of the file "alkit"
    for fnames in os.walk("./alkit"): 
        for f in fnames: 
            alkit_in = f 
        for i in alkit_in:
            os.path.exists("./alkit/"+i)
            os.remove("./alkit/"+i)
    
                    
    
    
    E1.delete(first=0,last=len(sit))
    E2.delete(first=0,last=len(sit2))
    print()
    print()
    print()
    print(">#/>#/>#/>#/>#/>#/>#  Finish   />#/>#/>#/>#/>#/>#/>#/>#/>#/")
    

    
    


      
pencere = Tk()
 
pencere.title("Library")
pencere.geometry("680x350")
 


#grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()
 
Welcome = Label(uygulama, text="Welcome")
Step1 = Label(uygulama, text="! Put the book you will buy in the alkyd folder and your face in the facetake folder")
book_in_lib = Label(uygulama, text="Books in the library")
book_in_lib2 = Label(uygulama, text="Recommended books")
L1 = Label(uygulama, text="Book:")
E1 = Entry(uygulama, bd =2)
L2 = Label(uygulama, text="Name-Surname:")
E2 = Entry(uygulama, bd =2)
Lb1 = Listbox(uygulama)
Lb2 = Listbox(uygulama)


  

encode = {}
for fnames in os.walk("./res"): #This function is going to /res file and read inside file
    for f in fnames: # It is read res file in side
        encode = f #This is convert to string if we didn't chance it  we use to list structure. 



cntrl = {}
clk=0
number = 0
out = 0
tutma = []
tutma2 = []


for delet2 in range(0,len(encode)):
    kit_del2 = str(encode[delet2])
    tutma2.append(kit_del2[:-4])
    Lb1.insert(1,tutma2[delet2])
    
    
for li in range(4):
    shd_book = random.randint(1,len(encode)-1)
    cntrl[clk] = encode[shd_book]
    clk = clk + 1    
    
for delet in range(0,4):
    kit_del = str(cntrl[delet])
    tutma.append(kit_del[:-4])
    
for ai in range (1,4):
    if cntrl[out] != cntrl[ai]:
        Lb2.insert(1,tutma[out])
    
    out = out + 1


button = Button(uygulama, text = " Searc " , width=8,height=2)
button.config(command=alinanmetin)

Welcome.grid(row = 0 , column = 1)
book_in_lib.grid(row =4 ,column=1, padx=10)
book_in_lib2.grid(row =4 ,column=0, padx=10)
Step1.grid(row = 1 , column = 1)
L1.grid(row = 2 , column = 0)
E1.grid(row = 2 , column = 1)
L2.grid(row = 3 , column = 0)
E2.grid(row = 3 , column = 1)
Lb1.grid(row =5 , column = 1,padx=10, pady=10)
Lb2.grid(row =5 , column = 0,padx=10, pady=10)
button.grid(row = 4 , column = 2,padx=10, pady=10)
 
  
   

pencere.mainloop()
