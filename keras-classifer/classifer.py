import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

# return the best three results


def top_n(matrix_prob, label_map):
	ans = []
	for line in matrix_prob:
		rank = [label_map[item[0]] for item in sorted(enumerate(line), key=lambda v:v[1], reverse=True)]
		ans.append(rank[:3])
	return ans
# basic neural network model


def basic_model():
	model = Sequential()
	model.add(Dense(output_dim=600, input_dim=100, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(output_dim=42, input_dim=600, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


if __name__ == '__main__':

	X_pre = pd.read_csv('train_mean_x.txt', header=None, encoding='utf-8')
	Y = pd.read_csv('y_train1.txt', header=None, encoding='utf-8')
	X_test = pd.read_csv('test_370.txt', header=None, encoding='utf-8')

	matrix_y = np_utils.to_categorical(Y,42)
	# KerasClassifier analysis
	classifier = KerasClassifier(build_fn=basic_model, nb_epoch=10, batch_size=600)
	classifier.fit(X_pre, Y)

	pred_prob = classifier.predict_proba(X_test)

	with open('SMPCUP2017_LabelSpace_Task2.txt', encoding='gbk') as flabel:
		label_map = flabel.read().split()
	pd.DataFrame(top_n(pred_prob, label_map)).to_csv('FINALRESULT.txt', index=None, header=None, encoding='utf-8')


