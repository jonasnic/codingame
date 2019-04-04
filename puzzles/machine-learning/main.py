# Reference: https://www.tensorflow.org/versions/r1.0/get_started/mnist/pros
import os
import random
import input_data
import tensorflow as tf

# Removing annoying warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load MNIST Data
mnist = input_data.read_data_sets(raw_input(), raw_input(), raw_input())

# Start TensorFlow InteractiveSession
sess = tf.InteractiveSession()

# Placeholders
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

# Variables
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

sess.run(tf.global_variables_initializer())

# Predicted Class and Loss Function
y = tf.matmul(x, W) + b

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

# Train the Model
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

for _ in range(1000):
    batch = mnist.train.next_batch(100)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})

# Uncomment to get a prediction number for each image
result = sess.run(tf.argmax(y, 1), feed_dict={x: mnist.validation.images})
print(' '.join(map(str, result)))
