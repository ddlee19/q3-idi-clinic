### **Get Brand Aggregate Stats**
#### /api/v1.0/brands/stats

**Example 1 of 1**
```
{
  "avg_hectares_lost_per_brand": 13188634, 
  "brands": [
    {
      "avg_risk_score_current": 3.081, 
      "brand": "Colgate-Palmolive Company", 
      "brandid": 10, 
      "country": "United States", 
      "mill_count": 178, 
      "nonrspo_mill_count": 127, 
      "risk_score_current": 5, 
      "risk_score_future": 5, 
      "risk_score_past": 2, 
      "rspo_mill_count": 51
    }, 
    {
      "avg_risk_score_current": 3.065, 
      "brand": "Ferrero", 
      "brandid": 1, 
      "country": "Luxembourg", 
      "mill_count": 31, 
      "nonrspo_mill_count": 9, 
      "risk_score_current": 3, 
      "risk_score_future": 1, 
      "risk_score_past": 5, 
      "rspo_mill_count": 22
    }, 
    {
      "avg_risk_score_current": 2.94, 
      "brand": "Nestl\u00e9", 
      "brandid": 11, 
      "country": "Switzerland", 
      "mill_count": 934, 
      "nonrspo_mill_count": 757, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 177
    }, 
    {
      "avg_risk_score_current": 2.938, 
      "brand": "Mars, Incorporated", 
      "brandid": 12, 
      "country": "United States", 
      "mill_count": 770, 
      "nonrspo_mill_count": 604, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_mill_count": 166
    }, 
    {
      "avg_risk_score_current": 2.936, 
      "brand": "General Mills, Inc", 
      "brandid": 6, 
      "country": "United States", 
      "mill_count": 957, 
      "nonrspo_mill_count": 778, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 179
    }, 
    {
      "avg_risk_score_current": 2.935, 
      "brand": "Kellogg Company", 
      "brandid": 2, 
      "country": "United States", 
      "mill_count": 954, 
      "nonrspo_mill_count": 773, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 181
    }, 
    {
      "avg_risk_score_current": 2.927, 
      "brand": "PepsiCo", 
      "brandid": 3, 
      "country": "United States", 
      "mill_count": 958, 
      "nonrspo_mill_count": 779, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 179
    }, 
    {
      "avg_risk_score_current": 2.925, 
      "brand": "Johnson & Johnson", 
      "brandid": 5, 
      "country": "United States", 
      "mill_count": 777, 
      "nonrspo_mill_count": 630, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 147
    }, 
    {
      "avg_risk_score_current": 2.924, 
      "brand": "The Hershey Company", 
      "brandid": 7, 
      "country": "United States", 
      "mill_count": 933, 
      "nonrspo_mill_count": 759, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 174
    }, 
    {
      "avg_risk_score_current": 2.922, 
      "brand": "L'Oreal", 
      "brandid": 8, 
      "country": "France", 
      "mill_count": 831, 
      "nonrspo_mill_count": 663, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 168
    }, 
    {
      "avg_risk_score_current": 2.913, 
      "brand": "Royal FrieslandCampina N.V.", 
      "brandid": 4, 
      "country": "Netherlands", 
      "mill_count": 384, 
      "nonrspo_mill_count": 293, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 91
    }, 
    {
      "avg_risk_score_current": 2.909, 
      "brand": "The Procter & Gamble Company", 
      "brandid": 9, 
      "country": "United States", 
      "mill_count": 472, 
      "nonrspo_mill_count": 393, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 79
    }, 
    {
      "avg_risk_score_current": 2.855, 
      "brand": "Unilever", 
      "brandid": 13, 
      "country": "Netherlands", 
      "mill_count": 248, 
      "nonrspo_mill_count": 215, 
      "risk_score_current": 1, 
      "risk_score_future": 3, 
      "risk_score_past": 1, 
      "rspo_mill_count": 33
    }
  ], 
  "dist_of_brand_avgs_for_treecover": {
    "forest_area": {
      "max": 81372.33240995077, 
      "mean": 64017.45941709475, 
      "min": 40669.36523339657, 
      "quartile_1": 63506.88749525615, 
      "quartile_2": 64479.98155364814, 
      "quartile_3": 64969.36664569085, 
      "std": 8822.224597715463
    }, 
    "land_area": {
      "max": 93494.07737911376, 
      "mean": 74181.51738419666, 
      "min": 46976.89371916507, 
      "quartile_1": 73254.15019203046, 
      "quartile_2": 74660.26042609861, 
      "quartile_3": 76565.12137320495, 
      "std": 10156.741723644674
    }, 
    "remaining_proportion_of_forest": {
      "max": 0.5945867259076147, 
      "mean": 0.5704795181599341, 
      "min": 0.534801036224924, 
      "quartile_1": 0.5687452414441122, 
      "quartile_2": 0.5717592098105282, 
      "quartile_3": 0.573449153421871, 
      "std": 0.012924927397724129
    }, 
    "risk_score_current": {
      "max": 3.0813953488372094, 
      "mean": 2.9437837210295035, 
      "min": 2.854625550660793, 
      "quartile_1": 2.9219330855018586, 
      "quartile_2": 2.927038626609442, 
      "quartile_3": 2.937830687830688, 
      "std": 0.0614566217078667
    }, 
    "risk_score_future": {
      "max": 3.0290697674418605, 
      "mean": 2.962585074331517, 
      "min": 2.903225806451613, 
      "quartile_1": 2.9570815450643777, 
      "quartile_2": 2.9609544468546636, 
      "quartile_3": 2.9701327433628317, 
      "std": 0.02758954189621564
    }, 
    "risk_score_past": {
      "max": 3.225806451612903, 
      "mean": 2.9733157877466843, 
      "min": 2.8237885462555066, 
      "quartile_1": 2.947089947089947, 
      "quartile_2": 2.9553903345724906, 
      "quartile_3": 2.986081370449679, 
      "std": 0.08779567976199684
    }, 
    "treeloss_2001": {
      "max": 681.8419668307849, 
      "mean": 583.7486505664112, 
      "min": 541.4174091406084, 
      "quartile_1": 565.2927516252834, 
      "quartile_2": 574.4492359252723, 
      "quartile_3": 579.0028644501276, 
      "std": 41.61843819078603
    }, 
    "treeloss_2002": {
      "max": 786.1981912412547, 
      "mean": 607.898929343819, 
      "min": 398.63048197343454, 
      "quartile_1": 601.4314013099881, 
      "quartile_2": 605.5418675169183, 
      "quartile_3": 623.8533878248975, 
      "std": 86.29607141636474
    }, 
    "treeloss_2003": {
      "max": 472.06692718320835, 
      "mean": 370.27005581959577, 
      "min": 198.68616318785575, 
      "quartile_1": 358.83183342009386, 
      "quartile_2": 395.8149693861197, 
      "quartile_3": 397.7503727770177, 
      "std": 64.27643993573452
    }, 
    "treeloss_2004": {
      "max": 1145.445072298523, 
      "mean": 984.4081249905053, 
      "min": 894.0058358413132, 
      "quartile_1": 943.2961093374148, 
      "quartile_2": 986.6609801298458, 
      "quartile_3": 996.5040378151278, 
      "std": 74.87710479448724
    }, 
    "treeloss_2005": {
      "max": 1231.9462855662086, 
      "mean": 945.1583130449307, 
      "min": 702.1300075901328, 
      "quartile_1": 925.9213260441719, 
      "quartile_2": 932.9986523719167, 
      "quartile_3": 962.3166236474525, 
      "std": 113.6271639996394
    }, 
    "treeloss_2006": {
      "max": 1294.5033956983673, 
      "mean": 1101.2962351464705, 
      "min": 704.3542201138517, 
      "quartile_1": 1089.534120964655, 
      "quartile_2": 1102.4433382038044, 
      "quartile_3": 1143.3443915010812, 
      "std": 137.29209685914634
    }, 
    "treeloss_2007": {
      "max": 1339.0495786473184, 
      "mean": 1117.7624503332158, 
      "min": 729.1336736242886, 
      "quartile_1": 1081.944574677455, 
      "quartile_2": 1120.825607507243, 
      "quartile_3": 1158.136546878671, 
      "std": 144.2281517596145
    }, 
    "treeloss_2008": {
      "max": 1395.3413174397513, 
      "mean": 1153.3551042100557, 
      "min": 739.7165806451611, 
      "quartile_1": 1133.1436041985571, 
      "quartile_2": 1161.8606523605165, 
      "quartile_3": 1191.5826527766908, 
      "std": 145.681992837899
    }, 
    "treeloss_2009": {
      "max": 1871.25434568541, 
      "mean": 1510.8273752149476, 
      "min": 729.0410094876662, 
      "quartile_1": 1507.85217931336, 
      "quartile_2": 1555.358511954459, 
      "quartile_3": 1577.4440664961642, 
      "std": 258.6193528037765
    }, 
    "treeloss_2010": {
      "max": 1386.926358642135, 
      "mean": 1065.4562332940177, 
      "min": 898.8480910815937, 
      "quartile_1": 1007.9283105182586, 
      "quartile_2": 1049.361413066111, 
      "quartile_3": 1081.5417965768238, 
      "std": 118.55756496183865
    }, 
    "treeloss_2011": {
      "max": 1682.3105597305012, 
      "mean": 1268.9778366387472, 
      "min": 1068.3321404174571, 
      "quartile_1": 1189.2038040673515, 
      "quartile_2": 1250.4001690009345, 
      "quartile_3": 1277.4372585572182, 
      "std": 150.35030552983304
    }, 
    "treeloss_2012": {
      "max": 2331.869224151334, 
      "mean": 1851.0015560425443, 
      "min": 1358.8117798861483, 
      "quartile_1": 1837.2686409028727, 
      "quartile_2": 1852.17898866356, 
      "quartile_3": 1858.4417698754612, 
      "std": 221.1545917844891
    }, 
    "treeloss_2013": {
      "max": 1221.8718595491057, 
      "mean": 964.8373487397473, 
      "min": 732.6757229601519, 
      "quartile_1": 944.8296951447251, 
      "quartile_2": 959.8158593789458, 
      "quartile_3": 967.7326218115567, 
      "std": 111.46090125384762
    }, 
    "treeloss_2014": {
      "max": 2158.525329359938, 
      "mean": 1523.5814144751116, 
      "min": 1052.122075901328, 
      "quartile_1": 1478.487818860878, 
      "quartile_2": 1503.4904132762326, 
      "quartile_3": 1512.0042968590901, 
      "std": 250.3894607648432
    }, 
    "treeloss_2015": {
      "max": 1410.5334133675253, 
      "mean": 1197.6392274939667, 
      "min": 706.7366072106262, 
      "quartile_1": 1194.2888580765637, 
      "quartile_2": 1217.591191650853, 
      "quartile_3": 1262.1962954947855, 
      "std": 170.23208592869233
    }, 
    "treeloss_2016": {
      "max": 2084.5370581395355, 
      "mean": 1824.1552636979166, 
      "min": 1164.777074003795, 
      "quartile_1": 1781.674312791783, 
      "quartile_2": 1842.8288045093839, 
      "quartile_3": 1953.4136214833757, 
      "std": 238.7097382181238
    }, 
    "treeloss_2017": {
      "max": 1214.6275086810053, 
      "mean": 1001.0125645656542, 
      "min": 648.5910626185957, 
      "quartile_1": 1000.1948426411844, 
      "quartile_2": 1016.9667407969652, 
      "quartile_3": 1023.3916139122322, 
      "std": 126.30546671553515
    }, 
    "treeloss_2018": {
      "max": 1150.3762964498576, 
      "mean": 962.6573628701198, 
      "min": 640.6268083491462, 
      "quartile_1": 960.0474275867481, 
      "quartile_2": 969.2167893941311, 
      "quartile_3": 988.3294790478077, 
      "std": 115.38584588737818
    }, 
    "treeloss_2019": {
      "max": 1055.092962943768, 
      "mean": 895.7439180850249, 
      "min": 581.1268690702088, 
      "quartile_1": 886.9761225806445, 
      "quartile_2": 892.8160167619642, 
      "quartile_3": 923.967549872122, 
      "std": 112.44821364718027
    }, 
    "treeloss_sum": {
      "max": 25831.998657683336, 
      "mean": 20929.7879645728, 
      "min": 14530.565111954456, 
      "quartile_1": 20863.716808953664, 
      "quartile_2": 20954.12246078432, 
      "quartile_3": 21228.6378624579, 
      "std": 2519.777475494593
    }, 
    "treeloss_sum_proportion_of_forest": {
      "max": 0.4651989637750761, 
      "mean": 0.4295204818400657, 
      "min": 0.40541327409238476, 
      "quartile_1": 0.42655084657812853, 
      "quartile_2": 0.42824079018947114, 
      "quartile_3": 0.43125475855588835, 
      "std": 0.01292492739772425
    }, 
    "treeloss_sum_proportion_of_land": {
      "max": 0.3741538552130954, 
      "mean": 0.34837535823036975, 
      "min": 0.3306936318462948, 
      "quartile_1": 0.3465624346578897, 
      "quartile_2": 0.34845191090005745, 
      "quartile_3": 0.3501859380021145, 
      "std": 0.010230700156102874
    }
  }, 
  "mill_dist_all": {
    "max": 958, 
    "mean": 648.2307692307693, 
    "min": 31, 
    "quartile_1": 384, 
    "quartile_2": 777, 
    "quartile_3": 934, 
    "std": 338.564655038038
  }, 
  "mill_dist_non_rspo": {
    "max": 767, 
    "mean": 512.3846153846154, 
    "min": 9, 
    "quartile_1": 288, 
    "quartile_2": 620, 
    "quartile_3": 749, 
    "std": 275.2818369300629
  }, 
  "mill_dist_rspo": {
    "max": 194, 
    "mean": 135.84615384615384, 
    "min": 22, 
    "quartile_1": 90, 
    "quartile_2": 173, 
    "quartile_3": 187, 
    "std": 63.87337232609291
  }, 
  "total_num_countries": 1, 
  "total_num_mills": 1084, 
  "total_num_mills_with_brands": 1051, 
  "total_num_suppliers": 840
}
```
