from src import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
with tf.Session() as sess:
    print("a=2, b=3")
    print("Addition with constants: %i" % sess.run(a+b))
    print("Multiplication with constants: %i" % sess.run(a*b))
    print(tf.get_default_graph())
writer = tf.summary.FileWriter("/log",tf.get_default_graph())
writer.close()