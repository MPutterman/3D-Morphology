import numpy as np
class morphology_3d():
    def __init__(self):
        pass

    def erosion(self,img,selem=np.array([[[False,False,False],[False,True,False],[False,False,False]],[[False,True,False],[True,True,True],[False,True,False]],[[False,False,False],[False,True,False],[False,False,False]]]),thresh=2):
        out=np.zeros_like(img)
        for i in range(len(img)):
            
            for j in range(len(img[0])):
                out[i][j] = self.erode_point(img,selem,i,j,thresh=thresh)
        return out
    def erode_point(self,img,selem,r,c,thresh):
        print(r)
        l1=len(selem)//2
        l2=len(selem[0])//2
        l3=len(selem[0][0])//2
        val = img[r][c]
        arr_points=[]
        
        for i in range(-1*l1,l1):
            for j in range(-1*l2,l2):
                if (r+i>=0) and (r+i<len(img)) and (c+j>=0) and (c+j<len(img[0])):
                    for k in range(-1*l3,l3):
                        if selem[i+l1][j+l2][k+l3] ==1:
                            if abs(img[r+i][c+j] - (img[r][c]+k))<thresh:
                                arr_points.append(img[r+i][c+j])
        
        return np.min(np.asarray(arr_points))
        
    def dilation(self,img,selem=np.array([[[False,False,False],[False,True,False],[False,False,False]],[[False,True,False],[True,True,True],[False,True,False]],[[False,False,False],[False,True,False],[False,False,False]]]),thresh=2):
        
        out=np.zeros_like(img)
        for i in range(len(img)):
            for j in range(len(img[0])):
                out[i][j] = self.dilate_point(img,selem,i,j,thresh=thresh)
        img=out.copy()
        return out
    def dilate_point(self,img,selem,r,c,thresh):
        print(r)
        l1=len(selem)//2
        l2=len(selem[0])//2
        l3=len(selem[0][0])//2
        val = img[r][c]
        arr_points=[]
        for i in range(-1*l1,l1):
            for j in range(-1*l2,l2):
                if (r+i>=0) and (r+i<len(img)) and (c+j>=0) and (c+j<len(img[0])):
                    for k in range(-1*l3,l3):
                        if selem[i+l1][j+l2][k+l3]==1:
                            if abs(img[r+i][c+j] - (img[r][c]+k))<thresh:
                                arr_points.append(img[r+i][c+j])
        return np.max(np.asarray(arr_points))
    def opening(self,selem):
        self.erosion(selem=selem)
        return self.dilation(selem=selem)
    def closing(self,selem):
        self.dilation(selem=selem)
        return self.erosion(selem=selem)
