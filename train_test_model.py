from neural_network import *

# HERE I DECLARED THE INITAL ML MODEL
model = Pintoil_Model()

# HERE I AM GOIN TO GENERATE THE IMAGES
path_train_data = './dataset1/train'
path_test_data = "./dataset1/test"

data_train_generate = model.images_generator(path_train_data)
data_test_generate = model.images_generator(path_test_data)
print(data_train_generate.class_indices)

# HERE I WILL TRAIN ADN EVALUATE THE MODEL AT THE SAME TIME
results_model = model.model_results(data_train_generate,data_test_generate)

image_process1= model.image_test_transformation('/Users/pintojav/Downloads/dog_test_image.jpg')
image_process2= model.image_test_transformation('/Users/pintojav/Downloads/famale_engineer.jpg')

model_23=model.model_architecture().predict(image_process1)
model_27=(model.model_architecture().predict(image_process1) > 0.5).astype("int32")

print(model_23)
print(model_27)