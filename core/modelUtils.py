import cv2
import pytesseract



# images_array = []


# num_images = int(input("Enter number of images: "))
# for i in range (num_images):
#     images_array.append(str(input("Enter image full path: ")))


# for i in range (len(images_array)):
#     img = cv2.imread(images_array[i])
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     dta = pytesseract.image_to_string(img)
#     dta_array = dta.split('\n')
#     # for j in range (len(dta_array)):
#     #     #print("Line ", j+1)
#     #     print(dta_array[j])

#     return dta_array

import os

folder2 = os.path.dirname(__file__)
folder3 = os.path.dirname(folder2)

print(folder3)

def medWing_model(imagepath):
    print(folder3,imagepath)
    images_array = [folder3+"/media/"+str(imagepath)]


    # num_images = int(input("Enter number of images: "))
    # for i in range (num_images):
    #     images_array.append(str(input("Enter image full path: ")))

    dta_array = []
    for i in range (len(images_array)):
        img = cv2.imread(images_array[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dta = pytesseract.image_to_string(img, config = "--psm 6 --oem 3 -c tessedit_char_unblacklist=0123456789")
        dta_array = dta.split('\n')
        print(dta_array)
        print(type(dta_array))
        for j in range (len(dta_array)):
            #print("Line ", j+1)
            print(dta_array[j])
    
    med = {}
    for j in range (len(dta_array)):
        #print("Line ", j+1)
        print(dta_array[j])
        d = dta_array[j].split()
        med_dict = {}
        if(len(d)>1):
            med_dict["item"]=d[0] 
            med_dict["quantity"]=d[1]
        else:
            try:
                med_dict["item"]=d[0] 
                med_dict["quantity"]=1
            except:
                pass
        if(len(med_dict)>=1):
            med[f"order{j+1}"]=med_dict
            
    return med

