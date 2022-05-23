import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3, 8),
    tf.keras.layers.SimpleRNN(7),
    tf.keras.layers.Dense(6)
])
model.summary()
