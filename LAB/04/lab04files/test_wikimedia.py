import wikimedia
images = wikimedia.find_images('Eiffel Paris France',4) 

images[0].show() ## view the first image in the returned list
images[1].show() ## view the first image in the returned list
images[2].show() ## view the third image in the returned list
images[3].show() ## view the fourth image in the returned list
