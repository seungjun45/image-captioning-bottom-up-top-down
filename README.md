<h1> Image captioning using Bottom-up, Top-down Attention</h1>

# this is a python3.0 (for generating hdf files) version of : https://github.com/poojahira/image-captioning-bottom-up-top-down


<h2> Requirements </h2>

python 3.6<br>
torch 0.4.1<br>
h5py 2.8<br>
tqdm 4.26<br>
nltk 3.3<br>

<h2> Data preparation </h2>

Download the MSCOCO <a target = "_blank" href="http://images.cocodataset.org/zips/train2014.zip">Training</a> (13GB)  and <a href=http://images.cocodataset.org/zips/val2014.zip>Validation</a> (6GB)  images. 

Also download Andrej Karpathy's <a target = "_blank" href=http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip>training, validation, and test splits</a>. This zip file contains the captions.

Unzip all files and place the folders in directory you want (you need to change the file directory names in 'address_server_caption.py'.)

<br>

Next, download the bottom up image features : <a target = "_blank" href="https://imagecaption.blob.core.windows.net/imagecaption/trainval_36.zip"> train_val <a target = "_blank" href="https://imagecaption.blob.core.windows.net/imagecaption/test2014_36.zip"> test </a>.

Unzip the folder and place unzipped folder in any folder (you need to change the file directory names in 'address_server_caption.py'.)

<br>

Next type this command in a python 3 environment: 
```bash
python bottom-up_features/tsv.py
```

```bash
python bottom-up_features/tsv_test.py
```


This command will create the following files - 
<ul>
<li>An HDF5 file containing the bottom up image features for train, val, and test splits, 36 per image for each split, in an I, 36, 2048 tensor where I is the number of images in the split.</li>
<li>PKL files that contain training and validation image IDs mapping to index in HDF5 dataset created above.</li>
</ul>

Move these files to the folder (any directory you want, just change the 'address_server_caption.py').
