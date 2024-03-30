import numpy as np
from sklearn import linear_model, metrics
from sklearn.model_selection import GridSearchCV
from scipy.linalg import khatri_rao

# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y_train ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to train your model using training CRPs
	# X_train has 32 columns containing the challenge bits
	# y_train contains the responses
	
	# THE RETURNED MODEL SHOULD BE A SINGLE VECTOR AND A BIAS TERM
	# If you do not wish to use a bias term, set it to 0
    # print(len(X_train))
	X_train_mapped = np.array([my_map(X_train[i]) for i in range(len(X_train))])
	# print(X_train_mapped)
	y_train = np.array(y_train)
	y_train = 2*y_train - 1
	print(y_train)
      
	# Define ElasticNet model
	el_clf = linear_model.ElasticNet(alpha = 0.0171, l1_ratio=0.47)
	el_clf.fit(X_train_mapped, y_train)
    
	w = el_clf.coef_
	b = el_clf.intercept_
	
	#print(w.shape, b.shape, clf.n_iter_)

	#test_data = np.genfromtxt('test.dat', delimiter=' ', dtype=None)
	#X_test = test_data[:,:-1]
	#y_test = test_data[:,-1]
	#y_test = 2*y_test - 1
	#X_test_mapped = np.array([my_map(X_test[i]) for i in range(len(X_test))])
	
	#y_pred = el_clf.predict(X_test_mapped); y_pred = np.array([sign(y_pred[i]) for i in range(len(y_pred))])
	# Evaluate the model
	#accuracy = metrics.accuracy_score(y_test, y_pred)
	#conf_matrix = metrics.confusion_matrix(y_test, y_pred)

	#print(f"Accuracy Test: {accuracy}")
	#print(f"Confusion Matrix Test:\n{conf_matrix}")
      
	#y_pred = el_clf.predict(X_train_mapped); y_pred = np.array([sign(y_pred[i]) for i in range(len(y_pred))])
	# Evaluate the model
	#accuracy = metrics.accuracy_score(y_train, y_pred)
	#conf_matrix = metrics.confusion_matrix(y_train, y_pred)
	
	#print(f"Accuracy Train: {accuracy}")
	#print(f"Confusion Matrix Train:\n{conf_matrix}")

	return w, b


################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
	X = np.array(X) 
	  
	if X.ndim == 1:
		d = 1 - 2 * X
		t = np.ones(32)
		t = np.cumprod(d[::-1])[::-1]
		matrix = np.triu(np.outer(t, t),1)
		feat = matrix[np.triu_indices(matrix.shape[0],1)]
		feat = np.concatenate((feat, t))
		del t, d, matrix
    
	else:
        
		for i in range(len(X)):
			d = 1 - 2 * X[i]
			t = np.ones(32)
			t = np.cumprod(d[::-1])[::-1]
			matrix = np.triu(np.outer(t, t),1)
			matrix = matrix[np.triu_indices(matrix.shape[0],1)]
			matrix = np.concatenate((matrix, t))
			if i == 0:
				feat = matrix
			else:
				feat = np.vstack((feat, matrix))
			del t, d, matrix 
	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
	
	return feat

#train_data = np.genfromtxt('train.dat', delimiter=' ', dtype=None)
#X_train = train_data[:,:-1]
# print(X_train.shape)
#y_train = train_data[:,-1]
#w,b = my_fit(X_train, y_train)
#print(b)

#num = 0 
#for i in range(len(w)):
#	if w[i] != 0:
#		num+=1
#print(num)


