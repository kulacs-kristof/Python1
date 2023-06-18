from tkinter import dnd


taxiID = [5240, 1215, 3673, 5400, 1257, 4666, 5998, 2538, 6594, 7864, 400, 6482, 5856, 7211, 1094, 6591, 6514, 8267, 8002, 2718, 4261, 3449, 6710, 2605, 1098, 3514, 5846, 4126, 1369, 3018, 6729, 5687, 7578, 2643, 4359, 945, 5114, 5930, 5149, 3465, 5579, 8397, 2643, 4586, 6852, 4219, 4849, 4069, 4705, 2685, 6361, 6940, 5571, 7303, 5149, 747, 772, 3165, 945, 6043, 733, 7744, 316, 8350, 4342, 7891, 2819, 5138, 7323, 1944, 5349, 7063, 4458, 2556, 6669, 1750, 6023, 102, 1587, 5140, 2374, 7061, 3478, 6559, 4330, 117, 6196, 3143, 5022, 4205, 4638, 7006, 2697, 7244, 6232, 1094, 5548, 5062, 2037, 76, 5659, 4531, 6043, 5757, 4097, 6197, 1262, 293, 53, 3338, 2341, 6923, 8315, 8350, 2163, 4846, 4715, 7723, 4494, 8170, 2179, 3207, 7468, 7937, 3235, 4586, 3504, 3717, 7097, 3645, 8271, 8661, 2503, 5704, 8396, 1901, 3469, 4710, 3723, 1390, 6054, 8565, 920, 1098, 1746, 3237, 4593, 4870, 2329, 4017, 3573, 1620, 4017, 2186, 340, 5548, 6727, 1944, 5619, 5178, 4401, 4813, 6117, 6923, 7368, 4443, 3595, 65, 2435, 6101, 1611, 4456, 109, 7766, 3895, 6025, 8479, 6159, 901, 7810, 1447, 3776, 7195, 4770, 5475, 866, 6798, 2843, 3173, 5990, 2121, 3588, 8656, 1362, 723, 7042, 5058, 6523, 2066, 5263, 8044, 1886, 2747, 4320, 6950, 8718, 3062, 8185, 8483, 7197, 1412, 7006, 4352, 1168, 5867, 4446, 3209, 6213, 7689, 7690, 3217, 7489, 4496, 4114, 4938, 7540, 797, 2940, 4866, 6301, 1159, 3209, 6749, 2863, 8054, 2127, 5114, 6956, 1347, 229, 4174, 4999, 6614, 2901, 5564, 4362, 6113, 3924, 4107, 1483, 2601, 8583, 118, 2486, 6513, 8232, 8596, 3546, 5475, 1460, 6820, 7018, 6902, 5117, 50, 5029, 5406, 4119, 3617, 2236, 3387, 1210, 6717, 1270, 827, 2147, 298, 2642, 7861, 2102, 1438, 2022, 3997, 4089, 6237, 1426, 2330, 5254, 4495, 3923, 8232, 2828, 6650, 7802, 8647, 8679, 7307, 3931, 3684, 5071, 1618, 2468, 3278, 1180, 2435, 5226, 4044, 8648, 3178, 688, 1750, 6744, 4999, 5971, 6863, 5636, 4924, 7643, 3410, 3004, 5640, 748, 1010, 7365, 6134, 4770, 2059, 1513, 4635, 2870, 6899, 3254, 8040, 7531, 8648, 3237, 4326, 6620, 548, 3915, 847, 6950, 3233, 2559, 2845, 4611, 2596, 3400, 610, 700, 8546, 7676, 1164, 5795, 5044, 7968, 5896, 760, 4653, 513, 8661, 4026, 3662, 7006, 1213, 7895, 3544, 7005, 710, 4296, 4247, 349, 1644, 8566, 797, 3671, 8016, 3014, 1901, 6366, 2595, 7689, 7745, 2533, 6675, 8588, 7627, 731, 4488, 3238, 857, 2912, 1302, 3862, 8022, 7667, 1074, 4748, 4900, 6086, 2640, 8348, 6967, 6956, 8734, 3921, 2221, 3181, 8718, 5139, 1129, 8446, 549, 554, 7833, 5161, 1508, 8030, 4296, 4497, 4309, 1385, 1030, 4338, 1968, 4000, 93, 6378, 2978, 2400, 1829, 6830, 2421, 5881, 1447, 5348, 3506, 5739, 2723, 5180, 1036, 2877, 3373, 491, 4880, 2973, 6317, 5548, 4123, 8247, 642, 4728, 2149, 3600, 6185, 92, 3963, 7776, 6481, 1110, 2952, 6923, 6104, 1736, 6833, 8271, 4809, 1326, 6147, 8120, 6552, 873, 1895, 8061, 286, 2607, 7596, 2545, 973, 250, 4092, 4570, 5048, 4787, 6185, 703, 8310, 1461, 431, 6434, 3209, 370, 8185, 7011, 6513, 5280, 3772, 349, 2820, 5881, 7273, 7912, 2863, 3654, 672, 2559, 456, 3089, 3514, 6219, 7484, 8263, 621, 8117, 7210, 8672, 5494, 4591, 8089, 3068, 2872, 7011, 3861, 5273, 2845, 8336, 8016, 7674, 1763, 5676, 5933, 5170, 5382, 4438, 7810, 6054, 450, 4411, 4643, 7969, 8137, 3629, 4303, 3514, 6577, 4111, 6743, 65, 5357, 1904, 8273, 4891, 8727, 1005, 8044, 2152, 7063, 8171, 4958, 5697, 1405, 4919, 1482, 7540, 4559, 5327, 8067, 8088, 5226, 3351, 4009, 3017, 505, 7299, 3298, 7299, 6970, 3588, 4961, 2904, 6699, 772, 8203, 3024, 8188, 2680, 5433, 360, 6369, 2214, 8578, 1827, 451, 8247, 3354, 8190, 8327, 1265, 2560, 7066, 1742, 375, 896, 6969, 1644, 7345, 12, 4852, 3595, 8710, 3371, 567, 2785, 7255, 4146, 7806, 4532, 1747, 3515, 6633, 3617, 6876, 6577, 866, 6867, 6553, 3069, 7028, 1911, 2986, 5426, 8211, 3356, 2733, 8606, 3469, 414, 4304, 6513, 7307, 6344, 1679, 6644, 3218, 7676, 4285, 8044, 8227, 4060, 1278, 3240, 569, 4060, 3384, 7255, 561, 6940, 8301, 5422, 6907, 2450, 3068, 4692, 6185, 6744, 97, 6858, 5015, 4620, 1638, 5151, 7925, 6602, 7436, 3360, 4247, 1763, 1455, 3772, 4680, 2026, 1852, 5991, 7006, 5818, 3792, 6290, 1633, 8117, 7415, 3395, 2410, 3895, 1827, 8508, 422, 3022, 5834, 3799, 1483, 6065, 25, 3886, 4993, 7257, 6970, 6868, 8719, 6252, 4559, 3018, 7758, 4844, 1010, 6305, 8758, 767, 5776, 397, 3773, 5138, 3163, 2564, 6078, 7355, 6145, 6682, 2879, 4276, 8564, 1405, 1667, 1970, 3055, 1776, 7540, 5807, 6197, 4958, 3040, 4051, 1026, 4872, 7540, 7766, 788, 5222, 4920, 7693, 8200, 5729, 6034, 2206, 5796, 8378, 1959, 7939, 2672, 4596, 6877, 2927, 3649, 5625, 532, 8353, 2175, 5404, 6524, 3567, 8376, 3146, 4063, 4685, 7992, 3875, 5519, 8044, 5631, 5881, 684, 7384, 5263, 2986, 3547, 8648, 2048, 3541, 4109, 686, 3217, 3238, 3865, 3433, 393, 2653, 1426, 3899, 7579, 46, 920, 3, 6826, 7586, 3736, 4332, 1707, 5998, 7187, 4025, 5637, 4928, 4675, 2036, 1545, 4490, 329, 6611, 6322, 6369, 2058, 8336, 6358, 5131, 4325, 8030, 4877, 8088, 4576, 5380, 3684, 2618, 2240, 8636, 5117, 3295, 5112, 5179, 4362, 1030, 3004, 5502, 7198, 5784, 6094, 2179, 6746, 2226, 8645, 4438, 1555, 2969, 6458, 4443, 2059, 7854, 4297, 7961, 3620, 340, 8264, 7766, 6777, 554, 5780, 5580, 7135, 4409, 7586, 1163, 8188, 3045, 5869, 5428, 6755, 8398, 7712, 8734, 3014, 4903, 2665, 5028, 6922, 3210, 977, 4182, 3920, 7523, 2635, 920, 171, 6775, 6945, 1759, 5782, 5348, 8324, 6046, 1800, 4353, 3247, 1164, 8376, 8149, 123, 981, 3863, 3786, 7809, 2993, 400, 5401, 547, 2211, 5896, 6742, 1460, 901, 2139, 1109, 7033, 1691, 1506, 1538, 618, 4857, 5014, 5083, 3233, 6129, 297, 1311, 733, 505, 8436, 4934, 4007, 8414, 1534, 6317, 2649, 4659, 7900, 177, 2708, 3043, 3891, 8380, 6065, 6401, 4494, 2139, 2118, 1955, 2214, 2914, 2457, 2601, 229, 7717, 5367, 6943, 2186, 4467, 1545, 8672, 2966, 4005, 4680, 3462, 4261, 8014, 710, 7969, 3600, 5587, 6195, 2448, 3997, 5025, 6627, 5573, 2041, 6008, 8307, 4089, 2276, 1284, 3694, 2716, 3612, 5341, 5832, 1473, 3395, 5899, 4251, 1924, 1545, 7198, 2916, 6046, 2743, 7665, 3360, 7750, 5796, 5232, 5196, 1109, 153, 747, 5846, 4438, 1513, 2467, 4900, 2166, 4152, 5131, 7589, 6853, 2847, 4993, 6290, 2833, 7590, 6054, 5226, 4527, 8269, 6290, 1460, 7205, 2179, 5501, 4675, 717, 7863, 1987, 2452, 177, 7755, 7315, 2918, 8344, 2167, 8710, 2447, 4069, 3018, 3993, 5525, 8463, 3736, 4618, 6089, 3862, 8636, 4927, 32, 6016, 3178, 4601, 4433, 464, 7517, 6376, 5767, 8014, 3862, 7468, 7352, 668, 4202, 5108, 6650, 6398, 7390, 1897, 972, 4296, 2063, 8063, 1463, 3312, 6180, 8309, 6717, 1545, 3062, 4811, 2058, 3433, 4292, 2618, 5548, 1523, 7028, 6535, 1193, 1164, 2514, 778, 6305, 2004, 3495, 7213, 8685, 5435, 4195, 3165, 5411, 7374, 197, 5257, 8696, 1322, 1928, 812, 1462, 4689, 1486, 8563, 3016, 3387, 4320, 3258, 1037, 6786, 7891, 4301, 567, 6907, 3612, 2283, 1294, 255, 2081, 3004, 2318, 284, 5329, 74, 1383, 2601, 1380, 1869, 3721, 778, 8634, 527, 2009, 8361, 3340, 938, 5571, 814, 8274, 475, 386, 349, 4825, 6620, 3033, 433, 7063, 8565, 1731, 1240, 157, 5990, 2388, 7999, 2215, 53, 6654, 4790, 4934, 1744, 169, 3649, 3909, 7961, 6755, 7407, 2259, 6113, 5178, 2733, 6569, 3792, 1000, 7230, 1309, 2847, 3846, 1751, 7349, 5857, 1472, 2845, 2932, 6562, 1886, 8749, 7430, 733, 7587, 3478, 5631, 3601, 4254, 4128, 29, 6115, 1742, 0, 3954, 3824, 4855, 3941, 2088, 5901, 827, 2663, 3147, 76, 1322, 5114, 6505, 998, 304, 8200, 7748, 5161, 8154, 3018, 5825, 5243, 6944, 8108, 6407, 5540, 5511, 8210, 1811, 8063, 2742, 5775, 6101, 177, 4287, 1438, 5044, 3567, 3617, 5408, 4168, 3649, 2271, 4168, 8491, 3675, 8247, 7701, 5240, 5301, 5143, 4532, 7150, 8569, 4494, 5997, 7356, 6211, 6232, 5937, 1534, 3175, 6575, 5983, 4790, 5677, 4015, 4029, 5293, 3291, 1959, 8164, 8634, 8414, 416, 6927, 2828, 6785, 1302, 103, 7, 1852, 6076, 6631, 4958, 1586, 2139, 4443, 5579, 1092, 8647, 117, 7860, 5313, 1552, 6614, 5869, 8312, 3027, 8540, 5900, 6429, 1529, 595, 199, 7210, 8630, 1115, 4206, 7587, 4993, 6597, 7555, 6858, 4143, 3206, 2916, 977, 4737, 6806, 2991, 1671, 7541, 1234, 5054, 3637, 1243, 8289, 8564, 2845, 7777, 5659, 1274, 602, 6426, 1564, 5704, 1901, 1257, 593, 3877, 3216, 1378, 316, 2745, 1302, 7112, 7577, 6837, 5175, 1942, 3026, 2572, 5076, 1106, 5828, 7540, 4735, 8082, 1282, 2036, 6058, 342, 1261, 7456, 2218, 5343, 2782, 8630, 2768, 3313, 5538, 2612, 7888, 1615, 567, 8561, 2796, 5140, 1163, 3915, 8414, 768, 6585, 7776, 7384, 4488, 4542, 4213, 7451, 4106, 6200, 2699, 8640, 6544, 2992, 8200, 8749, 8682, 6401, 225, 6779, 2856, 4951, 6902, 517, 6853, 5301, 8273, 4560, 7523, 6985, 6867, 4664, 1381, 456, 5268, 3465, 6537, 4752, 6196, 7651, 2884, 5138, 6096, 4210, 7629, 4832, 7776, 3946, 1314, 2022, 5025, 5787, 8588, 6923, 4880, 5655, 2330, 1905, 8264, 3296, 6861, 506, 2003, 3931, 5948, 1842, 2221, 8634, 1257, 7528, 1563, 8630, 7861, 8630, 5813, 6185, 5894, 1079, 3428, 376, 7556, 4832, 1981, 5130, 2251, 8392, 1521, 7589, 8316, 5997, 3595, 4425, 279, 218, 6553, 6611, 7766, 8048, 404, 6353, 7257, 6120, 5573, 3453, 8758, 2670, 4026, 5384, 5921, 8407, 7210, 6353, 1669, 4432, 4433, 6898, 5243, 8496, 5983, 4694, 5899, 3473, 5475, 5827, 7323, 5112, 323, 5730, 469, 8396, 7173, 4586, 4216, 8147, 6451, 8315, 7513, 5829, 3173, 8414, 6562, 7782, 7546, 7330, 8626, 1989, 7471, 1164, 1095, 6877, 8613, 5138, 5472, 920, 3458, 5863, 5548, 760, 4710, 7355, 3267, 1265, 4761, 770, 1684, 7196, 8565, 8407, 7307, 8384, 6095, 4659, 7373, 3099, 8586, 3214, 6151, 686, 4246, 1746, 6691, 5885, 1284, 1877, 4198, 2640, 7284, 7092, 5680, 2534, 6871, 532, 8344, 6008, 6038, 2833, 4374, 7452, 1589, 1959, 8279, 3179, 1385, 4316, 2500, 4762, 6837, 7727, 5349, 7375, 7663, 8709, 2235, 6072, 6577, 233, 92, 6717, 422, 3876, 8759, 50, 3264, 6989, 54, 7, 2240, 7029, 3882, 4458, 1058, 2337, 2147, 6713, 4638, 7400, 4763, 1596, 5343, 284, 6074, 68, 6482, 8159, 4106, 7171, 2953, 8657, 8149, 3232, 1964, 3400, 920, 4460, 3454, 5310, 4846, 4886, 6075, 6343, 554, 4494, 3594, 6792, 7374, 4026, 6673, 7622, 5110, 6419, 4702, 3181, 1559, 390, 1521, 4860, 5180, 1115, 5628, 1261, 3501, 7554, 1383, 3876, 3620, 1631, 8652, 3741, 8728, 2697, 2324, 261, 4715, 6298, 7356, 4284, 2214, 1305, 807, 2696, 4702, 6131, 2802, 2805, 5659, 4219, 4659, 6317, 2890, 3058, 4612, 2418, 8232, 6, 5523, 8193, 8709, 4446, 3373, 3235, 841, 3581, 6524, 2053, 7536, 4020, 524, 4029, 739, 5848, 2607, 7340, 7596, 904, 2560, 1979, 2698, 1319, 8482, 1420, 3523, 6259, 4946, 1401, 5812, 8166, 5390, 4060, 274, 4252, 5400, 3657, 2297, 8397, 3721, 4325, 4142, 8262, 93, 4303, 5993, 4466, 6042, 7748, 7531, 2088, 7545, 3886, 4089, 4205, 8031, 6830, 4723, 4954, 3506, 7323, 3691, 8718, 1762, 6943, 8534, 7396, 2796, 1147, 6596, 6043, 625, 1152, 935, 3793, 1654, 3773, 4997, 4114, 3909, 3750, 4111, 5519, 5496, 1462, 1409, 4229, 827, 5548, 6922, 318, 1482, 3728, 1381, 1521, 3350, 2633, 6824, 4584, 1265, 4559, 6407, 716, 2206, 1445, 8482, 2888, 521, 7033, 59, 7750, 306, 8649, 2693, 4005, 1898, 515, 266, 2605, 1221, 5139, 1051, 8569, 629, 2221, 3480, 3736, 5901, 6766, 5813, 242, 3479, 1644, 3175, 4432, 678, 3882, 4330, 3586, 7923, 7402, 2925, 4833, 2560, 7523]

