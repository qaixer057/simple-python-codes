# https://www.delftstack.com/howto/python/plot-roc-curve-python/
import scikitplot.plotters as skplt
import matplotlib.pyplot as plt

print("ROC Curve for Testing Data")
preds = clf_voting.predict_proba(X_test)
skplt.plot_roc_curve(y_test, preds)
plt.savefig("ROC for Testing.png")
plt.show()
