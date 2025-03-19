from skimage.io import imread, imsave

# NOTE: Função que serve para ler a imagem
def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

# NOTE: Função que serve para escrever a imagem
def save_image(image, path):
    imsave(path, image)