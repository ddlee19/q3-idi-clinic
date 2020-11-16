### **Get Brand Aggregate Stats**
#### /api/v1.0/brands/stats

**Example 1 of 1**
```
{
  "avg_hectares_lost_per_brand": 18312487, 
  "brands": [
    {
      "brand": "General Mills, Inc", 
      "brandid": 6, 
      "country": "United States", 
      "mill_count": 826, 
      "nonrspo_mill_count": 672, 
      "risk_score_current": 2, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_mill_count": 154
    }, 
    {
      "brand": "Kellogg Company", 
      "brandid": 2, 
      "country": "United States", 
      "mill_count": 822, 
      "nonrspo_mill_count": 666, 
      "risk_score_current": 2, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_mill_count": 156
    }, 
    {
      "brand": "PepsiCo", 
      "brandid": 3, 
      "country": "United States", 
      "mill_count": 820, 
      "nonrspo_mill_count": 667, 
      "risk_score_current": 2, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_mill_count": 153
    }, 
    {
      "brand": "The Hershey Company", 
      "brandid": 7, 
      "country": "United States", 
      "mill_count": 777, 
      "nonrspo_mill_count": 633, 
      "risk_score_current": 2, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_mill_count": 144
    }, 
    {
      "brand": "L'Oreal", 
      "brandid": 8, 
      "country": "France", 
      "mill_count": 686, 
      "nonrspo_mill_count": 540, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 146
    }, 
    {
      "brand": "Johnson & Johnson", 
      "brandid": 5, 
      "country": "United States", 
      "mill_count": 589, 
      "nonrspo_mill_count": 483, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_mill_count": 106
    }, 
    {
      "brand": "Royal FrieslandCampina N.V.", 
      "brandid": 4, 
      "country": "Netherlands", 
      "mill_count": 92, 
      "nonrspo_mill_count": 49, 
      "risk_score_current": 5, 
      "risk_score_future": 3, 
      "risk_score_past": 5, 
      "rspo_mill_count": 43
    }, 
    {
      "brand": "Ferrero", 
      "brandid": 1, 
      "country": "Luxembourg", 
      "mill_count": 13, 
      "nonrspo_mill_count": 0, 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 5, 
      "rspo_mill_count": 13
    }
  ], 
  "dist_of_brand_avgs_for_treecover": {
    "forest_area": {
      "max": 629036.4076596639, 
      "mean": 593787.106732518, 
      "min": 567124.4817285067, 
      "quartile_1": 591715.3244347109, 
      "quartile_2": 592475.5662714059, 
      "quartile_3": 592902.6186725422, 
      "std": 16779.480164909168
    }, 
    "land_area": {
      "max": 761100.3005378152, 
      "mean": 709037.9483549171, 
      "min": 674286.3435746606, 
      "quartile_1": 704813.8358344247, 
      "quartile_2": 706213.4846560126, 
      "quartile_3": 707380.8861575003, 
      "std": 23833.699895661473
    }, 
    "remaining_proportion_of_forest": {
      "max": 0.595610518512331, 
      "mean": 0.5812106165046218, 
      "min": 0.5183073127982093, 
      "quartile_1": 0.5866363464697236, 
      "quartile_2": 0.5906912475646464, 
      "quartile_3": 0.5912623026751994, 
      "std": 0.0256296163210958
    }, 
    "risk_score_current": {
      "max": 3.607142857142857, 
      "mean": 3.05832872254613, 
      "min": 2.923076923076923, 
      "quartile_1": 2.9772846638655466, 
      "quartile_2": 2.9859505390208088, 
      "quartile_3": 3.008117594696842, 
      "std": 0.22345182041903788
    }, 
    "risk_score_future": {
      "max": 2.972270363951473, 
      "mean": 2.9463754672541445, 
      "min": 2.919236417033774, 
      "quartile_1": 2.9373579007199697, 
      "quartile_2": 2.9517126972740315, 
      "quartile_3": 2.953909579395961, 
      "std": 0.0177620726696675
    }, 
    "risk_score_past": {
      "max": 3.5952380952380953, 
      "mean": 3.0217238583267854, 
      "min": 2.6923076923076925, 
      "quartile_1": 2.964732643490672, 
      "quartile_2": 2.970581521086147, 
      "quartile_3": 2.9991929355434044, 
      "std": 0.25367568202692675
    }, 
    "treeloss_2001": {
      "max": 10901.265149321265, 
      "mean": 8540.737882627218, 
      "min": 7697.947595269645, 
      "quartile_1": 7828.43160992395, 
      "quartile_2": 7890.932421200333, 
      "quartile_3": 8627.795448580317, 
      "std": 1255.039661428139
    }, 
    "treeloss_2002": {
      "max": 9545.52307983193, 
      "mean": 8018.621843169127, 
      "min": 7604.801837104072, 
      "quartile_1": 7759.055826109759, 
      "quartile_2": 7791.195186674417, 
      "quartile_3": 7902.639761476791, 
      "std": 629.0556496739176
    }, 
    "treeloss_2003": {
      "max": 4784.62062184874, 
      "mean": 4337.682446990969, 
      "min": 4157.38231257008, 
      "quartile_1": 4221.114917913477, 
      "quartile_2": 4255.978002298025, 
      "quartile_3": 4365.351512039786, 
      "std": 207.40608065633322
    }, 
    "treeloss_2004": {
      "max": 18344.366310924375, 
      "mean": 15627.56053713501, 
      "min": 14610.37293587522, 
      "quartile_1": 14787.995701039117, 
      "quartile_2": 14815.706212005041, 
      "quartile_3": 15924.954926336031, 
      "std": 1439.3847832226152
    }, 
    "treeloss_2005": {
      "max": 19865.592306722687, 
      "mean": 16205.444887151389, 
      "min": 15056.656454795726, 
      "quartile_1": 15093.087399957807, 
      "quartile_2": 15257.613801456864, 
      "quartile_3": 16453.17184226683, 
      "std": 1806.0504984870138
    }, 
    "treeloss_2006": {
      "max": 21286.4175, 
      "mean": 16621.278085168404, 
      "min": 14157.76180995475, 
      "quartile_1": 16107.014681679615, 
      "quartile_2": 16165.898850313322, 
      "quartile_3": 16364.359638490943, 
      "std": 2036.88591851256
    }, 
    "treeloss_2007": {
      "max": 18908.35804621849, 
      "mean": 15093.312416513, 
      "min": 13737.331438914027, 
      "quartile_1": 14571.420856850273, 
      "quartile_2": 14653.481272279307, 
      "quartile_3": 14759.840023524745, 
      "std": 1582.9671088128316
    }, 
    "treeloss_2008": {
      "max": 18294.504054621848, 
      "mean": 15047.830165828507, 
      "min": 13083.378407239816, 
      "quartile_1": 14721.940899048472, 
      "quartile_2": 14800.355587732414, 
      "quartile_3": 14925.769590526257, 
      "std": 1459.7821328584614
    }, 
    "treeloss_2009": {
      "max": 23891.69117647058, 
      "mean": 19434.264898859503, 
      "min": 14715.773782805427, 
      "quartile_1": 19383.496117465642, 
      "quartile_2": 19432.2671136051, 
      "quartile_3": 19556.01678817116, 
      "std": 2456.7004617572375
    }, 
    "treeloss_2010": {
      "max": 18876.855800904978, 
      "mean": 15316.743682719785, 
      "min": 14110.199028542449, 
      "quartile_1": 14241.80983139664, 
      "quartile_2": 14373.771004231396, 
      "quartile_3": 15467.213608406128, 
      "std": 1840.6138521563441
    }, 
    "treeloss_2011": {
      "max": 15504.474135746606, 
      "mean": 14162.760722133184, 
      "min": 13577.22946117067, 
      "quartile_1": 13644.684825920216, 
      "quartile_2": 13770.714357781673, 
      "quartile_3": 14321.867389554662, 
      "std": 823.885854473049
    }, 
    "treeloss_2012": {
      "max": 26816.306840336132, 
      "mean": 20970.417529972336, 
      "min": 16394.008723981897, 
      "quartile_1": 20681.90154019699, 
      "quartile_2": 20749.373948528177, 
      "quartile_3": 20846.776743028327, 
      "std": 2814.1383620286765
    }, 
    "treeloss_2013": {
      "max": 12150.053579831932, 
      "mean": 10728.040894215494, 
      "min": 10143.896904977377, 
      "quartile_1": 10512.466050418026, 
      "quartile_2": 10554.142264985552, 
      "quartile_3": 10694.297500110675, 
      "std": 600.3723996525874
    }, 
    "treeloss_2014": {
      "max": 15700.399920168067, 
      "mean": 14682.761191184964, 
      "min": 14372.600932126694, 
      "quartile_1": 14493.866018216157, 
      "quartile_2": 14547.17526913014, 
      "quartile_3": 14645.784950399124, 
      "std": 421.4097895436748
    }, 
    "treeloss_2015": {
      "max": 12526.222500000002, 
      "mean": 11057.985432146754, 
      "min": 8399.795076923077, 
      "quartile_1": 11198.074569890192, 
      "quartile_2": 11276.272599902935, 
      "quartile_3": 11323.357346583716, 
      "std": 1165.6430712413576
    }, 
    "treeloss_2016": {
      "max": 20318.281701680673, 
      "mean": 17085.174185587242, 
      "min": 14414.485140271492, 
      "quartile_1": 16934.46757712539, 
      "quartile_2": 17029.88927066543, 
      "quartile_3": 17050.725048705404, 
      "std": 1589.3457532544487
    }, 
    "treeloss_2017": {
      "max": 13812.922134453784, 
      "mean": 11289.628141589252, 
      "min": 9404.124027149319, 
      "quartile_1": 11155.786847216928, 
      "quartile_2": 11184.177302354761, 
      "quartile_3": 11210.223474169035, 
      "std": 1195.0433805443759
    }, 
    "treeloss_2018": {
      "max": 12217.36558403361, 
      "mean": 10289.239345917053, 
      "min": 9086.602805429862, 
      "quartile_1": 10147.420837760254, 
      "quartile_2": 10171.308176667491, 
      "quartile_3": 10190.863726576188, 
      "std": 866.4620010863513
    }, 
    "treeloss_2019": {
      "max": 11954.40593697479, 
      "mean": 9625.223988956654, 
      "min": 8640.960108597284, 
      "quartile_1": 9383.062241027765, 
      "quartile_2": 9401.282534190714, 
      "quartile_3": 9427.698124022645, 
      "std": 978.2945765477976
    }, 
    "treeloss_sum": {
      "max": 303639.2467521008, 
      "mean": 254134.70827786584, 
      "min": 239511.48114027147, 
      "quartile_1": 247192.12319765563, 
      "quartile_2": 247621.10358494497, 
      "quartile_3": 249500.95690498146, 
      "std": 20291.209390242137
    }, 
    "treeloss_sum_proportion_of_forest": {
      "max": 0.48169268720179065, 
      "mean": 0.4187893834953781, 
      "min": 0.40438948148766907, 
      "quartile_1": 0.40873769732480036, 
      "quartile_2": 0.4093087524353537, 
      "quartile_3": 0.4133636535302765, 
      "std": 0.02562961632109581
    }, 
    "treeloss_sum_proportion_of_land": {
      "max": 0.39672579233859695, 
      "mean": 0.34894429084120115, 
      "min": 0.3380772390960229, 
      "quartile_1": 0.34129333287364355, 
      "quartile_2": 0.3419902180906228, 
      "quartile_3": 0.34460615512536585, 
      "std": 0.019453631377365128
    }
  }, 
  "mill_dist_all": {
    "max": 826, 
    "mean": 578.125, 
    "min": 13, 
    "quartile_1": 464, 
    "quartile_2": 731, 
    "quartile_3": 820, 
    "std": 335.178177562749
  }, 
  "mill_dist_non_rspo": {
    "max": 660, 
    "mean": 523.0, 
    "min": 49, 
    "quartile_1": 507, 
    "quartile_2": 625, 
    "quartile_3": 656, 
    "std": 220.44576052474525
  }, 
  "mill_dist_rspo": {
    "max": 167, 
    "mean": 120.5, 
    "min": 13, 
    "quartile_1": 93, 
    "quartile_2": 151, 
    "quartile_3": 163, 
    "std": 60.41522986797286
  }, 
  "total_num_countries": 1, 
  "total_num_mills": 1095, 
  "total_num_mills_with_brands": 991, 
  "total_num_suppliers": 804
}
```
