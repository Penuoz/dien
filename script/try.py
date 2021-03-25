import tensorflow as tf

# sess = tf.Session()
# tf.train.import_meta_graph(r"E:\dien\script\dnn_save_path\ckpt_noshuffDIEN3--100.meta")
# tf.summary.FileWriter("log", sess.graph)
# sess.close()

a = tf.get_variable('a', [4,2])
b = tf.reshape(a, [-1, 1])
# b = tf.nn.embedding_lookup(a, [[[0,1], [2,4]]])
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(a))
    print(sess.run(b))
    # print(sess.run(tf.reduce_sum(b, 1)))