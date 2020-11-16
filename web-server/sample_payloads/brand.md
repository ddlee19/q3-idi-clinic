### **Get Brand**
#### /api/v1.0/brands/<int\:brand_id>

**Example 1 of 1:**

/api/v1.0/brands/1
```
{
  "agg_stats": {
    "forest_area": 6324462.752470586, 
    "land_area": 7459526.92552941, 
    "remaining_proportion_of_forest": 0.5972332945817617, 
    "risk_score_current": 3, 
    "risk_score_future": 3, 
    "risk_score_past": 5, 
    "treeloss_2001": 102626.9054117647, 
    "treeloss_2002": 81867.47823529411, 
    "treeloss_2003": 51089.06152941177, 
    "treeloss_2004": 184782.77258823533, 
    "treeloss_2005": 189246.92682352941, 
    "treeloss_2006": 172939.17635294114, 
    "treeloss_2007": 149832.91164705885, 
    "treeloss_2008": 143089.3605882353, 
    "treeloss_2009": 167277.06105882346, 
    "treeloss_2010": 186913.95776470585, 
    "treeloss_2011": 152593.7936470588, 
    "treeloss_2012": 171647.49811764708, 
    "treeloss_2013": 104544.57952941176, 
    "treeloss_2014": 156248.37635294118, 
    "treeloss_2015": 91170.6677647059, 
    "treeloss_2016": 151785.0458823529, 
    "treeloss_2017": 100775.19988235293, 
    "treeloss_2018": 97893.75070588234, 
    "treeloss_2019": 90958.50247058822, 
    "treeloss_sum": 2547283.026352941, 
    "treeloss_sum_proportion_of_forest": 0.4027667054182384, 
    "treeloss_sum_proportion_of_land": 0.3414805056383865
  }, 
  "avg_stats": {
    "forest_area": {
      "max": 738690.4058823528, 
      "mean": 567124.4817285067, 
      "min": 393741.53576470603, 
      "quartile_1": 471109.02529411775, 
      "quartile_2": 626005.4265882352, 
      "quartile_3": 676415.4225882353, 
      "std": 121206.34677502552
    }, 
    "land_area": {
      "max": 787341.6123529413, 
      "mean": 674286.3435746606, 
      "min": 501693.1665882354, 
      "quartile_1": 554527.1964705883, 
      "quartile_2": 724651.0856470588, 
      "quartile_3": 784654.4191764706, 
      "std": 119133.85070087097
    }, 
    "remaining_proportion_of_forest": {
      "max": 0.7878322261166021, 
      "mean": 0.5956105185123309, 
      "min": 0.2963054393308261, 
      "quartile_1": 0.4556955711058951, 
      "quartile_2": 0.6793647278851342, 
      "quartile_3": 0.7471171942707941, 
      "std": 0.18058596859734696
    }, 
    "risk_score_current": {
      "max": 5.0, 
      "mean": 2.923076923076923, 
      "min": 1.0, 
      "quartile_1": 2.0, 
      "quartile_2": 3.0, 
      "quartile_3": 4.0, 
      "std": 1.3821202589704016
    }, 
    "risk_score_future": {
      "max": 4.0, 
      "mean": 2.923076923076923, 
      "min": 1.0, 
      "quartile_1": 3.0, 
      "quartile_2": 3.0, 
      "quartile_3": 3.0, 
      "std": 0.8623164985025763
    }, 
    "risk_score_past": {
      "max": 5.0, 
      "mean": 2.6923076923076925, 
      "min": 1.0, 
      "quartile_1": 1.0, 
      "quartile_2": 2.0, 
      "quartile_3": 4.0, 
      "std": 1.6012815380508714
    }, 
    "treeloss_2001": {
      "max": 35584.66694117647, 
      "mean": 10901.265149321263, 
      "min": 1250.520705882353, 
      "quartile_1": 3312.954, 
      "quartile_2": 7900.675411764706, 
      "quartile_3": 12387.883764705879, 
      "std": 11310.636834931285
    }, 
    "treeloss_2002": {
      "max": 19858.443882352938, 
      "mean": 7604.801837104073, 
      "min": 1519.1414117647055, 
      "quartile_1": 2411.195647058824, 
      "quartile_2": 4320.922235294118, 
      "quartile_3": 12979.641176470586, 
      "std": 6353.336045050285
    }, 
    "treeloss_2003": {
      "max": 9522.255882352942, 
      "mean": 4495.184253393665, 
      "min": 965.3502352941176, 
      "quartile_1": 2526.537882352941, 
      "quartile_2": 4373.221764705882, 
      "quartile_3": 5039.222117647058, 
      "std": 2318.690518451777
    }, 
    "treeloss_2004": {
      "max": 55736.94635294117, 
      "mean": 17445.796126696834, 
      "min": 1890.5572941176472, 
      "quartile_1": 5544.13411764706, 
      "quartile_2": 9381.579176470588, 
      "quartile_3": 30289.244823529414, 
      "std": 17016.78780478587
    }, 
    "treeloss_2005": {
      "max": 44478.44188235295, 
      "mean": 18132.384678733037, 
      "min": 2027.8916470588235, 
      "quartile_1": 4923.428117647059, 
      "quartile_2": 8957.844705882353, 
      "quartile_3": 29266.16647058826, 
      "std": 16707.11541636824
    }, 
    "treeloss_2006": {
      "max": 74919.66458823529, 
      "mean": 14157.761809954749, 
      "min": 1357.4509411764705, 
      "quartile_1": 3744.818470588235, 
      "quartile_2": 6344.681647058823, 
      "quartile_3": 10570.857529411764, 
      "std": 20692.465176595746
    }, 
    "treeloss_2007": {
      "max": 39500.17517647058, 
      "mean": 13737.331438914025, 
      "min": 1971.682588235294, 
      "quartile_1": 5686.210588235294, 
      "quartile_2": 7299.691764705883, 
      "quartile_3": 25254.99105882353, 
      "std": 11822.277379941961
    }, 
    "treeloss_2008": {
      "max": 33260.195294117635, 
      "mean": 13083.378407239818, 
      "min": 1841.7621176470586, 
      "quartile_1": 4555.848705882353, 
      "quartile_2": 8721.263647058824, 
      "quartile_3": 18921.94764705882, 
      "std": 11196.075015457325
    }, 
    "treeloss_2009": {
      "max": 30598.12764705882, 
      "mean": 14715.773782805427, 
      "min": 4736.666117647059, 
      "quartile_1": 9389.27188235294, 
      "quartile_2": 14200.12164705882, 
      "quartile_3": 18210.683647058824, 
      "std": 7367.365809187635
    }, 
    "treeloss_2010": {
      "max": 53760.908470588234, 
      "mean": 18876.855800904978, 
      "min": 5835.954352941178, 
      "quartile_1": 8220.414705882353, 
      "quartile_2": 10558.93976470588, 
      "quartile_3": 21876.71647058824, 
      "std": 16048.115971901861
    }, 
    "treeloss_2011": {
      "max": 44427.42000000001, 
      "mean": 15504.474135746605, 
      "min": 4045.695529411765, 
      "quartile_1": 6637.9450588235295, 
      "quartile_2": 8315.128235294118, 
      "quartile_3": 16329.763058823522, 
      "std": 13849.287122270776
    }, 
    "treeloss_2012": {
      "max": 39359.16494117648, 
      "mean": 16394.008723981897, 
      "min": 5813.892705882354, 
      "quartile_1": 7629.446823529412, 
      "quartile_2": 12199.32176470588, 
      "quartile_3": 22558.92952941176, 
      "std": 11832.923830178557
    }, 
    "treeloss_2013": {
      "max": 24486.81952941176, 
      "mean": 10143.896904977375, 
      "min": 3606.417529411765, 
      "quartile_1": 6011.136, 
      "quartile_2": 7835.301176470587, 
      "quartile_3": 11271.338823529411, 
      "std": 6676.733276635067
    }, 
    "treeloss_2014": {
      "max": 26356.62847058824, 
      "mean": 14372.600932126694, 
      "min": 7080.071999999999, 
      "quartile_1": 8445.618705882354, 
      "quartile_2": 12879.091411764704, 
      "quartile_3": 18182.68164705882, 
      "std": 6745.44948258766
    }, 
    "treeloss_2015": {
      "max": 20547.095647058817, 
      "mean": 8399.795076923076, 
      "min": 4159.0912941176475, 
      "quartile_1": 6758.684117647057, 
      "quartile_2": 7832.235176470587, 
      "quartile_3": 8851.569176470588, 
      "std": 4071.1554851732553
    }, 
    "treeloss_2016": {
      "max": 26608.01329411764, 
      "mean": 14414.485140271492, 
      "min": 4414.340470588235, 
      "quartile_1": 9900.106235294115, 
      "quartile_2": 12381.195176470586, 
      "quartile_3": 21187.636941176468, 
      "std": 7144.312244473174
    }, 
    "treeloss_2017": {
      "max": 15164.728588235295, 
      "mean": 9404.12402714932, 
      "min": 4726.205294117647, 
      "quartile_1": 6953.113764705882, 
      "quartile_2": 8700.815294117647, 
      "quartile_3": 11924.166000000001, 
      "std": 3253.909560799033
    }, 
    "treeloss_2018": {
      "max": 13463.163529411766, 
      "mean": 9086.602805429864, 
      "min": 4058.377411764706, 
      "quartile_1": 7662.021529411765, 
      "quartile_2": 9006.846000000001, 
      "quartile_3": 11156.488941176467, 
      "std": 2860.4984272312836
    }, 
    "treeloss_2019": {
      "max": 15285.096705882352, 
      "mean": 8640.960108597284, 
      "min": 3816.843176470588, 
      "quartile_1": 4554.696352941177, 
      "quartile_2": 7147.039411764706, 
      "quartile_3": 13958.372470588234, 
      "std": 4510.0733949921105
    }, 
    "treeloss_sum": {
      "max": 478691.7292941176, 
      "mean": 239511.48114027147, 
      "min": 102604.01611764707, 
      "quartile_1": 134261.09788235294, 
      "quartile_2": 183196.78941176477, 
      "quartile_3": 347850.93141176464, 
      "std": 139838.69980946011
    }, 
    "treeloss_sum_proportion_of_forest": {
      "max": 0.7036945606691739, 
      "mean": 0.40438948148766907, 
      "min": 0.21216777388339808, 
      "quartile_1": 0.2528828057292058, 
      "quartile_2": 0.3206352721148657, 
      "quartile_3": 0.5443044288941049, 
      "std": 0.18058596859734696
    }, 
    "treeloss_sum_proportion_of_land": {
      "max": 0.6100669512529168, 
      "mean": 0.3380772390960229, 
      "min": 0.17745668901334505, 
      "quartile_1": 0.2189495243072779, 
      "quartile_2": 0.2709174942985928, 
      "quartile_3": 0.4418043273138136, 
      "std": 0.15375903563792448
    }
  }, 
  "brand": "Ferrero", 
  "brandid": 1, 
  "country": "Luxembourg", 
  "country_count": 1, 
  "description": "Ferrero SpA, more commonly known as Ferrero Group, is an Italian manufacturer of branded chocolate and confectionery products, and the second biggest chocolate producer and confectionery company in the world. It was founded in 1946 in Alba, Piedmont, Italy, by Pietro Ferrero, a confectioner and small-time pastry maker who laid the groundwork for Nutella and famously added hazelnut to save money on chocolate. Family-owned to this day, the company has built itself into an international group with commercial interests in the Americas, Australasia, Asia and Africa, as well as in Western and Eastern Europe. The Group, which is headquartered in Luxembourg, has three R&D centres and twenty production plants.  Thanks to the dedicated commitment of 22,000 employees, brands like Nutella, Ferrero Rocher, Mon Cheri, Tic Tac, Kinder Bueno, Kinder Sorpresa and Raffaello have become worldwide successes.  For Ferrero, respecting nature is so important that the Group considers the objectives of its environmental policy on a par with its production goals. In order to do this, it has set ambitious goals on every impact it could have on the environment.", 
  "external_link": "https://www.ferrerocsr.com/", 
  "mill_count": 13, 
  "mills": [
    {
      "country": "Indonesia", 
      "mill_name": "BANGUN BANDAR MILL", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 5, 
      "risk_score_future": 4, 
      "risk_score_past": 2, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Serdang Bedagai", 
      "umlid": "po1000000451"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUNGAI LIPUT", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 3, 
      "risk_score_future": 4, 
      "risk_score_past": 1, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Aceh Tamiang", 
      "umlid": "po1000001251"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "GUNTUNG IDAMAN NUSA 2", 
      "prnt_comp": "GUNTUNG IDAMAN NUSA", 
      "risk_score_current": 5, 
      "risk_score_future": 4, 
      "risk_score_past": 3, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Indragiri Hilir", 
      "umlid": "po1000006505"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "TANAH GAMBUS", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 4, 
      "risk_score_future": 3, 
      "risk_score_past": 3, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Batu Bara", 
      "umlid": "po1000000352"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "BLANG SIMPO", 
      "prnt_comp": "PERKASA SUBUR SAKTI", 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 1, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Aceh Timur", 
      "umlid": "po1000000706"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "PKS 2", 
      "prnt_comp": "DHARMA SATYA NUSANTARA", 
      "risk_score_current": 1, 
      "risk_score_future": 3, 
      "risk_score_past": 1, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Kalimantan Timur", 
      "sub_state": "Kutai Timur", 
      "umlid": "po1000000939"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "NAGA SAKTI", 
      "prnt_comp": "BUANA WIRALESTARI MAS", 
      "risk_score_current": 4, 
      "risk_score_future": 3, 
      "risk_score_past": 4, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Kampar", 
      "umlid": "po1000001061"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "AEK LOBA", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 3, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Asahan", 
      "umlid": "po1000001252"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "LAE BUTAR", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 2, 
      "risk_score_future": 3, 
      "risk_score_past": 2, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Aceh Singkil", 
      "umlid": "po1000001775"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SEUMANYAM", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 1, 
      "risk_score_future": 3, 
      "risk_score_past": 1, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Nagan Raya", 
      "umlid": "po1000001777"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "BATANG KULIM", 
      "prnt_comp": "MUSIM MAS", 
      "risk_score_current": 3, 
      "risk_score_future": 2, 
      "risk_score_past": 5, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Pelalawan", 
      "umlid": "po1000000054"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "PANGKALAN LESUNG", 
      "prnt_comp": "MUSIM MAS", 
      "risk_score_current": 3, 
      "risk_score_future": 2, 
      "risk_score_past": 5, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Pelalawan", 
      "umlid": "po1000000355"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUKAJADI SAWIT MEKAR 2", 
      "prnt_comp": "SUKAJADI SAWIT MEKAR", 
      "risk_score_current": 1, 
      "risk_score_future": 1, 
      "risk_score_past": 5, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Kalimantan Tengah", 
      "sub_state": "Kotawaringin Timur", 
      "umlid": "po1000000134"
    }
  ], 
  "nonrspo_mill_count": 0, 
  "rspo_member_since": "2005-01-17", 
  "rspo_mill_count": 13, 
  "supplier_count": 7, 
  "suppliers": [
    {
      "country": "Indonesia", 
      "mill_count": 6, 
      "name": "SOCFIN INDONESIA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 2, 
      "name": "MUSIM MAS"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "BUANA WIRALESTARI MAS"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "DHARMA SATYA NUSANTARA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "GUNTUNG IDAMAN NUSA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "PERKASA SUBUR SAKTI"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "SUKAJADI SAWIT MEKAR"
    }
  ]
}
```