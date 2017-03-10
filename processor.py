# NEURAL NET PROCESSOR
import tensorflow as tf

sess = tf.InteractiveSession()

# MODEL
x = tf.placeholder(tf.float32, shape=[None, 10])
y_ = tf.placeholder(tf.float32, shape=[None, 2])

W = tf.Variable(tf.zeros([10, 2]))
b = tf.Variable(tf.zeros([2]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

# TRAINING
y_ = tf.placeholder(tf.float32, [None, 2])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)