fuvarHossz = [900, 240, 2400, 300, 360, 2400, 1800, 540, 153, 780, 3120, 660, 300, 1320, 540, 480, 480, 360, 300, 1920, 780, 60, 1200, 480, 660, 600, 360, 720, 2160, 240, 1800, 900, 660, 180, 780, 840, 5100, 540, 1980, 240, 360, 335, 3540, 300, 360, 244, 60, 1680, 660, 1140, 360, 300, 960, 900, 1080, 1200, 458, 360, 1560, 1680, 300, 540, 840, 360, 420, 660, 240, 840, 0, 360, 960, 360, 240, 480, 720, 1140, 300, 406, 2220, 1320, 420, 780, 360, 900, 960, 420, 960, 1140, 180, 600, 600, 300, 540, 2640, 480, 600, 240, 600, 180, 420, 120, 540, 840, 360, 300, 300, 240, 611, 300, 2400, 1200, 240, 780, 420, 660, 3480, 540, 0, 300, 480, 360, 1620, 1080, 480, 300, 1380, 540, 702, 1020, 1080, 240, 0, 780, 180, 2100, 840, 1500, 300, 540, 2460, 1800, 240, 1500, 600, 360, 240, 0, 120, 600, 0, 180, 660, 0, 480, 2340, 540, 420, 420, 420, 180, 1020, 540, 1, 900, 240, 420, 360, 1260, 180, 480, 480, 780, 540, 360, 4080, 180, 578, 660, 540, 60, 1440, 660, 0, 600, 300, 360, 360, 1920, 300, 540, 420, 0, 600, 540, 2280, 900, 180, 420, 240, 0, 540, 960, 180, 240, 720, 420, 120, 900, 3000, 300, 420, 1440, 900, 420, 840, 1260, 420, 660, 420, 960, 660, 420, 480, 1533, 1260, 1440, 420, 480, 660, 2520, 180, 960, 360, 0, 240, 540, 2040, 360, 60, 660, 360, 360, 480, 1200, 480, 1320, 900, 420, 180, 1140, 420, 660, 1380, 540, 360, 540, 360, 360, 240, 1740, 960, 540, 300, 1380, 300, 660, 360, 1440, 2640, 480, 660, 780, 120, 420, 900, 300, 1860, 1980, 780, 660, 900, 0, 300, 360, 1920, 480, 420, 960, 600, 420, 840, 180, 960, 1740, 180, 420, 180, 180, 180, 420, 1680, 1560, 660, 600, 600, 180, 960, 2160, 540, 840, 60, 420, 540, 2460, 720, 660, 180, 240, 0, 300, 240, 1620, 180, 240, 420, 900, 660, 1020, 600, 480, 1063, 240, 1140, 300, 1020, 540, 540, 300, 360, 540, 660, 420, 720, 540, 720, 600, 360, 180, 1387, 480, 540, 840, 2340, 360, 1020, 240, 900, 720, 600, 720, 60, 1320, 660, 780, 240, 2100, 420, 420, 360, 3480, 720, 1020, 1020, 3780, 720, 840, 240, 420, 240, 420, 420, 1200, 1320, 660, 480, 1440, 240, 2640, 420, 1140, 294, 960, 780, 420, 780, 2760, 540, 300, 420, 1080, 660, 780, 180, 600, 2640, 720, 600, 420, 360, 660, 720, 720, 660, 180, 1980, 1260, 2400, 780, 420, 234, 900, 1980, 180, 716, 960, 180, 780, 960, 780, 240, 360, 60, 60, 540, 540, 600, 240, 780, 540, 1140, 660, 600, 540, 360, 720, 1860, 300, 240, 420, 360, 10, 600, 2340, 900, 840, 300, 840, 540, 360, 360, 600, 420, 720, 180, 1380, 960, 180, 0, 180, 480, 1980, 600, 660, 1380, 300, 240, 2520, 240, 60, 420, 240, 240, 360, 960, 0, 1140, 300, 2940, 1080, 900, 660, 0, 660, 1260, 240, 1620, 840, 420, 1560, 0, 4140, 300, 360, 2520, 480, 9120, 1200, 240, 420, 300, 300, 600, 600, 600, 360, 420, 1320, 540, 1980, 540, 1860, 420, 900, 1620, 1200, 600, 1140, 480, 420, 840, 300, 420, 4260, 960, 240, 1020, 420, 420, 360, 660, 0, 1140, 420, 240, 480, 1140, 720, 840, 660, 360, 720, 780, 0, 0, 420, 2820, 360, 240, 2280, 300, 660, 780, 1860, 600, 480, 365, 480, 1413, 180, 1560, 120, 120, 600, 2340, 1585, 1140, 540, 300, 420, 300, 2940, 21, 240, 854, 480, 840, 300, 1920, 300, 540, 180, 360, 420, 60, 540, 780, 1320, 360, 600, 900, 360, 300, 300, 1020, 360, 0, 300, 60, 360, 480, 660, 600, 600, 1320, 240, 180, 660, 240, 300, 660, 1740, 360, 360, 540, 780, 360, 0, 420, 2280, 660, 2640, 0, 660, 480, 300, 600, 120, 1020, 1020, 300, 240, 480, 1740, 2100, 240, 480, 60, 420, 900, 1740, 1140, 180, 960, 540, 0, 600, 660, 480, 507, 240, 540, 1560, 1740, 600, 1080, 480, 360, 360, 300, 894, 1800, 1500, 1800, 300, 240, 1260, 7920, 420, 1005, 480, 1380, 1200, 360, 360, 1380, 900, 420, 660, 420, 780, 480, 1860, 600, 780, 960, 540, 300, 660, 240, 360, 720, 0, 0, 960, 840, 600, 420, 661, 300, 300, 420, 540, 0, 300, 720, 480, 540, 240, 360, 420, 300, 420, 600, 540, 300, 480, 540, 1020, 420, 780, 2100, 300, 360, 540, 240, 300, 540, 60, 600, 900, 1200, 300, 540, 1080, 600, 600, 240, 1680, 234, 600, 240, 540, 420, 720, 540, 1860, 300, 1620, 0, 1980, 1200, 1020, 0, 420, 540, 840, 960, 1260, 180, 265, 1320, 420, 2820, 3120, 240, 1649, 1620, 600, 420, 240, 600, 1380, 840, 240, 300, 1620, 1020, 540, 360, 1680, 2400, 360, 60, 600, 20, 2160, 1560, 480, 660, 360, 360, 300, 1740, 240, 720, 2580, 1380, 360, 420, 1140, 0, 180, 600, 1740, 180, 1680, 300, 480, 720, 420, 780, 780, 840, 420, 660, 300, 274, 240, 780, 480, 1140, 300, 480, 1200, 2520, 600, 240, 360, 480, 480, 960, 720, 780, 480, 1620, 720, 360, 780, 540, 60, 480, 540, 480, 420, 1080, 480, 180, 780, 3120, 1320, 480, 480, 540, 840, 360, 300, 1800, 360, 180, 720, 840, 240, 540, 660, 780, 1740, 2100, 1440, 0, 1140, 300, 300, 3180, 720, 1560, 540, 480, 1180, 600, 960, 420, 300, 300, 240, 540, 1320, 360, 600, 600, 420, 1200, 712, 3180, 540, 1080, 3900, 420, 1200, 1140, 360, 420, 300, 780, 300, 660, 300, 600, 360, 240, 420, 660, 780, 60, 0, 900, 420, 538, 120, 300, 1500, 540, 480, 420, 240, 780, 240, 478, 480, 840, 600, 2040, 780, 360, 600, 600, 240, 240, 60, 1080, 540, 180, 780, 360, 600, 540, 960, 540, 240, 120, 1080, 360, 540, 180, 480, 600, 540, 180, 480, 300, 480, 180, 540, 1560, 540, 1800, 600, 540, 840, 1560, 411, 300, 420, 300, 2160, 1200, 600, 1020, 1680, 720, 420, 180, 720, 720, 420, 3180, 120, 540, 540, 360, 660, 0, 660, 480, 540, 540, 300, 480, 780, 2340, 300, 240, 720, 1380, 480, 240, 240, 480, 0, 360, 540, 420, 1080, 1200, 300, 960, 540, 120, 360, 900, 1500, 240, 900, 1980, 240, 1260, 360, 1920, 840, 240, 660, 601, 7860, 240, 540, 240, 0, 1200, 600, 2100, 1860, 420, 540, 2280, 2040, 660, 3180, 660, 420, 960, 540, 660, 780, 960, 300, 420, 840, 840, 780, 840, 1740, 0, 780, 720, 1800, 420, 720, 660, 900, 120, 180, 600, 600, 600, 300, 720, 780, 2220, 360, 660, 360, 1260, 480, 2640, 240, 1860, 600, 300, 480, 840, 300, 240, 180, 720, 660, 660, 660, 660, 240, 240, 420, 1740, 780, 480, 840, 480, 660, 540, 120, 540, 420, 480, 212, 780, 360, 120, 1080, 240, 1140, 360, 600, 900, 360, 420, 1200, 660, 960, 240, 60, 840, 1920, 3660, 1920, 498, 180, 0, 420, 1980, 240, 660, 240, 780, 0, 960, 360, 660, 720, 180, 720, 240, 180, 480, 480, 2460, 420, 1020, 420, 780, 840, 420, 240, 180, 180, 120, 3780, 1020, 900, 600, 540, 360, 360, 720, 0, 240, 2760, 240, 180, 1020, 480, 360, 300, 420, 2591, 1020, 840, 780, 900, 660, 0, 540, 660, 621, 960, 240, 480, 180, 7320, 240, 780, 720, 0, 360, 240, 480, 300, 420, 600, 840, 240, 420, 720, 2820, 480, 660, 300, 11, 360, 1440, 600, 420, 600, 325, 600, 720, 180, 720, 540, 780, 1440, 480, 1500, 300, 180, 180, 900, 120, 360, 300, 420, 1680, 0, 173, 660, 300, 1020, 840, 420, 240, 480, 420, 540, 1380, 840, 1020, 1380, 540, 480, 300, 300, 120, 420, 660, 240, 840, 1260, 540, 300, 240, 960, 480, 960, 540, 600, 1680, 1140, 960, 240, 420, 600, 120, 540, 1647, 780, 600, 360, 300, 1560, 360, 660, 1380, 480, 540, 420, 240, 0, 1440, 600, 1620, 960, 480, 300, 960, 569, 2220, 1080, 180, 1320, 1980, 780, 240, 420, 240, 360, 540, 480, 900, 360, 780, 660, 60, 840, 420, 405, 1020, 420, 540, 300, 720, 184, 900, 300, 480, 480, 300, 780, 780, 360, 957, 960, 780, 720, 1080, 180, 2460, 540, 60, 420, 540, 360, 300, 660, 600, 480, 300, 900, 3300, 2220, 180, 240, 960, 900, 1440, 660, 840, 600, 300, 540, 300, 480, 4260, 840, 600, 480, 1140, 480, 960, 300, 2880, 120, 600, 360, 2580, 660, 600, 360, 780, 540, 300, 180, 539, 120, 3360, 840, 300, 1140, 540, 720, 540, 420, 540, 420, 720, 1020, 1740, 540, 1080, 900, 1200, 180, 540, 240, 2362, 180, 60, 240, 660, 360, 180, 1740, 1140, 600, 780, 1200, 300, 480, 1020, 360, 1980, 300, 180, 540, 360, 660, 120, 360, 540, 780, 420, 180, 660, 720, 540, 1500, 0, 660, 498, 360, 540, 2700, 480, 600, 0, 420, 660, 600, 660, 1440, 240, 300, 660, 780, 780, 780, 240, 431, 780, 720, 588, 540, 480, 0, 540, 240, 540, 180, 420, 240, 480, 360, 420, 120, 60, 300, 840, 2580, 420, 420, 780, 1740, 720, 660, 660, 1500, 60, 2700, 360, 480, 240, 589, 600, 720, 0, 120, 900, 420, 1980, 1380, 720, 480, 180, 180, 480, 720, 540, 540, 300, 300, 1020, 1320, 720, 600, 240, 1020, 540, 600, 480, 660, 360, 1380, 180, 360, 540, 0, 540, 180, 300, 720, 360, 840, 120, 900, 780, 360, 960, 1800, 1020, 660, 60, 1140, 1080, 420, 480, 480, 360, 480, 835, 600, 360, 360, 1320, 360, 2100, 780, 600, 840, 420, 720, 120, 480, 540, 420, 1740, 840, 0, 2220, 960, 240, 780, 420, 360, 1020, 840, 240, 300, 2280, 780, 2051, 1560, 600, 300, 0, 240, 480, 900, 480, 480, 2220, 360, 300, 480, 376, 180, 2280, 1380, 2340, 0, 300, 660, 180, 720, 0, 840, 960, 300, 780, 360, 540, 1020, 2100, 420, 300, 300, 1620, 300, 2400, 611, 540, 360, 420, 600, 420, 2220, 780, 660, 660, 300, 720, 720, 240, 2460, 1020, 1320, 240, 2880, 360, 1200, 1800, 540, 960, 0, 1020, 420, 2400, 420, 480, 540, 1620, 900, 240, 1560, 360, 540, 660, 1560, 600, 360, 1080, 1380, 420, 480, 600, 0, 240, 1020, 960, 480, 360, 420, 1440, 180, 0, 480, 1200, 2700, 660, 780, 480, 840, 900, 180, 540, 360, 480, 720, 840, 529, 600, 420, 720, 180, 180, 720, 1140, 840, 780, 780, 420, 1740, 360, 660, 840, 660, 1080, 120, 960, 540, 1800, 720, 960, 120, 660, 1380, 960, 420, 4740, 120, 0, 600, 780, 360, 300, 1680, 360, 600, 480, 690, 1320, 420, 420, 360, 780, 780, 660, 1441, 720, 1020, 420, 360, 240, 780, 360, 0, 360, 1020, 360, 720, 360, 240, 480, 1740, 840, 540, 0, 360, 600, 660, 720, 1080, 10, 480, 416, 420, 1980, 540, 600, 600, 1500, 540, 1860, 1200, 840, 480, 540, 396, 2280, 720, 480, 274, 720, 360, 120, 720, 480, 540, 840, 540, 300, 480, 600, 1440, 120, 360, 2220, 780, 180, 420, 480, 900, 300, 1500, 360, 1620, 420, 540, 300, 1200, 420, 2460, 297, 540, 480, 1320, 480, 1260, 600, 300, 840, 240, 1200, 1080, 360, 180, 660, 240, 1440, 540, 900, 900, 480, 420, 1740, 60, 120, 840, 1620, 300, 540, 900, 780, 480]

