'''
Com	 o	 objetivo	 de	 reduzir	 a	 quantidade	 de	 informações	 a
serem	processadas,	a	conversão	de	imagens	coloridas	em	RGB	para
imagens	em	tons	de	cinza	é	uma	tarefa	quase	sempre	realizada	em
sistemas	 de	 Visão	Computacional.	As	imagens	 em	 tons	 de	 cinza,
Convertendo	imagens	em	RGB	para	tons	de	cinza apesar	de	representarem	menos	detalhes,
mantêm	as	características importantes	dos	objetos	ou	regiões	de	interesse,	tais	como	bordas,
regiões,	manchas	e	junções. --> única matriz
'''

import cv2
imagem = cv2.imread("img/2.jpg")

#	Convertendo	e	exibindo	a	imagem	em	tons	de	cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#mostrando imagem

cv2.imshow("Imagem", imagem)

#fechando janelas
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
é	válido	mencionar	 que	a	imagem	em	 tons
de	 cinza,	 após	 a	 conversão,	 é	 gerada	 a	 partir	 da	 soma	 ponderada
dos	 canais	 de	 cor	 vermelho,	 verde	 e	 azul.	 Nessa	 soma,	 os	 canais
vermelho	e	verde	apresentam	um	peso	(coeficiente	de ponderação)
maior	 quando	 comparado	 ao	 canal	 azul,	justamente	 pelo	fato	 do
olho	humano	ser	mais	sensível	a	essas	cores.
'''