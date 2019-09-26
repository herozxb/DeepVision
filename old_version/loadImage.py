from __future__ import print_function

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
labels = [i for i in range(len(filenames))]
print(labels)



# step 2: create a dataset returning slices of `filenames`
dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))

# step 3: parse every image in the dataset using `map`
def _parse_function(filename, label):
    image_string = tf.io.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    # This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image_decoded, tf.float32)
    image = tf.image.resize(image, [64, 64])
    return image, label

dataset = dataset.map(_parse_function)
dataset = dataset.batch(1)
dataset = dataset.prefetch(1)

for i,j in dataset:
    try:
        tf.print(i)
    except:
        print("bad image")

















