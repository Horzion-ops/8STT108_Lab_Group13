import pandas as pd
import numpy as np
import statsmodels.api as sm


df = pd.read_csv('data_Labo4.csv', sep=';')
df['has_satell'] = (df['satell'] > 0).astype(int)


X1 = sm.add_constant(df['width'])
y1 = df['has_satell']
logit_model_width = sm.Logit(y1, X1)
logit_result_width = logit_model_width.fit()
print(logit_result_width.summary())


glm_model_width = sm.GLM(y1, X1, family=sm.families.Binomial())
glm_result_width = glm_model_width.fit()
print(glm_result_width.summary())


width_25 = np.array([1, 25])
log_odds_25 = logit_result_width.predict(width_25)
print(f"Log odds for 25 cm shell width: {log_odds_25}")


probability_25 = 1 / (1 + np.exp(-log_odds_25))
print(f"Probability of having satellites for 25 cm shell width: {probability_25}")

X2 = sm.add_constant(df['weight'])
logit_model_weight = sm.Logit(y1, X2)
logit_result_weight = logit_model_weight.fit()
print(logit_result_weight.summary())


beta0, beta1 = logit_result_weight.params
print(f"Regression equation: log(p / (1 - p)) = {beta0} + {beta1} * weight")


weight_2000 = np.array([1, 2000])
log_odds_2000 = logit_result_weight.predict(weight_2000)
probability_2000 = 1 / (1 + np.exp(-log_odds_2000))
print(f"Probability of having satellites for 2000g weight: {probability_2000}")
