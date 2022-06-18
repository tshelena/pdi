# PDI

### Aplicando filtros de imagem.

#### Imagem Original:

![image](https://user-images.githubusercontent.com/54648687/174456652-195f48c5-fbf8-4a44-9458-dbea2e5f3cc3.png)



#### 1. Filtro de Média

Esse filtro é do grupo passa baixas e é um filtro linear. Substitui cada pixel pela média aritmética dos pixels
da vizinhança. Pode ter diversos tamanhos de máscaras.

Imagem após aplicação do filtro:
  
![image](https://user-images.githubusercontent.com/54648687/174442293-1ca2f5ea-edb1-4d07-bfe7-95067c56ec81.png)


#### 2. Filtro de Mediana

Este filtro também é do grupo passa baixas, porém, é um filtro não lienar. Substitui a intensidade de cada pixel
pela mediana das intensidades na vizinhança do pixel. Também pode ter diversos tamanhos de máscaras.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442301-1379f1a6-3329-4068-9307-e0f2b7c69888.png)

#### 3. Filtro de Moda

Este filtro também é do grupo passa baixas e não linear. Seleciona o valor que ocorre com
maior frequência na vizinhança para substituir o valor do pixel central.

Imagem após aplicação do filtro:

#### 4.	Filtro de Robert 

Este filtro possui a fórmula mais simples na detecção de bordas, mas tem uma grande desvantagem, na diferença de realce em algumas bordas da imagem, relacionado aos pontos de cinza. É não linear.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174456522-7ac2c2f5-1f4e-4a76-8628-b6ca598bdfc5.png)


#### 5.	Filtro de Sobel

Este filtro detecta bordas horizontais e verticais separadamente em uma imagem em escalas-de-cinza. As cores da imagem são transformadas de RGB para escalas-de-cinza. O resultado é uma imagem transparente com linhas pretas e alguns restos de cores.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442311-efb1592a-6384-4b41-a81b-55dfc9f89674.png)


#### 6.	Filtro Negativo

Este filtro subtrai de cada pixel -255, o que dá a exata cor "oposta" a original do pixel, assim gerando a imagem negativa.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442315-f663eccd-d89c-486e-b25b-da6d68aa6e7f.png)


#### 7. Filtro Gaussiano

Este filtro é um filtro passa-baixo usado para reduzir o ruído (componentes de alta frequência) e borrar as regiões de uma imagem, ou ela por completo.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442353-9d9eb58c-9329-4309-82cd-dba996829264.png)


#### 8.	Filtro Laplace

Este filtro não exige processamento individual horizontal e vertical, é linear e é um filtro que implementa uma derivada de segunda ordem da imagem, dessa forma detectando regiões de alta variação de cor, ou seja, bordas. É comumente utilizado em combinação com o filtro Gaussiano.

Imagem após aplicação do filtro:


![image](https://user-images.githubusercontent.com/54648687/174442361-6461f4ac-e82d-4f78-84eb-290741c01ed3.png)


#### 9.	Filtro Prewitt

Este filtro também é um detector de borda. Tem o mesmo conceito do de Sobel (sem o peso para o pixel mais central) e de Roberts (sua máscara abrange uma área de 3 x 3)

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174456513-1b76e7b6-a1c2-4e65-b757-4514e56d9393.png)


#### 10.	Filtro Binário

Este filtro altera toda a imagem para tons preto e branco conforme o valor de corte escolhido sendo determinado, em ambos os casos, pela tonalidade do objeto em estudo tornando possível separar na imagem duas classes: objeto e fundo.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442556-d8ed6938-e6bd-4b0b-a391-74f633d21bba.png)


#### 11.	Filtro Binário Invertido

Este filtro funciona exatamente igual ao Filtro Binário, apenas invertendo na imagem o que é branco, por preto e vice-versa.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442564-0da64827-b038-4955-9c11-b18991e311c9.png)

#### 12.	Filtro de Trunc

Nste filtro o pixel de destino é definido para o limite (thresh), se o valor do pixel de origem for maior que o limite. Caso contrário, é definido para o valor do pixel de origem. O maxValue é ignorado

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442573-a115e2f1-e686-48cc-ba5e-45dbfd102a2b.png)


#### 13.	Filtro de Tozero

Neste filtro O valor do pixel de destino é definido como o valor do pixel da origem correspondente , se o valor do pixel de origem for maior que o limite. Caso contrário, é definido como zero.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442581-77130688-5600-4885-803b-697dae8b2971.png)

#### 14.	Filtro de Tozero Invertido

Neste filtro O valor do pixel de destino é definido como zero, se o valor do pixel de origem for maior que o limite. Caso contrário, é definido para o valor do pixel de origem.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442587-632ebae5-c0be-40be-a008-07437613c70e.png)


#### 15.	Filtro Sharpen

Este filtro aguça as bordas dos elementos sem aumentar o ruído ou defeito. É o um dos melhores filtros de nitidez.

Imagem após aplicação do filtro:

![image](https://user-images.githubusercontent.com/54648687/174442644-891f96fc-1271-4598-b847-c93f50ff8128.png)


#### 16.	Normalizar duas imagens filtradas

Normalizar as imagens significa transformá-las em valores tais que a média e o desvio padrão da imagem se tornem 0,0 e 1,0, respectivamente. Para fazer isso, primeiro a média do canal é subtraída de cada canal de entrada e, em seguida, o resultado é dividido pelo desvio padrão do canal.

Imagem original / Imagem normalizada:

![image](https://user-images.githubusercontent.com/54648687/174457595-7343ad7e-0af5-4941-8684-226ef769b503.png)
![image](https://user-images.githubusercontent.com/54648687/174457515-12367f7a-d853-4882-9044-8c91446ac2b9.png)


Imagem com filtro Sobel / Imagem normalizada após a aplicação do filtro Sobel:

![image](https://user-images.githubusercontent.com/54648687/174457602-fd88da6b-ac0b-4776-9e63-c8f9d893d5db.png)
![image](https://user-images.githubusercontent.com/54648687/174457525-311da95f-8cc2-4372-84b5-2f7ec46413e4.png)


Imagem com filtro Negativo / Imagem normalizada após a aplicação do filtro Negativo:
![image](https://user-images.githubusercontent.com/54648687/174457615-3ad2562d-6ab6-4462-a7a5-4a90964350c6.png)![image](https://user-images.githubusercontent.com/54648687/174457623-be907206-1be3-4444-9be8-5b3562b4b019.png)





