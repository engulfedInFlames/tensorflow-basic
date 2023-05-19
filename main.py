import tensorflow as tf
import numpy as np


def my_print(tensor):
    print("Datatype of every element: ", tensor.dtype)
    print("Number of dimensions (rank): ", tensor.ndim)
    print("Shape of tensor: ", tensor.shape)
    print("Elements along the 0 axis: ", tensor.shape[0])
    print("Elements along the last axis: ", tensor.shape[-1])
    print("Total number of elements in our tensor: ", tf.size(tensor))
    print("Total number of elements in our tensor: ", tf.size(tensor).numpy())


# pip install tensorflow-directml
