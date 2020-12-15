### **Get Brand**
#### /api/v1.0/brands/<int\:brand_id>

**Example 1 of 1:**

/api/v1.0/brands/1
```
{
  "agg_stats": {
    "forest_area": 1102429.0867058823, 
    "land_area": 1273118.063294117, 
    "remaining_proportion_of_forest": 0.6498923681551027, 
    "risk_score_current": 3, 
    "risk_score_future": 1, 
    "risk_score_past": 5, 
    "treeloss_2001": 13807.421294117648, 
    "treeloss_2002": 10336.663764705883, 
    "treeloss_2003": 5362.0725882352945, 
    "treeloss_2004": 23633.46494117647, 
    "treeloss_2005": 18897.85129411764, 
    "treeloss_2006": 18902.94423529412, 
    "treeloss_2007": 19821.64729411765, 
    "treeloss_2008": 20534.44305882353, 
    "treeloss_2009": 18388.01258823529, 
    "treeloss_2010": 22986.139411764703, 
    "treeloss_2011": 27234.009882352933, 
    "treeloss_2012": 34676.81823529412, 
    "treeloss_2013": 18676.124823529404, 
    "treeloss_2014": 29737.10011764706, 
    "treeloss_2015": 19247.49670588235, 
    "treeloss_2016": 33477.242823529414, 
    "treeloss_2017": 17426.114470588236, 
    "treeloss_2018": 16680.826941176463, 
    "treeloss_2019": 16142.442352941182, 
    "treeloss_sum": 385968.8368235295, 
    "treeloss_sum_proportion_of_forest": 0.3501076318448973, 
    "treeloss_sum_proportion_of_land": 0.30316814123653074
  }, 
  "avg_stats": {
    "forest_area": {
      "max": 193978.16082352944, 
      "mean": 40669.36523339657, 
      "min": 1607.2161176470574, 
      "quartile_1": 10495.865294117652, 
      "quartile_2": 18086.65976470588, 
      "quartile_3": 39378.224647058814, 
      "std": 49532.749722518194
    }, 
    "land_area": {
      "max": 195701.8782352941, 
      "mean": 46976.89371916508, 
      "min": 2024.8503529411762, 
      "quartile_1": 13864.130647058824, 
      "quartile_2": 21684.098470588237, 
      "quartile_3": 53760.50029411765, 
      "std": 52358.07363717588
    }, 
    "remaining_proportion_of_forest": {
      "max": 0.9247698149151318, 
      "mean": 0.5348010362249239, 
      "min": 0.1427636288715487, 
      "quartile_1": 0.41241169788238496, 
      "quartile_2": 0.4898538552400279, 
      "quartile_3": 0.6568154936227932, 
      "std": 0.1945847152721802
    }, 
    "risk_score_current": {
      "max": 5.0, 
      "mean": 3.064516129032258, 
      "min": 1.0, 
      "quartile_1": 2.5, 
      "quartile_2": 3.0, 
      "quartile_3": 3.5, 
      "std": 1.0625592962581034
    }, 
    "risk_score_future": {
      "max": 4.0, 
      "mean": 2.903225806451613, 
      "min": 1.0, 
      "quartile_1": 3.0, 
      "quartile_2": 3.0, 
      "quartile_3": 3.0, 
      "std": 0.7463171224833502
    }, 
    "risk_score_past": {
      "max": 5.0, 
      "mean": 3.225806451612903, 
      "min": 1.0, 
      "quartile_1": 3.0, 
      "quartile_2": 3.0, 
      "quartile_3": 4.0, 
      "std": 1.2304383343441703
    }, 
    "treeloss_2001": {
      "max": 2999.728588235295, 
      "mean": 575.7662732447818, 
      "min": 8.116941176470588, 
      "quartile_1": 117.17929411764703, 
      "quartile_2": 375.1475294117648, 
      "quartile_3": 617.3565882352941, 
      "std": 719.709162487551
    }, 
    "treeloss_2002": {
      "max": 2117.272588235294, 
      "mean": 398.6304819734345, 
      "min": 16.01541176470588, 
      "quartile_1": 80.44694117647057, 
      "quartile_2": 149.31, 
      "quartile_3": 324.14082352941176, 
      "std": 595.0643838417456
    }, 
    "treeloss_2003": {
      "max": 1021.8589411764708, 
      "mean": 198.6861631878558, 
      "min": 0.09, 
      "quartile_1": 48.52923529411765, 
      "quartile_2": 113.0756470588235, 
      "quartile_3": 272.50870588235296, 
      "std": 230.44745034042361
    }, 
    "treeloss_2004": {
      "max": 4489.2303529411765, 
      "mean": 900.4584705882352, 
      "min": 4.160823529411766, 
      "quartile_1": 154.84905882352942, 
      "quartile_2": 346.16894117647047, 
      "quartile_3": 1170.136764705882, 
      "std": 1188.066613302895
    }, 
    "treeloss_2005": {
      "max": 3150.5544705882353, 
      "mean": 702.1300075901329, 
      "min": 6.409411764705883, 
      "quartile_1": 129.08294117647057, 
      "quartile_2": 265.60235294117643, 
      "quartile_3": 1106.1220588235292, 
      "std": 858.2563211674182
    }, 
    "treeloss_2006": {
      "max": 4142.239764705882, 
      "mean": 704.3542201138519, 
      "min": 4.194000000000001, 
      "quartile_1": 56.058, 
      "quartile_2": 323.01670588235294, 
      "quartile_3": 808.0012941176473, 
      "std": 1038.7015071130422
    }, 
    "treeloss_2007": {
      "max": 3680.380235294118, 
      "mean": 729.1336736242886, 
      "min": 2.392941176470588, 
      "quartile_1": 114.88041176470588, 
      "quartile_2": 305.8976470588236, 
      "quartile_3": 891.2235882352943, 
      "std": 982.0964220065136
    }, 
    "treeloss_2008": {
      "max": 3008.169176470589, 
      "mean": 739.7165806451615, 
      "min": 0.4111764705882353, 
      "quartile_1": 121.70417647058821, 
      "quartile_2": 465.77117647058816, 
      "quartile_3": 1075.9358823529412, 
      "std": 824.4154041838596
    }, 
    "treeloss_2009": {
      "max": 2755.9665882352947, 
      "mean": 729.041009487666, 
      "min": 9.322941176470588, 
      "quartile_1": 229.7599411764706, 
      "quartile_2": 383.1264705882353, 
      "quartile_3": 975.5685882352941, 
      "std": 750.1505668906011
    }, 
    "treeloss_2010": {
      "max": 7802.240823529409, 
      "mean": 898.8480910815936, 
      "min": 14.024117647058823, 
      "quartile_1": 175.79894117647055, 
      "quartile_2": 374.43988235294114, 
      "quartile_3": 1022.1382941176469, 
      "std": 1440.3394146167907
    }, 
    "treeloss_2011": {
      "max": 6900.195529411764, 
      "mean": 1068.3321404174571, 
      "min": 4.666235294117646, 
      "quartile_1": 161.80552941176472, 
      "quartile_2": 317.00329411764704, 
      "quartile_3": 973.7726470588234, 
      "std": 1807.5650246639561
    }, 
    "treeloss_2012": {
      "max": 9369.13023529412, 
      "mean": 1358.8117798861479, 
      "min": 16.32635294117647, 
      "quartile_1": 191.09311764705888, 
      "quartile_2": 445.6792941176471, 
      "quartile_3": 1240.931823529412, 
      "std": 2322.7848981874035
    }, 
    "treeloss_2013": {
      "max": 4054.881529411764, 
      "mean": 732.6757229601516, 
      "min": 14.57505882352941, 
      "quartile_1": 89.64564705882353, 
      "quartile_2": 342.53682352941183, 
      "quartile_3": 1135.7918823529412, 
      "std": 922.3462696459475
    }, 
    "treeloss_2014": {
      "max": 5132.85988235294, 
      "mean": 1052.1220759013283, 
      "min": 25.292470588235286, 
      "quartile_1": 186.12582352941175, 
      "quartile_2": 719.1656470588237, 
      "quartile_3": 1480.3847647058824, 
      "std": 1256.3446595085986
    }, 
    "treeloss_2015": {
      "max": 5405.0527058823545, 
      "mean": 706.7366072106262, 
      "min": 2.8987058823529415, 
      "quartile_1": 123.5648823529412, 
      "quartile_2": 360.8936470588234, 
      "quartile_3": 813.6719999999998, 
      "std": 1035.5492517813207
    }, 
    "treeloss_2016": {
      "max": 4671.859411764705, 
      "mean": 1164.7770740037952, 
      "min": 4.5539999999999985, 
      "quartile_1": 226.28117647058824, 
      "quartile_2": 682.2264705882352, 
      "quartile_3": 1506.3818823529414, 
      "std": 1270.3261684556846
    }, 
    "treeloss_2017": {
      "max": 2904.667411764706, 
      "mean": 648.5910626185957, 
      "min": 15.93, 
      "quartile_1": 131.3260588235294, 
      "quartile_2": 286.99129411764704, 
      "quartile_3": 954.0072352941174, 
      "std": 743.6375222935819
    }, 
    "treeloss_2018": {
      "max": 2253.289058823529, 
      "mean": 640.626808349146, 
      "min": 12.842470588235296, 
      "quartile_1": 154.58982352941172, 
      "quartile_2": 432.1492941176471, 
      "quartile_3": 1057.011529411765, 
      "std": 578.318632201922
    }, 
    "treeloss_2019": {
      "max": 2629.844117647059, 
      "mean": 581.1268690702087, 
      "min": 2.25, 
      "quartile_1": 133.1955882352941, 
      "quartile_2": 308.81011764705886, 
      "quartile_3": 799.5944117647059, 
      "std": 669.3299016897903
    }, 
    "treeloss_sum": {
      "max": 57740.93929411765, 
      "mean": 14530.565111954456, 
      "min": 535.0768235294117, 
      "quartile_1": 4739.867823529407, 
      "quartile_2": 9541.664823529409, 
      "quartile_3": 16579.684235294113, 
      "std": 15140.116573440844
    }, 
    "treeloss_sum_proportion_of_forest": {
      "max": 0.8572363711284513, 
      "mean": 0.4651989637750761, 
      "min": 0.07523018508486827, 
      "quartile_1": 0.3431845063772068, 
      "quartile_2": 0.5101461447599721, 
      "quartile_3": 0.587588302117615, 
      "std": 0.1945847152721802
    }, 
    "treeloss_sum_proportion_of_land": {
      "max": 0.6525160882352277, 
      "mean": 0.37415385521309547, 
      "min": 0.07456756712181964, 
      "quartile_1": 0.27252806924646455, 
      "quartile_2": 0.364772990397692, 
      "quartile_3": 0.5056511385973309, 
      "std": 0.16023470700964199
    }
  }, 
  "brand": "Ferrero", 
  "brandid": 1, 
  "country": "Luxembourg", 
  "country_count": 1, 
  "description": "Ferrero SpA, more commonly known as Ferrero Group, is an Italian manufacturer of branded chocolate and confectionery products, and the second biggest chocolate producer and confectionery company in the world. It was founded in 1946 in Alba, Piedmont, Italy, by Pietro Ferrero, a confectioner and small-time pastry maker who laid the groundwork for Nutella and famously added hazelnut to save money on chocolate. Family-owned to this day, the company has built itself into an international group with commercial interests in the Americas, Australasia, Asia and Africa, as well as in Western and Eastern Europe. The Group, which is headquartered in Luxembourg, has three R&D centres and twenty production plants.  Thanks to the dedicated commitment of 22,000 employees, brands like Nutella, Ferrero Rocher, Mon Cheri, Tic Tac, Kinder Bueno, Kinder Sorpresa and Raffaello have become worldwide successes.  For Ferrero, respecting nature is so important that the Group considers the objectives of its environmental policy on a par with its production goals. In order to do this, it has set ambitious goals on every impact it could have on the environment.", 
  "external_link": "https://www.ferrerocsr.com/", 
  "mill_count": 31, 
  "mills": [
    {
      "country": "Indonesia", 
      "mill_name": "BATANG KULIM", 
      "prnt_comp": "MUSIM MAS", 
      "risk_score_current": 5.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 5.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Pelalawan", 
      "umlid": "po1000000054"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "TANAH GAMBUS", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 5.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 4.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Batu Bara", 
      "umlid": "po1000000352"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "AGROWIRATAMA", 
      "prnt_comp": "AGRO WIRATAMA", 
      "risk_score_current": 5.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 4.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Barat", 
      "sub_state": "Pasaman Barat", 
      "umlid": "po1000000092"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUNGAI LILIN", 
      "prnt_comp": "HINDOLI", 
      "risk_score_current": 5.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Selatan", 
      "sub_state": "Musi Banyuasin", 
      "umlid": "po1000000058"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "BLANG SIMPO", 
      "prnt_comp": "PERKASA SUBUR SAKTI", 
      "risk_score_current": 4.0, 
      "risk_score_future": 4.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Aceh Timur", 
      "umlid": "po1000000706"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "BANGUN BANDAR MILL", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 4.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Serdang Bedagai", 
      "umlid": "po1000000451"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUNGAI LIPUT", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 4.0, 
      "risk_score_future": 4.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Aceh Tamiang", 
      "umlid": "po1000001251"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "UKUI I", 
      "prnt_comp": "INTI INDOSAWIT SUBUR", 
      "risk_score_current": 4.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, MB", 
      "state": "Riau", 
      "sub_state": "Pelalawan", 
      "umlid": "po1000000148"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "MANGGALA", 
      "prnt_comp": "TUNGGAL MITRA PLANTATIONS", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 4.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Rokan Hilir", 
      "umlid": "po1000000330"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SEUMANYAM", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Nagan Raya", 
      "umlid": "po1000001777"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SINGKIL SEJAHTERA MAKMUR", 
      "prnt_comp": "SINGKIL SEJAHTERA MAKMUR", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": " ", 
      "state": "Aceh", 
      "sub_state": "Aceh Singkil", 
      "umlid": "po1000010059"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "MUTIARA SAWIT LESTARI", 
      "prnt_comp": "MUTIARA SAWIT LESTARI", 
      "risk_score_current": 3.0, 
      "risk_score_future": 4.0, 
      "risk_score_past": 2.0, 
      "rspo_model": " ", 
      "state": "Aceh", 
      "sub_state": "Aceh Timur", 
      "umlid": "po1000009355"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "MULTI AGRINDO SUMATERA", 
      "prnt_comp": "MULTI AGRINDO SUMATERA", 
      "risk_score_current": 3.0, 
      "risk_score_future": 4.0, 
      "risk_score_past": 2.0, 
      "rspo_model": " ", 
      "state": "Sumatera Utara", 
      "sub_state": "Serdang Bedagai", 
      "umlid": "po1000007473"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "GUNTUNG IDAMAN NUSA 2", 
      "prnt_comp": "GUNTUNG IDAMAN NUSA", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 2.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Indragiri Hilir", 
      "umlid": "po1000006505"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "LIBO SAWIT PERKASA", 
      "prnt_comp": "LIBO SAWIT PERKASA", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 4.0, 
      "rspo_model": " ", 
      "state": "Riau", 
      "sub_state": "Siak", 
      "umlid": "po1000004239"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SEI NILO", 
      "prnt_comp": "SURYA BRATASENA PLANTATION", 
      "risk_score_current": 3.0, 
      "risk_score_future": 2.0, 
      "risk_score_past": 4.0, 
      "rspo_model": " ", 
      "state": "Riau", 
      "sub_state": "Pelalawan", 
      "umlid": "po1000004159"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUNGAI PINANG", 
      "prnt_comp": "BINA SAINS CEMERLANG", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 4.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Selatan", 
      "sub_state": "Musi Rawas", 
      "umlid": "po1000000316"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "MUKUT", 
      "prnt_comp": "HINDOLI", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Selatan", 
      "sub_state": "Musi Banyuasin", 
      "umlid": "po1000003254"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "AEK LOBA", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 4.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Asahan", 
      "umlid": "po1000001252"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "NEGERI LAMA", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Sumatera Utara", 
      "sub_state": "Labuhanbatu", 
      "umlid": "po1000001250"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "NAGA SAKTI", 
      "prnt_comp": "BUANA WIRALESTARI MAS", 
      "risk_score_current": 3.0, 
      "risk_score_future": 4.0, 
      "risk_score_past": 1.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Kampar", 
      "umlid": "po1000001061"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "PANGKALAN LESUNG", 
      "prnt_comp": "MUSIM MAS", 
      "risk_score_current": 3.0, 
      "risk_score_future": 2.0, 
      "risk_score_past": 5.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Riau", 
      "sub_state": "Pelalawan", 
      "umlid": "po1000000355"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "AGATHIS", 
      "prnt_comp": "TH INDO PLANTATIONS", 
      "risk_score_current": 3.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": " ", 
      "state": "Riau", 
      "sub_state": "Indragiri Hilir", 
      "umlid": "po1000010255"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "LAE BUTAR", 
      "prnt_comp": "SOCFIN INDONESIA", 
      "risk_score_current": 2.0, 
      "risk_score_future": 2.0, 
      "risk_score_past": 5.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Aceh", 
      "sub_state": "Aceh Singkil", 
      "umlid": "po1000001775"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUKAJADI SAWIT MEKAR 1", 
      "prnt_comp": "SUKAJADI SAWIT MEKAR", 
      "risk_score_current": 2.0, 
      "risk_score_future": 1.0, 
      "risk_score_past": 5.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Kalimantan Tengah", 
      "sub_state": "Kotawaringin Timur", 
      "umlid": "po1000000106"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "FAJAR BAIZURY & BROTHERS", 
      "prnt_comp": "FAJAR BAIZURI & BROTHERS", 
      "risk_score_current": 2.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 1.0, 
      "rspo_model": " ", 
      "state": "Aceh", 
      "sub_state": "Nagan Raya", 
      "umlid": "po1000004565"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "PULAU TIGA", 
      "prnt_comp": "PERKEBUNAN NUSANTARA I", 
      "risk_score_current": 2.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 1.0, 
      "rspo_model": " ", 
      "state": "Aceh", 
      "sub_state": "Aceh Tamiang", 
      "umlid": "po1000004567"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "DOLOK SINUMBAH", 
      "prnt_comp": "PERKEBUNAN NUSANTARA IV", 
      "risk_score_current": 2.0, 
      "risk_score_future": 2.0, 
      "risk_score_past": 4.0, 
      "rspo_model": "RSPO Certified, MB", 
      "state": "Sumatera Utara", 
      "sub_state": "Simalungun", 
      "umlid": "po1000005868"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "ANUGRAH MULTI SAWITA", 
      "prnt_comp": "ANUGRAH MULTI SAWITA", 
      "risk_score_current": 2.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 3.0, 
      "rspo_model": " ", 
      "state": "Sumatera Utara", 
      "sub_state": "Asahan", 
      "umlid": "po1000008388"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "PKS 2", 
      "prnt_comp": "DHARMA SATYA NUSANTARA", 
      "risk_score_current": 1.0, 
      "risk_score_future": 3.0, 
      "risk_score_past": 1.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Kalimantan Timur", 
      "sub_state": "Kutai Timur", 
      "umlid": "po1000000939"
    }, 
    {
      "country": "Indonesia", 
      "mill_name": "SUKAJADI SAWIT MEKAR 2", 
      "prnt_comp": "SUKAJADI SAWIT MEKAR", 
      "risk_score_current": 1.0, 
      "risk_score_future": 1.0, 
      "risk_score_past": 5.0, 
      "rspo_model": "RSPO Certified, IP", 
      "state": "Kalimantan Tengah", 
      "sub_state": "Kotawaringin Timur", 
      "umlid": "po1000000134"
    }
  ], 
  "nonrspo_mill_count": 9, 
  "rspo_member_since": "2005-01-17", 
  "rspo_mill_count": 22, 
  "supplier_count": 22, 
  "suppliers": [
    {
      "country": "Indonesia", 
      "mill_count": 7, 
      "name": "SOCFIN INDONESIA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 2, 
      "name": "MUSIM MAS"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 2, 
      "name": "SUKAJADI SAWIT MEKAR"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 2, 
      "name": "HINDOLI"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "MUTIARA SAWIT LESTARI"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "TH INDO PLANTATIONS"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "SURYA BRATASENA PLANTATION"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "SINGKIL SEJAHTERA MAKMUR"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "PERKEBUNAN NUSANTARA IV"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "PERKEBUNAN NUSANTARA I"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "PERKASA SUBUR SAKTI"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "AGRO WIRATAMA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "ANUGRAH MULTI SAWITA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "MULTI AGRINDO SUMATERA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "LIBO SAWIT PERKASA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "INTI INDOSAWIT SUBUR"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "GUNTUNG IDAMAN NUSA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "FAJAR BAIZURI & BROTHERS"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "DHARMA SATYA NUSANTARA"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "BUANA WIRALESTARI MAS"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "BINA SAINS CEMERLANG"
    }, 
    {
      "country": "Indonesia", 
      "mill_count": 1, 
      "name": "TUNGGAL MITRA PLANTATIONS"
    }
  ]
}
```