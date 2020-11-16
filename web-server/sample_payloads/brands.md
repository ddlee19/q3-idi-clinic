### **Get Brands**
#### /api/v1.0/brands

**Example 1 of 2:**

Retrieving All Brands

/api/v1.0/brands
```
[
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
]
```

**Example 2 of 2:**

Querying by UML Id

/api/v1.0/brands?mill_id=po1000000316

```
[
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
  }
]
```