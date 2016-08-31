import bottleneck as bn


def reduce_functions():
    return func_dict()['reduce']


def move_functions():
    return func_dict()['move']


def nonreduce_functions():
    return func_dict()['nonreduce']


def nonreduce_axis_functions():
    return func_dict()['nonreduce_axis']


def all_functions():
    a = []
    funcs = func_dict()
    for key in funcs:
        for func in funcs[key]:
            a.append(func)
    return a


def func_dict():
    d = {}
    d['reduce'] = [bn.nansum,
                   bn.nansum2,
                   bn.nanmean,
                   bn.nanmean2,
                   bn.nanstd,
                   bn.nanstd2,
                   bn.nanvar,
                   bn.nanvar2,
                   bn.nanmin,
                   bn.nanmin2,
                   bn.nanmax,
                   bn.nanmax2,
                   bn.median,
                   bn.median2,
                   bn.nanmedian,
                   bn.nanmedian2,
                   bn.ss,
                   bn.ss2,
                   bn.nanargmin,
                   bn.nanargmin2,
                   bn.nanargmax,
                   bn.nanargmax2,
                   bn.anynan,
                   bn.anynan2,
                   bn.allnan,
                   bn.allnan2,
                   ]
    d['move'] = [bn.move_sum,
                 bn.move_sum2,
                 bn.move_mean,
                 bn.move_mean2,
                 bn.move_std,
                 bn.move_std2,
                 bn.move_var,
                 bn.move_var2,
                 bn.move_min,
                 bn.move_min2,
                 bn.move_max,
                 bn.move_max2,
                 bn.move_argmin,
                 bn.move_argmin2,
                 bn.move_argmax,
                 bn.move_argmax2,
                 bn.move_median,
                 bn.move_median2,
                 bn.move_rank,
                 bn.move_rank2,
                 ]
    d['nonreduce'] = [bn.replace]
    d['nonreduce_axis'] = [bn.partsort,
                           bn.partsort2,
                           bn.argpartsort,
                           bn.argpartsort2,
                           bn.rankdata,
                           bn.nanrankdata,
                           bn.push,
                           ]
    return d
