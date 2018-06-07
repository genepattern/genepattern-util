def minimum_edit_distance(s1, s2):
    """
    This function computes a distance between two stings
    From: https://rosettacode.org/wiki/Levenshtein_distance#Python
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


def extract_classes(list_of_strings, number_of_classes=2, affinity='euclidean'):
    """
    This function will apply clustering to get representative classes
    and will return a list/array with numeric identifiers for each sample.
    Adapted from here:
    https://stats.stackexchange.com/questions/123060/clustering-a-long-list-of-strings-words-into-similarity-groups
    """
    import numpy as np
    import sklearn.cluster

    words = np.asarray(list_of_strings)  # So that indexing with a list will work
    lev_similarity = -1 * np.array([[minimum_edit_distance(w1, w2) for w1 in words] for w2 in words])
    affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
    affprop.fit(lev_similarity)
    list_of_numbers = np.array(affprop.labels_)
    return list_of_numbers.astype('str')


def assign_label(sample, classes, case_sensitive):
    """
    This simplistic function will go through each class in order,
    it stops once it finds a class which is contained in the sample string.
    """
    label = '__no_class__'
    flag = 'go'
    for current_class in classes:
        if flag == 'go':
            if case_sensitive:
                if current_class in sample:
                    label = current_class
                    flag = 'stop'
            else:
                if current_class.lower() in sample.lower():
                    label = current_class.lower()
                    flag = 'stop'
    return label


def str_list_2_num(str_list):
    """
    Take a list of strings to correlative numbers
    """
    import numpy as np

    classes = np.unique(str_list)
    num_list = []
    #     print(classes)
    for current_string in str_list:
        num = 0
        flag = 'go'
        for current_class in classes:
            if flag == 'go':
                if current_class == current_string:
                    num_list.append(num)
                    flag = 'stop'
                num += 1
    return np.array(num_list)


def list_2_cls(input_list, name_of_out='output.cls', sep='\t'):
    """
    This function creates a CLS file from a list-like object
    Copied and modified from Cuzcatlan
    """
    import numpy as np

    cls = open(name_of_out, 'w')
    cls.write("{}{}{}{}1\n".format(len(input_list), sep, len(np.unique(input_list)), sep))
    cls.write("#{}{}\n".format(sep, sep.join(np.unique(input_list).astype(str))))
    num_list = str_list_2_num(input_list)
    cls.write(sep.join(num_list.astype(str)) + '\n')
    #     print(sep.join(input_list.astype(str)))
    #     print(num_list)
    cls.close()


def make_cls(df, name, classes=None, case_sensitive=False, sep='\t'):
    """
    This function creates a CLS file from the column names of a GCT file
    """
    import numpy as np

    if classes is None:
        classes = extract_classes(list(df.columns))

    labels = []
    for sample in list(df.columns):
        labels.append(assign_label(sample, classes, case_sensitive))

    # Now that we have a list of labels, we turn these into a numeric list:
    if not name.endswith('.cls'):
        name += '.cls'
    name = name.replace(' ', '_')  # Simple reformatting, in case there were any spaces
    list_2_cls(np.array(labels), name_of_out=name, sep=sep)

    return name