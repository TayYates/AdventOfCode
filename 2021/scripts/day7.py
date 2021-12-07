from statistics import median

crabPositions = [1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,12,186,94,505,338,1527,356,122,360,745,28,227,799,305,177,1188,317,3,462,986,230,438,542,112,1334,620,1351,697,7,478,155,208,175,28,107,1501,238,40,0,469,20,945,699,144,822,189,290,37,1158,920,175,102,1042,590,1219,1110,514,126,142,28,282,1198,80,223,196,13,974,543,28,867,816,959,864,45,556,1106,219,259,14,817,312,1743,151,189,1199,300,823,749,747,42,1525,59,587,222,894,240,635,600,1179,324,1435,274,223,1095,25,423,115,472,22,443,827,622,171,102,175,303,67,86,103,0,1541,1086,217,1497,0,1217,919,1107,1052,1003,298,225,593,42,107,461,286,1254,7,827,724,1216,966,682,1660,201,27,190,1159,120,467,1151,886,173,106,6,141,1946,60,5,901,718,74,1040,149,1,839,986,0,817,1454,781,1541,108,1432,564,782,1747,492,24,949,369,1773,166,72,1372,1473,72,243,251,69,752,916,412,837,56,50,378,1332,0,432,310,281,622,107,414,1069,635,1898,483,1284,213,1613,664,0,29,1257,410,716,44,1529,661,430,1152,1023,25,1641,929,582,161,219,198,982,916,1079,83,19,346,45,452,398,161,12,1077,9,1300,363,438,368,30,195,245,657,404,244,219,99,644,191,1139,133,386,738,36,573,194,223,1224,144,537,1520,1124,389,21,610,652,347,619,121,557,1291,349,5,423,241,83,306,850,24,169,584,997,19,507,395,1076,1005,265,1057,1,1268,598,86,807,52,1160,253,325,462,48,707,694,960,1169,102,238,1108,425,420,15,1710,19,381,980,263,363,70,99,361,973,391,131,372,172,22,13,106,1579,961,20,788,25,126,340,206,17,717,286,1077,362,510,243,177,1063,551,667,1534,409,340,1071,415,160,1067,223,120,77,612,117,160,292,185,1167,214,1519,1265,1355,698,344,157,130,863,48,666,7,459,888,193,657,419,14,320,650,490,290,498,225,720,829,1613,509,645,339,301,868,275,457,1307,125,9,518,43,15,9,7,390,568,1847,165,42,256,432,337,38,11,1485,1758,47,257,1268,1898,701,622,346,111,109,210,27,437,1381,622,7,1226,226,1682,94,63,502,12,1308,723,215,276,460,7,159,599,78,1198,304,268,588,1086,44,1389,3,654,1602,834,165,570,736,1289,817,496,396,977,886,912,926,395,395,401,334,262,491,1138,78,0,757,622,10,299,85,355,1097,312,633,452,1409,27,275,458,101,393,508,1206,1,788,51,299,74,560,143,1610,237,223,1259,669,286,1046,668,733,508,665,354,651,40,1374,495,778,101,578,78,17,358,621,1080,38,142,33,182,538,912,76,446,79,1193,70,477,161,498,487,642,901,464,210,916,1410,674,71,208,709,304,80,1048,87,386,1665,907,573,305,974,242,836,811,90,11,64,175,98,162,390,69,145,468,818,1637,21,730,15,590,620,459,5,392,119,134,496,925,367,16,16,1443,687,1045,1704,256,667,10,850,1555,831,103,658,1097,745,380,48,210,994,163,428,669,1547,833,4,177,222,342,882,69,1350,500,154,218,358,183,83,739,297,1302,368,53,524,577,765,149,801,17,206,293,578,94,149,702,861,998,512,364,525,1849,682,1,204,96,119,815,118,1317,103,688,641,317,361,364,332,1020,1522,5,306,460,527,206,406,93,1433,221,70,1116,894,1240,157,299,812,121,1324,166,254,429,89,599,92,540,77,323,156,546,374,184,666,126,812,888,1195,412,305,325,216,1165,274,705,556,135,35,260,107,371,1515,125,703,149,433,515,698,163,369,537,63,1119,346,321,166,157,326,173,1022,50,929,14,1100,1289,334,1017,72,510,203,417,562,147,1098,1371,396,60,941,266,1195,960,629,698,46,443,1278,1601,1123,14,114,928,98,561,742,1501,860,610,941,591,3,120,1362,1176,75,185,144,851,570,55,317,126,179,202,1552,854,585,195,70,756,328,720,732,851,1080,1303,277,6,214,85,136,1594,469,345,176,835,126,1035,1006,66,1082,26,31,10,942,1546,186,575,712,775,14,920,169,733,220,1069,1300,19,47,816,675,102,307,1336,5,37,6,1258,340,373,26,42,4,358,260,174,635,245,108,466,891,662,658,341,10,777,613,749,164,118,235,997,74,674,120,501,924,1393,601,3,374,8,187,58,13,284,20,26,541,381,281,1135,19,1538,1306,1292,643,538,653,716,614,47,245,198,926,1845,95,864,234,476,18,1002,240,326,293,955,1196,907,129,115,250,991,1313,1801,60,183,16,150,440,900]
#crabPositions = [16,1,2,0,4,2,7,1,2,14]

##########################
# part 1
idealPosition = median(crabPositions)
fuelUsed = 0
# fuel is the distance from crab position to median
for crab in crabPositions:
    fuelUsed += abs(crab - idealPosition)
# answer
print(fuelUsed)

##########################
# part 2
oldFuelUsed = 1000000000
# brute force for all possible medians
for i in range(1, len(crabPositions)):
    newFuelUsed = 0
    for crab in crabPositions:
        # this is the addition version of n!, it's written as ((n)*(n+1))/2
        nthTriangle = ((abs(i - crab))*(abs(i - crab) + 1))/2
        newFuelUsed += nthTriangle
    # always keep the most efficient run
    if newFuelUsed < oldFuelUsed:
        oldFuelUsed = newFuelUsed
# answer
print(oldFuelUsed)