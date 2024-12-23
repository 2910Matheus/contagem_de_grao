# Documentação do Processo Realizado para o Projeto

## Contexto do Projeto
Este projeto foi desenvolvido como parte de um processo seletivo para vaga de estágio da TCX visão computacional. O objetivo era segmentar grãos em imagens com base em suas cores (“marrom”, “branco” e “rosa”), realizar uma contagem de cada cor e gerar relatórios detalhados, utilizando ferramentas de visão computacional com a biblioteca OpenCV.

O desafio também incluía a geração de imagens segmentadas com os grãos destacados, além de calcular a área média dos grãos de cada cor.

---

## Linha do Tempo do Desenvolvimento

### **Segunda-feira (16/12):**
Recebi o projeto e comecei a me organizar. Li os requisitos do desafio e pesquisei sobre as ferramentas principais necessárias para realização do trabalho.

### **Terça e Quarta-feira:**
Realizei um curso na **Alura** para consolidar meu conhecimento sobre OpenCV e visão computacional. Este curso foi um dos poucos que aparentava agregar algo ao desafio, com ele obtive ideias e os fundamentos técnicos da biblioteca e aplicar.
- **Curso realizado:** Certificado do Curso de Visão Computacional com OpenCV
(https://cursos.alura.com.br/user/matheusmaia2910/course/analise-classificacao-faces-visao-computacional-opencv/certificate)


### **Quinta e Sexta-feira:**
Assisti a vídeos-aula para complementar o aprendizado. Abaixo, os links das fontes utilizadas:
1. [Python + OpenCV: Processamento de imagens do zero](https://www.youtube.com/watch?v=oAH_GJclePY&list=PL-t7zzWJWPtx3enns2ZAV6si2p9zGhZJX)
2. [Técnicas de segmentação com OpenCV](https://www.youtube.com/watch?v=PMspTfswXvc)

Estes materiais me ajudaram a aprofundar meu entendimento sobre as técnicas de segmentação e manipulação de cores no espaço HSV, além de boas práticas na utilização de OpenCV.

### **Sábado e Domingo:**
Iniciei o desenvolvimento do projeto.
- Construi as funções principais para carregar imagens, converter para o espaço HSV e realizar a segmentação.
- Realizei testes iniciais com diferentes faixas de cores para ajustar os parâmetros de segmentação e filtrar ruídos.

### **Domingo para Segunda-feira:**
Estruturei o repositório Git. Organizei os arquivos em uma estrutura clara e adicionei documentações detalhadas, incluindo este arquivo e o README do projeto.

---

## Pontos Positivos e Aprendizados
Durante o desenvolvimento, identifiquei diversos pontos positivos que contribuíram para meu aprendizado:

- **Familiaridade com OpenCV:** Aprendi a manipular o espaço HSV para segmentação de cores e a utilizar contornos para isolar regiões de interesse em imagens.
- **Boas práticas de organização:** O curso e os vídeos me ajudaram a estruturar o código de forma modular, facilitando a manutenção e a expansão futura.
- **Processo iterativo:** Desenvolvi melhor minha habilidade de testar, ajustar e validar resultados conforme avançava no trabalho.
- **Utilização de ferramentas adicionais:** Usei o **GIMP** para identificar valores de HSV diretamente de amostras na imagem, o que foi fundamental para ajustar os intervalos de cor de forma mais precisa.

### Valores de HSV obtidos com o GIMP
- **Fundo:**
  **Valores HSV**
  - [124   9 219]
  - [120  10 213]
  - [125   7 218]
  - [125   7 219]
  - [133   8 218]
  - [125   7 211]
  - [125   7 207]
  - [125   7 207]
  - [130  11 205]
  - [132   6 206]
- **Branco:**
  **Valores HSV**
  - [132   6 218]
  - [125   7 221]
  - [120   9 218]
  - [165   2 208]
  - [ 36   7 191]
  - [165   3 183]
  - [126   7 194]
  - [120   3 191]
- **Marrom:**
   **Valores HSV**
  - [14 75 44]
  - [ 16 103  37]
  - [ 13 163  25]
  - [11 65 55]
  - [16 52 74]
- **Rosa:**
  **Valores HSV**
  - [  8  92 149]
  - [  7 109 143]
  - [  8 104 160]
  - [  8  75 173]
  - [  9 101 141]

---

## Desafios Encontrados
O principal desafio foi a **detecção da cor branca**. Como o branco está muito próximo de valores claros no espaço HSV, foi difícil definir uma faixa que fosse precisa sem incluir ruídos do fundo. Algumas tentativas que tentei ao longo do processo foram: 
- Criar bordas nos objetos para tentar identificar eles já que geravam uma sombra.
- Criar uma detecção para o fundo e até mesmo tentar alterar o tom de fundo.
- Tentar aperfeiçoar a imagem com filtros e ajustes na iluminação.

Ao final através de algumas tentativas e erros resolvi adotar a seguinte técnica:
Ajustar iterativamente os limites inferiores e superiores, além de aplicar filtros para reduzir interferências.
A contagem ainda não se aproximou do resultado esperado, continuei com empecilho da cor, mas resolvi seguir com esse projeto até mesmo para futuros aprendizados, aonde eu com uma base mais profunda possa retornar e realizar o desafio de uma forma que consiga solucionar esse problema que enfrentei..

---

## Conclusão
Este projeto foi uma excelente oportunidade para consolidar meus conhecimentos em visão computacional e boas práticas em desenvolvimento. A experiência não apenas me preparou melhor para desafios futuros na área, mas também reforçou minha organização e capacidade de aprendizado autônomo.

Estou confiante de que a experiência adquirida será útil não apenas para este processo seletivo, mas também para minha carreira como desenvolvedor.

