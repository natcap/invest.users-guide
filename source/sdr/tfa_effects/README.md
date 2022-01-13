# script and data used to generate the image `tfa_effects.png`

The image `tfa_effects.png` is meant to illustrate the effect of the TFA value on the stream, SDR, and mask outputs. It was generated using the script in this folder. The data are outputs from the SDR model[^1] run on the SDR test dataset[^2]. All parameters were set to the defaults, except TFA which was set to 100, 400, and 1000.

Run `python tfa_effects_script.py <path/to/invest/test/data>` from within this directory to re-create the file `tfa_effects.png` (requires `matplotlib`, `numpy`, and `pygeoprocessing`).

[^1]: invest revision `f22a9a6e9196905dde2d9c63b9cd668560d837b3` was used.

[^2]: test data revision `ac7023d684478485fea89c68f8f4154163541e1d` was used.
