import numpy as np
import pandas as pd

fgp = __import__('FaST-GP')

def make_ls_data(lengthscale, n_obs, n_sim):
    # X = np.random.uniform(size=(n_obs, 1), low=0, high=100)
    X = np.linspace(0, 100, n_obs)[:, None]
    K = fgp.SE_kernel(X, lengthscale)
    I = np.eye(n_obs)

    exp_tab = pd.DataFrame(index=range(n_obs))
    names = ['GP{}'.format(i) for i in range(n_sim)]
    true_values = pd.DataFrame(index=names, columns=['mu', 's2_t', 's2_e'])

    for g in names:
        # mu = 0 * np.random.uniform(low=0., high=100.)
        s2_t = np.exp(np.random.uniform(low=-10., high=10.))
        # s2_e = np.exp(np.random.uniform(low=-5., high=5.))
        s2_e = 1.0

        y = np.random.multivariate_normal(np.zeros((n_obs,)), (s2_t * K + s2_e * I))
    
        exp_tab[g] = y
        # true_values.loc[g, 'mu'] = mu
        true_values.loc[g, 's2_t'] = s2_t
        true_values.loc[g, 's2_e'] = s2_e

    return X, exp_tab, true_values
