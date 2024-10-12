# -*- coding: utf-8 -*-
"""lab03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bZHzbLQKwCjY04eZmA3BrIbV3kWRjHNj
"""

matches = [
    {
      "T": "S",
      "matches": {
        "S<=35": ["Gel-S", "Gel-S", "DeluxFF", "IceCold", "IceCold"],
        "S>35<=70": ["Gel-S", "Gel-S", "DeluxFF", "IceCold", "IceCold"],
        "S>70<=100": ["Gel-SPlus", "Gel-SPlus", "DeluxFF", "IceCold", "IceCold"],
        "S>100<=130": ["Gel-SPlus", "Gel-SPlus", "DeluxFF", "DeluxFF", "DeluxFF"],
        "S>130": ["Frost++", "Frost++", "Frost++", "Frost++", "Frost++"
      ]}
    },
    {
      "T": "D",
      "matches": {
          "D<=50": ["Gel-D", "Gel-DPlus", "Gel-DPlus", "IceCold", "IceCold"],
          "D>50<=100": ["Gel-D", "Gel-DPlus", "Gel-DPlus", "IceCold", "IceCold"],
          "D>100<=125": ["Gel-D", "Gel-DPlus", "DupCold", "Frost++", "Frost++"],
          "D>125<=150": ["Gel-D", "Gel-DPlus", "DupCold", "Frost++", "Frost++"],
          "D>150": ["Gel-D", "DupCold", "DupCold", "Frost++", "Frost++"]
      }
    }
]

fridge_type = str(input(""))
fridge_users = int(input(""))
fridge_watts = int(input(""))

for item in matches:
  if item["T"] == fridge_type:
    # permite encontrar o total de pessoas baseado no index da matrix [0, 1 , 2, 3] || [1, 2, 3, 4]
    fridge_users -= 1
    if (fridge_watts <= 35 and fridge_type == "S"):
      match_id = f"{fridge_type}<=35"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 35 and fridge_watts <= 70 and fridge_type == "S"):
      match_id = f"{fridge_type}>35<=70"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 70 and fridge_watts <= 100 and fridge_type == "S"):
      match_id = f"{fridge_type}>70<=100"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 100 and fridge_watts <= 130 and fridge_type == "S"):
      match_id = f"{fridge_type}>100<=130"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 130 and fridge_type == "S"):
      match_id = f"{fridge_type}>130"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts <= 50 and fridge_type == "D"):
      match_id = f"{fridge_type}<=50"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 50 and fridge_watts <= 100 and fridge_type == "D"):
      match_id = f"{fridge_type}>50<=100"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 100 and fridge_watts <= 125 and fridge_type == "D"):
      match_id = f"{fridge_type}>100<=125"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 125 and fridge_watts <= 150 and fridge_type == "D"):
      match_id = f"{fridge_type}>125<=150"
      print(item["matches"][match_id][(fridge_users)])
    elif (fridge_watts > 150 and fridge_type == "D"):
      match_id = f"{fridge_type}>150"
      print(item["matches"][match_id][(fridge_users)])
    else:
      print("error")