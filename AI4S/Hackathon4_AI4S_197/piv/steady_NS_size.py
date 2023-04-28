"""
while true; do python steady_NS_size.py --save_path='./data/test_size';done
"""

from steady_NS import *

if __name__ == "__main__":
    idx = 0
    last_idx = get_last_idx(path.joinpath('result.csv'))
    idx = last_idx + 1
    executed_flag = False
    for r in range(repeat):
        for noise_type in ['contamined', 't1', 'normal']:
            for noise in [0.20]:
                for abnormal_ratio in [0]:
                    for N in [200, 400, 600, 800, 1000]:
                        _data = []
                        abnormal_size = int(N * abnormal_ratio)
                        if executed_flag:
                            sys.exit()
                        for weight in [1E-0]:
                            if idx > last_idx:
                                run_experiment(idx, N=N, noise=noise, noise_type=noise_type, weight=weight,
                                               loss_type='l1', _data=_data, abnormal_size=abnormal_size)
                                # executed_flag = True
                            idx += 1
                            if idx > last_idx:
                                run_experiment(idx, N=N, noise=noise, noise_type=noise_type, weight=weight,
                                               loss_type='square', _data=_data, abnormal_size=abnormal_size)
                                # executed_flag = True
                            idx += 1
    if executed_flag:
        sys.exit()
    for r in range(repeat):
        for noise_type in ['outlinear']:
            for noise in [0.0]:
                for abnormal_ratio in [0.20]:
                    for N in [1000, 800, 600, 400, 200]:
                        _data = []
                        abnormal_size = int(N * abnormal_ratio)
                        if executed_flag:
                            sys.exit()
                        for weight in [1E-0]:
                            if idx > last_idx:

                                run_experiment(idx, N=N, noise=noise, noise_type=noise_type, weight=weight,
                                               loss_type='l1', _data=_data, abnormal_size=abnormal_size)
                                # executed_flag = True
                            idx += 1
                            if idx > last_idx:

                                run_experiment(idx, N=N, noise=noise, noise_type=noise_type, weight=weight,
                                               loss_type='square', _data=_data, abnormal_size=abnormal_size)
                                # executed_flag = True
                            idx += 1
    if executed_flag:
        sys.exit()
    for r in range(repeat):
        for noise_type in ['outlinear']:
            for noise, abnormal_ratio in zip([0.20], [0.20]):
                for N in [1000, 800, 600, 400, 200]:
                    _data = []
                    abnormal_size = int(N * abnormal_ratio)
                    if executed_flag:
                        sys.exit()
                    for weight in [1E-0]:
                        if idx > last_idx:

                            run_experiment(idx, N=N, noise=noise, noise_type=noise_type, weight=weight,
                                           loss_type='l1', _data=_data, abnormal_size=abnormal_size)
                            # executed_flag = True
                        idx += 1
                        if idx > last_idx:

                            run_experiment(idx, N=N, noise=noise, noise_type=noise_type, weight=weight,
                                           loss_type='square', _data=_data, abnormal_size=abnormal_size)
                            # executed_flag = True
                        idx += 1
    if executed_flag:
        sys.exit()

    time.sleep(1)
