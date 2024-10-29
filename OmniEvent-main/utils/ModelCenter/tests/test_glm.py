import torch
import bmtrain as bmt

from model_center.model import GLM, GLMConfig
from model_center.tokenizer import GLMTokenizer

def main():
    path = "glm-10b-zh"
    config = GLMConfig.from_pretrained(path)
    config.dropout_p = 0
    glm = GLM.from_pretrained(path, config=config)
    tokenizer = GLMTokenizer.from_pretrained(path)

    input_ids = torch.tensor([[50002, 36780, 26381, 43488, 40769, 43462, 43487, 4284, 9108, 44421, 45980, 45020, 19962, 43561, 43504, 4953, 284, 43410, 43359, 2220, 44300, 45698, 43897, 43373, 1581, 453, 269, 729, 43913, 1957, 2633, 43776, 17422, 284, 43488, 1836, 43738, 1367, 43373, 785, 2178, 3215, 43359, 44300, 45698, 43897, 43362, 1836, 12021, 277, 14821, 4625, 43881, 43508, 7216, 45278, 43959, 1221, 44254, 45782, 44874, 45724, 1221, 13660, 41534, 353, 619, 1221, 43770, 43660, 1221, 43770, 46314, 1221, 6337, 14529, 1221, 44611, 43660, 44874, 45724, 1221, 1836, 43371, 43487, 102, 4515, 29615, 43359, 1836, 43360, 37443, 40066, 43361, 1180, 2428, 44913, 45024, 47618, 3556, 43359, 2343, 43488, 1836, 43738, 43487, 16884, 14537, 1788, 43490, 46032, 867, 733, 43359, 4561, 43363, 45569, 15230, 44709, 43936, 43373, 9460, 15932, 43359, 4755, 43536, 20116, 18867, 3757, 43569, 43361, 43414, 15534, 63, 43490, 1836, 8365, 1531, 43359, 43699, 3183, 13201, 43881, 43359, 2318, 43676, 43881, 43361, 1656, 18674, 514, 1328, 43383, 43576, 2645, 6264, 43388, 25858, 44904, 43828, 49480, 45130, 43359, 43403, 20982, 43388, 4011, 44431, 43625, 10199, 43969, 43359, 10427, 39971, 44997, 43433, 43367, 44008, 44294, 43623, 44087, 43367, 43721, 44495, 44528, 43590, 43367, 13809, 44889, 44781, 43367, 3873, 7553, 43359, 43414, 8940, 1836, 43380, 45166, 11127, 43654, 17, 264, 43427, 14353, 43361, 43414, 67, 3765, 43488, 1836, 43738, 43487, 43360, 2440, 645, 194, 4670, 1226, 645, 43394, 17906, 43359, 43368, 1440, 43359, 460, 25, 10696, 43561, 4183, 43359, 30465, 43459, 44916, 43435, 43867, 43359, 4561, 44124, 43476, 45370, 43476, 43361, 1831, 3410, 43359, 4435, 43881, 487, 43359, 6, 43387, 44122, 2411, 43610, 3649, 43359, 400, 67, 43359, 18387, 27847, 2451, 43424, 43491, 242, 43498, 43359, 44300, 45698, 43897, 43386, 43488, 1836, 43738, 43487, 622, 24500, 1107, 3223, 33658, 33993, 3514, 44249, 24500, 1107, 43383, 1584, 43576, 2620, 43359, 28, 8, 31939, 71, 43881, 43488, 1836, 43738, 43487, 43360, 43389, 44300, 45698, 43897, 43383, 155, 43488, 1836, 43738, 43487, 4844, 251, 43453, 6423, 43360, 4698, 43361, 44584, 43921, 914, 3730, 556, 44419, 43599, 46318, 6627, 7758, 43427, 43359, 43414, 1473, 43488, 6207, 43738, 413, 60, 5382, 43881, 3152, 43488, 1836, 43738, 1367, 737, 1669, 27128, 43488, 6207, 43738, 413, 15425, 932, 1423, 43361, 43511, 961, 43359, 43385, 906, 43385, 43881, 115, 43359, 1328, 150, 43359, 43374, 23407, 43881, 3152, 43517, 43825, 43589, 44021, 4625, 43361, 83, 886, 7758, 43427, 43359, 1994, 43881, 569, 16019, 43881, 8280, 43361, 28, 4268, 43414, 2333, 43654, 1037, 25598, 43359, 38, 43792, 45202, 43415, 13776, 43370, 43361, 14315, 38249, 11085, 44498, 582, 43359, 3016, 1849, 43415, 16505, 44872, 43780, 43361, 43374, 836, 15534, 63, 462, 1836, 830, 43361, 3016, 1453, 28, 15534, 1836, 43706, 60, 31436, 44048, 43361, 26269, 28, 43430, 15534, 137, 47, 4553, 43881, 1412, 43361, 4232, 652, 876, 23907, 2897, 6436, 2778, 6546, 277, 43361, 3016, 956, 932, 95, 10035, 1429, 43361, 681, 17, 240, 236, 277, 44, 272, 43384, 1836, 513, 10326, 264, 43361, 272, 472, 1263, 392, 1086, 1368, 43359, 1553, 13080, 15733, 272, 43361, 1836, 43946, 472, 14900, 3537, 44655, 45264, 44135, 44593, 792, 43361, 11660, 9268, 818, 2831, 18867, 43359, 1836, 386, 43517, 272, 43589, 1513, 43361, 966, 3395, 43367, 8031, 28079, 277, 43359, 11360, 43881, 44016, 43566, 43994, 43361, 47, 961, 43379, 1836, 43377, 4347, 43359, 10326, 818, 2831, 264, 43361, 19, 43544, 43881, 1836, 247, 43994, 43359, 155, 1724, 672, 43361, 39296, 126, 43576, 3935, 780, 71, 43881, 43488, 1836, 43738, 4813, 11504, 264, 43838, 43378, 43359, 4420, 16687, 43362, 11703, 32579, 38036, 43432, 3005, 1880, 786, 4758, 43838, 286, 49022, 6543, 43438, 43534, 45315, 43361, 3935, 326, 43359, 267, 19645, 19847, 43430, 2234, 13117, 22806, 43554, 137, 43511, 47309, 43961, 44994, 3321, 490, 32, 8170, 7398, 13838, 43361, 43783, 1008, 43367, 351, 24209, 43359, 5337, 44400, 43961, 45264, 43894, 43359, 3278, 43576, 32487, 32, 933, 43430, 43851, 43471, 34500, 215, 3935, 780, 43359, 6660, 43430, 47094, 12190, 43379, 44293, 11138, 137, 43414, 15487, 82, 43524, 2234, 43359, 374, 3218, 18667, 43359, 43481, 472, 4363, 43361, 23281, 43430, 32579, 38036, 43432, 71, 43359, 740, 4049, 707, 43361, 43373, 34845, 43359, 43377, 9350, 1553, 29557, 45490, 43421, 11165, 43359, 6685, 170, 43359, 18604, 10552, 7721, 43554, 2234, 43361, 961, 12602, 2892, 9057, 1974, 43359, 2172, 43359, 1264, 1248, 4758, 3703, 4049, 9057, 153, 648, 43361, 47, 43359, 43374, 5743, 6758, 1836, 2089, 43359, 922, 10548, 818, 43376, 264, 388, 181, 43361, 24500, 1107, 43383, 43881, 43488, 1836, 43738, 43487, 43395, 8510, 8, 3132, 43689, 43389, 41415, 23106, 44731, 43429, 43389, 44300, 45698, 43897, 43383, 6360, 808, 43770, 12285, 43412, 37, 43359, 1850, 156, 43656, 44731, 2054, 43361, 10678, 43881, 43488, 40769, 43462, 43487, 8642, 143, 246, 44526, 43359, 19157, 43469, 44526, 57, 43359, 3622, 2333, 2466, 7758, 43427, 43359, 349, 4800, 1608, 43359, 43881, 39115, 43361, 104, 342, 43881, 43488, 1836, 43738, 43487, 8642, 143, 7217, 43976, 43389, 585, 1548, 1836, 43738, 43487, 19257, 43373, 8978, 43387, 4903, 43361, 3708, 7006, 43359, 21384, 830, 11858, 4903, 43359, 192, 5585, 1560, 2440, 645, 43378, 43359, 17421, 7217, 43361, 43386, 3106, 300, 43359, 43374, 44467, 53, 571, 2440, 645, 43361, 28906, 93, 3957, 2892, 43359, 1377, 2440, 3058, 23217, 43383, 50008, 50006, 6228, 45698, 43897, 67, 3765, 43488, 1836, 43738, 43487, 43360, 2440, 645, 194, 43368, 1440, 43359, 460, 25, 10696, 43561, 4183, 43359, 30465, 43459, 44916, 43435, 43867, 43361, 1831, 3410, 43359, 4435, 43881, 487, 43359, 6, 43387, 44122, 2411, 43610, 3649, 43359, 400, 67, 43359, 18387, 27847, 2451, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]).int().cuda()
    sep = torch.tensor([845]).int().cuda()
    position_ids = torch.tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 844, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]).int().cuda()
    block_position_ids = torch.tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]).int().cuda()

    print(tokenizer.decode(input_ids[0].tolist()))

    selector = input_ids!=0
    logits1 = glm(input_ids, position_ids, block_position_ids, sep)
    print(logits1)
    logits2 = glm(input_ids)
    print((logits2-logits1)[selector].nonzero())
    logits2 = glm(input_ids, position_ids=position_ids)
    print((logits2-logits1)[selector].nonzero())
    logits2 = glm(input_ids, block_position_ids=block_position_ids)
    print((logits2-logits1)[selector].nonzero())
    logits2 = glm(input_ids, sep=sep)
    print((logits2-logits1)[selector].nonzero())

if __name__ == "__main__":
    bmt.init_distributed()
    main()
