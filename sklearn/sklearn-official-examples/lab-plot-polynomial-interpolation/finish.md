# Summary

In this lab, we learned how to approximate a function with polynomials up to a certain degree using ridge regression. We showed two different ways of doing this given `n_samples` of 1d points `x_i`. We used `make_pipeline` function to add non-linear features and demonstrated how these transformers are well-suited to model non-linear effects with a linear model. We plotted the function, training points, and the interpolation using polynomial features and B-splines. We also plotted all columns of both transformers separately and showed the knots of spline. Finally, we demonstrated the use of periodic splines.