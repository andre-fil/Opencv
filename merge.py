'''
Da	 mesma	 maneira	 como	 podemos	 segmentar	 os	 canais	 de
uma	imagem	RGB,	também	é	possível	realizar	a	operação	inversa,
ou	seja,	mesclar	novamente	esses	canais	resultando	em	uma	única
imagem	 colorida.
'''

import cv2

imagem = cv2.imread('img/2.jpg')

#separando canais de cores para posterior junção

azul, verde, vermelho = cv2.split(imagem)

#juntando canais

imgAlterada1 = cv2.merge((azul, vermelho, azul))

cv2.imshow("Imagem", imgAlterada1)



#fechando janelas

cv2.waitKey(0)
cv2.destroyAllWindows()