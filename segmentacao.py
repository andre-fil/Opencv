#códigos que trabalharão a segmentação das imagens em canais de cores RGB
import cv2

imagem = cv2.imread('img/2.jpg')

'''
Segmentando as cores
     --> criando três natrizes, uma para cada canal de cor, para armazenar os numeros inteiros que representem a intensidade
        de cor de cada píxel. (cada elemento da matriz é a intensidade da cor referente a cada pixel)
'''

'''
Geralmente,	a	biblioteca	OpenCV	trata	o	espaço	de	cor	RGB
(red,	 green,	 blue)	 como	 BGR	 (blue,	 green,	red),	 invertendo	 a
ordem	 dos	 canais.	 Por	 este	 motivo,	 quando	 utilizamos	 a
função	 	 split	 ,	 conforme	 demonstrado	 no	 código,
declaramos	as	variáveis	na	sequência	azul,	verde,	vermelho.
'''
    
azul, verde, vermelho = cv2.split(imagem)

#mostrando resultados  separdaos
cv2.imshow("Canal R", vermelho)
cv2.imshow("canal G", verde)
cv2.imshow("Canal B", azul)

#salvando arquivos de imagens
cv2.imwrite("img/2RED.jpg", vermelho)
cv2.imwrite("img/2GREEN.jpg", verde)
cv2.imwrite("img/2BLUE.jpg", azul)




#Fechando janelas
cv2.waitKey(0)
cv2.destroyAllWindows()