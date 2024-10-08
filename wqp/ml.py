# It will be the definition of our model, as a Scikit-Learn pipeline

from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline


def build_wine_predictor_model():

    model = Pipeline(steps=[
        ('regression', ElasticNet(alpha=1.0, l1_ratio=0.5, fit_intercept=True))
    ])
    return model