def GetTobbEzer():
    db = 0
    for time in fuvarHossz:
        if time > 1000:
            db += 1
    print(f'1.Feladat: {db}')

def MinKeres():
    minindex = 0
    min = fuvarHossz[minindex]
    for i in range(0, len(fuvarHossz)):
        if fuvarHossz[i] < min:
            min = fuvarHossz[i]
            minindex = i
    print(f'2.Feladat: legrövidebb: {minindex}. - {min}')
    minmasodikkeres(minindex)

def minmasodikkeres(kizartindex):
    minindex = 0
    min = fuvarHossz[minindex]
    for i in range(0 ,len(fuvarHossz)):
        if min > fuvarHossz[i] and i != kizartindex:
            min = fuvarHossz[i]
            minindex = i
    print(f'3.Feladat: {minindex}. - {min}')

def atlagszamol():
    osszeg = db = 0
    for hossz in fuvarHossz:
        if hossz / 60 < 10:
            osszeg += hossz
            db += 1
    print(f'4.Feladat: a 10 percnél rövidebb fuvarok átlaga: {osszeg/db}')

def fuvardijszamol():
    dij = 0
    for hossz in fuvarHossz:
        if hossz < 1000:
            dij = 3000
        elif:
            dij = 3000
            if ((hossz - 1000) / 60) % 1 == 0:
                dij += ((hossz - 1000) / 60) * 500
            else:


GetTobbEzer()
MinKeres()
atlagszamol()