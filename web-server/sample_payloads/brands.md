### **Get Brands**
#### /api/v1.0/brands

**Example 1 of 2:**

Retrieving All Brands ("uml_id" query parameter not provided)

/api/v1.0/brands
```
[
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
]
```

**Example 2 of 3:**

Retrieving Brands Using Valid UML Id

/api/v1.0/brands?uml_id=po1000000316

```
[
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
  }
]
```

**Example 3 of 3:**

Retrieving Brands Using Invalid UML Id

/api/v1.0/brands?uml_id=po0000000000

```
[]
```