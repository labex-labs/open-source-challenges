# Conclusion

In this lab, we learned how to use Gaussian process regression with noise-level estimation in Python, using the scikit-learn library. We generated some data with a single feature using a sine function, added some noise to the generated data to create a more realistic training dataset, and visualized the generated data. We created a Gaussian process regressor using an additive kernel adding a RBF and WhiteKernel kernels, and visualized the predictions made by the Gaussian process regressor. We also inspected the Log-Marginal-Likelihood (LML) of GaussianProcessRegressor for different hyperparameters to get a sense of the local minima.