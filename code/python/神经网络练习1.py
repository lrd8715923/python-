import tensorflow as tf
import numpy as np
import add_layer as al
import matplotlib.pyplot as plt
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1],name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1],name='y_input')
l1 = al.addlayer(xs, 1, 10,n_layer=1,activation_function=tf.nn.relu)
prediction = al.addlayer(l1, 10, 1,n_layer=2, activation_function=None)
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    tf.summary.scalar('loss',loss)
with tf.name_scope('train'): 
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init=tf.initialize_all_variables()
sess=tf.Session()
merged=tf.summary.merge_all()
writer = tf.summary.FileWriter("C:\code\python", sess.graph)
sess.run(init)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()
plt.show()
for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        result=sess.run(merged,feed_dict={xs:x_data,ys:y_data})        
        writer.add_summary(result,i)       
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value=sess.run(prediction,feed_dict={xs:x_data})
        lines=ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(0.5)
