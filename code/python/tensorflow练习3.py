import tensorflow as tf
state=tf.Variable(0,name='counter')
print(state.name)
one=tf.constant(1)
new_value=tf.add(state,one)
updata=tf.assign(state,new_value)
init=tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        sess.run(updata)
        print(sess.run(state))