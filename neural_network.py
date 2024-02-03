from keras.models import Sequential
from keras.layers import Activation,Dropout,Flatten,Conv2D,MaxPool2D,Dense
from keras.preprocessing.image import ImageDataGenerator


class Pintoil_Model:

    def __init__(self,input_shape=(200,200,3), filters=33, kernel_size=(3,3), activation=['relu','sigmoid','softmax'], pool_size=(2,2),dense_layer_hiden=128, dense_layer_output=2,droup_layer=0.5):
        self.input_shape = input_shape
        self.filters = filters
        self.kernel_size = kernel_size
        self.activation = activation
        self.pool_size = pool_size
        self.dense_layer_hiden = dense_layer_hiden
        self.dense_layer_output = dense_layer_output
        self.droup_layer = droup_layer

    def model_architecture(self):
        model = Sequential()

        model.add(Conv2D(filters=self.filters,kernel_size=self.kernel_size,input_shape=self.input_shape,activation=self.activation[0]))
        model.add(MaxPool2D(pool_size=self.pool_size))

        model.add(Conv2D(filters=self.filters, kernel_size=self.kernel_size, input_shape=self.input_shape,
                         activation=self.activation[0]))
        model.add(MaxPool2D(pool_size=self.pool_size))

        model.add(Conv2D(filters=self.filters, kernel_size=self.kernel_size, input_shape=self.input_shape,
                         activation=self.activation[0]))
        model.add(MaxPool2D(pool_size=self.pool_size))

        model.add(Flatten())

        model.add(Dense(self.dense_layer_hiden))
        model.add(Activation(self.activation[0]))

        model.add(Dropout(self.droup_layer))

        model.add(Dense(self.dense_layer_output))
        model.add(Activation(self.activation[1]))

        model.compile(loss='binary_crossetropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        return model

    def save_model(self,model_name='pintoil'):
        model=self.model_architecture()
        model.save(f'{model_name}.h5')

    def model_summary(self):
        model = self.model_architecture()
        print(model.summary())

    @staticmethod
    def images_data_generator(rotation_range=30, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.2, zoom_range=0.2, fill_node='nearest'):
        image_generator=ImageDataGenerator(rotation_range=rotation_range,
                                           width_shift_range=width_shift_range,
                                           height_shift_range=height_shift_range,
                                           rescale=1/255,
                                           shear_range=shear_range,
                                           zoom_range=zoom_range,
                                           horizontal_flip=True,
                                           fill_mode=fill_node)
        return image_generator

    def images_generator(self,images_path,batch_size=15,class_mode='binary'):
        images_generate = self.images_data_generator()
        image_generator_results=images_generate.flow_from_directory(images_path=images_path,target_size=self.input_shape[:2],batch_size=batch_size,class_mode=class_mode)
        return image_generator_results


    def model_results(self,train_images_generator,test_images_generator,epochs=5,step_per_epochs=150, validation_step=10):
        results=self.model_architecture().fit_generator(train_images_generator=train_images_generator,epochs=epochs,step_per_epochs=step_per_epochs,validation_data=test_images_generator,validation_steps=validation_step)
        return results

