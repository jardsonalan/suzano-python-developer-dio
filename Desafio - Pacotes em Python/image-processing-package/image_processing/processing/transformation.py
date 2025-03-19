from skimage.transform import resize

# NOTE: Função para fazer a transformação apenas de uma imagem
def resize_image(image, proportion):
    assert 0 <= proportion <= 1, 'Especifique uma proporção válida entre 0 e 1.'
    height = round(image.shape[0] * proportion) # Pega a altura da imagem
    width = round(image.shape[1] * proportion) # Pega a largura da imagem
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized