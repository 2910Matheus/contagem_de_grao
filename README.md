# Segmentação e Contagem de Grãos por Cor (Visão Computacional - OpenCV)

## Descrição do Problema
Este projeto utiliza a biblioteca OpenCV para realizar a segmentação de grãos em imagens fornecidas. O objetivo é identificar os grãos com base em suas cores (marrom, branco e rosa), contar a quantidade de grãos de cada cor e calcular a área média de cada grão segmentado.  

O programa gera uma imagem segmentada com os grãos classificados por cor e um relatório contendo os resultados da análise.  

---
# Questão 1: Segmentação e Contagem de Grãos por Cor (Visão Computacional OpenCV)

### Descrição do Problema
Utilizando a pasta de imagens fornecida, desenvolva um programa que faça a segmentação dos grãos com base em suas cores. O programa deve contar o número de grãos de cada cor (marrom, branco e rosa) e exibir os resultados.

### Requisitos Técnicos
- Utilize a biblioteca **OpenCV** para segmentação.
- O programa deve:
  - Gerar uma imagem segmentada com os grãos classificados por cor.
  - Imprimir ou salvar um relatório com a contagem de grãos de cada cor.

### Desafios Adicionais (Opcional)
- Implemente um sistema para lidar com grãos sobrepostos ou parcialmente segmentados.
- Calcule a área média dos grãos de cada cor.
- 
---

## Funcionalidades
- Segmentação de grãos por cores utilizando faixas HSV.
- Contagem do número de grãos de cada cor.
- Cálculo da área média dos grãos segmentados.
- Geração de imagens segmentadas com os contornos desenhados.
- Relatório detalhado com a contagem e a área média dos grãos por cor.  

---
## Estrutura do Projeto

```
├── README.MD: Contém a explicação e apresentação do projeto.
├── main.py: Contém o código principal para processamento das imagens.
├── Imagens_questao1: Pasta contendo as imagens a serem processadas.
   └── Imagens_segmentadas: Pasta contendo as imagens já processadas.
├── relatorio.txt: Arquivo de saída gerado após o processamento, contendo os resultados.  
├── requirements.txt: Arquivo contendo o requirementos das ferramentas utilizadas.  
└── Nota.MD: Explicação, cronograma e notas dos passos para realizar o projeto.
```
---

## Como Executar o Projeto
### Pré-requisitos
1. **Python 3.7 ou superior** instalado.
2. Bibliotecas necessárias:
   - OpenCV: `pip install opencv-python`
   - NumPy: `pip install numpy`

### Passos para Execução
1. **Clone ou baixe este repositório.**
2. **Coloque as imagens fornecidas na pasta `Imagens_questao1/`.**
3. **Edite o caminho para a pasta de imagens no arquivo `main.py`**, ajustando a variável `image_folder`:
   ```python
   image_folder = r"C:\\caminho\\para\\Imagens_questao1"
4. **Execute o script principal: `python main.py`**

# Tecnologias Utilizadas
- `Python`
- `OpenCV`
- `Numpy`
- `Gimp`



