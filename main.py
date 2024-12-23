import cv2
import numpy as np
import os

# Caminho da pasta de imagens
image_folder = r"C:\\caminho\\para\\Imagens_questao1"

faixas_cores = {
    "branco": ([115, 0, 200], [135, 15, 230]),
    "marrom": ([8, 50, 10], [22, 255, 100]),
    "rosa": ([6, 60, 100], [12, 160, 200]),
}

def carregar_imagem(caminho_imagem):
    """
    Carrega uma imagem do caminho especificado e a converte do espaço BGR para HSV.

    Parâmetros:
        caminho_imagem (str): Caminho completo para a imagem.

    Retorno:
        tuple: Um par contendo:
            - imagem (numpy.ndarray): A imagem original no espaço BGR.
            - imagem_hsv (numpy.ndarray): A imagem convertida para o espaço HSV.

    Exceções:
        FileNotFoundError: Caso a imagem não seja encontrada no caminho especificado.
    """
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        raise FileNotFoundError(f"Imagem não encontrada: {caminho_imagem}")
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    return imagem, imagem_hsv

def segmentar_por_cor(imagem_hsv, faixas_cores):
    """
    Segmenta uma imagem HSV com base em faixas de cores fornecidas, identificando contornos válidos.

    Parâmetros:
        imagem_hsv (numpy.ndarray): Imagem no espaço de cores HSV.
        faixas_cores (dict): Dicionário contendo faixas de cores no formato:
                             {nome_cor: ([limite_inferior], [limite_superior])}.

    Retorno:
        tuple: Um triplo contendo:
            - contagem_cores (dict): Contagem de contornos válidos por cor.
            - area_media (dict): Área média dos contornos válidos por cor.
            - imagem_segmentada (numpy.ndarray): Imagem com os contornos desenhados.

    Observação:
        Apenas contornos com área maior que 100 pixels são considerados válidos.
    """
    contagem_cores = {}
    area_media = {}
    imagem_segmentada = np.zeros_like(imagem_hsv)

    for cor, (limite_inferior, limite_superior) in faixas_cores.items():
        limite_inferior = np.array(limite_inferior, dtype=np.uint8)
        limite_superior = np.array(limite_superior, dtype=np.uint8)
        mascara = cv2.inRange(imagem_hsv, limite_inferior, limite_superior)

        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos_validos = [c for c in contornos if cv2.contourArea(c) > 100]  # Ajuste da área mínima
        contagem_cores[cor] = len(contornos_validos)
        area_total = sum(cv2.contourArea(c) for c in contornos_validos)
        area_media[cor] = area_total / len(contornos_validos) if contornos_validos else 0

        cor_rgb = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        for c in contornos_validos:
            cv2.drawContours(imagem_segmentada, [c], -1, cor_rgb, -1)

    return contagem_cores, area_media, imagem_segmentada

def salvar_imagem_segmentada(caminho_saida, imagem_segmentada):
    """
    Salva uma imagem segmentada no caminho especificado.

    Parâmetros:
        caminho_saida (str): Caminho completo onde a imagem segmentada será salva.
        imagem_segmentada (numpy.ndarray): Imagem segmentada a ser salva.

    Retorno:
        None
    """
    cv2.imwrite(caminho_saida, imagem_segmentada)

def processar_imagens():
    """
    Processa múltiplas imagens de uma pasta, realiza a segmentação por cor e gera um relatório.

    Etapas:
        1. Para cada imagem:
            - Carregar a imagem e convertê-la para HSV.
            - Realizar a segmentação com base nas faixas de cor.
            - Salvar a imagem segmentada.
            - Registrar os resultados (contagem de grãos e áreas médias).
        2. Gerar um relatório consolidado com os resultados de todas as imagens.

    Retorno:
        None
    """
    resultados_completos = {}

    for i in range(1, 16):
        nome_imagem = f"img{i}.jpg"
        caminho_imagem = os.path.join(image_folder, nome_imagem)

        if os.path.exists(caminho_imagem):
            try:
                imagem, imagem_hsv = carregar_imagem(caminho_imagem)
                contagem, areas, imagem_segmentada = segmentar_por_cor(imagem_hsv, faixas_cores)

                resultados_completos[nome_imagem] = {"contagem": contagem, "areas": areas}

                caminho_saida_imagem = os.path.join(image_folder, f"segmentada_{nome_imagem}")
                salvar_imagem_segmentada(caminho_saida_imagem, imagem_segmentada)
            except Exception as e:
                print(f"Erro ao processar {nome_imagem}: {e}")
        else:
            print(f"Imagem {nome_imagem} não encontrada no caminho fornecido.")

    caminho_relatorio = os.path.join(image_folder, "relatorio.txt")
    with open(caminho_relatorio, "w") as arquivo_relatorio:
        for nome_imagem, dados in resultados_completos.items():
            arquivo_relatorio.write(f"{nome_imagem}:\n")
            for cor, contagem in dados["contagem"].items():
                area_media = dados["areas"][cor]
                arquivo_relatorio.write(f"  {cor.capitalize()}: {contagem} grãos, Área Média: {area_media:.2f}\n")
            arquivo_relatorio.write("\n")

    print(f"Processamento concluído. Relatório salvo em {caminho_relatorio}")

if __name__ == "__main__":
    processar_imagens()
