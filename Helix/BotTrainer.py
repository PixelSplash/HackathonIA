import os
import numpy as np
import pandas as pd
from scipy.misc import imread
from sklearn.metrics import accuracy_score
import tensorflow as tf
import random

# To stop potential randomness
seed = 128
rng = np.random.RandomState(seed)

root_dir = os.path.abspath('../..')
data_dir = os.path.join(root_dir, 'data')
sub_dir = os.path.join(root_dir, 'sub')

# check for existence
os.path.exists(root_dir)
os.path.exists(data_dir)
os.path.exists(sub_dir)


train = []
train_x = []
train_y = []
val_x = []
val_y = []

f = open("DatosPosicion.txt","r", encoding="utf8")
content = f.readlines()
content = [x.strip() for x in content]

i = 0

for line in content:
    line = line.split()
    if(len(line) == 10):
        for j in range(10):
            
            line[j] = float(line[j])
            if(line[j] > 100):
                line[j] = 0.0
            
        train.append((line,0))
    else:
        for j in range(2):
            line[j] = float(line[j])
        if(line[2] == 'False'):
            line[2] = 0.0
        else:
            line[2] = 1.0
        
        train[i] = (train[i][0],line)
        i+=1             

for x in train:
    train_x.append(x[0])
    train_y.append(x[1])

split_size = int(len(train_x)*0.7)

train_x, val_x = train_x[:split_size], train_x[split_size:]
train_y, val_y = train_y[:split_size], train_y[split_size:]


#sample_submission = pd.read_csv(os.path.join(data_dir, 'Sample_Submission.csv'))



def dense_to_one_hot(labels_dense, num_classes=10):
    """Convert class labels from scalars to one-hot vectors"""
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    
    return labels_one_hot

def preproc(unclean_batch_x):
    """Convert values to range 0-1"""
    temp_batch = unclean_batch_x / unclean_batch_x.max()
    
    return temp_batch

def batch_creator(batch_size, dataset_length, dataset_name):
    """Create batch with random samples and return appropriate format"""

    batch_x = []
    batch_y = []
    i=0
    for i in range(0,batch_size):
        num = random.randrange(0,dataset_length)
        batch_x.append(eval(dataset_name + '_x')[num])

        #batch_x = preproc(batch_x)
        batch_y.append(eval(dataset_name + '_y')[num])
        
    return batch_x, batch_y







### set all variables

# number of neurons in each layer
input_num_units = 10
hidden_num_units = 5
output_num_units = 3

# define placeholders
x = tf.placeholder(tf.float32, [None, input_num_units])
y = tf.placeholder(tf.float32, [None, output_num_units])

# set remaining variables
epochs = 7
learning_rate = 0.05

### define weights and biases of the neural network (refer this article if you don't understand the terminologies)

weights = {
    'hidden': tf.Variable(tf.random_normal([input_num_units, hidden_num_units], seed=seed)),
    'output': tf.Variable(tf.random_normal([hidden_num_units, output_num_units], seed=seed))
}

biases = {
    'hidden': tf.Variable(tf.random_normal([hidden_num_units], seed=seed)),
    'output': tf.Variable(tf.random_normal([output_num_units], seed=seed))
}

hidden_layer = tf.add(tf.matmul(x, weights['hidden']), biases['hidden'])
hidden_layer = tf.nn.relu(hidden_layer)

output_layer = tf.matmul(hidden_layer, weights['output']) + biases['output']

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y, logits = output_layer))

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

#train_step = tf.train.GradientDescentOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    # create initialized variables
    sess.run(init)
    
    ### for each epoch, do:
    ###   for each batch, do:
    ###     create pre-processed batch
    ###     run optimizer by feeding batch
    ###     find cost and reiterate to minimize
    
    for epoch in range(epochs):
        avg_cost = 0
        #_,c = sess.run(train_step, feed_dict = {x: train_x, y: train_y})

        _,c = sess.run([optimizer, cost], feed_dict = {x: train_x, y: train_y})
            
        avg_cost = c
            
        print ("Epoch:", (epoch+1), "cost =", "{:.5f}".format(avg_cost))
    
    print ("\nTraining complete!")
    
    
    # find predictions on val set
    pred_temp = tf.equal(tf.argmax(output_layer, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(pred_temp, "float"))
    print ("Validation Accuracy:", accuracy.eval({x: val_x, y: val_y}))


    data = sess.run(output_layer, {x:train_x})
    for x in range(20):
        print(data[x+100]/10)
        print(train_y[x+100])
        print("---------------")
