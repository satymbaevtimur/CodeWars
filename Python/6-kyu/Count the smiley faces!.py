def count_smileys(arr):
    count = 0
    valid_eyes = [':', ';']
    valid_noses = ['', '-', '~']
    valid_mouths = [')', 'D']

    for face in arr:
        if (len(face) == 2 and face[0] in valid_eyes and face[1] in valid_mouths) or \
           (len(face) == 3 and face[0] in valid_eyes and face[1] in valid_noses and face[2] in valid_mouths):
            count += 1

    return count
