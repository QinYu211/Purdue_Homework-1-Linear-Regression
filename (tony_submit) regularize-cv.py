{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'Ridge' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-614bd698b31e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    116\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    117\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 118\u001b[1;33m     \u001b[0mmodel_best\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    119\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmodel_best\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcoef_\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    120\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmodel_best\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mintercept_\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-28-614bd698b31e>\u001b[0m in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m     34\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m         \u001b[1;31m#Evaluate the MSE on the test set\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 36\u001b[1;33m         \u001b[0mmse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0merror\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_test\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my_test\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mmodel\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     37\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     38\u001b[0m         \u001b[1;31m#Store the model and mse in lists for further processing\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-28-614bd698b31e>\u001b[0m in \u001b[0;36merror\u001b[1;34m(X, y, model, l)\u001b[0m\n\u001b[0;32m    104\u001b[0m     \u001b[0mreg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlinear_model\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mRidge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0malpha\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    105\u001b[0m     \u001b[0mmodel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mreg\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 106\u001b[1;33m     \u001b[0my_pred\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmodel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    107\u001b[0m     \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    108\u001b[0m     \u001b[0msummation\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'Ridge' object is not callable"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import Ridge\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import linear_model\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "def main():\n",
    "    #Importing dataset\n",
    "    diamonds = pd.read_csv('diamonds.csv')\n",
    "\n",
    "    #Feature and target matrices\n",
    "    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]\n",
    "    y = diamonds[['price']]\n",
    "\n",
    "    #Training and testing split, with 25% of the data reserved as the test set\n",
    "    X = X.to_numpy()\n",
    "    y = y.to_numpy()\n",
    "    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)\n",
    "\n",
    "    #Normalizing training and testing data\n",
    "    [X_train, trn_mean, trn_std] = normalize_train(X_train)\n",
    "    X_test = normalize_test(X_test, trn_mean, trn_std)\n",
    "\n",
    "    #Define the range of lambda to test\n",
    "    lmbda = np.logspace(-1, 2, num=101) # Lambda Values Needed for Submission\n",
    "\n",
    "    MODEL = []\n",
    "    MSE = []\n",
    "    for l in lmbda:\n",
    "        #Train the regression model using a regularization parameter of l\n",
    "        model = train_model(X_train,y_train,l)\n",
    "\n",
    "        #Evaluate the MSE on the test set\n",
    "        mse = error(X_test,y_test,model,l)\n",
    "\n",
    "        #Store the model and mse in lists for further processing\n",
    "        MODEL.append(model)\n",
    "        MSE.append(mse)\n",
    "\n",
    "    #Plot the MSE as a function of lmbda\n",
    "    #Fill in\n",
    "    plt.show()\n",
    "#     print(MODEL)\n",
    "#     print(MSE)\n",
    "    \n",
    "    #Find best value of lmbda in terms of MSE\n",
    "    ind =  min(MSE) #Fill in\n",
    "    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]\n",
    "\n",
    "    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))\n",
    "\n",
    "    return model_best\n",
    "\n",
    "\n",
    "#Function that normalizes features in training set to zero mean and unit variance.\n",
    "#Input: training data X_train\n",
    "#Output: the normalized version of the feature matrix: X, the mean of each column in\n",
    "#training set: trn_mean, the std dev of each column in training set: trn_std.\n",
    "def normalize_train(X_train):\n",
    "\n",
    "    mean = np.mean(X_train, axis = 0)\n",
    "    std = np.std(X_train, axis = 0)\n",
    "    \n",
    "    X = (X_train - mean) /std\n",
    "\n",
    "    return X, mean, std\n",
    "\n",
    "\n",
    "#Function that normalizes testing set according to mean and std of training set\n",
    "#Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each\n",
    "#column in training set: trn_std\n",
    "#Output: X, the normalized version of the feature matrix, X_test.\n",
    "def normalize_test(X_test, trn_mean, trn_std):\n",
    "\n",
    "    #Fill in(done)\n",
    "    mean = np.mean(X_test, axis = 0)\n",
    "    std = np.std(X_test, axis = 0)\n",
    "    \n",
    "    X = (X_test - mean) /std\n",
    "\n",
    "    return X\n",
    "\n",
    "\n",
    "#Function that trains a ridge regression model on the input dataset with lambda=l.\n",
    "#Input: Feature matrix X, target variable vector y, regularization parameter l.\n",
    "#Output: model, a numpy object containing the trained model.\n",
    "def train_model(X,y,l):\n",
    "\n",
    "    #Fill in\n",
    "    reg = linear_model.Ridge(alpha=l)\n",
    "    model = reg.fit(X,y)\n",
    "    \n",
    "    return model\n",
    "\n",
    "\n",
    "#Function that calculates the mean squared error of the model on the input dataset.\n",
    "#Input: Feature matrix X, target variable vector y, numpy model object\n",
    "#Output: mse, the mean squared error\n",
    "def error(X,y,model,l):\n",
    "\n",
    "    #Fill in\n",
    "    reg = linear_model.Ridge(alpha=l)\n",
    "    model = reg.fit(X,y)\n",
    "    y_pred = model(X,y,l)\n",
    "    n = len(y)\n",
    "    summation = 0\n",
    "    for i in range (0,n):  #looping through each element of the list\n",
    "        difference = y_pred[i] - y[i]  #finding the difference between observed and predicted value\n",
    "        squared_difference = difference**2  #taking square of the differene \n",
    "        summation = summation + squared_difference\n",
    "    mse = summation/n\n",
    "    \n",
    "    return mse\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    model_best = main()\n",
    "    print(model_best.coef_)\n",
    "    print(model_best.intercept_)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
