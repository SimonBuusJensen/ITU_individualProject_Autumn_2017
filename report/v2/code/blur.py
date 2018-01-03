def average_filtering_blur(input_image, kernel_size):
    kernel = numpy.ones(shape=(kernel_size, kernel_size), dtype=np.float32) 
    avg_kernel = kernel / (kernel_size ** 2)
    blurry_image = cv2.filter2D(src=input_image, ddepth=-1, kernel=avg_kernel)
    return blurry_image
