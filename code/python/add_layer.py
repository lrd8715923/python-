import tensorflow as tf
def addlayer(inputs, in_size, out_size,n_layer, activation_function=None):
    layer_name='layer%s'% n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]),name='W')
            tf.summary.histogram(layer_name + '/weights', Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_Plus_b'):
            Wx_Plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_Plus_b
        else:
            outputs = activation_function(Wx_Plus_b)
            tf.summary.histogram(layer_name + '/biases', biases)
        return outputs
