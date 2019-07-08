from __future__ import print_function

from tensorflow.keras.datasets import mnist
import numpy as np
np.random.seed(10)
from time import time
import numpy as np
import tensorflow.keras.backend as K
from tensorflow.keras.layers import Dense, Input,Layer, InputSpec
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import callbacks
from tensorflow.keras.initializers import VarianceScaling
from sklearn.cluster import KMeans
import metrics


from tensorflow.keras.models import Model
from tensorflow.keras import backend as K
from tensorflow.keras import layers
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Flatten, Reshape, Conv2DTranspose
from tensorflow.keras.models import Model
import numpy as np

#step 1
import tensorflow as tf
import os
import pathlib
data_root_orig = "/home/king/fashion"
data_root = pathlib.Path(data_root_orig)
print(data_root)
all_image_paths = list(data_root.glob('*.jpeg'))
all_image_paths = [str(path) for path in all_image_paths]
filenames = all_image_paths
#labels = [i for i in range(len(filenames))]
#print(labels)



# step 2: create a dataset returning slices of `filenames`
dataset = tf.data.Dataset.from_tensor_slices((filenames, filenames))

# step 3: parse every image in the dataset using `map`
def _parse_function(filename, label):
    image_string = tf.io.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    # This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image_decoded, tf.float32)
    image = tf.image.resize(image, [64, 64])
    return image, image

dataset = dataset.map(_parse_function)
dataset = dataset.batch(32)
dataset = dataset.prefetch(1)



def autoencoderConv2D_1(input_shape=(64, 64, 3), filters=[32, 64, 128, 1000]):
    input_img = Input(shape=input_shape)
    if input_shape[0] % 8 == 0:
        pad3 = 'same'
    else:
        pad3 = 'valid'
    x = Conv2D(filters[0], 5, strides=2, padding='same', activation='relu', name='conv1', input_shape=input_shape)(input_img)

    x = Conv2D(filters[1], 5, strides=2, padding='same', activation='relu', name='conv2')(x)

    x = Conv2D(filters[2], 3, strides=2, padding=pad3, activation='relu', name='conv3')(x)

    x = Flatten()(x)
    encoded = Dense(units=filters[3], name='embedding')(x)
    x = Dense(units=filters[2]*int(input_shape[0]/8)*int(input_shape[0]/8), activation='relu')(encoded)

    x = Reshape((int(input_shape[0]/8), int(input_shape[0]/8), filters[2]))(x)
    x = Conv2DTranspose(filters[1], 3, strides=2, padding=pad3, activation='relu', name='deconv3')(x)

    x = Conv2DTranspose(filters[0], 5, strides=2, padding='same', activation='relu', name='deconv2')(x)

    decoded = Conv2DTranspose(input_shape[2], 5, strides=2, padding='same', name='deconv1')(x)
    return Model(inputs=input_img, outputs=decoded, name='AE'), Model(inputs=input_img, outputs=encoded, name='encoder')
autoencoder, encoder = autoencoderConv2D_1()
autoencoder.summary()
pretrain_epochs = 500
batch_size = 256
autoencoder.compile(optimizer='adadelta', loss='mse')
autoencoder.fit(dataset, epochs=pretrain_epochs)
autoencoder.save_weights(save_dir+'/firstAutoEncoder.h5')
