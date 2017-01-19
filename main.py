import logging
import sys
from datetime import datetime

import tensorflow as tf

'''
1. import `Video` and `save_video` from the correct module of package "styler"
'''
from ... import Video
from ... import save_video


model_file = 'data/vg-30.pb'
model_name = 'vg-30'
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO,
    datefmt='%I:%M:%S')


def main():

    with open(model_file, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def)
        graph = tf.get_default_graph()

    with tf.Session(config=tf.ConfigProto(
            intra_op_parallelism_threads=4)) as session:

        logging.info("Initializing graph")
        session.run(tf.global_variables_initializer())

        image = graph.get_tensor_by_name("import/%s/image_in:0" % model_name)
        out = graph.get_tensor_by_name("import/%s/output:0" % model_name)
        shape = image.get_shape().as_list()

        '''
        2. set the `path` to  your input
        '''
        with Video(...) as v:
            frames = v.read_frames(image_h=shape[1], image_w=shape[2])

        logging.info("Processing image")
        start_time = datetime.now()

        '''
        3. Write a list comprehension to iterate through all frames,
           and make it be processed by Tensorflow.
        '''
        processed = [
            session.run(out, feed_dict={image: [frame]})
            ...
        ]

        '''
        4. Pass the results as a argument into function
        '''
        save_video('result.mp4',
                   fps=30, h=shape[1], w=shape[2],
                   frames=...)

        logging.info("Processing took %f" % (
            (datetime.now() - start_time).total_seconds()))
        logging.info("Done")


if __name__ == '__main__':
    main()
