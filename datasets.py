from sklearn import preprocessing
import numpy as np
import pandas as pd


def get_data(name="power"):

    if name == "power":
        return get_power_data()
    elif name == "communities":
        return get_communities_data()
    else:
        return None


def get_power_data():
    """
    Read the Individual household electric power consumption dataset
    """

    data = pd.read_csv('data/household_power_consumption.txt',
                       sep=';', low_memory=False)

    # Drop some non-predictive variables
    data = data.drop(columns=['Date', 'Time'], axis=1)

    print(data.head())

    # Replace missing values
    data = data.replace('?', np.nan)

    # Drop NA
    data = data.dropna(axis=0)

    # Normalize
    standard_scaler = preprocessing.StandardScaler()
    np_scaled = standard_scaler.fit_transform(data)
    data = pd.DataFrame(np_scaled)

    # Goal variable assumed to be the first
    return data.values[:, 1:].astype('float32'), \
        data.values[:, 0].astype('float32')


def get_communities_data():
    """
    Read the Communities and Crime dataset
    """

    data = None

    with open('data/communities.names', 'r') as f:
        columns = [x.split(' ')[1] for x in f.readlines() if "@attribute" in x]
        data = pd.read_csv('data/communities.data', names=columns)

        # Drop some non-predictive variables
        data = data.drop(columns=['state', 'county',
                                  'community', 'communityname',
                                  'fold'], axis=1)

        # Replace missing values
        data = data.replace('?', np.nan)

        # Drop NA
        data = data.dropna(axis=1)

        # Goal variable assumed to be the last
        return data.values[:, :-1], data.values[:, -1]

    return data
