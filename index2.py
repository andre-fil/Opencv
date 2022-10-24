import cv2

#Capaturar as múltiplas imagens da webcam
captura = cv2.VideoCapture(0)

#Permitir que se pegue as imagens de forma contínua
while True:
    
    #lendo e mostrando as imagens
    ret, frame = captura.read()
    cv2.imshow("IMG", frame)
    
    #condição de parada
    if cv2.waitKey(10)	&	0xFF ==	ord("q"):
	    break
 
 #fechando janelas
captura.relese()
cv2.destroyAllWindows()

 
    