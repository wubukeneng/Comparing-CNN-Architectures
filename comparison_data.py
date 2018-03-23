import numpy as np
from numpy import nan

data = np.array([
    ['AlexNet', 0.9**-1 *54.5,2.5e3,54.5],
    #['BN-AlexNet', 0.95**-1 *56.5,1.25e3,56.5],
    ['ResNet-152', 1.3**-1 *77.5, 23e3 ,77.5 ],
    #['ResNet-101', 1.7**-1 *77, 15.5e3, 77],
    #['ResNet-50', 3**-1 *76,8e3,76],
    ['ResNet-18', 5.9**-1 *69,4e3,69],
    ['GoogleNet', 6.8,3.1e3 ,68],
    #['Inception V3', 3.2**-1 *78,11e3,78],
    ['Inception V4', 2.5**-1 *80,18e3,80],
    #['BN-NIN', 7.2**-1 *63,2.5e3,63],
    ['ENet', 11.6**-1 *68, 1.6e3, 68 ],
    #['Xception', 22.855952, nan, 79],
    ['1.0 MobNet-224',4.2 ,2*569 , 70.6],
    #['1.0 MobNet-192',4.2 ,2*418 , 69.1],
    #['1.0 MobNet-160',4.2 ,2*290 , 67.2],
    ['1.0 MobNet-128',4.2 ,2*186 , 64.4],
    ['0.75 MobNet-224',1.9, 2*325, 69],
    ['0.5 MobNet-224', 0.2, 2 * 149, 64],
    #['0.25 MobNet-224', 0.2, 2*45, 51],
    ['DN-BC-121', 9, 550, 75.5], 
    #['DN-BC-169', 14, 700, 76.5], 
    #['DN-BC-201', 20, 850, 77.5], 
    ['DN-BC-264', 32 , 1200, 78.5],
    ['MSD-A', 0, 2*50, 63.5],
    #['MSD-B', 0, 2*125, 71],
    #['MSD-C', 0, 2*210, 75],
    ['MSD-D', 0, 2*320, 76],
    ['VGG-16',138, 31e3, 71], 
    ['MobNetV2-1',3.4,2*300,71.7],
    ['MobNetV2-1.4',6.9,2*585,74.7],
    ],dtype=object)
