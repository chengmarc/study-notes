# ----- Getting General Statistics -----
x = c(4.00, 5.26, 4.84, 6.77, 5.23, 5.64, 3.84, 6.43, 3.35, 4.28)
x_bar = mean(x)
s_squared <- var(x)
s <- sqrt(s_squared)
cat("\n", "Mean is: ", x_bar, "\n", "S is :", s, "\n", "S Squared (Variance) is: ", s_squared)

# ----- Plotting - Normal Distribution -----
mean = 0
standard_deviation = 1
x_values = seq(mean-3*standard_deviation, mean+3*standard_deviation, by=.01)
y_values = dnorm(x_values, mean, standard_deviation)
plot(x_values, y_values)
 
# ----- Plotting T Distribution -----
mean = 20
degree_of_freedom = 20
default = seq(-5, 5, by=.01)
x_values = seq(mean-5, mean+5, by=.01)
y_values = dt(default, degree_of_freedom)
plot(x_values, y_values)

# ----- Plotting Chi-squared Distribution -----
degree_of_freedom = 2
x_values = seq(0, degree_of_freedom^1.5+5, by=.01)
y_values = dchisq(x_values, degree_of_freedom)
plot(x_values, y_values)

# ----- Plotting F Distribution -----
degree_of_freedom_1 = 30
degree_of_freedom_2 = 40
x_values = seq(0, 5, by=.01)
y_values = df(x_values, degree_of_freedom_1, degree_of_freedom_2)
plot(x_values, y_values)

# ----- CI for Normal Distribution -----
percentile = 0.1
mean = 0
standard_deviation = 1
qnorm(percentile, mean=mean, sd=standard_deviation) 

# ----- CI for T Distribution -----
percentile = 0.025
degree_of_freedom = 46
qt(percentile, df=degree_of_freedom)

# ----- CI for Chi-squared Distribution -----
lower_percentile = 0.95
upper_percentile = 0.95
degree_of_freedom = 9
qchisq(lower_percentile, df=degree_of_freedom)
qchisq(upper_percentile, df=degree_of_freedom)

# ----- CI for F Distribution -----
percentile = 0.975
degree_of_freedom_1 = 24
degree_of_freedom_2 = 22
qf(percentile, df1=degree_of_freedom_1, df2=degree_of_freedom_2)

# ----- P-value for Normal Distribution -----
z_score = 1.98
mean = 0
standard_deviation = 1
pnorm(z_score, mean=mean, sd=standard_deviation) 

# ----- P-value for T Distribution -----
t_score = 0.95
degree_of_freedom = 2
pt(t_score, df=degree_of_freedom)

# ----- P-value for Chi-squared Distribution -----
chi_score = 0.95
degree_of_freedom = 2
pchisq(chi_score, df=6)

# ----- P-value for F Distribution -----
f_score = 9.5
degree_of_freedom_1 = 2
degree_of_freedom_2 = 2
pf(f_score, df1=degree_of_freedom_1, df2=degree_of_freedom_2)


theta = 0.3
x = rand
x = duniq(min = 0, max = theta)