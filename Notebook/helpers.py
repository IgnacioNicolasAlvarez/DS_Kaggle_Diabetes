def get_limits_mean_std(data):
    max_v = data.mean() + 2.5 * data.std()
    min_v = data.mean() - 2.5 * data.std()
    return max_v, min_v 

