import tensorflow as tf

sess = tf.Session()
tf.train.import_meta_graph(r"E:\dien\script\dnn_save_path\ckpt_noshuffDNN3--100.meta")
tf.summary.FileWriter("log", sess.graph)
sess.close()
