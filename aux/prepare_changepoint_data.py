"""
Generates a dataset with a changepoint
"""
import numpy as np
import pandas as pd

def gen_changepoint_dataset(mu: list, sigma: list, n: list, seed=2):
    if not (len(mu) == len(sigma) == len(n)):
        raise ValueError("Array length mismatch")

    samples = []
    for i in range(len(mu)):
        samples.append(np.random.normal(mu[i], sigma[i], n[i]))
    return np.concatenate(samples)

def main(output_file = '../data/process_changepoint.csv'):
    mu = [105, 108, 105]
    sigma = [1.5, 1.5, 1.5]
    n = [60, 40, 50]
    X = gen_changepoint_dataset(mu, sigma, n)
    df = pd.DataFrame({'Value': X})
    df.to_csv(output_file, index=None)

if __name__=='__main__':
    main()
