from sklearn import svm
import numpy as np
import os
import pickle
# trained on an vague dataset to check if working
data = np.genfromtxt("ourfile.txt",dtype="str",delimiter=",")
X=data[:, 0:3]
print("X-------",X)
Y=data[:, 3]
print("y-------",Y)
model = svm.SVC(kernel='rbf')
model.fit(X,Y)
classifier_filename = os.path.expanduser("E:\college\project traffic\SavedModels\SVMmodel.sav")
print("Trained model saved as SVMmodel in SavedModels")
outfile= open(classifier_filename,'wb')
pickle.dump(model,outfile)




