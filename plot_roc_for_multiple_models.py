import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255.0

test_labels = to_categorical(test_labels)

# Load Model 1
model1 = tf.keras.models.load_model('model.hdf5')
# Load Model 2
model2 = tf.keras.models.load_model('model2.hdf5')
# Load Model 3
model3 = tf.keras.models.load_model('model3.hdf5')

# Get predictions on the test dataset
y_pred_model1 = model1.predict(test_images)
y_pred_model2 = model2.predict(test_images)
y_pred_model3 = model3.predict(test_images)

# Compute the False Positive Rate (FPR) and True Positive Rate (TPR) for each model
fpr_model1, tpr_model1, _ = roc_curve(test_labels, y_pred_model1)
fpr_model2, tpr_model2, _ = roc_curve(test_labels, y_pred_model2)
fpr_model3, tpr_model3, _ = roc_curve(test_labels, y_pred_model3)

# Compute the Area Under the Curve (AUC) for each model
auc_model1 = auc(fpr_model1, tpr_model1)
auc_model2 = auc(fpr_model2, tpr_model2)
auc_model3 = auc(fpr_model3, tpr_model3)


# Plot the ROC curves
plt.figure(figsize=(8, 6))
plt.plot(fpr_model1, tpr_model1, label='Model 1 (AUC = {:.2f})'.format(auc_model1))
plt.plot(fpr_model2, tpr_model2, label='Model 2 (AUC = {:.2f})'.format(auc_model2))
plt.plot(fpr_model3, tpr_model3, label='Model 3 (AUC = {:.2f})'.format(auc_model3))
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')  # Diagonal line for random classifier
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.show()
