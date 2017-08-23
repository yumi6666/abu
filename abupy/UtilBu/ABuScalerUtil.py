# -*- encoding:utf-8 -*-
"""
    标准规范化数据工具模块
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import numpy as np
import pandas as pd

__author__ = '阿布'
__weixin__ = 'abu_quant'


def scaler_log10(group):
    """
    对输入的group进行np.log10
        eg.
                pd.DataFrame对象

                input:
                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	223.57	226.50	15.32	12.110	589.02	21.349	97.67
                2014-07-28	224.82	225.80	16.13	12.450	590.60	21.548	99.02
                2014-07-29	225.01	220.00	16.75	12.220	585.61	21.190	98.38
                2014-07-30	228.92	219.13	16.83	11.780	587.42	21.185	98.15

                output:
                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	2.3494	2.3551	1.1853	1.0831	2.7701	1.3294	1.9898
                2014-07-28	2.3518	2.3537	1.2076	1.0952	2.7713	1.3334	1.9957
                2014-07-29	2.3522	2.3424	1.2240	1.0871	2.7676	1.3261	1.9929
                2014-07-30	2.3597	2.3407	1.2261	1.0711	2.7689	1.3260	1.9919

                pd.Series对象

                input:
                2014-07-25    223.57
                2014-07-28    224.82
                2014-07-29    225.01
                2014-07-30    228.92
                2014-07-31    223.30

                output:
                2014-07-25    2.3494
                2014-07-28    2.3518
                2014-07-29    2.3522
                2014-07-30    2.3597
                2014-07-31    2.3489


                np.array

                input:
                array([[ 223.57 ,  226.5  ,   15.32 , ...,  589.02 ,   21.349,   97.67 ],
               [ 224.82 ,  225.8  ,   16.13 , ...,  590.6  ,   21.548,   99.02 ],
               [ 225.01 ,  220.   ,   16.75 , ...,  585.61 ,   21.19 ,   98.38 ],
               ...,
               [ 222.27 ,  160.88 ,   25.5  , ...,  742.74 ,   13.51 ,   98.66 ],
               [ 230.01 ,  160.25 ,   25.57 , ...,  739.77 ,   13.39 ,   97.34 ],
               [ 225.93 ,  163.09 ,   24.75 , ...,  740.92 ,   13.655,   97.76 ]])

               output:
               array([[ 2.3494,  2.3551,  1.1853, ...,  2.7701,  1.3294,  1.9898],
               [ 2.3518,  2.3537,  1.2076, ...,  2.7713,  1.3334,  1.9957],
               [ 2.3522,  2.3424,  1.224 , ...,  2.7676,  1.3261,  1.9929],
               ...,
               [ 2.3469,  2.2065,  1.4065, ...,  2.8708,  1.1307,  1.9941],
               [ 2.3617,  2.2048,  1.4077, ...,  2.8691,  1.1268,  1.9883],
               [ 2.354 ,  2.2124,  1.3936, ...,  2.8698,  1.1353,  1.9902]])

    :param group: pd.DataFrame对象, pd.Series对象, np.array对象
    """
    return np.log10(group)


def scaler_mm(group):
    """
    对输入的group进行(group - group.min()) / (group.max() - group.min())
            eg.
                pd.DataFrame对象

                input:
                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	223.57	226.50	15.32	12.110	589.02	21.349	97.67
                2014-07-28	224.82	225.80	16.13	12.450	590.60	21.548	99.02
                2014-07-29	225.01	220.00	16.75	12.220	585.61	21.190	98.38
                2014-07-30	228.92	219.13	16.83	11.780	587.42	21.185	98.15

                output:
                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	0.5612	0.7979	0.0973	0.9493	0.3396	0.5597	0.1718
                2014-07-28	0.5700	0.7920	0.1305	0.9913	0.3452	0.5699	0.2035
                2014-07-29	0.5713	0.7428	0.1559	0.9629	0.3276	0.5517	0.1885
                2014-07-30	0.5988	0.7354	0.1592	0.9084	0.3340	0.5514	0.1831

                pd.Series对象

                input:
                2014-07-25    223.57
                2014-07-28    224.82
                2014-07-29    225.01
                2014-07-30    228.92
                2014-07-31    223.30

                output:
                2014-07-25    0.5612
                2014-07-28    0.5700
                2014-07-29    0.5713
                2014-07-30    0.5988
                2014-07-31    0.5593


                np.array

                input:
                array([[ 223.57 ,  226.5  ,   15.32 , ...,  589.02 ,   21.349,   97.67 ],
               [ 224.82 ,  225.8  ,   16.13 , ...,  590.6  ,   21.548,   99.02 ],
               [ 225.01 ,  220.   ,   16.75 , ...,  585.61 ,   21.19 ,   98.38 ],
               ...,
               [ 222.27 ,  160.88 ,   25.5  , ...,  742.74 ,   13.51 ,   98.66 ],
               [ 230.01 ,  160.25 ,   25.57 , ...,  739.77 ,   13.39 ,   97.34 ],
               [ 225.93 ,  163.09 ,   24.75 , ...,  740.92 ,   13.655,   97.76 ]])

               output:

                array([[ 0.2838,  0.2876,  0.0141, ...,  0.7571,  0.0219,  0.1207],
                       [ 0.2854,  0.2867,  0.0151, ...,  0.7591,  0.0222,  0.1225],
                       [ 0.2857,  0.2792,  0.0159, ...,  0.7527,  0.0217,  0.1217],
                       ...,
                       [ 0.2821,  0.2026,  0.0273, ...,  0.9561,  0.0117,  0.122 ],
                       [ 0.2921,  0.2018,  0.0274, ...,  0.9523,  0.0116,  0.1203],
                       [ 0.2868,  0.2055,  0.0263, ...,  0.9538,  0.0119,  0.1209]])

    :param group: pd.DataFrame对象, pd.Series对象, np.array对象
    """
    return (group - group.min()) / (group.max() - group.min())


def scaler_std(group):
    """
    对输入的group进行(group - group.mean()) / group.std()
            eg.
                pd.DataFrame对象

                input:
                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	223.57	226.50	15.32	12.110	589.02	21.349	97.67
                2014-07-28	224.82	225.80	16.13	12.450	590.60	21.548	99.02
                2014-07-29	225.01	220.00	16.75	12.220	585.61	21.190	98.38
                2014-07-30	228.92	219.13	16.83	11.780	587.42	21.185	98.15

                output:

                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	-0.1924	1.2047	-1.5325	2.6732	-0.4127	0.4478	-1.1364
                2014-07-28	-0.1435	1.1791	-1.3850	2.8601	-0.3942	0.4860	-1.0202
                2014-07-29	-0.1361	0.9677	-1.2721	2.7337	-0.4525	0.4172	-1.0753
                2014-07-30	0.0169	0.9360	-1.2575	2.4919	-0.4314	0.4163	-1.0951

                pd.Series对象

                input:

                2014-07-25    223.57
                2014-07-28    224.82
                2014-07-29    225.01
                2014-07-30    228.92
                2014-07-31    223.30

                output:

                2014-07-25   -0.1924
                2014-07-28   -0.1435
                2014-07-29   -0.1361
                2014-07-30    0.0169
                2014-07-31   -0.2030


                np.array

                input:
                array([[ 223.57 ,  226.5  ,   15.32 , ...,  589.02 ,   21.349,   97.67 ],
               [ 224.82 ,  225.8  ,   16.13 , ...,  590.6  ,   21.548,   99.02 ],
               [ 225.01 ,  220.   ,   16.75 , ...,  585.61 ,   21.19 ,   98.38 ],
               ...,
               [ 222.27 ,  160.88 ,   25.5  , ...,  742.74 ,   13.51 ,   98.66 ],
               [ 230.01 ,  160.25 ,   25.57 , ...,  739.77 ,   13.39 ,   97.34 ],
               [ 225.93 ,  163.09 ,   24.75 , ...,  740.92 ,   13.655,   97.76 ]])

               output:

                array([[ 0.2497,  0.264 , -0.7675, ...,  2.0348, -0.738 , -0.3652],
                       [ 0.2558,  0.2606, -0.7635, ...,  2.0425, -0.7371, -0.3587],
                       [ 0.2568,  0.2323, -0.7605, ...,  2.0181, -0.7388, -0.3618],
                       ...,
                       [ 0.2434, -0.0565, -0.7178, ...,  2.7857, -0.7763, -0.3604],
                       [ 0.2812, -0.0596, -0.7174, ...,  2.7712, -0.7769, -0.3669],
                       [ 0.2612, -0.0457, -0.7214, ...,  2.7768, -0.7756, -0.3648]])

    :param group: pd.DataFrame对象, pd.Series对象, np.array对象
    """
    return (group - group.mean()) / group.std()


def scaler_matrix(group, type_look='look_max', mean_how=False):
    """
        将二维序列按照 type_look 进行整体数据缩放，把所有数据缩放到一个数量级值上

            eg:
            group:

                        tsla	bidu	noah	sfun	goog	vips	aapl
            2014-07-25	223.57	226.50	15.32	12.110	589.02	21.349	97.67
            2014-07-28	224.82	225.80	16.13	12.450	590.60	21.548	99.02
            2014-07-29	225.01	220.00	16.75	12.220	585.61	21.190	98.38
            2014-07-30	228.92	219.13	16.83	11.780	587.42	21.185	98.15

            if type_look == 'look_max':
                group_max = group.max()
                eg:
                    group_max:

                    tsla    286.04
                    bidu    250.34
                    noah     37.32
                    sfun     12.52
                    goog    776.60
                    vips     30.00
                    aapl    133.00
                max = group_max.max()
                eg:
                    max = 776.60

                scale_factor = max / group_max

                eg:
                    scale_factor:
                    tsla     2.7150
                    bidu     3.1022
                    noah    20.8092
                    sfun    62.0288
                    goog     1.0000
                    vips    25.8867
                    aapl     5.8391

            if type_look == 'look_min':
                group_min = group.min()
                eg:
                    group_min:

                    tsla    143.67
                    bidu    132.37
                    noah     12.95
                    sfun      4.44
                    goog    492.55
                    vips     10.35
                    aapl     90.34
                min = group_min.min()

                eg:
                    min = 4.44
                scale_factor = min / group_min

                eg:
                    scale_factor:

                    tsla    0.0309
                    bidu    0.0335
                    noah    0.3429
                    sfun    1.0000
                    goog    0.0090
                    vips    0.4290
                    aapl    0.0491


            通过计算出来的缩放系数，做个转置后 * 输入group, 如果使用的是look_max:
            eg.
                            tsla	    bidu	    noah	    sfun	    goog	vips	    aapl
                2014-07-25	606.9936	702.6440	318.7972	751.1682	589.02	552.6544	570.3047
                2014-07-28	610.3874	700.4725	335.6527	772.2580	590.60	557.8059	578.1875
                2014-07-29	610.9033	682.4798	348.5544	757.9914	585.61	548.5385	574.4504
                2014-07-30	621.5189	679.7809	350.2191	730.6987	587.42	548.4090	573.1074
            通过计算出来的缩放系数，做个转置后 * 输入group, 如果使用的是look_min:
            eg.
                            tsla	bidu	noah	sfun	goog	vips	aapl
                2014-07-25	6.9092	7.5973	5.2526	12.110	5.3096	9.1584	4.8003
                2014-07-28	6.9479	7.5739	5.5303	12.450	5.3239	9.2438	4.8666
                2014-07-29	6.9537	7.3793	5.7429	12.220	5.2789	9.0902	4.8351
                2014-07-30	7.0746	7.3501	5.7703	11.780	5.2952	9.0881	4.8238
    :param group: pd.DataFrame or np.array
    :param type_look: str对象，type_look in ('look_max', 'look_min)
    :param mean_how: bool, 默认False, 决策group_max或者group_min是使用max，min还是mean
    :return: 缩放后的pd.DataFrame，注意统一格式为pd.DataFrame，不管输入的是什么
    """

    if isinstance(group, list):
        # 如果参数group是list，这里进行转换np.array后做个旋转, 不建议传递list
        group = np.array(group).T

    if isinstance(group, np.ndarray):
        # 把np.ndarray转DataFrame，便统一处理
        group = pd.DataFrame(group)

    # 向前填充na，不能补0，否则如果可视化价格范围就会变大
    group.fillna(method='bfill', inplace=True)

    if type_look == 'look_max':
        # 向较大的序列看齐
        group_max = group.mean(axis=0) if mean_how else group.max(axis=0)
        max_v = group_max.max()
        # 计算出每个序列的放大因子
        scale_factor = max_v / group_max
    elif type_look == 'look_min':
        # 向较小的序列看齐
        group_min = group.mean(axis=0) if mean_how else group.min(axis=0)
        min_v = group_min.min()
        # 计算出每个序列的缩小因子
        scale_factor = min_v / group_min
    else:
        raise ValueError('type_look is error {}'.format(type_look))

    # 通过计算出来的缩放系数，做个转置后 * 输入group, 即为结果缩放后的group
    return scale_factor.T * group


def scaler_xy(x, y, type_look='look_max', mean_how=True):
    """
    只针对俩个输入的均值归一化, 取两个序列的平均值或者最大值后，谁的平均值或者最大值大就被认定为是大序列。
    根据type_look的值，选择向大序列值看齐，还是小序列值看齐，返回的序列中一个将保持不变，另一个被缩放，
    可以被看作是scaler_matrix的特殊情况接口

        eg：
            input x:
                    2014-07-25    223.57
                    2014-07-28    224.82
                    2014-07-29    225.01
                    2014-07-30    228.92
                    2014-07-31    223.30
            input y:
                    2014-07-25    15.32
                    2014-07-28    16.13
                    2014-07-29    16.75
                    2014-07-30    16.83
                    2014-07-31    16.06

            x, y = ABuScalerUtil.scaler_xy(x, y, type_look='look_max', mean_how=False)

            output y:
                    2014-07-25    208.3811
                    2014-07-28    219.3987
                    2014-07-29    227.8318
                    2014-07-30    228.9200
                    2014-07-31    218.4465

            x, y = ABuScalerUtil.scaler_xy(x, y, type_look='look_max', mean_how=True)

            output y:
                    2014-07-25    212.6588
                    2014-07-28    223.9025
                    2014-07-29    232.5088
                    2014-07-30    233.6192
                    2014-07-31    222.9308

            x, y = ABuScalerUtil.scaler_xy(x, y, type_look='look_min', mean_how=False)
            output x:
                    2014-07-25    16.4367
                    2014-07-28    16.5286
                    2014-07-29    16.5425
                    2014-07-30    16.8300
                    2014-07-31    16.4168

            x, y = ABuScalerUtil.scaler_xy(x, y, type_look='look_min', mean_how=True)
            output x:
                    2014-07-25    16.1060
                    2014-07-28    16.1961
                    2014-07-29    16.2098
                    2014-07-30    16.4915
                    2014-07-31    16.0866
    :param x:  pd.Series对象, np.array对象
    :param y: pd.Series对象, np.array对象
    :param type_look: str对象，type_look in ('look_max', 'look_min)
    :param mean_how: 决定是使用平均值还是最大值来决策序列更大
    :return: 缩放后的x，y，pd.Series对象 or np.array
    """

    # 如果是numpy array要先填充nan，否则统计方法的结果都是nan
    if isinstance(x, np.ndarray):
        np.nan_to_num(x)
    if isinstance(y, np.ndarray):
        np.nan_to_num(y)

    x_max = x.mean() if mean_how else x.max()
    y_max = y.mean() if mean_how else y.max()
    if type_look == 'look_max':

        # 向较大的序列看齐
        x, y = (x, x_max / y_max * y) \
            if x_max > y_max else (x * y_max / x_max, y)
    elif type_look == 'look_min':

        # 向较小的序列看齐
        x, y = (x * y_max / x_max, y) \
            if x_max > y_max else (x, y * x_max / y_max)
    else:
        raise ValueError('type_look is error {}'.format(type_look))
    return x, y
