import cv2
import numpy as np

def lan_answer(img, line, column, h_answer, w_answer):
    white = np.full((h_answer,w_answer,3), img[0][0][0])
    i = 1
    while True:
        comparison = white == img[line:line+h_answer,column + i*w_answer:column + (i+1)*w_answer,:]
        equal_image = comparison.all()
        if equal_image == True:
            break
        i+=1
    white = np.full((10,i*w_answer,3), img[0][0][0])
    j = 1
    while True:
        comparison = white == img[line + j * 10: line+ (j+1) * 10,column :column + i*w_answer,:]
        equal_image = comparison.all()
        if equal_image == True:
            break
        j+=1
    
    k = -1

    while True:
        comparison = white == img[line + k * 10: line+ (k+1) * 10,column :column + i*w_answer,:]
        equal_image = comparison.all()
        if equal_image == True:
            break
        k-=1
    return img[line + k *10: line + j*10, column :column + i*w_answer,:]

def extract_answer(file):
    
    for i in range(1,50):
            img = cv2.imread(file+f"/cau{i}.png", cv2.IMREAD_COLOR)
            h, w, c = img.shape
            answer_A = cv2.imread(file+"/answer_A.png", cv2.IMREAD_COLOR)
            answer_B = cv2.imread(file+"/answer_B.png", cv2.IMREAD_COLOR)
            answer_C = cv2.imread(file+"/answer_C.png", cv2.IMREAD_COLOR)
            answer_D = cv2.imread(file+"/answer_D.png", cv2.IMREAD_COLOR)
            h_answer, w_answer, c_answer = answer_A.shape
            a, b, c, d = True, True, True, True
            for line in range(h-h_answer):
                for column in range(w-w_answer):
                    if a:    
                        comparison_A = answer_A == img[line:line+h_answer,column:column+w_answer,:]
                        equal_image_A = comparison_A.all()
                        if equal_image_A == True:
                            img_A = lan_answer(img, line, column, h_answer, w_answer)
                            cv2.imwrite(file+f"/cau{i}_A.png", img_A)
                            a = False

                    if b: 
                        comparison_B = answer_B == img[line:line+h_answer,column:column+w_answer,:]
                        equal_image_B = comparison_B.all()
                        if equal_image_B == True:
                            img_B = lan_answer(img, line, column, h_answer, w_answer)
                            cv2.imwrite(file+f"/cau{i}_B.png", img_B)
                            b = False


                    comparison_C = answer_C == img[line:line+h_answer,column:column+w_answer,:]
                    equal_image_C = comparison_C.all()
                    if equal_image_C == True:
                        try:
                            img_C = lan_answer(img, line, column, h_answer, w_answer)
                            cv2.imwrite(file+f"/cau{i}_C.png", img_C)
                        except:
                            print("")

                    if d:
                        comparison_D = answer_D == img[line:line+h_answer,column:column+w_answer,:]
                        equal_image_D = comparison_D.all()
                        if equal_image_D == True:
                            img_D = lan_answer(img, line, column, h_answer, w_answer)
                            cv2.imwrite(file+f"/cau{i}_D.png", img_D)
                            d = True
    return




if __name__ == "__main__":
    extract_answer("dethi/dethi3")