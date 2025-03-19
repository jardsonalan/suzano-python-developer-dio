import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

# NOTE: Função para achar a diferença de duas imagens
def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Especificar 2 imagens com mesmo shape."
    gray_image1 = rgb2gray(image1) # Conversão para tons de cinza
    gray_image2 = rgb2gray(image2) # Conversão para tons de cinza
    (score, diferrence_image) = structural_similarity(gray_image1, gray_image2, full=True) # Serve para achar o score, valor de similaridade de 0 a 1
    print('Similaridade das imagens: ', score)
    normalized_difference_image = (diferrence_image-np.min(diferrence_image))/(np.max(diferrence_image)-np.min(diferrence_image)) # Normaliza a diferença da imagem
    return normalized_difference_image

def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image