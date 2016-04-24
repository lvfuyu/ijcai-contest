############################################################################
#
# Copyright (c) 2016 ICT MCG Group, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:

Authors: zhouxing(@ict.ac.cn)
Date:    2016/04/24 16:21:21
File:    get_user_merchant_feature.py
"""
import sys


def main():
    user_loc_m_fea = {}
    koubei_file = sys.argv[1]
    feature_file = sys.argv[2]
    with open(koubei_file) as f:
        for line in f:
            user, merchant, loc, ts = line.rstrip().split(',')
            # init`
            user_loc_m_fea.setdefault(user, {})
            user_loc_m_fea[user].setdefault(loc, {})
            user_loc_m_fea[user][loc].setdefault(merchant, {'cnt':0})
            # update feature
            user_loc_m_fea[user][loc][merchant]['cnt'] += 1
    # gen feature
    fres = open(feature_file, 'w')
    for user, loc_m_fea in user_loc_m_fea.items():
        user_action_cnt = 0 # total actions
        user_m_visit = 0 # cnt of visited merchant
        user_loc_visit = len(loc_m_fea) # cnt of visited location
        loc_actions = {} # actions in each location
        merchant_actions = {} #actions in each merchant
        for loc, m_fea in loc_m_fea.items():
            user_m_visit += len(m_fea)
            loc_actions[loc] = 0 # actions in eaah location
            for merchant, fea in m_fea.items():
                user_action_cnt += fea['cnt']
                loc_actions[loc] += fea['cnt']
                merchant_actions.setdefault(merchant, 0)
                merchant_actions[merchant] += fea['cnt']

        # gen feature
        fea_list = [user_action_cnt, user_m_visit, user_loc_visit]
        for loc, m_fea in loc_m_fea.items():
            for merchant, fea in m_fea.items():
                fres.write(user+','+merchant+','+loc + '\t' + ' '.join([str(val) for val in fea_list]) + ' ' + str(loc_actions[loc]) +' '+ str(merchant_actions[merchant]) + ' ' +str(fea['cnt'])+ '\n')

    fres.close()

if __name__ == '__main__':
    main()
# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
