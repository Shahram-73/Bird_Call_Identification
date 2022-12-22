import split_folders
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
split_folders.ratio('./dataset_image/', output="./data", seed=1337, ratio=(.8, .2)) # default valr