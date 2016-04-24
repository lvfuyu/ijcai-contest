# @brief: merge all feature
# author: zhouxing

import sys

def load_id_feature(filename):
    id_index_fea = {}
    with open(filename) as f:
        for line in f:
            name, nid_fea = line.rstrip().split('\t')
            nid, fea = nid_fea.split(' ', 1)
            id_index_fea[name] = {'index':0, 'fea':''}
            id_index_fea[name]['index'] = int(nid)
            id_index_fea[name]['fea'] = fea
    return id_index_fea

def main():
    uml_file = sys.argv[1]
    merchant_fea_file = sys.argv[2]
    location_fea_file = sys.argv[3]
    merge_feature = sys.argv[4]
    f_merge = open(merge_feature, 'w')
    # load location & merchant feature
    location_feature = load_id_feature(location_fea_file)
    merchant_feature = load_id_feature(merchant_fea_file)
    loc_len = len(location_feature)
    merchant_len = len(merchant_feature)
    with open(uml_file) as f:
        for line in f:
            uml, tuple_fea = line.rstrip().split('\t')
            uid, mid, lid = uml.split(',')
            fea_list = tuple_fea.split()  # u_m_l feature
            fea_list += merchant_feature[mid]['fea'].split() # merchant feature
            fea_list += location_feature[lid]['fea'].split() # location feature
            basic_feature_len = len(fea_list) - 1
            mid_findex = basic_feature_len + merchant_feature[mid]['index']
            loc_findex = basic_feature_len + merchant_len + location_feature[lid]['index']
            f_merge.write(uml + '\t' + ' '.join(['%d:%s'%(i, fea_list[i]) for i in
                range(len(fea_list))])
                    + ' ' + str(mid_findex) + ':1 ' + str(loc_findex) + ':1' + '\n')
    f_merge.close()


if __name__ == '__main__':
    main()
# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
