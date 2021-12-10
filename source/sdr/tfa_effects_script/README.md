# script and data used to generate the image `tfa_effects.png`

The image `tfa_effects.png` is meant to illustrate the effect of the TFA value on the stream, SDR, and mask outputs. It was generated using the script and data in this folder. The data are outputs from the SDR model run on the SDR test dataset. All parameters were set to the defaults, except TFA which was set to 100, 400, and 1000.

Run `python tfa_effects_script.py` from within this directory to re-create the file `tfa_effects.png`.