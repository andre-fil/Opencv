import cv2

#Lê e abre imagens
imagem	=	cv2.imread("img/0.jpg")
cv2.imshow("imagem", imagem)

#Faz janela de imagem aguarar
cv2.waitKey(0)
cv2.destroyAllWindows()