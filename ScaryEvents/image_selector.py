import random

def pick_random_image(image_weights):
    
    images = list(image_weights.keys())
    weights = list(image_weights.values())
    
    # random.choices bir liste döndürür, bu yüzden [0] ile içindeki metni alıyoruz
    picked_image = random.choices(images, weights=weights, k=1)[0]
    return picked_image