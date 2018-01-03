def salt_and_pepper(input_image, salt_and_pepper_amount):
    salt_vs_pepper = 0.5    # 50% Salt/50% Pepper
    
    # Salt mode
    n_salt = np.ceil(salt_and_pepper_amount * input_image.size * salt_vs_pepper)
    random_salt_coordinates = [np.random.randint(0, i-1, int(n_salt)) for i in img.shape]
    salty_image = input_image[random_salt_coordinates] = 1

    # Pepper mode
    n_pepper = np.ceil(salt_and_pepper_amount * input_image.size * (1. - salt_vs_pepper))
    random_pepper_coordinates = [np.random.randint(0, i-1, int(n_pepper)) for i in img.shape]
    salt_and_pepper_image = salty_image[random_pepper_coordinates] = 0
    
    return salt_and_pepper_image
