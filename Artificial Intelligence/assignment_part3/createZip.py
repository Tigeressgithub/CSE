# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:34:58 2021

@author: MV
"""

from zipfile import ZipFile
import os
from os.path import basename



data_loader =r'C:\Users\MV\Desktop\CSE 571\assignment_part3\Data_Loaders.py'
networks = r'C:\Users\MV\Desktop\CSE 571\assignment_part3\Networks.py'

with ZipFile('submission.zip', 'w') as zipObj2:
   # Add multiple files to the zip
   zipObj2.write(data_loader)
   zipObj2.write(networks)
   zipObj2.close()