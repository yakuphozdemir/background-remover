import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from rembg import remove

ctk.set_default_color_theme("blue")    # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("Dark")        # Modes: "Light", "Dark", "System"(MacOS)

root = ctk.CTk()
root.geometry("640x720")
#root.minsize(900,800)
defaultImage = ImageTk.PhotoImage(Image.open("image.png"))

destPath = ctk.StringVar(value="C:\\Users\\yakup\\Desktop")
imagePath = ctk.StringVar()
imageTypes = [".png", ".jpg", ".jpeg", ".svg"]

def resize(img):
    width, height = img.size
    #print(width, height)
    
    if width >= height:
        ratio = height/width
        new_w, new_h = 640, int(640*ratio)
    else:
        ratio = width/height
        new_w, new_h = int(600*ratio), 600
    #print(new_w, new_h)
    resizedImage = img.resize((new_w,new_h), Image.ANTIALIAS)
    return resizedImage

def openImage():
    global image
    openDirectory = filedialog.askopenfilename(initialdir=destPath)
    
    if any(element in openDirectory for element in imageTypes):
        image = Image.open(openDirectory)
        resizedImage = resize(image)
        resizedImage = ImageTk.PhotoImage(resizedImage)
        imageLabel.configure(image=resizedImage)
    elif openDirectory == "":
        ""
    else:
        messagebox.showerror(message="This is not a valid file. \nPlease select an image.", title="Error")
    
def bgRemover():
    global removedImage
    removedImage = remove(image)
    resizedImage = resize(removedImage)
    resizedImage = ImageTk.PhotoImage(resizedImage)
    imageLabel.configure(image=resizedImage)
    
def saveImage():
    output = filedialog.asksaveasfilename(title="Save as",defaultextension=".png", filetypes=(("Png Files", ".png"), 
                                                                                              ("Jpeg Files", ".jpeg"), 
                                                                                              ("Jpg Files", ".jpg"), 
                                                                                              ("Svg Files", ".svg"),
                                                                                              ("All Files", ".")
                                                                                              )  )
    removedImage.save(output, "png")
    
def theme(e):
    ctk.set_appearance_mode(optionMenu.get())
    
    
r = 10
imageLabel = ctk.CTkLabel(root, height=20, width=100, image=defaultImage, text="", corner_radius=10)
imageLabel.place(relx=0.5, rely=0, y=60, anchor="n")

openButton = ctk.CTkButton(root, corner_radius=r, text="Open Image", command=openImage)
openButton.place(in_=imageLabel, relx=0.5, rely=1, y=50, x=-180)

bgRemoveButton = ctk.CTkButton(root, corner_radius=r, text="Remove Background", command=bgRemover)
bgRemoveButton.place(in_=imageLabel, relx=0.5, rely=1, y=50, x=40)

saveButton = ctk.CTkButton(root, corner_radius=r, text="Save Image", command=saveImage)
saveButton.place(in_=imageLabel, relx=0.5, rely=1, y=120, x=-70)

optionMenu = ctk.CTkOptionMenu(root, corner_radius=r, values=["Dark", "Light"], command=theme)
optionMenu.place(relx=1, rely=0, anchor="ne", x=-20, y=20)


root.mainloop()