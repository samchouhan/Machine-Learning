#This is the basic example of Linear Regression model 
#It comes under superwised learning 
#The training set you feed to the algorithm includes the desired solutions called LABLES


from sklearn.linear_model import LinearRegression

# Training data
# Input: hours studied
X = [[1], [2], [3], [4], [5], [6]]

# Output: exam scores
y = [20, 30, 40, 50, 60, 70]

# Create the machine learning model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict the score for a student who studies 7 hours
prediction = model.predict([[7]])

print("Predicted exam score:", prediction[0])
